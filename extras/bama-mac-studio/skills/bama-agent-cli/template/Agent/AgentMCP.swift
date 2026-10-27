import Foundation
import CoreFoundation

// Version-Timestamp: 2026-10-27 08:17:03 AST

/// A small MCP server over stdin and stdout (JSON-RPC, one message per line).
/// Every AgentCommand becomes a tool ("items add" -> "items_add"), and each
/// call goes to the running app, like the CLI. Register it once:
///   claude mcp add --scope user __CLI_NAME__ -- ~/Applications/__APP_NAME__.app/Contents/MacOS/__APP_NAME__ mcp
/// Optional: Claude Code drives the CLI fine without it. Use it for Claude
/// Desktop and other clients that have no shell.
enum AgentMCP {
    static func serve() {
        while let line = readLine(strippingNewline: true) {
            guard let data = line.data(using: .utf8),
                  let message = try? JSONSerialization.jsonObject(with: data) as? JSONObject else { continue }
            // Notifications have no id and get no answer.
            guard let id = message["id"] else { continue }
            let method = message["method"] as? String ?? ""
            let params = message["params"] as? JSONObject ?? [:]
            var reply: JSONObject = ["jsonrpc": "2.0", "id": id]
            switch method {
            case "initialize":
                reply["result"] = [
                    "protocolVersion": params["protocolVersion"] as? String ?? "2025-06-18",
                    "capabilities": ["tools": [:]],
                    "serverInfo": ["name": "__CLI_NAME__", "version": "1.0"],
                    "instructions": "Tools that drive the __APP_NAME__ app on this Mac. Destructive tools only report what they would change unless yes is true.",
                ]
            case "ping":
                reply["result"] = [:] as JSONObject
            case "tools/list":
                reply["result"] = ["tools": AgentCommands.all.map(tool)]
            case "tools/call":
                reply["result"] = call(params)
            default:
                reply["error"] = ["code": -32601, "message": "unknown method \(method)"]
            }
            print(JSON.string(reply))
            fflush(stdout)
        }
    }

    private static func tool(_ command: AgentCommand) -> JSONObject {
        var schema = AgentCLI.schema(command)
        schema["name"] = command.name.replacingOccurrences(of: " ", with: "_")
        if var input = schema["inputSchema"] as? JSONObject {
            input["additionalProperties"] = false
            schema["inputSchema"] = input
        }
        schema["annotations"] = ["readOnlyHint": command.readOnly, "destructiveHint": command.destructive]
        schema["readOnly"] = nil
        schema["destructive"] = nil
        return schema
    }

    /// Validate original JSON values before converting to the CLI wire representation.
    private static func validatedArguments(_ values: JSONObject, for command: AgentCommand) throws -> [String: String] {
        guard values.count <= 32 else { throw AgentError.usage("at most 32 arguments are allowed") }
        let known = Set(command.params.map(\.name) + (command.destructive ? ["yes"] : []))
        guard Set(values.keys).isSubset(of: known) else { throw AgentError.usage("unknown argument") }
        var result: [String: String] = [:]
        for parameter in command.params {
            guard let value = values[parameter.name] else {
                if parameter.required { throw AgentError.usage("missing \(parameter.name)") }
                continue
            }
            switch parameter.kind {
            case .string:
                guard let string = value as? String, string.utf8.count <= 16_384,
                      !parameter.required || !string.isEmpty else { throw AgentError.usage("\(parameter.name) must be a bounded nonempty string") }
                result[parameter.name] = string
            case .boolean:
                guard let number = value as? NSNumber, CFGetTypeID(number) == CFBooleanGetTypeID() else {
                    throw AgentError.usage("\(parameter.name) must be a JSON boolean")
                }
                result[parameter.name] = number.boolValue ? "true" : "false"
            case .integer:
                guard let number = value as? NSNumber, CFGetTypeID(number) != CFBooleanGetTypeID(),
                      let integer = Int(number.stringValue) else { throw AgentError.usage("\(parameter.name) must be a JSON integer in range") }
                result[parameter.name] = String(integer)
            }
        }
        if let value = values["yes"], command.destructive {
            guard let number = value as? NSNumber, CFGetTypeID(number) == CFBooleanGetTypeID() else {
                throw AgentError.usage("yes must be a JSON boolean")
            }
            result["yes"] = number.boolValue ? "true" : "false"
        }
        return result
    }

    private static func call(_ params: JSONObject) -> JSONObject {
        let name = (params["name"] as? String ?? "").replacingOccurrences(of: "_", with: " ")
        do {
            guard let command = AgentCommands.all.first(where: { $0.name == name }) else { throw AgentError.usage("unknown tool \(name)") }
            guard params["arguments"] == nil || params["arguments"] is JSONObject else {
                throw AgentError.usage("arguments must be a JSON object")
            }
            let arguments = try validatedArguments(params["arguments"] as? JSONObject ?? [:], for: command)
            let reply = try AgentSocket.send(JSON.data(["command": name, "args": arguments]), launch: true)
            let object = (try? JSONSerialization.jsonObject(with: reply) as? JSONObject) ?? [:]
            let ok = object["ok"] as? Bool == true
            return ["content": [["type": "text", "text": JSON.string(ok ? object["result"] ?? [:] : object["error"] ?? [:])]],
                    "isError": !ok]
        } catch let error as AgentError {
            return ["content": [["type": "text", "text": JSON.string(error.json)]], "isError": true]
        } catch {
            return ["content": [["type": "text", "text": error.localizedDescription]], "isError": true]
        }
    }
}
