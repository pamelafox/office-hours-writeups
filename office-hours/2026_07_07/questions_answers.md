# July 7, 2026 Office Hours Q&A

## Announcements

📹 [0:43](https://youtube.com/watch?v=hTzvm4Hk-wQ&t=43)

### Copilot & GitHub

- **Kimi K2.7 Code** is now generally available in GitHub Copilot — the first open-weight model offered as a selectable option in the model picker. It's hosted on Azure and also deployable from Foundry. Performance is considered on par with Haiku-class models. The VS Code team made harness improvements to prevent infinite looping, which open-weight models are sometimes prone to. ([GitHub changelog](https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/))
- **GitHub Models is being retired** — it was great for getting started but wasn't making money.
- **Copilot Vision is GA** — attach images and PDFs to chat. ([GitHub changelog](https://github.blog/changelog/2026-07-01-copilot-vision-is-generally-available/))

### VS Code & AI

- **VS Code prompt tuning blog post** explains how the VS Code team A/B tested GPT-5.5 system prompt changes. They tried to get GPT-5.5 to avoid broad exploration and act more assertively, measuring metrics like commit retention and time-to-edit. It's a fascinating example of running evaluations at scale, and the learnings may be applicable to your own applications using GPT-5.5. ([Blog post](https://code.visualstudio.com/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers))

### Web IQ & Harrier Embeddings

- **Web IQ** blog post details the engineering behind Microsoft's new fast web grounding system. It uses DiskANN (the vector indexing algorithm from Microsoft Research used in Cosmos DB and PostgreSQL) and **Harrier embeddings** — an open embedding model that runs on CPU and supports retrieval, clustering, semantic similarity, classification, bitext mining, and reranking. You can try Harrier locally from Hugging Face. ([Web IQ blog](https://commandline.microsoft.com/grounding-system-agentic-web-engineering-retrieval/), [Harrier on Hugging Face](https://huggingface.co/microsoft/harrier-oss-v1-0.6b))

### Recap: AIE World Fair

- Pamela gave seven sessions at **AI Engineer World's Fair** in San Francisco covering Foundry models, hosted agents, model swapping, evaluations, and observability.
- Updated the [Foundry Hosted Agent Framework Demos](https://github.com/Azure-Samples/foundry-hosted-agentframework-demos) repo — upgraded all Python packages, MCP versions, SDKs, APIs, and added more evaluation content. Tested and working with the latest version of everything.
- Ran a **model swap workshop** comparing GPT-5.5, Kimi 2.6, DeepSeek V4 Flash, Claude Sonnet 4.5, and Mistral Large 3 across LLM calls, RAG, image input, tool calling, agent frameworks, evaluations, and prompt optimization. ([Repo](https://github.com/pamelafox/model-swap-workshop))
- Demoed **ASSERT** (from Microsoft Research Responsible AI group) — a new evaluation framework that bootstraps test sets from a YAML description of your agent's expected behaviors, generates scenarios, and runs them against multiple models. ([ASSERT examples](https://github.com/responsibleai/ASSERT/tree/main/examples))
- Demoed **DSPy** prompt optimization — declare your program's signature and metrics, and a genetic Pareto optimizer iterates prompts until it finds the optimal one. Useful for structured outputs, classification, and entity extraction with smaller/cheaper models. ([DSPy](https://dspy.ai/))
- Gave a talk on choosing the right stack for building AI apps, covering HTTP APIs vs. vendor SDKs vs. LLM-agnostic SDKs vs. agent frameworks. ([Slides](https://aka.ms/ai-stack-slides), [Demo code](https://aka.ms/ai-stack), [Python stack + Foundry models](https://github.com/pamelafox/python-stack-foundry-models/tree/main/examples))

## Do agents need to be hosted on Foundry/Azure to use Foundry evals and observability?

📹 [33:00](https://youtube.com/watch?v=hTzvm4Hk-wQ&t=1980)

Not necessarily. The goal is cloud-agnostic observability using OpenTelemetry and the GenAI semantic conventions. A [Build demo session](https://build.microsoft.com/en-US/sessions/DEM341?source=sessions) showed agents running on GCP (Google ADK), AWS (LangGraph), and Foundry all reporting traces to the same App Insights instance. The key is using the `microsoft-opentelemetry` distro and emitting spans with GenAI semantic conventions.

For **Foundry hosted agents** using Microsoft Agent Framework, observability is nearly zero-config — just ensure you have the App Insights connection string set as an environment variable and call `enable_instrumentation()` (which is already enabled by default).

For **external agents** (other clouds/frameworks), it requires more setup. The [Build26-DEM341 repo](https://github.com/microsoft/Build26-DEM341-any-agent-any-cloud-standardized-tracing-with-foundry-and-opentelemetry) shows examples for LangGraph on AWS and ADK on GCP, each with a `telemetry.py` that configures the Microsoft OpenTelemetry distro. The setup is more complex than expected — Pamela noted she'd ask the team if it can be simplified.

**Continuous evaluations** should work for external agents as long as you can get traces into App Insights, since continuous evals are based on App Insights traces.

The Foundry portal's monitor tab now shows operational metrics, cost, evaluation scores, tool calls, error rates, and even supports alerts (like pager duty for low evaluation pass rates). The Azure Monitor agents view understands GenAI semantic conventions and can display tool calls and evaluations across agents.

For evaluation results, the convention is `genai.evaluation.result` events tied to a `conversation_id` for joining evaluations to their corresponding traces.

Links shared:

* [Build DEM341 session](https://build.microsoft.com/en-US/sessions/DEM341?source=sessions)
* [DEM341 repo (any agent, any cloud, standardized tracing)](https://github.com/microsoft/Build26-DEM341-any-agent-any-cloud-standardized-tracing-with-foundry-and-opentelemetry)
* [LangGraph telemetry.py example](https://github.com/microsoft/Build26-DEM341-any-agent-any-cloud-standardized-tracing-with-foundry-and-opentelemetry/blob/main/src/agents/seattle-langgraph/telemetry.py)
* [LAB540 workshop (observe, optimize, protect hosted agents)](https://github.com/microsoft/Build26-LAB540-observe-optimize-and-protect-your-hosted-agents-in-microsoft-foundry)

### Are there any skills or best practices for setting up observability?

📹 [38:55](https://youtube.com/watch?v=hTzvm4Hk-wQ&t=2335)

The **Foundry Toolkit extension** for VS Code comes with skills for traces, evaluations, datasets, and troubleshooting. However, Pamela found the trace-related skills weren't as helpful as expected for App Insights setup specifically.

The practical recommendation: find the most similar example code (like the DEM341 repo's telemetry.py) and point your coding agent at it to implement telemetry for your specific framework and cloud setup.

## Are Foundry hosted agents GA?

📹 [48:15](https://youtube.com/watch?v=hTzvm4Hk-wQ&t=2895)

Not yet, but it's coming in the next few days. The docs no longer mark hosted agents as "preview," and the Build recap mentioned GA was expected by early July. The team confirmed the original June 30th GA date slipped slightly, and the SDKs are moving out of `.beta` to stable in preparation.

Some current limitations:

- [Virtual network configuration](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/virtual-networks?tabs=portal&pivots=templates) must be included when you first create the Foundry account — adding network injection to an existing account isn't supported for hosted agents.
- [Private ACR support](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent-private-azure-container-registry) depends on when the project was created — projects created after June 24th support a private ACR.
