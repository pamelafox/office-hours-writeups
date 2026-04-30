# April 29, 2026 - "Host your agents on Foundry" Day 2 (LangChain) Office Hours

This was a follow-up office hours after the "Host your agents on Foundry" Day 2 livestream about LangChain and LangGraph.

## Can Foundry managed conversations/memory be used standalone with a LangGraph agent hosted on Azure Web App?

📹 [02:50](https://youtube.com/watch?v=kOgg69Hdhi0&t=170)

For long-term memory, yes — the Azure AI Projects SDK has a CRUD API for Foundry Memory, so you can use it from anywhere as long as you authenticate to your Foundry project. However, this is currently long-term memory only (dynamic memories that persist across sessions).

For short-term memory (session history / managed conversations), as far as Pamela knows, that is not available as a standalone service outside of hosted agents. If it were available anywhere, it would be in the Azure AI Projects SDK.

Links shared:

* [Foundry Memory usage docs](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage?view=foundry&pivots=python)
* [From local to production blog post](https://devblogs.microsoft.com/foundry/from-local-to-production-the-complete-developer-journey-for-building-composing-and-deploying-ai-agents/#step-3:-make-agents-stateful-with-memory-in-foundry-agent-service-(public-preview))

## Is the knowledge retrieval MCP server part of Microsoft Foundry?

📹 [07:07](https://youtube.com/watch?v=kOgg69Hdhi0&t=427)

Yes, it's Foundry IQ (also known as Azure AI Search). You can access it through the MCP endpoint, REST API, or Python SDK. You don't have to go through Foundry — you can set up Azure AI Search directly in the Azure portal. You can also write a custom tool that does a retrieval request instead of using the MCP endpoint.

Currently supported knowledge sources: search index, blob index, OneLake index, SharePoint, remote SharePoint, and Microsoft Bing.

Links shared:

* [Query Knowledge Base via APIs or MCP](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-retrieve?pivots=python#call-the-mcp-endpoint)
* [What is a Knowledge Source?](https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-overview#supported-knowledge-sources)

### Can we connect Elasticsearch as a knowledge source to Foundry Agent Service?

📹 [34:38](https://youtube.com/watch?v=kOgg69Hdhi0&t=2078)

Not via Foundry IQ directly, but you can connect anything to your agent as long as you can authenticate to it — either as a Python tool or as an MCP server.

## How should I handle short-term and long-term memory when deploying LangGraph/LangChain as hosted agents?

📹 [10:00](https://youtube.com/watch?v=kOgg69Hdhi0&t=600)

The `langchain-azure-ai` package has an `AzureAIMemoryChatMessageHistory` class and `AzureAIMemoryRetriever` class that integrate with [Foundry Memory](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/langchain-memory). Foundry Memory supports two long-term memory types: user profile memory (stable user facts and preferences) and chat summary memory (distilled summaries of prior discussions). Short-term turn-by-turn state stays in LangChain/LangGraph runtime state, while Foundry Memory handles long-term user-level context that persists across sessions.

LangChain also has its own memory framework with different stores. You could use Redis (available as Azure Redis) or Cosmos DB.

Links shared:

* [langchain-azure-ai chat history implementation](https://github.com/langchain-ai/langchain-azure/blob/main/libs/azure-ai/langchain_azure_ai/chat_history/azure_ai_memory.py)
* [LangGraph memory docs](https://docs.langchain.com/oss/python/langgraph/add-memory)
* [Use Foundry Memory with LangChain and LangGraph](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/langchain-memory)

## How should I handle compaction for LangChain/LangGraph hosted agents?

📹 [15:22](https://youtube.com/watch?v=kOgg69Hdhi0&t=922)

Use LangChain's built-in summarization middleware as a starting point. It just needs a model, so you can pass in your Foundry model. The agent service itself does not do compaction. However, if you're using Azure OpenAI's Responses API, it has server-side compaction options (context management with a compact threshold). Agent Framework also has built-in compaction for in-memory history agents.

Links shared:

* [LangChain SummarizationMiddleware](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware)
* [Azure OpenAI Responses API compaction](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses?tabs=python-key#chaining-responses-together)
* [Agent Framework compaction docs](https://learn.microsoft.com/en-us/agent-framework/agents/conversations/compaction?pivots=programming-language-python#applicability-in-memory-history-agents-only)

## What features are unavailable when using LangChain/LangGraph instead of Agent Framework for hosted agents?

📹 [19:01](https://youtube.com/watch?v=kOgg69Hdhi0&t=1141)

The big difference is the responses adapter. Agent Framework has the responses server built in, making it straightforward to integrate with the Foundry platform (playground, evaluation, traces, monitoring). With LangChain, there's no official responses adapter — you'd need to maintain your own.

There's a [PR in langchain-azure](https://github.com/langchain-ai/langchain-azure/pull/501) with adapter code, but it's not yet merged and there are still bugs. The code from today's demo is based on that PR. Building a correct responses adapter is complex because you need to handle streaming, tool calls, multimodal content, and all the nuances of the Responses API.

If you can get the responses API layer fully working, you should get everything available to Agent Framework users (playground, evaluation, traces, monitoring). Without it, you can use the invocations API, but you lose those platform benefits.

Pamela's honest recommendation: if the PR doesn't get merged, she wouldn't recommend deploying LangChain hosted agents with the Responses API due to the complexity of maintaining the adapter yourself.

Links shared:

* [langchain-azure PR #501 with responses adapter](https://github.com/langchain-ai/langchain-azure/pull/501)
* [Foundry hosted LangChain demos repo](https://github.com/Azure-Samples/foundry-hosted-langchain-demos)

## How does scaling work with stateful hosted agents? How is state shared between replicas?

📹 [24:45](https://youtube.com/watch?v=kOgg69Hdhi0&t=1485)

Hosted agents run in per-session VM-isolated sandboxes. Each session gets a dedicated sandbox with a persistent file system. State is automatically restored when a session resumes, but state is isolated between sessions — it's not shared across sessions. [Sessions persist for up to 30 days](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents); the idle timeout is 15 minutes — if no request arrives within that window, the platform deprovisions the compute and persists the session state.

For multi-turn conversations: the first call to the agent gives you back a conversation/response ID. Subsequent calls must include that ID so the agent has the session history. The playground handles this automatically, but when calling programmatically, you need to include the previous response ID.

If you need to share state across sessions, use an external database like Redis or Cosmos DB.

Links shared:

* [Manage hosted agent sessions](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/manage-hosted-sessions?pivots=rest)
* [Runtime components - Conversations](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/runtime-components?tabs=python#conversations-and-conversation-items)
* [Invoke the agent](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent#invoke-the-agent)
* [Chaining responses together](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses?tabs=python-key#chaining-responses-together)

## How does pricing work for hosted agents with parallel API calls?

📹 [35:09](https://youtube.com/watch?v=kOgg69Hdhi0&t=2109)

You pay only for active execution. The new platform has fast startup (under 100 milliseconds) and zero idle cost — agents are suspended between conversation turns. For 20 parallel API calls, calculate based on how long each takes and how much memory it uses.

Links shared:

* [Foundry Agent Service pricing](https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/)

## What was the code mode tool mentioned on Monday similar to Monty?

📹 [37:49](https://youtube.com/watch?v=kOgg69Hdhi0&t=2269)

Code interpreter — it's built into Foundry/Responses API. It has access to pandas, pillow, and matplotlib, so it can make charts, annotate images, etc. Much more powerful than Monty since it has access to full Python libraries. You can enable it as a tool for your agent, via Foundry tools/Foundry toolbox.

Links shared:

* [Monty server by Drew Breunig](https://github.com/dbreunig/monty-server)
* [Responses API chat demo](https://mattgotteiner.github.io/responses-chat/)

## Can I host an app using Foundry local models (like Phi) in a hosted agent container?

📹 [40:41](https://youtube.com/watch?v=kOgg69Hdhi0&t=2441)

Likely not practical — the hosted agent containers don't have GPUs, so the Phi models probably wouldn't run at all. Instead, you could use Azure Container Apps with serverless GPU and point your agent at that endpoint. However, serverless GPUs are expensive, so it depends on your scale. It makes sense if you have high enough volume (e.g., Shopify moved from OpenAI to a small Qwen model and got 75x cost savings at scale).

Links shared:

* [Tutorial: Deploy NVIDIA NIM to Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/serverless-gpu-nim?tabs=bash)

## How can we aggregate cost of execution from Foundry Traces or App Insights?

📹 [43:12](https://youtube.com/watch?v=kOgg69Hdhi0&t=2592)

This is an open question — cost tracking for agents needs more work. The cost information should be available in the Azure portal, but it's not clear if Foundry's agent dashboard surfaces it directly yet. This was flagged as something that needs better documentation and tooling.

## Any recommendations for keyword classification routing in multi-agent environments?

📹 [44:02](https://youtube.com/watch?v=kOgg69Hdhi0&t=2642)

Using structured outputs to classify/route input to the best sub-agent works if your use cases are really distinct from each other. If there's any ambiguity between agents, you need an agentic loop that can recover if it makes the wrong selection rather than a hard routing decision.

## How do I set up tracing for different frameworks (LangGraph + OpenAI SDK)?

📹 [45:21](https://youtube.com/watch?v=kOgg69Hdhi0&t=2721)

- **LangGraph:** Use `enable_auto_tracing` from the `langchain-azure-ai` package.
- **OpenAI SDK directly:** Use the `opentelemetry-instrumentation-openai` package from PyPI and instrument it.

There are docs for LangChain tracing on Foundry, though `enable_auto_tracing` isn't fully documented there yet- the team says it will be soon!

Links shared:

* [Trace LangChain and LangGraph apps with Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/langchain-traces)
* [opentelemetry-instrumentation-openai on PyPI](https://pypi.org/project/opentelemetry-instrumentation-openai/)

## Would Cosmos DB make sense for LangChain/LangGraph hosted agents for short and long-term memories?

📹 [48:56](https://youtube.com/watch?v=kOgg69Hdhi0&t=2936)

Yes. For short-term memory, hosted agent sessions [persist for up to 30 days](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents), so Cosmos DB gives you persistence beyond that. For long-term memory, Cosmos DB now has vector search and full text search, so you can search memories effectively. It works well for chat history (used in the RAG demo repo).

For persistence with LangChain/LangGraph specifically, you can persist chat history of an agent to Cosmos DB with [`langchain-azure-cosmosdb`'s chat history class](https://github.com/langchain-ai/langchain-azure/blob/main/libs/azure-cosmosdb/src/langchain_azure_cosmosdb/_chat_history.py), and you can persist LangGraph state with the [same package's checkpointer](https://github.com/langchain-ai/langchain-azure/blob/main/libs/azure-cosmosdb/src/langchain_azure_cosmosdb/_chat_history.py).

Keep in mind: when using Cosmos DB with hosted agents, the agent has its own identity, so you need to assign the appropriate RBAC role to the agent's principal ID for keyless authentication.

Links shared:

* [AI Agent Memory Patterns with Cosmos DB (Cazton blog)](https://cazton.com/blogs/technical/ai-agent-memory-patterns)
* [Foundry hosted agent framework demos - postdeploy.sh](https://github.com/Azure-Samples/foundry-hosted-agentframework-demos/blob/main/infra/hooks/postdeploy.sh)

## Any recommendations to handle vector drift over the long run?

📹 [51:41](https://youtube.com/watch?v=kOgg69Hdhi0&t=3101)

These are Pamela's thoughts on vector drift, based off the kinds of vector drift described in [this blog post](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/vector-drift-in-azure-ai-search-three-hidden-reasons-your-rag-accuracy-degrades-/4493031).

1. **Embedding model mismatch** — this should never happen. Always use the same embedding model for indexing and querying. Store the model name in your environment variables or even in the column name.
2. **Fine-tuned embedding models** — if you fine-tune based on your data and your domain changes, you'd need to re-fine-tune and re-embed.
3. **Changing chunking strategy** — this is the real issue. If you change your chunking algorithm, ideally create a parallel index and re-chunk everything for consistency. Store chunking strategy as metadata.

Links shared:

* [Vector Drift in Azure AI Search (Tech Community blog)](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/vector-drift-in-azure-ai-search-three-hidden-reasons-your-rag-accuracy-degrades-/4493031)

## Announcements

📹 [00:32](https://youtube.com/watch?v=kOgg69Hdhi0&t=32)

**Pip 26.1 introduces dependency cooldowns** — a new feature that accepts a relative duration (number of days) to delay accepting newly uploaded packages. UV has a similar feature called `exclude-newer`, and Dependabot also has its own cooldown option.

Links shared:

* [What's new in pip 26.1](https://ichard26.github.io/blog/2026/04/whats-new-in-pip-26.1/)
* [UV dependency-metadata settings](https://docs.astral.sh/uv/reference/settings/#dependency-metadata)
* [UV Dependabot cooldown](https://docs.astral.sh/uv/guides/integration/dependabot/#dependency-cooldown)
