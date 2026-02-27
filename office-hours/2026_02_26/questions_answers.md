# Feb 26, 2026 Office Hours Q&A

Note: This session was a follow-up Q&A after the [Python + Agents Session 3 livestream](https://developer.microsoft.com/en-us/reactor/events/26690/), focused on monitoring and evaluating agents.

## Do you need an Azure account to use the Azure AI evaluation SDK, and is there a free level?

📹 [0:56](https://youtube.com/watch?v=D9vfGeoPh_I&t=56)

You don't necessarily need an Azure account for the quality evaluations. The local evaluation SDK works with any OpenAI-compatible model — you just need to set up the model configuration. In theory, you can use it with OpenAI.com, or even run it locally with Ollama if you have a capable enough machine and model.

The main limitation with GitHub Models is the token cap — some attendees hit limits, though Pamela managed to run evaluations with GPT-5 Mini on GitHub Models.

For the batch evaluation, the Azure AI project parameter is optional — you can output results locally. However, for **red teaming**, you do need a Foundry project because it requires access to the adversarial LLM.

There's also a newer way of doing evals using the OpenAI SDK in conjunction with the Azure AI Projects SDK, but that does require a Foundry project.

## Does a Microsoft 365 Family subscription include any tokens for Foundry or Azure?

📹 [9:01](https://youtube.com/watch?v=D9vfGeoPh_I&t=541)

No — M365 licenses are independent of Azure subscriptions. You'd need to set up an Azure account separately. Azure free trial accounts have very limited Foundry model access (around 1,000 tokens capacity) and likely can't create Foundry projects. The recommendation is to create a regular Azure account, set a budget limit (e.g., $20/month), and configure a budget alert.

## How do you set up custom spans within traces in OpenTelemetry?

📹 [5:01](https://youtube.com/watch?v=D9vfGeoPh_I&t=301)

When using the Agent Framework, spans are automatically set up for you. For custom spans, you create a tracer and use a context manager (`with` statement) to define a parent span, then set attributes on that span. Children spans created within that context automatically nest under the parent.

An example of this approach is the [OpenTelemetry middleware for MCP servers](https://github.com/Azure-Samples/python-mcp-demos/blob/main/servers/opentelemetry_middleware.py), which sets up a tracer provider and creates spans with attributes for each request.

Links shared:

* [OpenTelemetry middleware example](https://github.com/Azure-Samples/python-mcp-demos/blob/main/servers/opentelemetry_middleware.py)

## What if I get a deployment error because my Azure account doesn't have Owner access?

📹 [7:45](https://youtube.com/watch?v=D9vfGeoPh_I&t=465)

The keyless credential setup in the demo repo requires certain roles (like Owner) to create role assignments. If you only have Contributor access, you'll hit errors. Workarounds:

1. Get RBAC Owner access scoped to just a resource group and deploy to that group
2. Set up the resources manually instead of using the repo's infrastructure-as-code
3. Check the [Azure account requirements](https://github.com/Azure-Samples/azure-search-openai-demo/?tab=readme-ov-file#azure-account-requirements) for details on needed roles

Also, make sure the model version in the Bicep matches a supported version — one attendee fixed a deployment error by updating `main.bicep` to deploy `gpt-5-mini` instead of `gpt-4.1-mini`.

## Why did the LLM take 5 seconds to decide on tools?

📹 [10:28](https://youtube.com/watch?v=D9vfGeoPh_I&t=628)

LLMs have inherent latency, especially reasoning models like GPT-5 Mini. Several factors affect response time:

- **Deployment type**: Pay-as-you-go (standard) has higher latency than provisioned deployments, which give you dedicated infrastructure
- **Reasoning effort**: You can set a `reasoning_effort` parameter (low/medium/high) to trade off thinking time vs. speed. In the Agent Framework, pass it via `default_options` when creating the agent
- **Model choice**: Newer model versions (5.1, 5.2, etc.) are often faster than their predecessors at similar quality levels
- **Variability**: Never base performance conclusions on a single call — use load testing (e.g., [Locust](https://locust.io/)) and look at percentiles (P50, P99)

Pamela demonstrated measuring latency across evaluation runs using a custom [Textual](https://textual.textualize.io/)-based CLI tool, showing how latency varies significantly across models and runs.

## What about adding a validation/checker agent to improve quality?

📹 [16:50](https://youtube.com/watch?v=D9vfGeoPh_I&t=1010)

Adding a reflection/validation step doubles latency since it's another LLM call. Alternatives:

- Ask the LLM to self-report a **confidence level** in its response — surprisingly, LLMs can accurately indicate low confidence
- Only trigger a reflection step when confidence is low
- Use evaluation to verify that the extra step actually improves quality — in Pamela's RAG experiments, a naive reflection loop often didn't improve answers

Links shared:

* [Locust load testing](https://locust.io/)
* [Textual TUI framework](https://textual.textualize.io/)
* [Azure OpenAI model availability table](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?view=foundry-classic&pivots=azure-openai&tabs=global-standard-aoai%2Cglobal-standard#models-by-deployment-type)

## Is Microsoft Agent Framework GA yet? What's recommended for production today?

📹 [32:27](https://youtube.com/watch?v=D9vfGeoPh_I&t=1947)

Not yet GA — the latest release is 1.0.0 RC2 (release candidate 2), released just 19 hours before the session. It's very close to GA, likely weeks away. The agent API was expected to be stable by end of February, with the workflow API potentially seeing minor changes into March.

For customers wanting to build production agentic apps now, Agent Framework is the recommended choice because:

- **Semantic Kernel** is essentially in maintenance mode — that team now works on Agent Framework
- **AutoGen** team also now works on Agent Framework
- You should always **pin your dependency versions** to avoid breaking changes

The GitHub Copilot SDK was declared GA earlier that week, but Agent Framework is more complex and takes longer to stabilize.

Links shared:

* [Agent Framework on PyPI](https://pypi.org/project/agent-framework/#history)

## What are the uses for observability beyond debugging and performance?

📹 [37:28](https://youtube.com/watch?v=D9vfGeoPh_I&t=2248)

Beyond debugging and performance monitoring, observability traces can be used for **quality analysis**. Once traces are exported to a log workspace (e.g., App Insights), you can:

- Pull traces back out and send them to an agent or LLM to identify low-quality responses
- Use a coding agent (like Claude Code) to analyze traces from an observability platform and find issues
- Build automated evaluations based on patterns found in production traces
- Improve prompts based on real-world failure patterns

Hamel Husain recently demonstrated this approach using Claude Code with [Arize Phoenix](https://phoenix.arize.com/) (an open-source, OpenTelemetry-based observability platform) to analyze traces and build better evaluations.

Links shared:

* [Hamel Husain's blog](https://hamel.dev/)
* [Arize Phoenix](https://phoenix.arize.com/)
* [Automating Evals with Claude Code + Phoenix](https://maven.com/p/2c8410/automating-evals-with-claude-code-phoenix)

## Should LLM-as-a-judge evaluation run in the user-facing loop or offline?

📹 [41:54](https://youtube.com/watch?v=D9vfGeoPh_I&t=2514)

LLM-as-a-judge adds too much latency for the user-facing loop. The recommended approaches are:

1. **Online/continuous evaluation**: Sample a percentage of agent calls and queue evaluations in a separate thread (not the user-facing thread), then surface results in a dashboard. If using Foundry Agents, this is [built-in with configurable sampling](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/continuous-evaluation-agents).

2. **Confidence self-reporting**: During answer generation, ask the LLM to indicate its confidence level. Display this to users per the [HAX Toolkit](https://www.microsoft.com/en-us/research/project/hax-toolkit/) guidelines for communicating AI precision.

3. **Reflection steps** (use cautiously): Pamela's team experimented with adding an LLM-based reflection step in a [RAG agentic flow](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/bonus-rag-time-journey-agentic-rag/4404652), but it added 3+ extra LLM calls and often didn't improve quality. Azure AI Search later built in a more targeted reflection step, but it's optional due to the latency cost.

The terms to search for when researching this are **"online evaluation"** and **"continuous evaluation"**.

Links shared:

* [Continuously evaluate your AI agents (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/continuous-evaluation-agents)
* [HAX Toolkit](https://www.microsoft.com/en-us/research/project/hax-toolkit/)
* [Bonus RAG-time Journey: Agentic RAG blog post](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/bonus-rag-time-journey-agentic-rag/4404652)