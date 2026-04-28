# April 27, 2026 "Host your agents on Foundry" Day 1 - Office Hours Q&A

## When would it be better to deploy agents as hosted agents vs. using other Azure compute resources?

📹 [0:28](https://youtube.com/watch?v=o4-1LI3-uqw&t=28)

The number one advantage of deploying as hosted agents is the evaluation story. With hosted agents, it's much easier to set up scheduled evaluation, online/continuous evaluation, and evaluation alerts — that would be significant effort to replicate on your own compute platform.

Another advantage is having everything in the Foundry UI — the playground, traces, and tools all in one location, which can make it easier for other people in your organization to interact with the agent.

That said, if you're currently in production on Container Apps, you should stay there for now since hosted agents are still in public preview. You can test it out in parallel — set up performance tests and load testing to compare. Only move when you're really taking advantage of the hosted agent features like evaluation.

## Are the Foundry evaluations kept in our tenant? That's an important topic in Europe.

📹 [3:06](https://youtube.com/watch?v=o4-1LI3-uqw&t=186)

Evaluation is a per-region thing, and it does create storage behind the scenes. Pamela assumed the storage stays in the region but couldn't find a definitive doc statement confirming it. For organizations that need to be very certain, the recommended approach is to use "bring your own storage" — that way you control exactly where data is stored. She noted this as a follow-up question for the product team.

Links shared:

* [Evaluation regions and limits](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-regions-limits-virtual-network)

## Do you get more customizable orchestration with hosted agents?

📹 [4:51](https://youtube.com/watch?v=o4-1LI3-uqw&t=291)

Yes, compared to prompt agents. Prompt agents are quite limited — you can only configure instructions and tools through the SDK. With hosted agents, you can bring your own framework (Microsoft Agent Framework, LangChain, Pydantic AI, etc.) and build complex workflows, then wrap them as an agent in the responses host server.

However, it's the agent framework that provides the orchestration, not the Foundry Agent Service platform itself. The platform just hosts and runs your containerized agent code.

## Can you connect agents with external MCP tools using the agent platform?

📹 [6:25](https://youtube.com/watch?v=o4-1LI3-uqw&t=385)

Yes. Pamela showed the stage 4 demo code which connects to multiple MCP tools. In this case, the agent connects to both a Foundry toolbox (providing web search and code interpreter) and a separate knowledge base retrieval tool — each as separate MCP server connections.

There is currently a bug where the Foundry toolbox doesn't work with MCP tools when deployed — the team is actively hot-fixing it. In the meantime, you can connect MCP tools separately. You can add any MCP server as long as you handle the authentication (key, Entra, etc.) correctly.

Links shared:

* [Foundry hosted agent demos repo](https://github.com/Azure-Samples/foundry-hosted-agentframework-demos)

## How does safety play a role in using the web search tool regarding prompt injection?

📹 [8:27](https://youtube.com/watch?v=o4-1LI3-uqw&t=507)

All calls go through a Foundry model protected by Foundry guardrails (the RAI policy system). By default, guardrails check for jailbreak detection, hate, violence, sexual content, and self-harm, with blocking set to medium level. You can increase or decrease blocking levels in the Foundry portal under Build > Guardrails.

For web search specifically, the concern is **indirect attacks** (also called "prompt shields") — where a website contains embedded prompt injection that gets pulled into the grounded data. Direct jailbreak detection is always enabled by default, but indirect attack detection may not be. If you're doing any kind of RAG or web search grounding, you should create a custom RAI policy that explicitly enables indirect attack detection.

Links shared:

* [Prompt Shields in Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection)

## Is there something similar to code mode in Agent Framework, or can I use Pydantic Monty?

📹 [12:43](https://youtube.com/watch?v=o4-1LI3-uqw&t=763)

Pydantic AI has code mode powered by Monty (a Python sandbox rewritten in Rust that only implements safe parts of Python — no file system access, etc.). There isn't a direct equivalent in Agent Framework.

If you want code mode specifically, Pydantic AI is probably the best choice. The Pydantic AI maintainers are working on making it easy to deploy Pydantic AI agents with a generic Responses adapter. Some people have already deployed Pydantic AI to Foundry using the invocations protocol (the simpler HTTP endpoint approach), with AG-UI on top.

Links shared:

* [Pydantic Monty article](https://pydantic.dev/articles/pydantic-monty)
* [Pydantic AI Harness code mode](https://pydantic.dev/docs/ai/harness/code-mode/#_top)
* [Pydantic Monty GitHub](https://github.com/pydantic/monty)

### Live demo: Using Monty as a local tool in Agent Framework

📹 [40:26](https://youtube.com/watch?v=o4-1LI3-uqw&t=2426)

A community member shared that they use Monty as a tool in their Strava MCP server for data analysis. Pamela live-coded a minimal example of integrating Pydantic Monty as a local tool in an Agent Framework agent. The key points:

- Import `pydantic_monty` and create a tool function that accepts code and calls `monty.run(code)`
- `monty.run()` returns the result of the last expression in the code, so instruct the LLM to end with a variable (not a print statement)
- If you need print output, implement a print callback
- This should work fine when deployed as a hosted agent since Monty is just a Python/Rust library

Pamela published the working example as a GitHub Gist.

Links shared:

* [Agent Framework plus Monty tool (Gist)](https://gist.github.com/pamelafox/47c380e63687164fe1748c231f07998f)
* [Strava MCP with Monty example](https://github.com/saxenanurag/strava-mcp/blob/main/strava_mcp/services/analysis.py)

## What would be an efficient way to automatically analyze traces and logs?

📹 [14:54](https://youtube.com/watch?v=o4-1LI3-uqw&t=894)

Several approaches:

- **GitHub Copilot with Azure skills**: You can tell Copilot to grab error logs, find top errors, and report them. Pamela uses this extensively — she asks Copilot to determine whether errors are in her code vs. the platform/SDK, and then has it write detailed bug reports when appropriate. Push back on the LLM when debugging since it can be too quick to blame external factors.
- **Kusto queries in App Insights**: Copilot can write and execute KQL queries using the Azure Monitor tool.
- **Azure skills**: Check if there are relevant Azure skills that can pull in logs directly.
- **Cluster analysis in Foundry**: Foundry also has a built-in cluster analysis feature for evaluation results, which can automatically group and surface patterns in your traces.

The key is to go back and forth with the LLM when analyzing errors — don't accept the first diagnosis.

Links shared:

* [Cluster analysis in Foundry](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/cluster-analysis)

## Does hosted agent support per-agent identity and is there VNet support?

📹 [16:55](https://youtube.com/watch?v=o4-1LI3-uqw&t=1015)

**Per-agent identity:** Yes. Each hosted agent gets its own identity. The AZD post-deploy stage handles assigning roles to the agent identity automatically. If your agent code needs to access additional Azure services directly (e.g., Azure AI Search), you need to get the agent's principal ID and assign the role yourself. You can get the principal ID using `az di agent show`, which returns JSON containing the instance identity and principal ID. Pamela showed a `post-deploy.sh` script pattern for this.

**VNet support:** Yes, there is VNet support documented for Foundry Agent Service. One caveat noted in the docs is that the ACR must be reachable over a public network endpoint. Pamela recommended trying it out since she hadn't personally tested this flow yet.

Links shared:

* [Set up private networking for Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/virtual-networks?tabs=portal)

## If we wrap a workflow as an agent and it contains other agents using tools, would tracing still capture all internal information?

📹 [20:09](https://youtube.com/watch?v=o4-1LI3-uqw&t=1209)

Yes, as long as you're using Agent Framework with `enable_instrumentation()` called. The responses host server adds one parent span on top, and then Agent Framework emits spans for all chat client operations, function invocations, and agent operations underneath.

If your workflows do something that Agent Framework doesn't automatically instrument, you can emit your own custom spans. The Agent Framework observability docs list everything that's automatically instrumented.

Links shared:

* [Agent Framework Observability - Spans and Metrics](https://learn.microsoft.com/en-us/agent-framework/agents/observability?pivots=programming-language-python#spans-and-metrics)

## How do you pick a better model for querying a database (NL to SQL)?

📹 [22:32](https://youtube.com/watch?v=o4-1LI3-uqw&t=1352)

Pamela recommended a community-made LLM SQL Benchmark that specifically tests models on NL-to-SQL generation. According to that benchmark, Claude Sonnet, Opus, GLM, and Grok 4.1 all performed well.

More generally, for any specific use case, the best approach is to set up your own evaluation scenarios with your actual data and queries, rather than relying solely on generic benchmarks. GPT-5.5 was also mentioned as worth trying — the prompting guide describes it as a fundamentally different model (not just an incremental improvement over 5.4).

Links shared:

* [LLM SQL Benchmark](https://sql-benchmark.nicklothian.com/?utm_source=breadbox)

## Pros and cons of having each agent of a multi-agent system in its own sandbox?

📹 [25:10](https://youtube.com/watch?v=o4-1LI3-uqw&t=1510)

**Pros:**
- **Isolated file system**: Each sub-agent gets its own file system, so there are no collisions if agents store artifacts (e.g., deep research agents that save files during research, like LangChain's deep agents repo).
- **Isolated context windows**: Each agent maintains its own context without pollution from other agents.
- **Dedicated CPU/memory**: No competition for compute resources when running multiple agents in parallel.
- **Good for highly parallelized deep tasks** with lots of artifact creation and inspection.

**Cons:**
- More effort to set up currently.
- Pamela recommended only going for this approach when you really need the isolation — don't jump to it prematurely. Something coming at Build should make this easier.

## What is the pricing for hosted agents?

📹 [27:14](https://youtube.com/watch?v=o4-1LI3-uqw&t=1634)

Hosted agent billing began April 22nd during preview. You pay only for active execution — there is zero idle cost and faster startup with the new microVM platform. Pricing is:

- **Compute**: $0.0994 per vCPU-hour
- **Memory**: $0.0118 per GiB-hour
- **Model inference and persistent memory**: billed separately

Foundry Memory is free to use until June 1st.

Links shared:

* [Foundry Agent Service pricing page](https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/)
* [From Local to Production blog post (pricing section)](https://devblogs.microsoft.com/foundry/from-local-to-production-the-complete-developer-journey-for-building-composing-and-deploying-ai-agents/)

## Can you publish prompt agents when you have public network disabled?

📹 [30:05](https://youtube.com/watch?v=o4-1LI3-uqw&t=1805)

If the publish button has disappeared, it may be a bug or an intentional change related to network-disabled configurations. Pamela will check with the product team.

## Which endpoint do you use to connect to an agent from an external app?

📹 [30:20](https://youtube.com/watch?v=o4-1LI3-uqw&t=1820)

For calling a hosted agent via the responses API, the endpoint format is: `{base_url}/agents/{agent_name}/protocols/openai/responses`. The exact endpoint depends on whether you're using the invocations protocol or the responses API. The docs on deploying and invoking hosted agents cover both options. It's also possible that multiple endpoint formats are supported simultaneously.

Links shared:

* [Deploy a hosted agent - Invoke the agent](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent#invoke-the-agent-1)

## What RBAC roles are typically needed for hosted agents?

📹 [32:48](https://youtube.com/watch?v=o4-1LI3-uqw&t=1968)

Generally, AZD handles assigning the necessary RBAC roles during deployment. You only need to manually assign additional roles when your agent code directly accesses other Azure services.

Key roles Pamela highlighted from her Bicep templates:

- **Log Analytics Reader** on the Foundry project (important for traces to show up)
- **Azure AI User** on the project (for running operations)
- **ACR role** (set up automatically for container registry access)

If you're curious what roles are assigned to your agent's identity after a default deployment, you can get the agent's principal ID and use the Azure CLI to list all role assignments (change `create` to `list` in the role assignment command).

## Can we have agent endpoints proxied with an API gateway and have policies applied at the gateway level (rate limiting, auth)?

📹 [35:51](https://youtube.com/watch?v=o4-1LI3-uqw&t=2151)

This is an open question. The hosted agent endpoint is an HTTP endpoint using Entra authentication, so in theory an API gateway (Azure API Management) should be able to proxy it as long as it can pass along the Entra token. Azure also has a separate "AI gateway" concept within API Management with GenAI-specific capabilities.

Pamela couldn't find specific documentation about proxying Foundry Agent Service through API Management and noted this as a follow-up question for the product team.

Links shared:

* [Azure API Management GenAI Gateway capabilities](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)
* [Azure API Management Gateways overview](https://learn.microsoft.com/en-us/azure/api-management/api-management-gateways-overview)

## Announcements

📹 [28:39](https://youtube.com/watch?v=o4-1LI3-uqw&t=1719)

**Foundry Memory is free until June 1st**: The Foundry Memory preview (Azure in-memory history, Foundry memory provider) is free to use through June 1st. Pamela encouraged everyone to try it out now.

* [Memory usage in Foundry agents](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage?pivots=python)
* [From Local to Production blog post (memory section)](https://devblogs.microsoft.com/foundry/from-local-to-production-the-complete-developer-journey-for-building-composing-and-deploying-ai-agents/#step-3:-make-agents-stateful-with-memory-in-foundry-agent-service-(public-preview))

**Foundry Toolboxes**: A new blog post introduced toolboxes in Foundry for packaging and sharing tools.

* [Introducing Toolboxes in Foundry](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/)

**"Host your agents on Foundry" livestream series**: This session was a follow-up office hours after the Day 1 livestream. The series continues with LangChain on Wednesday and evaluation on Thursday.

* [Discussion thread with all resources](https://github.com/orgs/microsoft-foundry/discussions/380)
* [Day 1 livestream recording](https://www.youtube.com/live/8N7q0Ucr3rw)
* [Livestream series registration](https://aka.ms/AgentsOnFoundry/series)

**Microsoft Build**: June 2-3, with "lots of good announcements" expected.

**Agent Framework samples**: Pamela referenced the samples repo and the dynamic memory with Mem0 presentation.

* [Agent Framework Python samples](https://github.com/microsoft/agent-framework/tree/main/python/samples)
* [Dynamic Memory with Mem0 (session 2)](https://github.com/Azure-Samples/python-agentframework-demos/blob/main/presentations/english/session-2/README.md#dynamic-memory-with-mem0)
