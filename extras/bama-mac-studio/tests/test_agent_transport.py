"""Native socket and MCP regressions using an owned Foundation fixture.

Version-Timestamp: 2026-10-27 08:43:52 AST
"""
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / 'skills/bama-agent-cli/template/Agent'
HARNESS = r'''
import Foundation
import Darwin
import Dispatch

typealias JSONObject = [String: Any]
nonisolated struct AgentError: Error {
    var code: String; var message: String; var exit: Int32 = 1
    static func invalid(_ message: String) -> Self { Self(code: "invalid", message: message) }
    static func unavailable(_ message: String) -> Self { Self(code: "app_unavailable", message: message) }
    static func usage(_ message: String) -> Self { Self(code: "usage", message: message) }
    var json: JSONObject { ["ok": false, "error": ["code": code, "message": message]] }
}
nonisolated enum JSON {
    static func data(_ object: Any) -> Data { try! JSONSerialization.data(withJSONObject: object, options: [.sortedKeys]) }
    static func string(_ object: Any) -> String { String(decoding: data(object), as: UTF8.self) }
}
struct AgentCommand {
    struct Param {
        enum Kind: String { case string, integer, boolean }
        var name: String; var kind: Kind = .string; var required = false; var help = ""
    }
    var name: String; var params: [Param] = []; var readOnly = true; var destructive = false
}
enum AgentCommands {
    static let all = [AgentCommand(name: "fixture", params: [
        .init(name: "text", required: true), .init(name: "number", kind: .integer), .init(name: "flag", kind: .boolean)
    ], destructive: true)]
}
enum AgentCLI {
    static func schema(_ command: AgentCommand) -> JSONObject {
        ["name": command.name, "description": "fixture", "inputSchema": ["type": "object"]]
    }
}
@main struct Harness {
    @MainActor static func main() {
        switch CommandLine.arguments.dropFirst().first ?? "" {
        case "server", "double-server":
            AgentSocket.listen { request in
                guard let value = try? JSONSerialization.jsonObject(with: request) as? JSONObject else {
                    return JSON.data(AgentError.invalid("invalid JSON").json)
                }
                if value["mode"] as? String == "disconnect" { Thread.sleep(forTimeInterval: 0.1) }
                if ["bulk", "disconnect"].contains(value["mode"] as? String ?? "") {
                    return JSON.data(["ok": true, "result": ["text": String(repeating: "x", count: 4 * 1024 * 1024)]])
                }
                if value["mode"] as? String == "oversized" {
                    return JSON.data(["ok": true, "result": ["text": String(repeating: "x", count: 9 * 1024 * 1024)]])
                }
                if value["mode"] as? String == "large" {
                    return JSON.data(["ok": true, "result": ["text": String(repeating: "x", count: 100_000)]])
                }
                return JSON.data(["ok": true, "result": ["echo": value, "owner": ProcessInfo.processInfo.environment["FIXTURE_OWNER"] ?? "first"]])
            }
            if CommandLine.arguments.dropFirst().first == "double-server" {
                AgentSocket.listen { _ in JSON.data(["ok": true, "result": ["owner": "second"]]) }
            }
            print("READY"); fflush(stdout)
            dispatchMain()
        case "client":
            do {
                let request = Data((CommandLine.arguments.count > 2 ? CommandLine.arguments[2] : "{}").utf8)
                let reply = try AgentSocket.send(request, launch: ProcessInfo.processInfo.environment["FIXTURE_LAUNCH"] == "1")
                print(String(decoding: reply, as: UTF8.self))
            } catch let error as AgentError { print(JSON.string(error.json)) }
            catch { print(JSON.string(["ok": false, "error": ["message": error.localizedDescription]])) }
        case "mcp": AgentMCP.serve()
        default: fatalError("fixture mode required")
        }
    }
}
'''

