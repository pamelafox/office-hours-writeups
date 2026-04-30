# April 29, 2026 "Host your agents on Foundry" Day 2 (Langchain)

## Recording:

https://www.youtube.com/watch?v=kOgg69Hdhi0

## Slide content:

No slides for the office hours itself, this session was a follow-up office hours after this livestream:
https://developer.microsoft.com/en-us/reactor/events/26933/

# Browser open tabs

https://github.com/orgs/microsoft-foundry/discussions/380
https://streamyard.com/teams/yfgXFbwTJEBTHs5jbsSYAiTk/videos
https://github.com/pamelafox/presentation-writeups/blob/main/presentations/foundry-agents-agentframework/outputs/writeup.md
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-gps-lang-hosted,,ai-account-574klekaccm6k,ai-project-gps-lang-hosted/build/agents/hosted-langgraph-agent/build
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-gps-lang-hosted,,ai-account-574klekaccm6k,ai-project-gps-lang-hosted/build/agents/hosted-langgraph-agent/traces
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-gps-lang-hosted,,ai-account-574klekaccm6k,ai-project-gps-lang-hosted/build/agents/hosted-langgraph-workflow/build
https://github.com/Azure-Samples/foundry-hosted-langchain-demos
https://ichard26.github.io/blog/2026/04/whats-new-in-pip-26.1/
https://docs.astral.sh/uv/reference/settings/#dependency-metadata
https://docs.astral.sh/uv/guides/integration/dependabot/#dependency-cooldown
https://devblogs.microsoft.com/foundry/from-local-to-production-the-complete-developer-journey-for-building-composing-and-deploying-ai-agents/#step-3:-make-agents-stateful-with-memory-in-foundry-agent-service-(public-preview)
https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/
https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage?view=foundry&pivots=python
https://github.com/Azure/azure-sdk-for-python/tree/main
https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-overview#supported-knowledge-sources
https://github.com/Azure-Samples/foundry-hosted-langchain-demos
https://github.com/langchain-ai/langchain-azure/blob/main/libs/azure-ai/langchain_azure_ai/chat_history/azure_ai_memory.py
https://docs.langchain.com/oss/python/langgraph/add-memory
https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware
https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses?tabs=python-key#chaining-responses-together
https://learn.microsoft.com/en-us/agent-framework/agents/conversations/compaction?pivots=programming-language-python#applicability-in-memory-history-agents-only
https://github.com/langchain-ai/langchain-azure/pull/501
https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent#invoke-the-agent
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/runtime-components?tabs=python#conversations-and-conversation-items
edge://newtab/
https://login.microsoftonline.com/common/DeviceAuthTls/reprocess
https://github.com/dbreunig/monty-server
https://mattgotteiner.github.io/responses-chat/
file:///Users/pamelafox/Downloads/sf_pretend_monthly_rainfall.png
https://login.microsoftonline.com/common/DeviceAuthTls/reprocess
https://learn.microsoft.com/en-us/azure/container-apps/serverless-gpu-nim?tabs=bash
https://pypi.org/project/opentelemetry-instrumentation-openai/
https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/app/backend/requirements.in
https://www.bing.com/search?pglt=513&q=langchain+on+azure+microsoft+learn&cvid=b4e87a87a77b4ef98e507a4e487d72c8&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEAyCAgJEOkHGPxV0gEINzUyNWowajeoAgCwAgA&FORM=ANNAB1&PC=U531
https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/langchain-traces
https://github.com/Azure-Samples/foundry-hosted-agentframework-demos/blob/main/infra/hooks/postdeploy.sh
https://cazton.com/blogs/technical/ai-agent-memory-patterns
https://www.bing.com/search?q=vector+drift&qs=n&form=QBRE&sp=-1&lq=0&pq=vector+drift&sc=12-12&sk=&cvid=9958D9E5CB7F4DAEB13E5704AFF5DE72
https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/vector-drift-in-azure-ai-search-three-hidden-reasons-your-rag-accuracy-degrades-/4493031
https://login.microsoftonline.com/common/DeviceAuthTls/reprocess
https://members.clubpilates.com/
https://www.bing.com/search?q=system%20settings%20find%20users%20groups%20mac&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=system%20settings%20find%20users%20groups%20mac&sc=12-37&sk=&cvid=B37548EB56F04FD7BD45982C45975AD0
https://www.youtube.com/watch?v=Zr_WNqvTPGc
https://developer.microsoft.com/en-us/reactor/events/26933/


## Pasted chat

