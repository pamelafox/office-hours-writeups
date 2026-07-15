# July 14, 2026 Office Hours Q&A

## Announcements

### GPT-5.6 is available in GitHub Copilot and Microsoft Foundry

📹 [0:48](https://youtube.com/watch?v=Bvlb_LD7orA&t=48)

OpenAI's GPT-5.6 family is available in [GitHub Copilot](https://github.blog/changelog/2026-07-09-openais-gpt-5-6-sol-terra-and-luna-are-now-available-in-github-copilot/) and Foundry. Pamela had moved most coding work from Opus to GPT-5.6 Sol at medium reasoning. Sol is cheaper and more conservative, sometimes needing explicit encouragement to finish longer tasks. The [model guidance](https://developers.openai.com/api/docs/guides/latest-model) recommends leaner prompts, stating each instruction once, simplifying tool descriptions, and defining autonomy and approval boundaries.

New capabilities include hosted JavaScript for programmatic tool calling, multi-agent support, explicit cache breakpoints, persisted reasoning, and additional reasoning modes. Sol Ultra coordinates multiple agents across parallel workstreams but was available in Codex rather than Copilot at the time of the session. Medium or high reasoning is enough for most work. MAI Code 1 Flash is a cheaper, Haiku-class option for smaller tasks.

### Agent Framework includes a batteries-included harness

📹 [16:44](https://youtube.com/watch?v=Bvlb_LD7orA&t=1004)

The [Agent Framework harness](https://learn.microsoft.com/en-us/agent-framework/agents/harness) adds compaction, persistence, todos, memory, approvals, OpenTelemetry, web search, skills, background agents, a shell environment, and configurable looping on top of the base agent. The [Tokenomics video](https://www.youtube.com/watch?v=mB0IyELzjRg) covers context windows, caching, model routing, and other ways to manage token cost.

### Markdown-first options make cloud agents easier to build

📹 [20:00](https://youtube.com/watch?v=Bvlb_LD7orA&t=1200)

[GitHub Agentic Workflows](https://github.com/githubnext/agentics/tree/main/workflows) combine constrained YAML front matter with Markdown instructions. The front matter limits permissions, network access, tools, and safe outputs; the Markdown describes the work. This is useful for repository automation such as issue triage, release status, and weekly digests. Workflows can use [multiple AI engines](https://github.github.com/gh-aw/reference/engines/) (Copilot, Claude, Codex, Gemini, etc.). Bruno's [weekly AI news digest](https://github.com/elbruno/weekly-ai-news-digest) is a good example.

The [Azure Functions serverless agents runtime](https://learn.microsoft.com/en-us/azure/azure-functions/functions-serverless-agents-runtime#agent-files) uses a similar Markdown-first approach for event-driven agents. Agent files can use HTTP, queue, blob, Event Grid, and Service Bus triggers, connect to MCP servers and [Azure connectors](https://connectors.azure.com), load skills, and call custom Python tools. Use Agent Framework or LangChain when full code control matters, serverless agent files when Markdown and managed triggers are enough, and Copilot app automations for local workflows.

### GitHub Copilot desktop can run deployment work in parallel

📹 [30:38](https://youtube.com/watch?v=Bvlb_LD7orA&t=1838)

Pamela used the Copilot desktop app to prepare multiple changes to the [Azure Search OpenAI demo](https://github.com/Azure-Samples/azure-search-openai-demo) in parallel, including unattended test deployments. Making the repository parallel-friendly required isolated `azd` environments, environment-specific Azure resource names, and configurable local ports. Once those constraints were in place, an agent could deploy several test environments overnight, verify them, and return a morning report without making the user the deployment bottleneck.

### Foundry hosted agents are generally available

📹 [58:36](https://youtube.com/watch?v=Bvlb_LD7orA&t=3516)

The Foundry hosted agents product manager confirmed during the session that hosted agents are generally available. Some features within the broader Foundry Agent Service may still be in public preview.

## Should a larger model create the plan for a smaller model to implement?

📹 [13:10](https://youtube.com/watch?v=Bvlb_LD7orA&t=790)

Yes, that can work. One suggested setup is GPT-5.6 Sol as the primary driver with GPT-5.4 for cost-sensitive implementation work. The main tradeoff is prompt caching: switching models within one session loses the benefit of cached context.

A better handoff is a durable Markdown artifact such as `plan.md`, `AGENTS.md`, or an architectural decision record. Keep that source of truth concise and current, then start a new session with whichever model fits the next task. Fresh sessions reduce stale context and make it easier to choose a cheaper implementation model without losing the plan.

Best practices discussed:

- Keep `agents.md`, `plan.md`, and skills documentation constantly up to date
- Create new sessions frequently — less old context means more model flexibility
- Use ADRs (Architectural Decision Records): plan first, then implement, then verify

The [Tokenomics video](https://www.youtube.com/watch?v=mB0IyELzjRg) from Microsoft Mechanics covers token economics, caching, and model routing strategies.

## Can the Codex CLI run inside the GitHub Copilot desktop app?

📹 [35:45](https://youtube.com/watch?v=Bvlb_LD7orA&t=2145)

Not currently. The Copilot desktop app is built on the Copilot CLI harness and does not support replacing that harness with the Codex CLI. VS Code is more agent-agnostic — extensions and alternate harnesses can provide more flexibility there. The desktop app is more opinionated, so it may never offer the same range of harness choices.

## How should agents be built and deployed on AKS, and can they be registered with Foundry?

📹 [38:17](https://youtube.com/watch?v=Bvlb_LD7orA&t=2297)

Deploy your agent on AKS and then register it with Azure Foundry using the external agent registration flow. Foundry provides observability and control-plane capabilities while AKS hosts the runtime. If you want Microsoft to host and manage the agent lifecycle instead, use Foundry Hosted Agents rather than AKS.

Links shared (provided after the session by colleagues):

* [External agent registration](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/register-external-agent?tabs=portal)
* [AKS Agentic CLI](https://learn.microsoft.com/en-us/azure/aks/agentic-cli-for-aks-overview)
* [AKS AI/ML overview](https://learn.microsoft.com/en-us/azure/aks/ai-ml-overview)
* [AI Agent Protocol sample](https://github.com/leestott/generative-ui-foundry-hosted-agents)
* [AKS + tracing sample](https://github.com/nagkumar91/langchain-aks-graph-tracing)

## What is different about deep-agent architectures, and when are they useful?

📹 [39:11](https://youtube.com/watch?v=Bvlb_LD7orA&t=2351)

Many deep-agent capabilities are middleware and tools layered onto a normal agent rather than a fundamentally different architecture. Compaction intercepts an agent when its context grows too large, summarizes the conversation, and replaces older messages. Todo lists and memory can be exposed as tools. The [Agent Framework harness](https://learn.microsoft.com/en-us/agent-framework/agents/harness) and [LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) package common features so each application does not have to rebuild them.

Looping and background agents are more architectural. A harness can force the agent to continue until an iteration limit, an empty todo list, or a custom condition is reached (like the RALPH loop pattern). Background agents give delegated tasks separate context windows and can run independent work in parallel.

Subagents have startup and token costs, so parallelization only helps after the task is large enough. GPT-5.6 can delegate too aggressively, making explicit guidance about when to use subagents important. Full harnesses fit broad, open-ended agents best; a narrowly focused agent may not need compaction, background workers, or every built-in provider.

## What is the state of knowledge graphs in Work IQ and Azure AI Search?

📹 [44:12](https://youtube.com/watch?v=Bvlb_LD7orA&t=2652)

The Azure AI Search team is investigating GraphRAG again, but there is nothing to announce yet. The main challenge is making graph-based retrieval performant and cost-effective in production.

[GraphRAG global search](https://microsoft.github.io/graphrag/query/global_search/) supports high-level questions by reasoning over clusters of information. One possible Azure AI Search implementation would precompute semantic clusters into a separate index, then route each query either to that cluster index or to the original document index. A production feature would need to make that pattern scale efficiently.

Work IQ changes frequently and exposes MCP, REST, CLI, and A2A integration surfaces. Its internal retrieval can change, so the practical advice is to test whether it fetches the right information for the intended workload rather than depend on a particular internal graph implementation. The [Work IQ MCP tools](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/tool-reference) include read and write operations such as fetch, create entity, perform action, and call function.

The AI Search team is also reviewing ideas from Google Cloud's [Knowledge Catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) and its Open Knowledge Format. A Fabric advocate did [an experiment](https://github.com/videlalvaro/knowledge-catalog/tree/add-fibo-loans-bundle/okf/bundles/fibo_loans) that maps OKF bundles to Microsoft Fabric ontologies.

### Does Work IQ detect poor-quality or contradictory source data?

📹 [56:21](https://youtube.com/watch?v=Bvlb_LD7orA&t=3381)

No specific data-quality detection capability was confirmed. Retrieval quality still depends on the organization and quality of the underlying content.

For SharePoint, the practices that help people also help agents: define ownership, apply metadata consistently, make authoritative sources easy to identify, organize content into clear domains, and align permissions with business requirements. Architect the information system for the enterprise first and agent consumption second. If a workload requires stronger guarantees about correctness and precision than the source system provides, a purpose-built knowledge system may still be justified.

## What observability practices work well with Agent Framework and Langfuse?

📹 [49:38](https://youtube.com/watch?v=Bvlb_LD7orA&t=2978)

Use OpenTelemetry and the GenAI semantic conventions. Standard spans keep the telemetry portable: the same agent can export to Langfuse, Azure Application Insights, or both. Agents running outside Azure, including on AWS or Google Cloud, can also send standards-based telemetry to Application Insights.

Langfuse running locally in Docker and in production is a good setup for inspecting traces and diagnosing tool calls. Local Azure alternatives include Aspire or exporting local traces directly to Application Insights. Foundry's tracing experience has also improved significantly — it can show model and tool calls, GenAI attributes (`genai.tool.arguments`, tool types, etc.), token consumption, evaluations, and a replay-oriented user view.

Give coding agents documented access to their logs. Repository instructions should explain how to inspect deployed sessions and find errors so an agent can do the first pass through routine diagnostics. Treat its proposed root cause as a hypothesis, though; an agent can mistake a correlated symptom for the real failure.
