import Foundation
import CoreFoundation
import Darwin

// Version-Timestamp: 2026-10-27 08:43:52 AST
// Adapted from MIT BAMA. The socket is a same-user boundary, not caller authentication.

/// One JSON request and response per Unix socket connection.
nonisolated enum AgentSocket {
    static let maximumRequestBytes = 65_536
    static let maximumResponseBytes = 8 * 1024 * 1024
    private static let transportTimeout: TimeInterval = 5
    private enum ConnectionFailure: Error { case notRunning }

    static var path: String {
        let env = ProcessInfo.processInfo.environment
        if let path = env["APP_AGENT_SOCKET"], !path.isEmpty { return path }
        if let store = env["APP_STORE"], !store.isEmpty { return store + ".sock" }
        let dir = URL.applicationSupportDirectory.appending(path: "__APP_NAME__", directoryHint: .isDirectory)
        try? FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)
        return dir.appending(path: "agent.sock").path
    }

    private static func address(_ path: String) throws -> sockaddr_un {
        var address = sockaddr_un()
        address.sun_family = sa_family_t(AF_UNIX)
        let bytes = Array(path.utf8)
        guard bytes.count < MemoryLayout.size(ofValue: address.sun_path) else {
            throw AgentError.invalid("socket path is too long (over 103 bytes): \(path). Set APP_AGENT_SOCKET to a shorter path")
        }
        withUnsafeMutableBytes(of: &address.sun_path) { raw in
            raw.copyBytes(from: bytes)
            raw[bytes.count] = 0
        }
        return address
    }

    // MARK: App side

    /// The app opts in; repeated calls keep the existing listener and handler.
    static func listen(handle: @escaping @MainActor @Sendable (Data) -> Data) {
        guard ProcessInfo.processInfo.environment["APP_AGENT_ENABLED"] == "1",
              let listener = claimListener(path) else { return }
        let server = listener.socket
        let lease = listener.lock
        Thread.detachNewThread {
            // Keep the lock for the complete listener lifetime. Close releases it.
            defer { close(server); close(lease) }
            while true {
                let client = accept(server, nil, nil)
                guard client >= 0 else {
                    if errno == EBADF || errno == EINVAL { return }
                    if errno != EINTR { Thread.sleep(forTimeInterval: 0.05) }
                    continue
                }
                serve(client, handle: handle)
            }
        }
    }

    /// New processes share this private advisory lock, never remove its file,
    /// and hold its descriptor until their listener stops. Separate opens also
    /// conflict within a process, so a repeated listen cannot replace itself.
    private static func claimListener(_ path: String) -> (socket: Int32, lock: Int32)? {
        guard var address = try? address(path), let lease = listenerLock(path + ".lock") else { return nil }
        var keepLease = false
        defer { if !keepLease { close(lease) } }
        guard prepareSocketPath(path) else { return nil }
        let server = socket(AF_UNIX, SOCK_STREAM, 0)
        guard server >= 0 else { return nil }
        guard fcntl(server, F_SETFD, FD_CLOEXEC) == 0 else { close(server); return nil }
        let bound = withUnsafePointer(to: &address) {
            $0.withMemoryRebound(to: sockaddr.self, capacity: 1) { bind(server, $0, socklen_t(MemoryLayout<sockaddr_un>.size)) }
        }
        guard bound == 0, chmod(path, 0o600) == 0, Darwin.listen(server, 16) == 0 else {
            close(server)
            return nil
        }
        keepLease = true
        return (server, lease)
    }

    private static func listenerLock(_ path: String) -> Int32? {
        let lease = Darwin.open(path, O_RDWR | O_CREAT | O_NOFOLLOW | O_CLOEXEC | O_NONBLOCK, mode_t(0o600))
        guard lease >= 0 else { return nil }
        var opened = stat()
        guard fstat(lease, &opened) == 0,
              (opened.st_mode & mode_t(S_IFMT)) == mode_t(S_IFREG), opened.st_uid == getuid(),
              opened.st_nlink == 1, opened.st_mode & mode_t(0o777) == mode_t(0o600),
              flock(lease, LOCK_EX | LOCK_NB) == 0 else { close(lease); return nil }
        var named = stat()
        guard lstat(path, &named) == 0, named.st_dev == opened.st_dev, named.st_ino == opened.st_ino else {
            close(lease)
            return nil
        }
        return lease
    }

    /// Called only with the ownership lock held. Preserve non-sockets, links,
    /// foreign ownership and every live or uncertain endpoint, including older
    /// servers that do not implement our lock protocol.
    private static func prepareSocketPath(_ path: String) -> Bool {
        var original = stat()
        if lstat(path, &original) != 0 { return errno == ENOENT }
        guard (original.st_mode & mode_t(S_IFMT)) == mode_t(S_IFSOCK), original.st_uid == getuid(),
              isStaleSocket(path) else { return false }
        var current = stat()
        guard lstat(path, &current) == 0, current.st_dev == original.st_dev,
              current.st_ino == original.st_ino, current.st_uid == getuid(),
              (current.st_mode & mode_t(S_IFMT)) == mode_t(S_IFSOCK) else { return false }
        return unlink(path) == 0
    }

    private static func isStaleSocket(_ path: String) -> Bool {
        guard var address = try? address(path) else { return false }
        let probe = socket(AF_UNIX, SOCK_STREAM, 0)
        guard probe >= 0 else { return false }
        defer { close(probe) }
        guard (try? configure(probe)) != nil else { return false }
        let result = withUnsafePointer(to: &address) {
            $0.withMemoryRebound(to: sockaddr.self, capacity: 1) { connect(probe, $0, socklen_t(MemoryLayout<sockaddr_un>.size)) }
        }
        // No request is sent. Successful, pending or ambiguous connection means
        // the endpoint must be preserved. Only a definite refusal is stale.
        return result != 0 && errno == ECONNREFUSED
    }

    private static func serve(_ client: Int32, handle: @escaping @MainActor @Sendable (Data) -> Data) {
        defer { close(client) }
        guard (try? configure(client)) != nil else { return }
        let reply: Data
        do {
            let request = try readLine(client, limit: maximumRequestBytes, role: "request", timeout: transportTimeout)
            let result = DispatchQueue.main.sync { MainActor.assumeIsolated { handle(request) } }
            reply = boundedReply(result)
        } catch let error as AgentError {
            reply = JSON.data(error.json)
        } catch {
            reply = JSON.data(AgentError.invalid(error.localizedDescription).json)
        }
        // Never retry a stalled/disconnected write, including an error response.
        try? write(client, reply + Data("\n".utf8), timeout: transportTimeout)
    }

    /// A completed mutation remains successful even when its full result cannot
    /// be transported. Callers must read back with a bounded query, not replay it.
    private static func boundedReply(_ result: Data) -> Data {
        guard result.count > maximumResponseBytes else { return result }
        if let object = try? JSONSerialization.jsonObject(with: result) as? JSONObject,
           let ok = object["ok"] as? NSNumber, CFGetTypeID(ok) == CFBooleanGetTypeID() {
            if ok.boolValue {
                return JSON.data(["ok": true, "result": [
                    "completed": true, "result_omitted": true, "reason": "response_limit",
                    "response_limit_bytes": maximumResponseBytes,
                    "message": "Command completed; read back state with a bounded query. Do not repeat the mutation automatically."
                ]])
            }
            return JSON.data(AgentError(code: "response_limit", message:
                "Command reported failure; oversized error details were omitted. Check state before retrying.", exit: 1).json)
        }
        return JSON.data(AgentError(code: "delivery_uncertain", message:
            "Handler returned an oversized unclassified response; result omitted. Read back state and do not repeat the mutation automatically.", exit: 1).json)
    }

    // MARK: CLI side

    /// Launch/retry only before request delivery. A lost response never replays an action.
    static func send(_ request: Data, launch: Bool) throws -> Data {
        guard request.count <= maximumRequestBytes else {
            throw AgentError.invalid("request exceeds the \(maximumRequestBytes) byte limit")
        }
        guard !request.contains(UInt8(ascii: "\n")) else {
            throw AgentError.invalid("request must be one JSON line")
        }
        do { return try exchange(request) }
        catch ConnectionFailure.notRunning {
            guard launch else { throw AgentError.unavailable("__APP_NAME__ is not running. Open it, or leave out --no-launch") }
        }
        try startApp()
        for _ in 0..<50 {
            Thread.sleep(forTimeInterval: 0.2)
            do { return try exchange(request) }
            catch ConnectionFailure.notRunning { continue }
        }
        throw AgentError.unavailable("__APP_NAME__ did not answer within 10 seconds on \(path)")
    }

    private static func exchange(_ request: Data) throws -> Data {
        let client = socket(AF_UNIX, SOCK_STREAM, 0)
        guard client >= 0 else { throw AgentError.unavailable("could not create an agent socket") }
        defer { close(client) }
        try configure(client)
        var address = try address(path)
        let connected = withUnsafePointer(to: &address) {
            $0.withMemoryRebound(to: sockaddr.self, capacity: 1) { connect(client, $0, socklen_t(MemoryLayout<sockaddr_un>.size)) }
        }
        if connected != 0 {
            let code = errno
            if code == ENOENT || code == ECONNREFUSED { throw ConnectionFailure.notRunning }
            guard code == EINPROGRESS else { throw AgentError.unavailable("socket connect failed: \(String(cString: strerror(code)))") }
            try wait(client, events: Int16(POLLOUT), deadline: deadline(after: transportTimeout))
            var result: Int32 = 0
            var size = socklen_t(MemoryLayout<Int32>.size)
            guard getsockopt(client, SOL_SOCKET, SO_ERROR, &result, &size) == 0, result == 0 else {
                if result == ENOENT || result == ECONNREFUSED { throw ConnectionFailure.notRunning }
                throw AgentError.unavailable("socket connection failed")
            }
        }
        // Any failure after this point is uncertain delivery and must not launch/retry.
        do {
            try write(client, request + Data("\n".utf8), timeout: transportTimeout)
            return try readLine(client, limit: maximumResponseBytes, role: "response", timeout: 30)
        } catch {
            let detail = (error as? AgentError)?.message ?? error.localizedDescription
            throw AgentError(code: "delivery_uncertain", message: "request may have completed; it was not retried: \(detail)", exit: 1)
        }
    }

    /// Opens a selected app/test copy with this process's explicit environment.
    private static func startApp() throws {
        let executable = URL(fileURLWithPath: CommandLine.arguments[0]).resolvingSymlinksInPath()
        let bundle = executable.deletingLastPathComponent().deletingLastPathComponent().deletingLastPathComponent()
        let process = Process()
        if bundle.pathExtension == "app" {
            process.executableURL = URL(fileURLWithPath: "/usr/bin/open")
            var arguments = ["-g", "-n", bundle.path]
            for key in ["APP_STORE", "APP_AGENT_SOCKET", "APP_TEST_ROOT", "APP_AGENT_ENABLED", "APP_AGENT_WRITES"] {
                if let value = ProcessInfo.processInfo.environment[key] { arguments += ["--env", "\(key)=\(value)"] }
            }
            if ProcessInfo.processInfo.environment["APP_STORE"] == nil { arguments.remove(at: 1) }
            process.arguments = arguments
        } else {
            process.executableURL = executable
            process.arguments = []
        }
        process.standardOutput = FileHandle.nullDevice
        process.standardError = FileHandle.nullDevice
        do { try process.run() } catch { throw AgentError.unavailable("could not start __APP_NAME__: \(error.localizedDescription)") }
    }

    // MARK: Bounded nonblocking bytes

    private static func configure(_ socket: Int32) throws {
        var one: Int32 = 1
        let flags = fcntl(socket, F_GETFL, 0)
        guard flags >= 0, fcntl(socket, F_SETFL, flags | O_NONBLOCK) == 0,
              setsockopt(socket, SOL_SOCKET, SO_NOSIGPIPE, &one, socklen_t(MemoryLayout<Int32>.size)) == 0 else {
            throw AgentError.unavailable("could not configure bounded agent transport")
        }
    }

    private static func deadline(after seconds: TimeInterval) -> UInt64 {
        DispatchTime.now().uptimeNanoseconds + UInt64(seconds * 1_000_000_000)
    }

    private static func wait(_ socket: Int32, events: Int16, deadline: UInt64) throws {
        while true {
            let now = DispatchTime.now().uptimeNanoseconds
            guard now < deadline else { throw AgentError.unavailable("agent transport timed out") }
            let milliseconds = min((deadline - now + 999_999) / 1_000_000, UInt64(Int32.max))
            var descriptor = pollfd(fd: socket, events: events, revents: 0)
            let ready = poll(&descriptor, 1, Int32(milliseconds))
            if ready < 0 && errno == EINTR { continue }
            guard ready > 0 else { throw AgentError.unavailable(ready == 0 ? "agent transport timed out" : "agent transport poll failed") }
            if descriptor.revents & events != 0 { return }
            throw AgentError.unavailable("agent peer disconnected")
        }
    }

    private static func readLine(_ socket: Int32, limit: Int, role: String, timeout: TimeInterval) throws -> Data {
        let end = deadline(after: timeout)
        var data = Data()
        var buffer = [UInt8](repeating: 0, count: 16_384)
        while true {
            try wait(socket, events: Int16(POLLIN), deadline: end)
            let count = recv(socket, &buffer, buffer.count, 0)
            if count < 0 && [EINTR, EAGAIN, EWOULDBLOCK].contains(errno) { continue }
            guard count > 0 else { throw AgentError.unavailable("agent peer closed before a complete \(role)") }
            if let newline = buffer[..<count].firstIndex(of: UInt8(ascii: "\n")) {
                guard data.count + newline <= limit else { throw AgentError.invalid("\(role) exceeds the \(limit) byte limit") }
                data.append(buffer, count: newline)
                return data
            }
            guard data.count + count <= limit else { throw AgentError.invalid("\(role) exceeds the \(limit) byte limit") }
            data.append(buffer, count: count)
        }
    }

    private static func write(_ socket: Int32, _ data: Data, timeout: TimeInterval) throws {
        let end = deadline(after: timeout)
        try data.withUnsafeBytes { raw in
            var offset = 0
            while offset < raw.count {
                try wait(socket, events: Int16(POLLOUT), deadline: end)
                let sent = Darwin.send(socket, raw.baseAddress! + offset, raw.count - offset, 0)
                if sent < 0 && [EINTR, EAGAIN, EWOULDBLOCK].contains(errno) { continue }
                guard sent > 0 else { throw AgentError.unavailable("agent peer disconnected during send; action was not retried") }
                offset += sent
            }
        }
    }
}
