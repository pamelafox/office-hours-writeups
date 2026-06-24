# June 23, 2026 Office Hours Q&A

## Announcements

📹 [0:58](https://youtube.com/watch?v=qYNprnqRhWE&t=58)

### Copilot & VS Code

- **Copilot BYOK (Bring Your Own Key)** is now available everywhere — CLI, app, VS Code. Supports Ollama, Foundry, OpenRouter, and any OpenAI/Anthropic endpoint for maximum model choice and cost efficiency. ([GitHub changelog](https://github.blog/changelog/2026-06-17-copilot-cli-supports-enterprise-bring-your-own-key-byok-models/), [VS Code blog](https://code.visualstudio.com/blogs/2026/06/18/byok-vscode))
- **Auto model selection GA** in Copilot Chat with a 10% billing discount. ([GitHub changelog](https://github.blog/changelog/2026-06-17-auto-mode-in-copilot-chat-available-for-all-users/))
- **MAI-Code-1-Flash** expanded across Copilot CLI, app, and VS Code — described as similar to Haiku in capability, good for simpler tasks. ([GitHub changelog](https://github.blog/changelog/2026-06-18-mai-code-1-flash-available-on-more-copilot-surfaces/))
- **Enterprise-managed MCP authorization** now in VS Code (v1.125). ([VS Code updates](https://code.visualstudio.com/updates/v1_125), [MCP blog post](https://thenewstack.io/mcp-gets-its-missing-enterprise-authorization-layer/))

### Agent Framework

- **Python 1.9.0** released with AgentLoopMiddleware (Ralph loop, predicate loop, judge loop), tool approval changes, and orchestrations 1.0. ([Release notes](https://github.com/microsoft/agent-framework/releases/tag/python-1.9.0))
- **HarnessAgent** added in 1.7.0 — a batteries-included preconfigured agent with call history persistence, compaction, to-do mode, memory, and skills. Similar to LangChain deep agents or the Copilot SDK. ([Release notes](https://github.com/microsoft/agent-framework/releases/tag/python-1.7.0))

### Industry

- **uv audit**: Native vulnerability scanning for Python dependencies. ([Blog post](https://astral.sh/blog/uv-audit))
- **SkillsBench**: Benchmark for how well models use skills — 87 tasks, 24 model-harness configurations. ([skillsbench.ai](https://www.skillsbench.ai/))
- **"A Theory of Prompt Injection"** paper: Explains prompt injection as role confusion — LLMs identify roles by writing style, not tags. ([Paper](https://role-confusion.github.io/))
- **OpenAI Responses API**: WebSocket mode for lower latency and tool search for large toolsets. ([Docs](https://developers.openai.com/api/docs/guides/tools-tool-search))

### What Pamela's been up to

- Ran a 4-hour MCP workshop: Using & building MCP servers with GitHub Copilot. ([Tutorial](https://pamelafox.github.io/github-copilot-mcp-tutorial/))
- Announced Microsoft IQ Deep Dive with Python series (July 28–30). ([Sign up](https://aka.ms/IQDeepDivePython/series/x))
- Experimented with "In the Weights" website to see if LLMs have memorized her. ([intheweights.com](https://intheweights.com/p/pamela-fox))
- Preparing model-swap-workshop for AI Engineer World's Fair. ([Repo](https://github.com/pamelafox/model-swap-workshop))
- Next week's office hours may be cancelled due to AI Engineer World's Fair (June 29-July 2 in San Francisco).

## Discussion: New agent-framework loop middleware

📹 [6:01](https://youtube.com/watch?v=qYNprnqRhWE&t=361)

The [Agent Framework Python 1.9.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.9.0) release added an [AgentLoopMiddleware](https://github.com/microsoft/agent-framework/pull/6174) for re-running agents until some condition is met. While agents already run until they reach an answer, that answer may not match your actual goal. The middleware offers three loop strategies:

- **Ralph loop**: The original famous loop (basis for CodeX's and Claude Code's "goal" mode). It has no explicit exit criteria, is bounded by an optional max iteration count, and includes feedback tracking with a progress log.
- **Predicate loop**: Uses a callback function that returns true/false — e.g., "are there remaining to-dos?" or "are background tasks still running?" The agent keeps looping until the predicate returns false.
- **Judge loop**: An LLM judge decides whether the original request was answered using structured output. The agent keeps looping if the judge says it's not done.

The release also added changes to approval handling, since human approval can interrupt loops. Additionally, in 1.7.0 they added a [HarnessAgent](https://github.com/microsoft/agent-framework/pull/6041) — a batteries-included preconfigured agent with call history persistence, compaction, to-do mode, memory, and skills (similar to LangChain deep agents or the Copilot SDK).

Links shared:

* [AgentLoopMiddleware PR](https://github.com/microsoft/agent-framework/pull/6174)
* [HarnessAgent PR](https://github.com/microsoft/agent-framework/pull/6041)

### Do loops without proper specs lead to high token consumption and undesired features?

📹 [11:06](https://youtube.com/watch?v=qYNprnqRhWE&t=666)

Yes — Pamela agreed that using loops without proper specs can lead to high token consumption. She gave the example of the Agent Framework's new judge loop sample, where the agent prompt says "explain why the sky is blue" but the judge checks for "includes at least one good joke." That's going to loop for a long time because the agent never got asked for a joke.

The key insight: your agent prompt should have as much information as your judge prompt. If your output consistently fails the LLM-as-judge check, that criteria probably belongs in the system prompt too. The LLM-as-judge should be a second check, not the primary source of requirements.

One exception: you might intentionally keep your system prompt shorter to save tokens, relying on the judge to catch edge cases. But that means your assumptions could break when you switch models. Also consider prompt caching — a few extra sentences in the system prompt isn't a big deal if you can take advantage of caching.

### Are the loops open to modify the middleware to add agents, evaluation, etc?

📹 [14:27](https://youtube.com/watch?v=qYNprnqRhWE&t=867)

Yes. The loop middleware is an agent middleware (the highest-level middleware in Agent Framework), which intercepts the `agent.run` call and gets access to messages, the agent object, the result, and whether to terminate.

You can add additional middleware, or since it's all open source, you can copy the loop middleware code and modify it to suit your needs. Pamela emphasized that middleware is generally pretty modifiable — it's designed so you can build your own. She recommends taking a framework's middleware as a basis and modifying it rather than feeling limited to what's provided out of the box.

Links shared:

* [Agent middleware layers (presentation)](https://github.com/Azure-Samples/python-agentframework-demos/blob/main/presentations/english/session-1/README.md#agent-middleware-layers)

## How do users authenticate to multiple MCP servers in production systems?

📹 [20:07](https://youtube.com/watch?v=qYNprnqRhWE&t=1207)

For general users (not developers) using MCP with agents like GitHub Copilot or Claude Desktop, the new [enterprise managed authorization](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/) feature helps. Admins can provision MCP connectors for their whole organization through their identity provider (starting with Okta), so users get connector access automatically on first login without per-app OAuth.

Without enterprise managed auth, users individually authenticate to each MCP server. The coding agent (VS Code, Claude, etc.) acts as an OAuth client — it remembers connections, handles refresh tokens, and stores credentials. Pamela demonstrated this with the Hugging Face MCP server, showing how VS Code remembers previous logins and handles re-authentication automatically.

The advantage of enterprise managed authorization is better auditing and fewer login prompts when multiple MCP servers go through the same identity provider. Currently Okta is the first supported identity provider; Entra does not support it yet.

Links shared:

* [Enterprise-Managed Authorization: Zero-touch OAuth for MCP](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/)
* [Configure MCP server access for your organization (GitHub docs)](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-server-access)

### Is the authorization linked with specific MCP tool permissions? Where would that be configured?

📹 [26:57](https://youtube.com/watch?v=qYNprnqRhWE&t=1617)

At the enterprise level, GitHub Copilot Enterprise/Business lets you [create an MCP registry](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-registry) and set an allow list policy to control which MCP servers developers can use. However, this is at the server level, not the tool level — Pamela didn't see a way to enforce per-tool restrictions at the enterprise level.

For per-tool restrictions, there are a few options:
- **If you build the server yourself**: You can decorate tools with group requirements and check user membership via the Graph API before allowing tool access. Pamela showed an example from her [Cosmos DB identity-aware MCP server](https://github.com/pamelafox/azure-cosmosdb-identity-aware-mcp-server/blob/main/servers/main.py) where tools require the admin group.
- **As a user**: You can turn tools on/off, make custom agents (`.agent.md` files) that only allow certain tools, or use [tool filtering](https://blog.pamelafox.org/2025/09/filter-tools-from-mcp-servers.html).
- **For external servers you don't control**: You'd need some sort of proxy/middleware.

Links shared:

* [Filter the tools from MCP servers (blog post)](https://blog.pamelafox.org/2025/09/filter-tools-from-mcp-servers.html)
* [Cosmos DB identity-aware MCP server](https://github.com/pamelafox/azure-cosmosdb-identity-aware-mcp-server/blob/main/servers/main.py)
* [MCP allow list enforcement (GitHub docs)](https://docs.github.com/en/copilot/reference/mcp-allowlist-enforcement)

### Can Foundry Toolbox be used for MCP tool filtering/proxying?

📹 [33:40](https://youtube.com/watch?v=qYNprnqRhWE&t=2020)

Yes — Foundry Toolbox is a possible option for this because when you add an MCP server to a toolbox, you can allow only certain tools. Pamela demonstrated creating a toolbox in the Foundry portal and showed that when configuring an MCP server within it, you can specify which tools to allow.

However, the Foundry Toolbox MCP server currently doesn't work well as a user-facing MCP server connected directly from VS Code, because it uses Microsoft Entra which doesn't yet fully support MCP OAuth (DCR/CIMD). It works well for programmatic Python agents (like those built with Microsoft Agent Framework), but not for the interactive VS Code MCP flow. Pamela shared a [example Agent Framework code](https://gist.github.com/pamelafox/b5a415a103e80966d68fa4aee2b2acf5) for connecting to a Foundry Toolbox. When you create a toolbox in Foundry, that code will be auto-generated for you.

Links shared:

* [Foundry Toolbox MAF code (gist)](https://gist.github.com/pamelafox/b5a415a103e80966d68fa4aee2b2acf5)

## Discussion: Tool search is now a first-class model capability

📹 [42:40](https://youtube.com/watch?v=qYNprnqRhWE&t=2560)

Following up from a previous week's discussion about deferred tool loading and large MCP toolsets, Pamela shared that both OpenAI and Anthropic now train their models with [tool search](https://developers.openai.com/api/docs/guides/tools-tool-search) as a first-class capability. The models have actually been trained to search for tools when they don't have what they need, not just the harnesses (like coding agents) implementing it.

This is specifically designed with MCP in mind — the OpenAI docs even reference MCP directly, recommending deferred loading for MCP servers. VS Code implements this too: when you add a new MCP server, it asks whether to always include the tools or defer loading, with defer as the default.

Links shared:

* [OpenAI tool search docs](https://developers.openai.com/api/docs/guides/tools-tool-search)
* [Anthropic tool search docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)

## Have you seen any use cases for agents doing write actions in production systems?

📹 [44:53](https://youtube.com/watch?v=qYNprnqRhWE&t=2693)

Yes, several patterns:

- **Code modernization**: Agents making wide-scale programmatic code changes and sending PRs for human review. This works well because PRs are reviewable.
- **Automated emails/calendar events**: Agents sending communications to event attendees.
- **Report generation**: Agents writing new documents (reports, summaries) that sit somewhere ready for human review — lower risk since they're creating something new.
- **Customer service/bookings**: A company presented at Build about using agents for customer service handling refunds and rebookings across airline agencies in Asia.
- **Data classification**: LLMs used in production for classification tasks, sometimes with agent tooling.

The key principle: be most cautious when agents update existing human-created documents or delete anything. Writing something new (PRs, reports) that awaits human review is lower risk. Always set up evaluations and tests.