allwritesri — 11:11 AM
can we connect elasticsearch as a knowledge source to the foundry agent service?
Pamela FoxRole icon, Microsoft — 11:11 AM
https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-retrieve?pivots=python#call-the-mcp-endpoint
Query Knowledge Base via APIs or MCP - Azure AI Search
Learn how to Query a knowledge base using the retrieve action or MCP endpoint in Azure AI Search using REST APIs, Azure SDKs, or any MCP-compatible client.
Query Knowledge Base via APIs or MCP - Azure AI Search
Sol — 11:11 AM
Thanks
ohh right… tool. or even a separate agent do it
Pamela FoxRole icon, Microsoft — 11:13 AM
https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-overview#supported-knowledge-sources
What is a Knowledge Source? - Azure AI Search
Learn about the knowledge source object used for agentic retrieval workloads in Azure AI Search.
What is a Knowledge Source? - Azure AI Search
lpk — 11:14 AM
Could you please detail a bit about the usecases of Foundry Memory in terms of short term session & long term memory? (Just heard about it for the first time as part of the 1st Q! - sounds cool) 
Silvestre-PO — 11:14 AM
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-memory?tabs=conversational-agent#memory-types
What is Memory? - Microsoft Foundry
Learn what memory is in Microsoft Foundry Agent Service (preview), how it works, and how to use long-term memories safely.
What is Memory? - Microsoft Foundry
Pamela FoxRole icon, Microsoft — 11:16 AM
https://github.com/langchain-ai/langchain-azure/blob/main/libs/azure-ai/langchain_azure_ai/chat_history/azure_ai_memory.py
GitHub
langchain-azure/libs/azure-ai/langchain_azure_ai/chat_history/azure...
Build secure LangChain applications on Azure. Contribute to langchain-ai/langchain-azure development by creating an account on GitHub.
Build secure LangChain applications on Azure. Contribute to langchain-ai/langchain-azure development by creating an account on GitHub.
Ron — 11:16 AM
i was wondering if we can just use the langchain framework memory?
https://docs.langchain.com/oss/python/concepts/memory
Docs by LangChain
Memory overview - Docs by LangChain
Memory overview - Docs by LangChain
I use redis, but I don't know if it supports cosmosdb
It is called checkpoint if I remember it correctly.
Patrick Schwarz — 11:18 AM
Think this is the proper Documentation for Long Term memory
Sol — 11:18 AM
😂😂😂😂
Pamela FoxRole icon, Microsoft — 11:19 AM
https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware
SummarizationMiddleware | langchain
Python API reference for agents.middleware.summarization.SummarizationMiddleware in langchain. Part of the LangChain ecosystem.
SummarizationMiddleware | langchain
quentinb305 — 11:19 AM
But the Agent Service is not making compaction?
https://learn.microsoft.com/en-us/agent-framework/agents/conversations/compaction?pivots=programming-language-python#applicability-in-memory-history-agents-only
Compaction
Learn how to manage conversation history size with compaction strategies that keep context within token limits.
Compaction
Pamela FoxRole icon, Microsoft — 11:20 AM
https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses?tabs=python-key#compact-a-response
Use the Azure OpenAI Responses API - Microsoft Foundry
Learn how to use the Azure OpenAI Responses API to create, retrieve, and delete stateful responses with Python or REST, including streaming and tools.
Use the Azure OpenAI Responses API - Microsoft Foundry
Patrick Schwarz — 11:20 AM
How is the pricing and scaling of the hosted agents working? So what happens for 20 parallel Agent api calls?
quentinb305 — 11:20 AM
"Compaction applies only to agents that manage their own conversation history in memory. Agents that rely on service-managed context or conversation state do not benefit from compaction because the service already handles context management. "

