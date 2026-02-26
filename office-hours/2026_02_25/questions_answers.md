# Feb 25, 2026 Office Hours Q&A

Note: This session was a follow-up Q&A after the [Python + Agents Session 2 livestream](https://developer.microsoft.com/en-us/reactor/events/26689/), focused on adding context and memory to agents using the Microsoft Agent Framework.

## How can we configure the GitHub workspace to call paid, authenticated Azure LLMs?

📹 [0:54](https://youtube.com/watch?v=X0m0GxJRT0Y&t=54)

The [python-agentframework-demos](https://github.com/Azure-Samples/python-agentframework-demos) repo README has instructions for configuring model providers. If you're not using GitHub Models in a Codespace, you need to set up a `.env` file. Options:

- **GitHub Models locally**: Set up a personal access token as described in the README.
- **Azure AI Foundry models**: Use the Bicep provisioning included in the repo (`azd up`) which will write the `.env` file for you automatically. Or manually create a `.env` with your endpoint and chat deployment name.
- **Other providers**: OpenAI, Ollama, etc. are also supported with similar `.env` configuration.

The `.env.sample` shows the required variables: endpoint and chat deployment. By default, keyless authentication is used (no API key). If you want to use a key, you'd need to modify the code. Running `azd up` as suggested in the README will provision the resources and write the `.env` file automatically.

Links shared:

* [python-agentframework-demos README - Using Azure AI Foundry Models](https://github.com/Azure-Samples/python-agentframework-demos?tab=readme-ov-file#using-azure-ai-foundry-models)

## Will this series cover hosting agents in Azure, such as options and best practices?

📹 [4:11](https://youtube.com/watch?v=X0m0GxJRT0Y&t=251)

The original plan was to do a separate follow-up series specifically about hosting agents on Azure, since this series emphasizes code you can run locally (mostly free with GitHub Models). However, there's been a lot of demand for deployment content.

Next week's session (Session 3) will include one deployment example using Azure Container Apps. But there are many more options:

- **Azure Container Apps** — just requires writing a Dockerfile for your Python agent
- **Azure Functions**
- **Container App Jobs** — for long-running workflows
- **Foundry Hosted Agents**

For Container Apps specifically, it's really about writing the right Dockerfile. For example, deploying an agent using the Playwright MCP server requires a Dockerfile that installs both Python and npm/Playwright.

The [official documentation on hosting options](https://learn.microsoft.com/en-us/agent-framework/get-started/hosting?pivots=programming-language-python) covers some of these, though it doesn't mention Container Apps specifically (since that's just a Docker container).

Links shared:

* [Agent Framework hosting documentation](https://learn.microsoft.com/en-us/agent-framework/get-started/hosting?pivots=programming-language-python)
* [Playwright MCP on Azure Container Apps example](https://github.com/simonjj/playwright-mcp-on-aca)

## How should you manage multi-tier memory to store lots of information while keeping local storage manageable?

📹 [7:09](https://youtube.com/watch?v=X0m0GxJRT0Y&t=429)

The session demos used mem0's basic option, but mem0 offers more advanced features including **graph memory** for remembering entities and relationships. User memories typically go into the system prompt, while conversation history stays as messages in the thread — these are handled separately.

For inspiration, look at existing memory systems. For example, you can inspect GitHub Copilot's memory to see what memories are being stored and how summarization works.

Links shared:

* [mem0 Graph Memory documentation](https://docs.mem0.ai/open-source/features/graph-memory)

### Should the original conversation be saved when summarizing, or is it useful to toss the details?

📹 [21:55](https://youtube.com/watch?v=X0m0GxJRT0Y&t=1315)

You could definitely store the original in memory as long as you're not worried about memory constraints (it's just text). For inspiration on how to implement summarization, look at LangChain's built-in summarization middleware — the session's middleware example was inspired by it, though simplified.

A cautionary tale about summarization: Pamela shared an experience where GitHub Copilot compacted a conversation and lost critical context. She said "yes please" to a one-line caption request, but after summarization, Copilot interpreted the "yes please" as agreement to implement an entire plan. Key takeaways:

- Be very careful that summarization retains the most recent context
- Consider only summarizing everything *before* the last message
- In your summarizer prompt, account for short follow-up messages like "yes please" that reference specific prior context
- Set up example conversations as test cases for your summarization to evaluate edge cases like this

Links shared:

* [LangChain context editing middleware](https://github.com/langchain-ai/langchain/blob/94a58825d352e15b2f5a132859b08827f7b208fb/libs/langchain_v1/langchain/agents/middleware/context_editing.py)

## What's a good plan to learn how to build agents with the Agent Framework?

📹 [9:01](https://youtube.com/watch?v=X0m0GxJRT0Y&t=541)

1. **Run all the examples** from the session and make sure you understand them
2. **Ask Copilot questions** about code you don't understand — it can dig into the Agent Framework source code and explain things
3. **Pick one example and build on it** — extend something that already works for a scenario relevant to you (home life, developer workflows, etc.)
4. **Choose a domain you have expertise in** — this is critical because LLMs can be convincingly wrong, so you need to be able to evaluate whether the agent's answers are good

Links shared:

* [Python + Agents Session 1 write-up](https://github.com/pamelafox/presentation-writeups/blob/main/presentations/python-agents-session1/outputs/writeup.md)

## VS Code often forgets you have a venv in your project — does it swap that knowledge out of its memory?

📹 [11:18](https://youtube.com/watch?v=X0m0GxJRT0Y&t=678)

To investigate what information Copilot actually receives, use the **Chat Debug View**: click the "..." menu in the Copilot chat panel and select "Show Chat Debug View." This reveals everything sent to the LLM, including:

- All available tools
- The full system prompt from GitHub Copilot
- Memory guidelines and stored memories (user and repository memories)
- Environment info (OS, workspace folders)
- Current date, terminal info, last command run

In the demo, the environment info listed the OS as Linux (because of the dev container) and showed workspace folders, but did *not* mention the venv — even though one existed. This might be because the venv is in `.gitignore`. The Python environment tools *should* return this info, but it may not always work correctly. If you encounter this bug, use the thumbs-down button to report an issue — it pre-fills your VS Code info and routes it to the right repo.

## Why would you use Agent Framework instead of the Foundry SDK, and why consider non-Foundry hosting options?

📹 [15:01](https://youtube.com/watch?v=X0m0GxJRT0Y&t=901)

**Foundry SDK / Foundry Agents** run the entire agent loop in the cloud. Benefits:

- Built-in tools (Bing search, code interpreter) are easy to use since the agent is already running in Azure
- Built-in session management with threads — no need to set up your own database
- Less setup overall

**Drawbacks of hosted agents:**

- Less flexibility — you can't add middleware at as many points as with Agent Framework
- If the agentic loop runs in the cloud, it's harder to insert yourself into it and customize
- The portal experience may not expose all SDK capabilities
- Foundry is undergoing significant changes (Classic vs New UI, hub-based vs new projects, agents v1 vs v2)

**When to choose Agent Framework:** If you need deep customization, extensive middleware, or find yourself hitting limitations with the hosted service. You can also host Agent Framework apps on Foundry as "hosted agents" to get some Foundry management benefits.

**When Foundry SDK is fine:** If it has everything you need and you don't find yourself needing more customization.

Links shared:

* [Azure AI Foundry SDK overview](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview?view=foundry-classic&pivots=programming-language-python)

## Can you confirm that designing your overall project cannot be LLM agnostic?

📹 [17:45](https://youtube.com/watch?v=X0m0GxJRT0Y&t=1065)

The demos use the OpenAI chat completions API, which is widely supported (OpenAI models, Azure OpenAI, Ollama, many others). However, OpenAI has introduced the **Responses API**, which is more agentic:

- Supports built-in tools (code interpreter, web search on Azure)
- Has a notion of state (stateful or stateless)
- Azure is standardizing on Responses API
- Foundry provides a generic Responses API layer across *all* its models (DeepSeek, Mistral, Llama, etc.)

The series used chat completions because **GitHub Models doesn't support Responses API yet**, and the demos were designed to run on GitHub Models. In production, the recommendation is to use **Responses API** for maximum model agnosticism when models are on Foundry — you can then point at any Foundry model and your code will work.

Links shared:

* [AI Model Starter Kit (Responses API examples)](https://github.com/Azure-Samples/ai-model-start?tab=readme-ov-file#the-ai-model-starter-kit)

## What are the issues with Foundry?

📹 [30:27](https://youtube.com/watch?v=X0m0GxJRT0Y&t=1827)

There's a lot changing in the Foundry ecosystem:

- **Two kinds of projects**: hub-based projects and the new Foundry projects
- **Two UIs**: Foundry Classic and Foundry New — some features work in one but not the other
- **Two agent service versions**: agents v1 and agents v2
- **Breaking changes** as things evolve

You need to keep track of which kind of project you're in, which UI you're using, and which agent service version you're on.

### Is Foundry IQ using GraphRAG with knowledge graphs?

📹 [31:34](https://youtube.com/watch?v=X0m0GxJRT0Y&t=1894)

First, clarification on the three "IQ" services at Microsoft:

- **Foundry IQ** — basically Azure AI Search's knowledge-base feature
- **Fabric IQ** — built on top of Microsoft Fabric ontologies
- **Work IQ** — built on top of Microsoft Graph, available as an MCP server

Foundry IQ does **not** use GraphRAG at this point. The AI Search team has looked into it but hasn't found a good way to productionize graph RAG queries efficiently with consistent results. The team is also exploring other retrieval improvements like **ColBERT** (multi-vector embeddings), but the challenge is always making research approaches work at production scale for everyone.

Links shared:

* [Weaviate multi-vector embeddings tutorial](https://docs.weaviate.io/weaviate/tutorials/multi-vector-embeddings)

## Is there any middleware for context caching that can cut down on token usage?

📹 [33:32](https://youtube.com/watch?v=X0m0GxJRT0Y&t=2012)

There are two different kinds of caching to consider:

**LLM-level caching** (handled by the model provider):
- Anthropic models have long-context caching
- OpenAI models cache structured output JSON schemas (first call is slow, subsequent calls are faster)
- Many LLMs implement system prompt caching — if you keep the first N tokens of the system prompt the same, they'll be cached
- You can take advantage of this by keeping your system prompt prefix stable

**Middleware-level token reduction** (your code):
- Truncation — removing oldest messages (risks losing important context)
- Heuristic-based removal — e.g., LangChain's context editing middleware clears older tool results after a certain number
- The key is having a heuristic that doesn't require an LLM call to determine what to remove
- Always evaluate whether your heuristic still produces good results

### Does model routing save tokens?

📹 [39:45](https://youtube.com/watch?v=X0m0GxJRT0Y&t=2385)

Model routing can save costs by using cheaper LLMs for simpler questions. It can also indirectly reduce token usage because some LLMs are more verbose than others — for example, some models generate 10 different queries for AI Search while others generate only 2. You can also control verbosity through system prompts or by cutting off excessive tool calls.

Links shared:

* [Performance Benchmarking LLM Models (Anthony Shaw)](https://tonybaloney.github.io/posts/performance-benchmarking-llm-models.html)

## Do we have examples with App Service and UV on Azure?

📹 [36:54](https://youtube.com/watch?v=X0m0GxJRT0Y&t=2214)

App Service for Linux announced UV support in November 2025 via a [blog post](https://techcommunity.microsoft.com/blog/appsonazureblog/what%E2%80%99s-new-for-python-on-app-service-for-linux-pyproject-toml-uv-and-more/4468903). Gwen Sadler (from the team) has been working with the App Service team on this. Attendees reported issues getting it to work — Gwen and others were encouraged to collaborate and report any bugs to the App Service team.

Links shared:

* [What's new for Python on App Service for Linux: pyproject.toml, UV, and more](https://techcommunity.microsoft.com/blog/appsonazureblog/what%E2%80%99s-new-for-python-on-app-service-for-linux-pyproject-toml-uv-and-more/4468903)

## Is it possible to use skills (like GitHub Copilot skills) in the Microsoft Agent Framework?

📹 [38:17](https://youtube.com/watch?v=X0m0GxJRT0Y&t=2297)

Yes! Support was just recently added. The .NET support shipped first, and Python support was merged as a [PR #4210](https://github.com/microsoft/agent-framework/pull/4210). It's implemented as a **context provider** — if you have skills defined in the file system, you can advertise them to the agent. To try it, you'll need to point your dependency at the latest main branch of the Agent Framework, update the git hash, run `uv sync`, and test it out.

Links shared:

* [Agent Framework PR #4210 - Python agent skills support](https://github.com/microsoft/agent-framework/pull/4210)

## What about the TOON notation format for reducing token usage?

📹 [41:44](https://youtube.com/watch?v=X0m0GxJRT0Y&t=2504)

Be cautious about new notation formats designed to save tokens. Research (shared by Drew Brunig) found that **saving a handful of tokens in the data format is wasted if models are not trained on the format**. In testing, TOON actually consumed *more* tokens because models didn't understand the syntax and couldn't use it well.

The same principle applies generally: we benefit enormously from the fact that LLMs know existing formats like YAML deeply — they understand its syntax, know PyYAML for parsing, and can interact with it in many ways. Even if everyone "silently hates YAML," it works well with LLMs because they're trained on it extensively.

For context-related topics, Pamela recommended following Drew Brunig, who is writing a book on the subject.

Links shared:

* [TOON format](https://github.com/toon-format/toon)