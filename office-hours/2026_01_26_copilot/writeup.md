# GitHub Copilot CLI & SDK Exploration - January 26, 2026

📹 [Recording](https://www.youtube.com/live/Jkpov6Oygy0)

This livestream explored the GitHub Copilot CLI and the GitHub Copilot SDK for Python, testing various features and discovering several issues along the way.

## What We Tried

### GitHub Copilot CLI

#### Installation & Upgrade

📹 [0:00](https://youtube.com/watch?v=Jkpov6Oygy0&t=0)

- Upgraded from version 0.0.263 to 0.0.395 using npm
- Discovered that pressing Ctrl+C rapidly exits the CLI
- Staff mode activated (available for Microsoft/GitHub employees)
- Default model: Claude Opus 4.5

#### Slash Review Command

📹 [8:20](https://youtube.com/watch?v=Jkpov6Oygy0&t=500)

- Used `/review` to review code changes
- Tested multi-model review: `review my code with Opus, Gemini, and GPT-5.2 Codex`
- Three background agents ran in parallel, each doing code review
- Reviews from Opus and Gemini found legitimate issues (variable naming, performance)
- GPT-5.2 Codex was too slow to complete

#### Custom Agents

📹 [19:00](https://youtube.com/watch?v=Jkpov6Oygy0&t=1140)

- Tested the triagger custom agent from `.github/agents/`
- Agent found and recommended closing a stale issue
- **Issue discovered**: Agent couldn't close issues despite having explicit tool permissions in agent.md

#### MCP Server Setup

📹 [21:30](https://youtube.com/watch?v=Jkpov6Oygy0&t=1290)

- Attempted to add Microsoft Learn MCP server via `/mcp add`
- **Issue discovered**: Ctrl+S to save server config doesn't work on Mac

#### Keyboard Shortcuts Learned

- `Shift+Tab`: Cycle between plan and agent modes
- `Ctrl+D`: Queue up a prompt to run after current operation completes

### GitHub Copilot SDK (Python)

#### PR Visualization Example

📹 [30:00](https://youtube.com/watch?v=Jkpov6Oygy0&t=1800)

- Tested the PR visualization recipe from the SDK cookbook
- **Issue discovered**: Example code had outdated types (class names changed)
- Fixed enum comparison bug: `event.type == "assistant_message"` doesn't work because `SessionEventType` is an enum, not a string literal
- Successfully generated PR age visualization chart
- SDK shamed repository for having 34 open PRs with average age of 317 days

#### Model Selection

📹 [46:00](https://youtube.com/watch?v=Jkpov6Oygy0&t=2760)

- **Issue discovered**: Cannot use Opus 4.5 model - SDK has limited model selection (only claude-sonnet-4 and similar)

#### MCP Server Integration

📹 [50:00](https://youtube.com/watch?v=Jkpov6Oygy0&t=3000)

- Configured Microsoft Learn MCP server with SDK
- **Issue discovered**: MCP servers require explicit `tools=["*"]` configuration - empty list means no tools allowed
- Successfully got MCP server tools working after adding explicit tool permission

#### Custom Agent Configuration

📹 [58:00](https://youtube.com/watch?v=Jkpov6Oygy0&t=3480)

- Attempted to use existing `.github/agents/triagger.agent.md` with SDK
- **Issue discovered**: No factory method to load agent from existing agent.md file - must manually parse YAML and recreate config
- Tool namespacing differs between VS Code (`github/tool`) and CLI (`github_tool`)
- SDK successfully used triagger agent to find and close a stale issue

## Issues to Report to GitHub Team

### GitHub Copilot CLI Issues

1. **MCP Server Save Doesn't Work on Mac**
   - When using `/mcp add`, pressing Ctrl+S to save the server configuration does nothing
   - Workaround: None found

2. **Custom Agents Don't Respect Tool Whitelist**
   - Custom agents defined in `.github/agents/` have an `allowed_tools` section
   - CLI ignores this and uses its own tool set
   - Example: Triagger agent has explicit permission to close issues via GitHub MCP, but CLI said it couldn't close issues

3. **Unclear Which Agent Updates Are Displayed**
   - When running multiple review agents in parallel, the streaming output doesn't indicate which agent each update comes from

### GitHub Copilot SDK Issues

4. **Example Code Has Outdated Types**
   - PR visualization recipe references `CopilotClientAsync` which doesn't exist
   - Should be `CopilotClient` with async session methods
   - Options are now passed via `CopilotOptions` class instead of direct parameters

5. **Event Type Comparison Bug in Examples**
   - Example code compares `event.type == "assistant_message"` (string)
   - `SessionEventType` is an enum, so this never matches
   - Should use `event.type == SessionEventType.ASSISTANT_MESSAGE`

6. **Limited Model Selection**
   - Cannot use Opus 4.5 or other models
   - Only a small set of models are allowed (claude-sonnet-4, etc.)
   - Error message shown when attempting to use opus-4.5

7. **MCP Servers Require Explicit Tool Permission**
   - `tools=["*"]` must be explicitly set in MCP server config
   - Default (empty list) means no tools are allowed
   - This is counterintuitive and different from other agent frameworks

8. **Tool Execution Events Don't Show Arguments**
   - `event.data.tool_requests` exists but arguments aren't accessible as documented
   - Makes it hard to see what commands are being run
   - Only see tool names like "bash" without knowing what's being executed

9. **Assistant Messages Arrive as Blank Content**
   - For `SessionEventType.ASSISTANT_MESSAGE` events, `event.data.content` is empty
   - The actual message content appears to be in a different attribute
   - Causes output to show blank lines where messages should appear

10. **No Factory Method for Loading Existing Agents**
    - SDK requires manually parsing agent.md files and recreating `CustomAgentConfig`
    - Should have a method like `CustomAgentConfig.from_file("path/to/agent.md")`
    - Tool namespacing differs between VS Code format (`github/tool`) and CLI format (`github_tool`)

### General Interoperability Issues

11. **Disconnect Between VS Code and CLI/SDK Formats**
    - Agent.md files work in VS Code but require significant translation for CLI/SDK
    - Tool names use different separators (slash vs underscore)
    - MCP server configuration format differs

## Links Shared

- [Evan Boyle on X](https://x.com/_Evan_Boyle) - Follow for CLI updates
- [GitHub Copilot CLI Repo](https://github.com/github/copilot-cli)
- [GitHub Copilot CLI Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)
- [GitHub Copilot SDK Repo](https://github.com/github/copilot-sdk)
- [SDK Experiments Branch](https://github.com/Azure-Samples/azure-search-openai-demo/compare/main...pamelafox:azure-search-openai-demo:sdkexperiments)
- [Microsoft Learn MCP Server](https://learn.microsoft.com/en-us/training/support/mcp)

## Participants

Stream host: Pamela Fox (@PamelaFox)
Live chat contributors: @john0isaac, @CarlosPCmx, @arielrivera, @HatmanStack, @yashhgami, @takescake