@unittest.skipUnless(sys.platform == 'darwin' and shutil.which('swiftc'), 'requires Darwin Swift toolchain')
class AgentTransport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='bama-agent-test-', dir='/tmp')
        cls.folder = Path(cls.temp.name).resolve()
        (cls.folder / 'Harness.swift').write_text(HARNESS)
        cls.binary = cls.folder / 'fixture'
        command = ['swiftc', '-swift-version', '6', '-default-isolation', 'MainActor', str(AGENT / 'AgentSocket.swift'), str(AGENT / 'AgentMCP.swift'), str(cls.folder / 'Harness.swift'), '-o', str(cls.binary)]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode:
            raise AssertionError('fixture compile failed:\n' + result.stderr)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.socket_path = self.folder / ('s' + str(time.monotonic_ns()))
        self.env = {**os.environ, 'APP_AGENT_ENABLED': '1', 'APP_AGENT_SOCKET': str(self.socket_path)}
        self.server = subprocess.Popen([str(self.binary), 'server'], env=self.env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(self.server.stdout.readline().strip(), 'READY')
        self.addCleanup(self.stop_server)

    def stop_server(self):
        if self.server.poll() is None:
            self.server.terminate()
        self.server.communicate(timeout=5)
        self.socket_path.unlink(missing_ok=True)

    def client(self, request):
        value = subprocess.run([str(self.binary), 'client', json.dumps(request)], env=self.env, capture_output=True, text=True, timeout=12)
        self.assertEqual(value.returncode, 0, value.stderr)
        return json.loads(value.stdout)

    def mcp(self, arguments):
        message = {'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call', 'params': {'name': 'fixture', 'arguments': arguments}}
        result = subprocess.run([str(self.binary), 'mcp'], input=json.dumps(message) + '\n', env=self.env, capture_output=True, text=True, timeout=12)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)['result']

    def extra_server(self, path, owner, mode='server'):
        process = subprocess.Popen([str(self.binary), mode], env={**self.env, 'APP_AGENT_SOCKET': str(path), 'FIXTURE_OWNER': owner}, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        def cleanup():
            if process.poll() is None: process.terminate()
            process.communicate(timeout=5)
        self.addCleanup(cleanup)
        self.assertEqual(process.stdout.readline().strip(), 'READY')
        return process

    def query_at(self, path):
        result = subprocess.run([str(self.binary), 'client', '{}'], env={**self.env, 'APP_AGENT_SOCKET': str(path)}, capture_output=True, text=True, timeout=4)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def new_socket_path(self):
        return self.folder / ('o' + str(time.monotonic_ns()))

    def test_second_process_cannot_replace_a_live_endpoint(self):
        inode = self.socket_path.lstat().st_ino
        self.extra_server(self.socket_path, 'second')
        self.assertEqual(self.query_at(self.socket_path)['result']['owner'], 'first')
        self.assertEqual(self.socket_path.lstat().st_ino, inode)

    def test_simultaneous_starts_keep_one_durable_owner(self):
        path = self.new_socket_path()
        processes = {}
        for owner in ('alpha', 'beta'):
            processes[owner] = subprocess.Popen([str(self.binary), 'server'], env={**self.env, 'APP_AGENT_SOCKET': str(path), 'FIXTURE_OWNER': owner}, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        def cleanup():
            for process in processes.values():
                if process.poll() is None: process.terminate()
                process.communicate(timeout=5)
        self.addCleanup(cleanup)
        for process in processes.values():
            self.assertEqual(process.stdout.readline().strip(), 'READY')
        owner = self.query_at(path)['result']['owner']
        self.assertIn(owner, processes)
        inode = path.lstat().st_ino
        for name, process in processes.items():
            if name != owner:
                process.terminate(); process.wait(timeout=5)
        self.extra_server(path, 'third')
        self.assertEqual(self.query_at(path)['result']['owner'], owner)
        self.assertEqual(path.lstat().st_ino, inode)

    def test_repeated_listen_keeps_the_first_handler(self):
        path = self.new_socket_path()
        self.extra_server(path, 'first', mode='double-server')
        self.assertEqual(self.query_at(path)['result']['owner'], 'first')

    def test_stale_owned_socket_is_recovered_under_private_lock(self):
        path = self.new_socket_path()
        stale = socket.socket(socket.AF_UNIX); stale.bind(str(path)); stale.close()
        self.extra_server(path, 'recovered')
        self.assertEqual(self.query_at(path)['result']['owner'], 'recovered')
        lock = Path(str(path) + '.lock')
        self.assertTrue(lock.is_file())
        self.assertEqual(lock.stat().st_mode & 0o777, 0o600)

    def test_unrelated_file_and_socket_symlink_are_preserved(self):
        path = self.new_socket_path(); path.write_text('keep unrelated file')
        inode = path.lstat().st_ino
        self.extra_server(path, 'refused')
        self.assertEqual(path.read_text(), 'keep unrelated file')
        self.assertEqual(path.lstat().st_ino, inode)
        link = self.new_socket_path(); link.symlink_to(path)
        self.extra_server(link, 'refused')
        self.assertTrue(link.is_symlink())
        self.assertEqual(path.read_text(), 'keep unrelated file')

    def test_lock_symlink_is_not_followed(self):
        path = self.new_socket_path(); target = self.folder / ('keep' + str(time.monotonic_ns()))
        target.write_text('keep lock target')
        lock = Path(str(path) + '.lock'); lock.symlink_to(target)
        self.extra_server(path, 'refused')
        self.assertFalse(path.exists())
        self.assertTrue(lock.is_symlink())
        self.assertEqual(target.read_text(), 'keep lock target')

    def test_live_legacy_socket_without_lock_is_not_reclaimed(self):
        path = self.new_socket_path(); listener = socket.socket(socket.AF_UNIX)
        listener.bind(str(path)); listener.listen(1); listener.settimeout(2)
        self.addCleanup(listener.close)
        inode = path.lstat().st_ino
        self.extra_server(path, 'refused')
        self.assertEqual(path.lstat().st_ino, inode)
        connection, _ = listener.accept()
        with connection:
            self.assertEqual(connection.recv(1), b'')

    def test_large_valid_response_is_not_limited_to_request_size(self):
        result = self.client({'mode': 'large'})
        self.assertTrue(result['ok'], result)
        self.assertEqual(len(result['result']['text']), 100_000)

    def test_completed_response_overflow_preserves_success(self):
        result = self.client({'mode': 'oversized'})
        self.assertTrue(result['ok'], result)
        self.assertTrue(result['result']['completed'])
        self.assertTrue(result['result']['result_omitted'])
        self.assertEqual(result['result']['reason'], 'response_limit')
        self.assertEqual(result['result']['response_limit_bytes'], 8 * 1024 * 1024)
        self.assertIn('Do not repeat', result['result']['message'])

    def test_disconnect_does_not_terminate_server(self):
        client = socket.socket(socket.AF_UNIX)
        client.connect(str(self.socket_path))
        client.sendall(b'{"mode":"disconnect"}\n')
        client.close()
        time.sleep(0.3)
        self.assertIsNone(self.server.poll(), 'server died after peer disconnected')
        self.assertTrue(self.client({})['ok'])

    def test_nonreading_peer_does_not_block_every_later_request(self):
        client = socket.socket(socket.AF_UNIX)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024)
        client.connect(str(self.socket_path))
        client.sendall(b'{"mode":"bulk"}\n')
        self.addCleanup(client.close)
        started = time.monotonic()
        self.assertTrue(self.client({})['ok'])
        self.assertLess(time.monotonic() - started, 8, 'a stalled writer blocked a later client')

    def raw_peer(self, payload, launch=False):
        path = self.folder / ('raw' + str(time.monotonic_ns()))
        listener = socket.socket(socket.AF_UNIX)
        listener.bind(str(path)); listener.listen(1)
        requests = []
        def answer():
            connection, _ = listener.accept()
            with connection:
                data = b''
                while b'\n' not in data:
                    part = connection.recv(4096)
                    if not part: break
                    data += part
                requests.append(data)
                if payload is not None:
                    try: connection.sendall(payload)
                    except (BrokenPipeError, ConnectionResetError): pass
        thread = threading.Thread(target=answer, daemon=True); thread.start()
        try:
            result = subprocess.run([str(self.binary), 'client', '{}'], env={**self.env, 'APP_AGENT_SOCKET': str(path), 'FIXTURE_LAUNCH': '1' if launch else '0'}, capture_output=True, text=True, timeout=8)
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout), requests
        finally:
            listener.close(); thread.join(timeout=2); path.unlink(missing_ok=True)

    def test_unframed_oversized_response_is_explicit(self):
        result, requests = self.raw_peer(b'x' * (9 * 1024 * 1024) + b'\n')
        self.assertFalse(result['ok'])
        self.assertIn('response', result['error']['message'])
        self.assertIn('limit', result['error']['message'])
        self.assertEqual(len(requests), 1)

    def test_delivered_request_without_reply_is_not_launched_or_retried(self):
        result, requests = self.raw_peer(None, launch=True)
        self.assertFalse(result['ok'])
        self.assertEqual(result['error']['code'], 'delivery_uncertain')
        self.assertIn('not retried', result['error']['message'])
        self.assertEqual(len(requests), 1)

    def test_exact_request_limit_allows_its_newline_frame(self):
        overhead = len(json.dumps({'text': ''}).encode())
        result = self.client({'text': 'x' * (65_536 - overhead)})
        self.assertTrue(result['ok'], result)

    def test_request_overflow_is_rejected_before_delivery(self):
        value = subprocess.run([str(self.binary), 'client', json.dumps({'text': 'x' * 70_000})], env={**self.env, 'APP_AGENT_SOCKET': str(self.folder / 'absent')}, capture_output=True, text=True, timeout=3)
        self.assertEqual(value.returncode, 0, value.stderr)
        result = json.loads(value.stdout)
        self.assertFalse(result['ok'])
        self.assertIn('request', result['error']['message'])
        self.assertIn('limit', result['error']['message'])

    def test_mcp_schema_advertises_unknown_key_rejection(self):
        message = {'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list'}
        result = subprocess.run([str(self.binary), 'mcp'], input=json.dumps(message) + '\n', env=self.env, capture_output=True, text=True, timeout=3)
        self.assertEqual(result.returncode, 0, result.stderr)
        schema = json.loads(result.stdout)['result']['tools'][0]['inputSchema']
        self.assertIs(schema.get('additionalProperties'), False)

    def test_mcp_keeps_declared_types_before_socket_conversion(self):
        value = self.mcp({'text': 'hello', 'number': 7, 'flag': True, 'yes': False})
        self.assertFalse(value['isError'], value)
        for arguments in [
            {'text': {'nested': 1}}, {'text': ['one']}, {'text': True}, {'text': 1}, {'text': 'ok', 'flag': 'true'},
            {'text': 'ok', 'number': True}, {'text': 'ok', 'number': 1.5},
            {'text': 'ok', 'number': '7'}, {'text': 'ok', 'yes': 'true'},
            {'text': 'ok', 'unknown': 'x'}, {'text': None}, {'text': 'x' * 16_385}, {}, [],
        ]:
            with self.subTest(arguments=arguments):
                self.assertTrue(self.mcp(arguments)['isError'], 'accepted invalid typed arguments: ' + repr(arguments))

if __name__ == '__main__':
    unittest.main()
