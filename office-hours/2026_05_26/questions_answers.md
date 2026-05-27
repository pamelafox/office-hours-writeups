## How do you like the GitHub Copilot Desktop app so far?

📹 [4:09](https://youtube.com/watch?v=mZ-WgdquFIE&t=249)

For Pamela personally, she loves the GitHub Copilot Desktop app, and sees no reason to use the CLI anymore, since she prefers graphical UIs over textual UIs. The desktop app is a wrapper for the CLI, so all MCP servers and skills are supported, plus extra features like workflows and inbox. It makes it easy to see what tools are being used, expand tool calls, and view code diffs.

The industry seems to have settled on similar UI paradigms across vendors. There's a spectrum from high code control to high agent agency:

<table>
<tr>
<th></th>
<th>Microsoft / GitHub</th>
<th>Google</th>
<th>Claude Code</th>
<th>OpenAI</th>
<th>OpenCode</th>
</tr>
<tr>
<td rowspan="5">High code control<br>↕<br>Low code control</td>
<td>VS Code + GitHub Copilot Chat</td>
<td>Antigravity IDE</td>
<td>VS Code + Claude Extension</td>
<td>?</td>
<td>?</td>
</tr>
<tr>
<td>VS Code Agents window</td>
<td>Antigravity IDE Agent Manager</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr>
<td>GitHub Copilot Desktop App</td>
<td>Antigravity 2.0</td>
<td>Claude Code Desktop App</td>
<td>Codex Desktop</td>
<td>OpenCode</td>
</tr>
<tr>
<td>GitHub Copilot CLI</td>
<td>Antigravity CLI</td>
<td>Claude Code CLI</td>
<td>Codex CLI</td>
<td>OpenCode</td>
</tr>
<tr>
<td>GitHub Copilot Cloud Agent</td>
<td>?</td>
<td>Claude GitHub App</td>
<td>?</td>
<td></td>
</tr>
</table>

### Can you create sub-agents with the GitHub Copilot desktop app?

📹 [13:15](https://youtube.com/watch?v=mZ-WgdquFIE&t=795)

It's unclear whether there's a UI-based way of making sub-agents in the desktop app. Skills can use sub-agents, and the desktop app has good support for skills, so sub-agents should work that way. There doesn't appear to be an explicit UI for creating sub-agents though — this needs to be confirmed with the team.

### Can you access the hooks of the GitHub Copilot desktop app?

📹 [17:23](https://youtube.com/watch?v=mZ-WgdquFIE&t=1043)

This is unknown — there doesn't appear to be documented hooks support for the desktop app yet. The GitHub Copilot CLI does support hooks, so the question is whether the desktop app exposes the same hook system. This is another question to follow up on with the product team.

## Are all models used through GitHub Copilot protected against prompt injection?

📹 [28:42](https://youtube.com/watch?v=mZ-WgdquFIE&t=1722)

According to the [GitHub Copilot model documentation](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features#ai-models), all models (including those hosted on Azure and AWS) go through GitHub Copilot's content filtering system for harmful/offensive content and public code matching. However, none of the model descriptions explicitly mention prompt injection protection specifically.

When setting up content safety filters, you can toggle on protections for "direct attack" or "indirect attack" (jailbreak attempts), but it's unclear whether those are enabled by default for Copilot models. The risk of enabling aggressive safety filters is false positives that frustrate users.

The discussion touched on the ["lethal trifecta"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) of security concerns: access to private data, ability to communicate externally, and exposure to untrusted content. Having many MCP servers enabled (Twitter, Gmail, Work IQ, etc.) with read/write access means an agent could theoretically take harmful actions if compromised by prompt injection.

Links shared:

* [NSA concerns in MCP design implementation](https://www.nsa.gov/) (shared by Sylvest)

## What security sandboxing options exist for coding agents?

📹 [34:59](https://youtube.com/watch?v=mZ-WgdquFIE&t=2099)

Several sandboxing options were discussed:

**[VS Code agent sandbox](https://code.visualstudio.com/docs/copilot/concepts/trust-and-safety#_agent-sandboxing)** (Settings → search "sandbox"): VS Code now has built-in sandbox settings for agent terminal commands, currently in preview. Options include fully off, on (very limited abilities), or on with network calls allowed. The tradeoff is that blocking network requests makes it hard to reference documentation.

**[Open Shell](https://github.com/NVIDIA/OpenShell)** (from Nvidia): Provides safe, private runtime sandboxing with declarative YAML policy files. Supports file system protection, network blocking, and process isolation. Has a `--copilot` flag for GitHub Copilot integration.

**[Docker SBX](https://docs.docker.com/reference/cli/sbx/)**: Runs AI coding agents in isolated microVM sandboxes. Install it and launch agents with `sbx run copilot`. Supports stored secrets through Docker's existing secret management. If you're already using Docker, this might be a natural fit.

For pure coding tasks, a sandbox with access to your issue tracker and documentation is usually sufficient. The difficulty comes with more varied productivity tasks (presentations, planning, research) that need broader web access.

## What is Docker Agent and how does it compare to Foundry hosted agents?

📹 [44:22](https://youtube.com/watch?v=mZ-WgdquFIE&t=2662)

[Docker Agent](https://docs.docker.com/ai-agents/) is a new way to define and run agents using YAML configuration files (similar to Claude agents). You describe what your agent does, specify which model to use, and define tools.

The interesting part is the number of ways you can expose your agent:
- **TUI** (Terminal UI)
- **CLI**
- **MCP mode**
- **A2A** (Agent-to-Agent)
- **ACP**
- **API server** (with SSE)
- **Chat server** (using Chat Completions API)

This is comparable to Foundry hosted agents in functionality. For models, it support a wide range of model providers, including Azure OpenAI deployments (with a key, not keyless). The variety of integration options is notable — we've moved beyond just full-stack chat apps to needing multiple integration protocols for agent-to-agent communication.

## Announcements

📹 [0:00](https://youtube.com/watch?v=mZ-WgdquFIE&t=0)

**Azure OpenAI Assistants API retiring August 26, 2026**: If you're using the Assistants API, you should migrate to the [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/assistants). There's a [migration guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate?tabs=python#migrate-classic-agents-to-new-agents) available.

**Agent Framework 1.6.0 released**: [Monty](https://github.com/microsoft/agent-framework/releases/tag/python-1.6.0) (a Python code sandbox) has been merged into agent-framework as a CodeAct provider, enabling more efficient tool calling.

**GitHub MCP server can reply to inline PR comments**: The [new tool](https://github.com/github/github-mcp-server/pull/1856) `add_reply_to_pull_request_comment` enables replying to inline PR review comments, useful for skills that collaboratively triage PR feedback.

**MCP release candidate (2026-07-28 RC)**: Major potential changes including a stateless core (no session ID), MCP apps built into the protocol, authorization hardening, and a deprecation policy. See the [modelcontextprotocol repo](https://github.com/modelcontextprotocol/modelcontextprotocol) for details.

**WorkOS auth.md**: A new [open agent registration protocol](https://workos.com/blog/agent-registration-with-auth-md) that builds on OAuth to give agents their own authorization endpoints.

**Gmail MCP server**: A colleague's [Gmail MCP server](https://github.com/mattgotteiner/gmail-local-mcp) that lets you search Gmail threads from your agent/desktop app.

**No office hours next week** due to Microsoft Build (June 2–3 in San Francisco). There is a virtual option for Build.
