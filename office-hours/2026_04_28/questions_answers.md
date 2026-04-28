# April 28, 2026 Python + AI Office Hours Q&A

## Update: Do Foundry evaluations stay in your tenant?

📹 [1:03](https://youtube.com/watch?v=YGTinUfdS6w&t=63)

Pamela followed up on a question from the previous day's office hours. She confirmed with the Foundry evaluation team that you **must bring your own storage container** if you want evaluation data to stay in your tenant. This is a hard requirement, not just a recommendation.

Links shared:

* [Evaluation regions and limits](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-regions-limits-virtual-network)

## How could we use GraphRAG from Cosmos DB in a hosted agent for memory and knowledge?

📹 [4:52](https://youtube.com/watch?v=YGTinUfdS6w&t=292)

The term "graph RAG" gets used in different ways — the Microsoft Research GraphRAG project versus any RAG approach that does a graph query. The Cosmos DB Conf session covered the approach described in [this Cazton blog post](https://cazton.com/blogs/technical/ai-agent-memory-patterns), which benchmarks four AI agent memory strategies (including an entity graph approach using Cosmos DB and OpenAI) across recall, token cost, and latency — the entity graph strategy achieved 100% recall.

For integrating any Azure service (including Cosmos DB) into a hosted agent using keyless auth:

1. **Get a token scoped to Cosmos DB** using the agent's managed identity — each hosted agent has its own identity and principal ID.
2. **Assign the necessary Cosmos DB role** to the agent's identity in your post-deploy script (the same pattern used for Azure AI Search).

For the **memory** use case, implement a custom **context provider** for Agent Framework — context providers are called on every agent invocation to inject memory. Look at the existing Redis or Mem0 context provider implementations as a starting point and ask GitHub Copilot to adapt one for Cosmos DB.

For the **knowledge retrieval** use case, implement a **tool** instead — tools are better for knowledge because you typically want the agent to decide when to query, whereas memory should always be checked.

Links shared:

* [Cosmos AI Knowledge Graphs](https://learn.microsoft.com/en-us/azure/cosmos-db/gen-ai/cosmos-ai-graph)
* [Agent Framework Redis context provider](https://github.com/microsoft/agent-framework/blob/main/python/packages/redis/agent_framework_redis/_context_provider.py)
* [AI Agent Memory Patterns benchmark (Cazton)](https://cazton.com/blogs/technical/ai-agent-memory-patterns)
* [Agent Framework Python examples](https://github.com/Azure-Samples/python-agentframework-demos/tree/main/examples)

## Which model is best for RAG-based chatbots?

📹 [19:17](https://youtube.com/watch?v=YGTinUfdS6w&t=1157)

Avoid GPT-4o (`gpt-4o`) for new projects — move to more recent models. Based on Pamela's own RAG evals, GPT-5 (full) performed well, and GPT-4.1 mini was a solid smaller option. She still needs to rerun evals on GPT-5.5 before merging an upgrade PR for the RAG demo.

The GPT-5.5 prompting guide recommends treating it as an entirely new model family to tune for, not just an incremental upgrade — worth reading if you're planning to migrate.

Links shared:

* [GPT-5: Will it RAG? (Pamela's blog post)](https://blog.pamelafox.org/2025/08/gpt-5-will-it-rag.html)
* [GPT-5.5 prompt guidance](https://developers.openai.com/api/docs/guides/prompt-guidance?model=gpt-5.5)
* [Using GPT-5.5 (upgrade guide)](https://developers.openai.com/api/docs/guides/latest-model)
* [Model retirement schedule](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule)

## How come I can't deploy the Mistral OCR model anymore?

📹 [21:52](https://youtube.com/watch?v=YGTinUfdS6w&t=1312)

There is a known open issue where Mistral models are not showing up in the Foundry catalog — the Foundry team is actively working on it. This is not a deprecation. The model should reappear once the issue is resolved.

Links shared:

* [Mistral OCR catalog entry](https://ai.azure.com/catalog/models/mistral-ocr-2503)
* [Mistral Document AI 2505 catalog entry](https://ai.azure.com/explore/models/mistral-document-ai-2505/)

## I'm getting 408 timeouts when asking the model to query multiple tools at once — is it a prompt issue or a model issue?

📹 [35:08](https://youtube.com/watch?v=YGTinUfdS6w&t=2108)

The "The operation was timeout." error message is a known Azure OpenAI error. A few things to investigate:

- **Enable debug logging**: Set `logging.basicConfig(level=logging.DEBUG)` locally to see all outgoing requests and identify exactly where the timeout occurs.
- **Check context window size**: If either tool is returning a very large response, the combined prompt may be hitting token limits or taking too long to process. Check your token usage.
- **Local vs. remote tools**: If your tools are local (running in your own code), a timeout is unexpected unless the prompt is very large. If they're remote tools (e.g., an MCP server), network latency could be a factor.
- **Retry with tenacity**: If the timeout is intermittent rather than consistent, the `tenacity` Python library can add retry logic on timeouts.

The key is to gather more data before guessing at the root cause — look at token counts, check whether the timeout happens before or after a response is received, and narrow down which tool or model call is failing.

Links shared:

* [tenacity documentation](https://tenacity.readthedocs.io/en/latest/)
* [Using the Responses API (Azure Foundry)](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses?tabs=python-key)

## Any inputs on PageIndex vs. vector RAG?

📹 [39:59](https://youtube.com/watch?v=YGTinUfdS6w&t=2399)

Based on feedback from Pamela's colleague who specializes in retrieval: PageIndex does work, but it's document-type dependent. It tends to perform best on **long documents** where traditional chunking and vector search struggle. It may not be a universal improvement. The recommendation is to set up your own evaluations with your actual data and compare retrieval quality.

There is no formal Microsoft support for PageIndex in any of the current RAG demos, but it's worth experimenting with if you have long-document use cases.

Links shared:

* [PageIndex GitHub](https://github.com/VectifyAI/PageIndex)

## Announcements

📹 [1:56](https://youtube.com/watch?v=YGTinUfdS6w&t=116)

**Foundry Hosted Agents public preview launched**: The new hosted agents platform (with fast microVM infrastructure) launched last week. It's in public preview and still stabilizing — some roughness expected.

* [Introducing the new hosted agents in Foundry Agent Service](https://devblogs.microsoft.com/foundry/introducing-the-new-hosted-agents-in-foundry-agent-service-secure-scalable-compute-built-for-agents/)
* [Granular cost and usage metrics for Foundry Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/tracking-every-token-granular-cost-and-usage-metrics-for-microsoft-foundry-agent/4503143)

**GitHub Copilot moving to usage-based billing**: Starting June 1, Copilot usage will consume GitHub AI Credits. Pamela noted she's been trying to use smaller models (Sonnet, Haiku, GPT-4.1) as a result. Strategies to manage costs: choose models intentionally, use auto mode (VS Code is improving task-based routing), or bring your own API keys.

* [GitHub Copilot usage-based billing announcement](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)
* [VS Code 1.117: Bring Your Own Key for Copilot Business and Enterprise](https://code.visualstudio.com/updates/v1_117#_bring-your-own-key-for-copilot-business-and-enterprise)

**GPT-5.5 now in Azure Foundry**: Available as of April 23rd.

* [GPT-5.5 in Microsoft Foundry](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/)

**MAI-Image-2**: Microsoft's new in-house text-to-image model, available in Foundry. Pamela demonstrated it generating a photorealistic Jedi costume image from a photo of her face — impressive facial likeness quality.

* [MAI-Image-2 website](https://mai-image2.com/)
* [Microsoft's new in-house AI models (MAI-Transcribe, MAI-Voice, MAI-Image)](https://techcommunity.microsoft.com/blog/appsonazureblog/microsoft%E2%80%99s-new-in%E2%8091house-ai-models-mai%E2%80%91transcribe-mai%E2%80%91voice-mai%E2%80%91image/4512731)

**Pydantic Monty $5K sandbox escape bounty**: Pydantic is running a competition to find exploits in the Monty Python sandbox. A good example of open-source security hardening through incentivized bug hunting.

* [Hack Monty: Win $5,000](https://pydantic.dev/articles/hack-monty)

**FastMCP 3.2**: Full MCP Apps support released.

* [FastMCP 3.2 blog post](https://jlowin.dev/blog/fastmcp-3-2)

**GitHub merge queues deep-dive**: A useful blog post for maintainers who merge many PRs concurrently — merge queues test PRs in order before merge to ensure compatibility.

* [Improving developer velocity with GitHub merge queue](https://humanwhocodes.com/blog/2026/04/improving-developer-velocity-github-merge-queue/)

**Deploying Anthropic (Claude) to Foundry**: Pamela showed a demo repo with Bicep for deploying Anthropic models to Foundry. The Bicep is similar to OpenAI model deployments but requires an organization name, country code, and industry. Not available on internal Microsoft accounts, but works on personal/customer subscriptions.

* [python-foundryagent-anthropic-demo](https://github.com/pamelafox/python-foundryagent-anthropic-demo/)

**presentation-skills repo**: Pamela published a new repo collecting all her Copilot skills for working with presentations (creating and writing up talks).

* [presentation-skills GitHub repo](https://github.com/pamelafox/presentation-skills)

**Azure Cosmos DB Conf**: Happening April 28 (today), live stream available.

* [Azure Cosmos DB Conf 2026](https://www.youtube.com/watch?v=OdPFriVuKtU)

**Upcoming events**:

* [Host your agents on Foundry livestream series (Apr 27–30)](https://aka.ms/AgentsOnFoundry/series)
* [AgentCon Silicon Valley: May 4](https://agentcon.city/silicon-valley)
* [PyCon US (Long Beach): May 13–19](https://us.pycon.org/2026)
* [Microsoft Build (SF): June 2–3](https://aka.ms/MS_Build_26_DAC26)
* [Posette (Postgres, Online): June 16](https://posetteconf.com/2026/)
