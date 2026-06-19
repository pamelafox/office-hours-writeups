# June 17, 2026 Office Hours Q&A

## Any learning resources for model evaluation?

📹 [7:18](https://youtube.com/watch?v=hQAqiMp57SY&t=438)

Pamela discussed several resources for learning about model evaluation. The most recent coverage was in the [Host your agents on Foundry live stream series](https://github.com/orgs/microsoft-foundry/discussions/380), which included a session on hosted agents that covered evaluations using the Foundry portal. There were also sessions on evaluations at Microsoft Build 2026.

She then demoed the new **rubric evaluators** feature in Foundry, which is based on [ASSERT research](https://commandline.microsoft.com/assert-written-intent-executable-evals/). The idea is to make evaluation easier by auto-generating custom evaluation rubrics. You describe your agent (e.g., "this agent queries data from a company knowledge base and gives back answers, it must always give back citations"), and Foundry generates a set of weighted sub-evaluators — things like evidential grounding, citation coverage and placement, citation traceability, uncertainty and limitations, and general quality. You can then run these rubrics against an agent, model, or data set, either through the portal or programmatically from Python.

She also shared her experience with evaluations in the [azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo/releases/tag/2026-06-11), where she upgraded the default model to gpt-5.4-mini. Finding a model that was better across the board on every metric was hard, and reasoning models no longer obey the seed parameter, making evaluations much more variable. Her approach is to run evals multiple times and calculate averages and statistical deviations.

For general guidance on evaluation, she recommended [Hamel Husain's blog](https://hamel.dev/) for best practices on using LLMs as judges.

Links shared:

* [Host your agents on Foundry live stream series](https://github.com/orgs/microsoft-foundry/discussions/380)
* [ASSERT: Turn specs into evals for any agent](https://commandline.microsoft.com/assert-written-intent-executable-evals/)
* [Rubric evaluators in Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rubric-evaluators)
* [Hamel Husain's blog](https://hamel.dev/)

## Where should I start learning about AI?

📹 [26:43](https://youtube.com/watch?v=hQAqiMp57SY&t=1603)

For people new to generative AI, Pamela recommended starting with the [Microsoft IQ Deep Dive with Python](https://developer.microsoft.com/en-us/reactor/series/S-1684/) series, a nine-part series covering the fundamentals. She also shared her blog post on [How I learn about generative AI](https://blog.pamelafox.org/2025/08/how-i-learn-about-generative-ai.html) for other approaches and resources. The team may run the beginner series again if there's enough interest.

Links shared:

* [Microsoft IQ Deep Dive with Python series](https://developer.microsoft.com/en-us/reactor/series/S-1684/)
* [Level up your Python + AI skills with our complete series](https://techcommunity.microsoft.com/blog/educatordeveloperblog/level-up-your-python--ai-skills-with-our-complete-series/4464546)
* [How I learn about generative AI (blog post)](https://blog.pamelafox.org/2025/08/how-i-learn-about-generative-ai.html)

## Is Scout (from Build) the same as OpenClaw?

📹 [31:00](https://youtube.com/watch?v=hQAqiMp57SY&t=1860)

Scout is basically a Microsoft-specific version of [OpenClaw](https://github.com/microsoft/openclaw-dev). It's a desktop app with automations and has really good integrations with Microsoft 365. OpenClaw is the open-source, bare version — just the Node repo that you can deploy yourself (e.g., on Azure Container Apps). By default, OpenClaw runs in an isolated container and doesn't have access to anything until you explicitly set up access. Scout adds those Microsoft 365 integrations on top.

Pamela also mentioned she deployed OpenClaw on Azure Container Apps and fixed a few issues with doing it on Mac, and encouraged people to try it out.

Links shared:

* [OpenClaw Dev repo](https://github.com/microsoft/openclaw-dev)

## Do the three IQs come with attack protection?

📹 [32:43](https://youtube.com/watch?v=hQAqiMp57SY&t=1963)

This is a continuation of a [previous discussion about AI security and guardrails](https://github.com/orgs/microsoft-foundry/discussions/280#discussioncomment-17255540). Pamela recapped the security mechanisms available across the Microsoft AI stack. Thanks to that question from the previous office hours, the docs for detecting content filtering in the [Responses API](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses?tabs=python#handle-guardrails-and-content-filtering) were improved.

For data protection, **Purview** lets you label data with sensitivity levels (e.g., highly confidential, public) so agents know how data is classified. Matt recently added Purview integration to a branch of the [azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo).

Pamela also explored [Foundry IQ's new governance and enterprise AI security capabilities](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-iq-new-governance-and-enterprise-ai-security-capabilities/4524825), and [Microsoft Agent 365](https://learn.microsoft.com/en-us/security/security-for-ai/agent-365-security) — a control plane for agents that wraps together Entra, Defender, Purview, and Intune. Agent 365 provides threat detection, including Defender integration with Work IQ MCP that can block unsafe tool invocations.

The discussion also touched on whether there should be a code analysis tool specifically for agent security — something that would look at your code and recommend improvements before you even deploy. The existing GitHub Copilot security review skill does code analysis, but it's generic rather than agent-specific.

Links shared:

* [Handle guardrails and content filtering in the Responses API](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses?tabs=python#handle-guardrails-and-content-filtering)
* [Foundry IQ: New governance and enterprise AI security capabilities](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-iq-new-governance-and-enterprise-ai-security-capabilities/4524825)
* [Secure AI agents at scale using Microsoft Agent 365](https://learn.microsoft.com/en-us/security/security-for-ai/agent-365-security)

## How many tools should ideally be in an agent? Should I use sub agents if there are too many tools?

📹 [45:10](https://youtube.com/watch?v=hQAqiMp57SY&t=2710)

There's no hard and fast rule. Every model sees tools differently — this [Tool Schema Rendering Atlas](https://evalstate-tool-research.static.hf.space/index.html) shows the actual differences in how tools are sent to models. The best approach is to run evaluations and check:

- Is the agent selecting the right tools at the right time?
- Is it using context efficiently?
- What's the latency and cost?

Reasons you might want to split into sub agents:
- **Context reduction**: Sub agents reduce the amount of context in the main agent
- **Risk isolation**: Less tools and functionality makes evaluation more deterministic and lowers security risk
- **Scoped tasks**: Coding agents load everything because tasks are diverse, but for more scoped use cases, fewer tools per agent can be better

There doesn't appear to be a hard limit on number of tools per model — the practical limits are how smart the model is and how large its context window is. Models also vary in their ability to correctly select and call tools, so evaluation is key.

Links shared:

* [Tool Schema Rendering Atlas](https://evalstate-tool-research.static.hf.space/index.html)

### Can tools have sub tools?

📹 [50:27](https://youtube.com/watch?v=hQAqiMp57SY&t=3027)

Not exactly. If you're trying to reduce the context of tool definitions, there's a concept of **deferred tool loading** (used by GitHub Copilot, for example) where only top-level tool groups are loaded initially, and specific tools are discovered and loaded on demand. But ultimately each tool is separate.

If a tool needs to call another tool, that's essentially the same thing as an agent — you'd structure it as a tool calling another agent inside of it. However, you don't always need to reach for tools. Sometimes a single LLM call with structured outputs inside a tool is sufficient — you only need tools when there are multiple possible actions that could happen.

## Announcements

### GitHub Copilot App now generally available

📹 [1:03](https://youtube.com/watch?v=hQAqiMp57SY&t=63)

The [GitHub Copilot App](https://gh.io/app-ga) is now generally available for macOS, Windows, and Linux. New features include **canvases** (custom UIs like to-do boards or deployment dashboards), **workflows/automations** (cron jobs — Pamela uses them for auto-accepting LinkedIn invites and daily issue triage), and bring-your-own-model support. The Copilot SDK and CLI also work with any open-source model, not just OpenAI.

### SpaceX to acquire Cursor for $60B; Cursor launches Origin

📹 [0:31](https://youtube.com/watch?v=hQAqiMp57SY&t=31)

[SpaceX announced plans to acquire Anysphere (Cursor) for $60 billion](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/). At the Cursor Compile conference, Cursor also launched **Origin** — a code storage and git hosting platform designed for agents.

### Anthropic Messages API and model swapping

📹 [16:44](https://youtube.com/watch?v=hQAqiMp57SY&t=1004)

Pamela discussed work to improve Anthropic model support in Foundry. The Anthropic Messages API has a nice feature for RAG: structured citation support where you specify documents that can be cited, and the model returns citations in a structured format (instead of hoping the model puts citations in square brackets). She shared a [model swap workshop repo](https://github.com/pamelafox/model-swap-workshop) that demonstrates swapping between multiple models (GPT-5.5, Mistral Large 3, Gemini K2.6, DeepSeek V4 Flash, and Anthropic models) deployed on Foundry.

Links shared:

* [Model swap workshop repo](https://github.com/pamelafox/model-swap-workshop)
* [Agent framework example with model swapping](https://github.com/pamelafox/python-stack-foundry-models/blob/main/examples/agentframework_agent.py)

### VS Code blog: Token efficiency improvements in Copilot Chat

📹 [22:53](https://youtube.com/watch?v=hQAqiMp57SY&t=1373)

A [new blog post](https://code.visualstudio.com/blogs/2026/06/17/improving-token-efficiency-in-github-copilot) covers how GitHub Copilot improves token efficiency through prompt caching. When you send a new message, the majority of the prompt is cached and cheaper to process. However, switching models mid-conversation loses the prompt cache entirely, increasing cost. Anthropic's API gives more control over caching with explicit cache breakpoints for tool definitions, system prompts, and conversation segments.

### Upcoming Microsoft IQ live stream series

📹 [25:18](https://youtube.com/watch?v=hQAqiMp57SY&t=1518)

A new live stream series on Microsoft IQ is coming at the end of July, covering Foundry IQ, Work IQ, and Fabric IQ, with office hours after each session.