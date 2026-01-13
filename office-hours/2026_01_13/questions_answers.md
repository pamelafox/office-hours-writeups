# Python + AI Office Hours Q&A - January 13, 2026

## What advantages do other formats have over .txt for prompts? How do you improve prompts with DSPy and evals?

📹 [4:55](https://youtube.com/watch?v=ePFH0-1cEck&t=295)

**Prompty** is a template format that mixes Jinja and YAML together. The YAML goes at the top for metadata, and the rest is Jinja templating. Jinja is the most common templating system for Python (used by Flask, etc.). The nice thing about Jinja is you can pass in template variables—useful for customization, passing in citations, etc. Prompty turns the file into a Python list of chat messages with roles and contents.

However, we're moving from Prompty to plain Jinja files because:
- Prompty doesn't support the Responses API
- Prompty hasn't seen much adoption—it's hard to get people to adopt new formats
- It's easier to just use text files, markdown files, or something people already know

**Recommendation**: Keep prompts separate from code when possible, especially long system prompts. Use plain .txt or .md if you don't need variables, or Jinja if you want to render variables. With agents and tools, some LLM-facing text (like tool descriptions in docstrings) will inevitably live in your code—that's fine.

**For iterating on prompts**: Run evaluations, change the prompt, and see whether it improves things. There are tools like DSPy and Agent Framework's Lightning that do automated prompt optimization/fine-tuning. Lightning says it "fine-tunes agents" but may actually be doing prompt changes. Most of the time, prompt changes don't make a huge difference, but sometimes they might.

Links shared:
- [Prompty file example](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/app/backend/approaches/prompts/chat_answer_question.prompty)
- [Agent Framework Lightning](https://github.com/microsoft/agent-framework/tree/main/python/packages/lab/lightning)
- [Agent Framework GAIA (evaluation)](https://github.com/microsoft/agent-framework/tree/main/python/packages/lab/gaia)

## What is the future of AI and which specialization should I pursue?

📹 [11:54](https://youtube.com/watch?v=ePFH0-1cEck&t=714)

If you enjoy software engineering and full-stack engineering, it's more about understanding the models so you understand why they do what they do, but it's really about how you're building on top of those models. There's lots of interesting stuff to learn, and it really depends on you and what you're most interested in doing.

## Which livestream series should I follow to build a project using several tools and agents, and should I use a framework?

📹 [13:33](https://youtube.com/watch?v=ePFH0-1cEck&t=813)

Everyone should understand tool calling before moving on to agents. From the original 9-part Python + AI series, start with tool calling, then watch the high-level agents overview. The upcoming six-part series in February will dive deeper into each topic, especially how to use Agent Framework.

At the bare minimum, you should understand LLMs, tool calling, and agents. Then you can decide whether to do everything with just tool calling (you can do it yourself with an LLM that has tool calling) or use an agent framework like LangChain or Agent Framework if you think it has enough benefits for you.

It's important to understand that agents are based on tool calling—it's the foundation of agents. The success and failure of agents has to do with the ability of LLMs to use tool calling.

Links shared:
- [Python + AI series](https://aka.ms/PythonAI/series)
- [Python + Agents series (English)](https://developer.microsoft.com/en-us/reactor/series/S-1631/)
- [Python + Agents series (Spanish)](https://developer.microsoft.com/en-us/reactor/series/S-1633/)

## How does Azure manage the context window? How do I maintain a long conversation with a small context window?

📹 [15:21](https://youtube.com/watch?v=ePFH0-1cEck&t=921)

There are three general approaches:

1. **Send the last N messages** - This is the most naive approach, but you don't actually know if they're going to fit.

2. **Send only messages that fit** - Pre-count the tokens and only send messages that fit inside your remaining tokens. This is hard to do correctly as you're basically reverse-engineering the models to figure out how to calculate tokens. There's a library for this if you want to attempt it.

3. **Summarize the conversation** - When the conversation gets too long, make a call to summarize it. You can either wait for an error from the LLM that says the context is too long and then summarize, or proactively summarize before hitting the limit.

With today's large context windows (128K, 256K), it's often easier to just wait for an error and tell the user to start a new chat, or do summarization when the error occurs. This approach is most likely to work across models since every model should throw an error when you're over the context window.

Links shared:

- [Truncating conversation history for OpenAI chat completions](https://blog.pamelafox.org/2024/06/truncating-conversation-history-for.html)
- [OpenAI Messages Token Helper](https://github.com/pamelafox/openai-messages-token-helper)

## How do we deal with context rot and how do we summarize context using progressive disclosure techniques?

📹 [19:17](https://youtube.com/watch?v=ePFH0-1cEck&t=1157)

Read through Kelly Hong's (Chroma researcher) blog post on context rot. The key point is that even with a 1 million token context window, you don't have uniform performance across that context window. She does various tests to see when performance starts getting worse, including tests on ambiguity, distractors, and implications.

A general tip for coding agents with long-running tasks: use a main agent that breaks the task into subtasks and spawns sub-agents for each one, where each sub-agent has its own focused context. This is the approach used by the LangChain Deep Agents repo.

You can also look at how different projects implement summarization. LangChain's summarization middleware is open source—you can see their summary prompt and approach. They do approximate token counting and trigger summarization when 80% of the context is reached.

Links shared:
- [P6: Context Rot - Hamel's Blog](https://hamel.dev/notes/llm/rag/p6-context_rot.html)
- [LangChain Deep Agents](https://github.com/langchain-ai/deepagents)
- [LangChain Deep Agents Quickstarts](https://github.com/langchain-ai/deepagents-quickstarts)
- [LangChain Summarization Middleware](https://github.com/langchain-ai/langchain/blob/1ead03c79de70c7a3334fc8a14fa711e15eb6f8d/libs/langchain_v1/langchain/agents/middleware/summarization.py#L151)

### How do I deal with context issues when using the Foundry SDK with a single agent?

📹 [25:03](https://youtube.com/watch?v=ePFH0-1cEck&t=1503)

If you're using the Foundry SDK with a single agent (hosted agent), you can implement something like middleware through hooks or events. Another approach is the LangChain Deep Agents pattern: implement sub-agents as tools where each tool has a limited context and reports back a summary of its results to the main agent.

For the summarization approach with Foundry agents, you'd need to figure out what events, hooks, or middleware systems they have available.

## Have you seen or implemented anything related to AG-UI or A2UI?

📹 [29:02](https://youtube.com/watch?v=ePFH0-1cEck&t=1742)

**AG-UI (Agent User Interaction Protocol)** is an open standard introduced by the CopilotKit team that standardizes how front-end applications communicate with AI agents. Both Pydantic AI and Microsoft Agent Framework have support for AG-UI—they provide adapters to convert messages to the AG-UI format.

The advantage of standardization is that if people agree on a protocol between backend and frontend, it means you can build reusable front-end components that understand how to use that backend.

Agent Framework also supports different UI event stream protocols, including Vercel AI (though Vercel is a competitor, so support may be limited). These are adapters—you can always adapt output into another format if needed, but it's nice when it's built in.

**A2UI** is created by Google with Consortium CopilotKit and relates to A2A (Agent-to-Agent). A2UI appears to be newer with less support currently in Agent Framework, though A2A is supported.

Links shared:
- [Agent Framework AG-UI](https://github.com/microsoft/agent-framework/tree/main/python/packages/ag-ui)
- [Pydantic AI AG-UI](https://ai.pydantic.dev/ui/ag-ui/)
- [A2UI](https://a2ui.org/)

## Can you comment on using a "harness" for long-running agents to solve complex tasks?

📹 [35:35](https://youtube.com/watch?v=ePFH0-1cEck&t=2135)

The Anthropic blog post discusses having an initializer agent and coding agent architecture. Key insights:

**Planning phase is crucial**: Start with planning where you encourage the agent to ask any questions it has. Get all questions answered before going into the long-running phase so someone can step away from it. Have the planning phase write out a plan in a markdown file so you can edit it yourself.

**Specialized agents**: The article discusses having a testing agent, quality assurance agent, and code cleanup agent—getting into the deep agents concept where each agent does its best job.

**Architecture options with Agent Framework**:
- **Supervisor architecture**: Sub-agents are used as tools; the supervisor calls them and gets responses
- **Magentic architecture**: Superpowered supervisor with progress ledger and progress checking (though with new models, it's unclear if progress ledgers or to-dos are even needed)
- **Handoff architecture**: Pass the entire conversation to the next agent

**Practical experimentation**: In VS Code, you can now have agents that run sub-agents. Try experimenting with that to see how it works inside a coding agent before building something complex.

It's hard to say which architecture works best without practical experience—you have to try it out and see what works for your use case.

Links shared:
- [Effective harnesses for long-running agents - Anthropic](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Agent Framework GAIA example](https://github.com/microsoft/agent-framework/tree/main/python/packages/lab/gaia)

## What do you think of Hindsight for agent memory solving context problems?

📹 [42:15](https://youtube.com/watch?v=ePFH0-1cEck&t=2535)

Hindsight stores documents, memories, and entities separately—distinguishing memories from entities is interesting. This is similar to what Mem0 does with their entity/graph/hierarchical options.

For search, Hindsight uses vector, keyword, fusion, cross-encoder, graph, and temporal approaches. AI Search does some of this (fusion, cross-encoder) but doesn't do graph currently.

This approach is also similar to Guido's TypeAgent project presented at PyCon, which uses LLMs to extract entities.

**Cost considerations**: Every time a message happens, you need to decide whether to retain it (usually an LLM call). Every new message requires checking if there's something to recall. Reflection also happens after messages. All of this adds latency and cost.

**When it's worth it**: If you're building a very personalized user-facing experience where users put a lot of personal data (like a therapy bot, email assistant, etc.), the extra cost may be justified.

Links shared:
- [Hindsight](https://hindsight.vectorize.io/)
- [Mem0](https://mem0.ai/)
- [Letta](https://www.letta.com/)
- [Mem0 with Azure AI Search](https://docs.mem0.ai/components/vectordbs/dbs/azure)
- [TypeAgent](https://pypi.org/project/typeagent/)
- [MemGPT paper](https://arxiv.org/pdf/2310.08560)

### Using Mem0 with AI Search for user preferences

📹 [49:30](https://youtube.com/watch?v=ePFH0-1cEck&t=2970)

One attendee shared they're using Mem0 with AI Search for user preferences and a separate approach for documents. Mem0 can use Azure AI Search as a vector database backend. For documents, consider using the new agentic knowledge bases in AI Search (presented at Build) which supports multi-sources like SharePoint and web.

## What was Pamela working on from Jan 6-Jan 13?

📹 [52:01](https://youtube.com/watch?v=ePFH0-1cEck&t=3121)

**Office Hours Writeups with Agent Skills**: A new repo that uses VS Code agent skills to turn office hours recordings into structured Q&A. It extracts the YouTube transcript, generates questions and answers, and posts them as comments to a GitHub Discussion thread. This uses two skills: one for YouTube transcripts and one for posting to GitHub Discussions.

**Entra OBO with Python MCP servers**: The demo from last week is now merged, with a video showing the Entra OBO flow.

**Azure Search OpenAI Demo updates**:
- Ported from mypy to ty (Astral's Rust-based type checker) - CI went from 2 minutes to 2 seconds
- Working on porting from Chat Completions to Responses API
- Porting from Prompty to Jinja
- ACL improvements

**ty type checker**: Highly recommended for Python type checking. It's incredibly fast (2 seconds vs 2 minutes for mypy). Note: it doesn't work well for multi-root workspaces in VS Code yet.

Links shared:
- [Office Hours Writeups repo](https://github.com/pamelafox/office-hours-writeups)
- [Office Hours Discussion Thread](https://github.com/orgs/microsoft-foundry/discussions/280)
- [Python MCP Demos with Entra OAuth](https://github.com/Azure-Samples/python-mcp-demos?tab=readme-ov-file#deploy-to-azure-with-entra-oauth-proxy)
- [mypy to ty migration PR](https://github.com/Azure-Samples/azure-search-openai-demo/pull/2911)
