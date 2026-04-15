## What is WorkIQ MCP and what does it work best for?

📹 [07:48](https://youtube.com/watch?v=EjHmFtoR8d4&t=468)

Pamela demos Work IQ, an MCP server that provides access to your Microsoft 365 data (Teams chats, emails, calendar, documents). It uses the same underlying retrieval as MS365 Copilot — you can access it from Teams, Edge browser (work mode), command line, or your coding agent. You add it to your `copilotmcpconfig.json` as a standard input/output (stdio) server.

There are two ways to use it:

1. **Directly via the CLI**: Use the `work IQ ask` command to chat with it directly, e.g., "What meetings do I have today?"
2. **As an MCP server tool**: Other agents can invoke Work IQ's `ask_work_iq` tool to query your M365 data as part of a larger workflow.

Pamela shows her [recap-my-week](https://github.com/pamelafox/recap-my-week) skill, which combines Work IQ, Twitter MCP, and GitHub MCP servers to generate a weekly activity summary. She uses it for reporting to her manager and generating weekly team rollups.

### How well does retrieval work?

📹 [29:35](https://youtube.com/watch?v=EjHmFtoR8d4&t=1775)

**What works well:** Personal productivity — weekly rollups, searching through newsletters and emails, finding presentations you or colleagues have given on topics. Finding meetings, documents, and presentations is faster at doing bulk searches than you could manually.

**What doesn't work well:** Highly structured queries or comprehensive retrieval. Getting every single chat with a particular person in strict chronological order doesn't work well yet. Questions like "What decision did we make about X?" can give wrong answers — Pamela tried asking about a product decision and it gave the opposite of what was actually decided. It can't reliably parse through conversation context, thumbs-up reactions, etc. to accurately determine outcomes. Retrieval for Teams chats especially needs to improve — the loose formatting makes them a hard retrieval problem.

**Overall take:** It's getting better over time. Use it for quick data gathering where you can verify the results, but don't rely on it for definitive answers about decisions or comprehensive retrieval.

Links shared:

* [Work IQ MCP Server](https://github.com/microsoft/work-iq)
* [Recap My Week skill](https://github.com/pamelafox/recap-my-week)

## Would autoresearch make sense for automatic RAG parameter tuning?

📹 [20:47](https://youtube.com/watch?v=EjHmFtoR8d4&t=1247)

Pamela has talked with colleagues experimenting with [autoresearch](https://github.com/karpathy/autoresearch) for vector search tuning, finding more efficient heuristics to speed up vector search for RAG.

For **numeric parameters** (temperature, reasoning effort), tuning is essentially running a matrix of evals and seeing which performs better. Autoresearch could help with hill-climbing — cutting out parameter combinations that clearly aren't worth pursuing. For example, if medium reasoning effort scores better than high, you might skip extra-high entirely.

For **text parameters** (prompts, agent skills), Pamela recommends looking at DSPy's [GEPA optimize_anything](https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/) approach. This was discussed at a recent DSPy meetup and can be used to optimize agent skills, cloud algorithms, agent architecture, and prompt optimization. She hasn't tried it yet but finds the approach compelling.

The practical question is: what parameters are worth fiddling with, how many evals can you afford to run, and which parameters are text (where optimize_anything helps) vs. numeric (where a systematic matrix of evals may suffice)?

Links shared:

* [autoresearch (Karpathy)](https://github.com/karpathy/autoresearch)
* [GEPA: optimize_anything blog post](https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/)
* [DSPy](https://github.com/stanfordnlp/dspy)

## Is deploying OpenClaw safe? What about privacy concerns?

📹 [35:27](https://youtube.com/watch?v=EjHmFtoR8d4&t=2127)

Pamela says the privacy concerns are definitely founded. The security risk with OpenClaw comes from giving agents access to your accounts and credentials (iMessage, Gmail, etc.) — that's what makes any agent insecure.

Microsoft is working on deploying OpenClaw to Azure in sandboxed containers with guardrails, and developers can look forward to more guidance on deploying OpenClaw securely.

The open question is: how capable will OpenClaw be inside a highly sandboxed environment? At its heart, OpenClaw is just another agent harness (like Codex or GitHub Copilot) — it runs tools in a loop with its own memory system. Its popularity came from its many built-in integrations, but those integrations are also where the security risks come from.

The plan is to start with a sandbox, then incrementally add tool access — "okay, you have access to just this" — so you can control what it can do while still finding it useful. OpenClaw is also more long-running and autonomous than other agents, which is what people like about it.

Bruno (colleague) has also been building a .NET version of OpenClaw, and there are Reactor sessions available about it.

Links shared:

* [Microsoft Reactor — OpenClaw sessions](https://developer.microsoft.com/en-us/reactor/?search=openclaw)
* [NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/) — the "enterprise wrapper" for OpenClaw

## How do I publish a Foundry hosted agent as an M365 Copilot agent?

📹 [48:23](https://youtube.com/watch?v=EjHmFtoR8d4&t=2903)

The [documentation says](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents#publish-hosted-agents-to-channels) you should be able to publish hosted agents to M365 Copilot and Teams channels, but it seems the publish button was removed from hosted agents this week. She's asking the product team for more information.

Links shared:

* [Hosted agents — publish to channels (docs)](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents#publish-hosted-agents-to-channels)

## Are there good resources to dig deeper on AI agents deployment?

📹 [52:41](https://youtube.com/watch?v=EjHmFtoR8d4&t=3161)

For Foundry hosted agents specifically, Pamela recommends **waiting about two weeks** for the upcoming live stream series ([Host your agents on Foundry](https://aka.ms/AgentsOnFoundry/series), Apr 27-30), since the SDKs are actively being redone and things are changing rapidly.

In the meantime, she recommends starting with the [seattle-hotel-agent](https://github.com/puicchan/seattle-hotel-agent) AZD example repo and the corresponding [blog post about azd AI agent debugging](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-logs-status/). That's what she used as the basis for her own hosted agent, and what she had a colleague use to get started. If you run into issues, file them in the AZD repo.

Links shared:

* [seattle-hotel-agent (AZD example)](https://github.com/puicchan/seattle-hotel-agent)
* [Azure Developer CLI: Debug hosted AI agents from your terminal](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-logs-status/)
* [Hosted agents overview (docs)](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents)
* [Deploy a hosted agent (tutorial)](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent?tabs=bash)

## Announcements

📹 [00:57](https://youtube.com/watch?v=EjHmFtoR8d4&t=57)

**Responses API migration:**

The [azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) migration agent is live. Pamela has now migrated pretty much every sample over to the Azure Responses API, including the large RAG sample. The Responses API enables easy access to built-in code interpreter and web search tools.

**Copilot CLI remote control from mobile:**

You can now [monitor and steer a running Copilot CLI session from your phone](https://github.blog/changelog/2026-04-13-remote-control-cli-sessions-on-web-and-mobile-in-public-preview/) using `copilot --remote`. This lets you kick off long-running tasks and check in from your mobile device.

**Copilot CLI multi-model reflection (rubber duck):**

The new [rubber duck feature](https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-combines-model-families-for-a-second-opinion/) has Copilot CLI use a different model family to provide a second opinion and critique on plans and implementations.

**VS Code agent customizations:**

A [new VS Code window](https://www.youtube.com/watch?v=os2eqa69gko) shows all your agent customizations in one place — AGENTS.md files, custom instructions, skills, and more.

**Agent-first development video series:**

Gwen's [introduction to agent-first development](https://code.visualstudio.com/learn/foundations/introduction-to-agent-first-development) series covers building apps with VS Code and Copilot using an agent-first approach.

**ParseBench document parsing benchmark:**

[ParseBench](https://www.llamaindex.ai/blog/parsebench) is a new benchmark with 2,000+ human-verified pages and 167K test rules for evaluating document OCR quality across tables, charts, formatting, and more.

**DSPy meetup and talks:**

Recent DSPy meetup featured talks on reasoning models and the GEPA optimize_anything approach. Dropbox also presented on search relevance with DSPy.

**MCP conformance suite:**

The [MCP conformance suite](https://github.com/modelcontextprotocol/conformance) is a tool for testing whether your MCP server complies with the MCP specification.

**Review PR comments skill:**

Pamela built a [review-pr-comments](https://github.com/pamelafox/review-pr-comments) Copilot CLI skill that reviews comments on an active pull request and decides whether to accept, iterate, or reject the suggested changes.

**Personal projects:**

* [recap-my-week](https://github.com/pamelafox/recap-my-week) — Agent skill that combines Work IQ, Twitter, and GitHub MCP servers to generate a weekly activity summary
* [comedy-roast](https://github.com/pamelafox/comedy-roast-skill) — Agent skill that generates a comedy roast based on your week's activity

**Anthropic — Project Glasswing:**

Discussed [Project Glasswing](https://www.anthropic.com/glasswing), Anthropic's new initiative to secure critical software for the AI era.