https://learn.microsoft.com/en-us/agent-framework/agents/conversations/compaction?pivots=programming-language-python#applicability-in-memory-history-agents-only 
Compaction
Learn how to manage conversation history size with compaction strategies that keep context within token limits.
Compaction
allwritesri — 11:22 AM
can someone please help on this query unable to find documentation
quentinb305 — 11:22 AM
Hosted Agent leverages Agent Service whatever the framework
so should leverage the compaction capability right?
Kosher — 11:27 AM
Quit hard to make Foundry as the enterprise product for custom enterprise agents, because LangChain/LangGraph is allowed to be hosted on Azure, but responses API isn’t compatible with it. And MAF doesn’t allow you to manage what comes into context.
Pamela FoxRole icon, Microsoft — 11:29 AM
https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/manage-hosted-sessions?pivots=rest
Manage hosted agent sessions - Microsoft Foundry
Create, invoke, and manage sessions for hosted agents in Foundry Agent Service by using the REST API, Python SDK, or Azure Developer CLI.
Manage hosted agent sessions - Microsoft Foundry
lpk — 11:29 AM
I have used 2 frameworks in my code - Langgraph & Open AI SDK for certain tools. I tried to do tracing for these 2 frameworks & 2  Azure openai models I have. Took some time & made it work but I think it'll be great to have more documentation on tracing for different frameworks.
Also many amazing features in app insights & would love to know where to explore it more!
allwritesri — 11:30 AM
like if my first message to go to first agent replica and my response goes to second agent how does the second agent knows the previous context.
if its stateless we used cosmos in our aks but our maf agent is stateless
Patrick Schwarz — 11:31 AM
You have to use the conversations in ms foundry. First call to Agent gives you back the conversation Id. Second call has to include the id so it has the Session history
Sol — 11:32 AM
If we deploy as a chat bubble on a website and call the endpoint which the agent is at, this would be useful to have session id.
Patrick Schwarz — 11:34 AM
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/runtime-components?tabs=python#conversations-and-conversation-items
Build with agents, conversations, and responses in Foundry Agent Se...
Learn how to create agents, manage conversations, and generate responses in Microsoft Foundry Agent Service with code examples in Python, C#, JavaScript, Java, and REST API.
Build with agents, conversations, and responses in Foundry Agent Se...
You can see in your foundry portal playground, next to the traces. There is a conversations tab.
Conversation Id is for the full conversation, response is id only One Message of the conversation 
Silvestre-PO — 11:40 AM
For the demonstrations in this series, how much have you spent on Azure?
asx — 11:41 AM
What was the code mode tool you mentioned on Monday that is similar to Monty?
Kalyan a.k — 11:41 AM
I have an app locally using foundry local models. can I host it as a Hosted agent keeping the Phi models in teh container?
lpk — 11:41 AM
How can we aggregate cost of execution from Foundry Traces or App Insights?
asx — 11:42 AM
Code interpreter is what I was looking for. Thank you.
Pamela FoxRole icon, Microsoft — 11:42 AM
https://github.com/dbreunig/monty-server
GitHub
GitHub - dbreunig/monty-server
Contribute to dbreunig/monty-server development by creating an account on GitHub.
Contribute to dbreunig/monty-server development by creating an account on GitHub.
lpk — 11:44 AM
How can we aggregate cost of execution for token usage from Foundry Traces or App Insights?
Pamela FoxRole icon, Microsoft — 11:46 AM
https://learn.microsoft.com/en-us/azure/container-apps/serverless-gpu-nim?tabs=bash
Tutorial: Deploy an NVIDIA Llama3 NIM to Azure Container Apps
Deploy a NVIDIA NIM to Azure Container Apps.
Tutorial: Deploy an NVIDIA Llama3 NIM to Azure Container Apps
Kalyan a.k — 11:47 AM
Any inputs using the Keyword Classification pattern even before burning tokens in a multi agent environment?
yes routing
lpk — 11:49 AM
I have used 2 frameworks in my code - Langgraph & Open AI SDK for certain tools. I tried to do tracing for these 2 frameworks & 2  Azure openai models I have. Took some time & made it work but I think it'll be great to have more documentation on tracing for different frameworks. 
Okayy Noted
Kalyan a.k — 11:51 AM
Any recommendtion or documentation to handle Vector drift over the long run?
Pamela FoxRole icon, Microsoft — 11:51 AM
https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/langchain-traces
Trace LangChain and LangGraph apps with Microsoft Foundry and Azure...
Learn how to trace LangChain and LangGraph applications in Foundry with the AzureAIOpenTelemetryTracer callback handler.
Trace LangChain and LangGraph apps with Microsoft Foundry and Azure...
https://pypi.org/project/opentelemetry-instrumentation-openai/
pablocotan — 11:52 AM
would it make sense to use Cosmos DB for LangChain/LangGraph hosted agents? And for agent-framework agents?  Would Cosmos DB bring extra benefits?
Pamela FoxRole icon, Microsoft — 11:52 AM
Langchain: enable_auto_tracing from langchain-azure-ai
pablocotan — 11:53 AM
sorry, for short and long term memories
Kalyan a.k — 11:54 AM
Any recommendtion or documentation to handle Vector drift over the long run?
Pamela FoxRole icon, Microsoft — 11:55 AM
https://cazton.com/blogs/technical/ai-agent-memory-patterns
AI Agent Memory Patterns | Cazton
Compare 4 AI agent memory strategies on recall, token cost & latency using Azure Cosmos DB and OpenAI. Entity Graph hit 100% recall. See the full benchmark.
Image
Kalyan a.k — 11:57 AM
yeah. incremental updates
RyanPrice1001 — 11:58 AM
Thanks Pamela! 🚀 🚀
Kalyan a.k — 11:58 AM
thank you Pamela
asx — 11:59 AM
Thank you so much!
lpk — 11:59 AM
Thank you so much for answering Pamela!!