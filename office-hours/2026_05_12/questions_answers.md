# May 12, 2026 Office Hours Q&A

## Where could I start learning about Python and AI?

📹 [0:31](https://youtube.com/watch?v=L7b_ppsJn2c&t=31)

Pamela recommended her blog post about [how she personally learns about generative AI](https://blog.pamelafox.org/2025/08/how-i-learn-about-generative-ai.html), which links to the Python + AI video series at the bottom. The most important thing is to actually try things hands-on — that's the way you really learn. The [Python + AI video series](https://techcommunity.microsoft.com/blog/educatordeveloperblog/level-up-your-python--ai-skills-with-our-complete-series/4464546) is designed for someone who knows some Python but doesn't yet know generative AI. All the videos are free to watch on YouTube.

Links shared:

* [How I learn about generative AI](https://blog.pamelafox.org/2025/08/how-i-learn-about-generative-ai.html)
* [Level up your Python + AI skills with our complete series](https://techcommunity.microsoft.com/blog/educatordeveloperblog/level-up-your-python--ai-skills-with-our-complete-series/4464546)

## Do you have links for free Azure credits to use Foundry?

📹 [1:48](https://youtube.com/watch?v=L7b_ppsJn2c&t=108)

Pamela doesn't have coupons to give out. The [Azure free trial](https://azure.microsoft.com/en-us/pricing/details/microsoft-foundry/) exists, but it likely doesn't work for Foundry model usage. Foundry's pricing page says it's "free to use and explore," but that likely just means you can browse the leaderboard and poke around — as soon as you start using models, you need to pay. That said, if you're just doing a few small tests, it's not very expensive — Pamela got a bill of about a dollar for her tests with Anthropic models building an agent. You really only need a proper payment setup if you're developing an app or doing evaluations that require many calls.

## How did the Code with Claude workshop use Foundry?

📹 [4:13](https://youtube.com/watch?v=L7b_ppsJn2c&t=253)

Pamela attended the Code with Claude conference and ran a [workshop](https://github.com/hnky/code-with-claude-foundry-workshop) using Claude models (Sonnet, Haiku, and Opus) deployed from Foundry. They used Microsoft Agent Framework pointed at an Anthropic model deployment to build a cupcake store ordering agent. The workshop repo shows how to set up the deployment name, API key, and endpoint.

You can also watch a video of [Pamela walking through the agent](https://www.youtube.com/watch?v=LYwV8IQVRIo).

Links shared:

* [Code with Claude Foundry workshop](https://github.com/hnky/code-with-claude-foundry-workshop)

## With the Copilot pricing changes and 9x multiplier, do you have any recommendations on getting around this?

📹 [7:07](https://youtube.com/watch?v=L7b_ppsJn2c&t=427)

GitHub Copilot is moving to usage-based billing starting June 1st, based on token usage. Pamela shared several free alternatives for prototyping:

- **[NVIDIA NIM](https://developer.nvidia.com/nim)** — A developer she met said you get free access to NIM API endpoints for "unlimited prototyping" (though there are likely limits like slower speeds)
- **[GitHub Models](https://github.com/marketplace?type=models)** — Free but hasn't been updated with the most recent models and doesn't support the responses API
- **[Ollama](https://ollama.com/)** — Run models locally for free if your machine is powerful enough. Pamela currently runs Qwen 3.5 and Gemma 4 locally on her new Mac M5 Max
- **[CanIRun.ai](https://www.canirun.ai/)** — A website that predicts which models you can run on your machine based on your hardware

For local models, Pamela noted that QPTD OS is good for agentic stuff, and she planned to download it for her new machine.

Links shared:

* [NVIDIA NIM](https://developer.nvidia.com/nim)
* [GitHub Models marketplace](https://github.com/marketplace?type=models)
* [Ollama](https://ollama.com/)
* [CanIRun.ai](https://www.canirun.ai/)

## Can you give advice to AI student graduates on what skills to pick up to get interviews lined up?

📹 [14:03](https://youtube.com/watch?v=L7b_ppsJn2c&t=843)

For software engineering roles, Pamela recommended:

1. **Know how to use agentic coding tools** — GitHub Copilot, Claude Code, or Codex. Companies increasingly expect developers to use these tools, and they help you write code faster even if you just use them as supercharged autocomplete.

2. **Know how to incorporate an LLM into things you're building** — Think of it like knowing regular expressions. Sometimes you need a regex, and now sometimes you need an LLM. LLMs are replacing regex in many places where you previously did fuzzy matching. You should be able to reach for an LLM as a tool and know how to write different kinds of tests for non-deterministic behavior.

3. **Standard interview prep** — Look at job descriptions for specific skills they want (distributed systems, API design, etc.), use Glassdoor for interview questions, and prepare for algorithmic/data structures questions.

The best approach is to find a job posting you're interested in, identify the skills it requires, and work on those specific skills.

### Can we be picky on which companies we want when we have no real experience?

📹 [19:00](https://youtube.com/watch?v=L7b_ppsJn2c&t=1140)

If you have no real experience, you typically start at an internship or junior level. You shouldn't work at a job you hate, but be open to working at lots of different places. Don't necessarily aim for the hardest-to-get-into companies (like OpenAI or Anthropic) right away — there are tons of companies out there that can be really interesting.

## What's the best approach for adding knowledge to agents — Karpathy Wiki, Vector RAG, or Knowledge Graphs?

📹 [20:15](https://youtube.com/watch?v=L7b_ppsJn2c&t=1215)

Pablo asked about the optimal retrieval approach for expert agents that need completeness, correctness, and pattern detection. Pamela agreed that different retrieval mechanisms work better for different types of queries and sources. Key points:

**Multi-source RAG with specialized retrieval layers:** Azure AI Search supports multi-source RAG where each source implements its own retrieval mechanism (e.g., Fabric ontology uses graph-like queries, Work IQ has its own retrieval approach). You can send queries in parallel to different sources using customized retrieval, then merge and rank results using reciprocal rank fusion or semantic ranking models.

**Completeness is the hardest problem:** The only way to truly know you've done a complete search is to look at everything. Azure AI Search has a semantic classification model that checks whether retrieved documents fully answer the query, and if not, performs another search. You can implement similar logic in your agent — break the question down into information needs, check which are covered by results, and keep searching if needs remain unmet.

**Graph RAG for completeness:** Graph RAG is good for completeness if the ontology is thorough, since you can keep following nodes until all are traversed. However, it's expensive, so you'd want a routing layer that identifies "deep queries" requiring comprehensive search versus queries that basic search can handle. You could implement this as an agent with tools for "basic search" and "deep search" with descriptions guiding when to use each.

**Related approaches:**
- [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Ingest sources into summaries, then search via an index file. Works at moderate scale (hundreds of pages)
- [TypeAgent-py](https://github.com/microsoft/typeagent-py) — Structured RAG that can ingest and extract entities and relations
- [Microsoft GraphRAG](https://microsoft.github.io/graphrag/) — The main Microsoft graph RAG project
- [LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) — A research paper about cheaper graph RAG (code not yet released)
- [Hindsight](https://github.com/vectorize-io/hindsight) — Agent memory package that uses semantic search, keyword search, graph traversal, and time series in parallel, then merges with a cross-encoder reranking model
- [Ralph Loop](https://claude.com/plugins/ralph-loop) — A persistent AI agent loop that keeps working until complete, useful for experimentation. Codex has a similar feature with `/goal`.

Links shared:

* [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
* [microsoft/typeagent-py](https://github.com/microsoft/typeagent-py)
* [Microsoft GraphRAG](https://microsoft.github.io/graphrag/)
* [LazyGraphRAG blog post](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)
* [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
* [Ralph Loop plugin](https://claude.com/plugins/ralph-loop)
* [Codex /goal use case](https://developers.openai.com/codex/use-cases/follow-goals)

## Can you explain what different IQ use cases like WorkIQ, FabricIQ, and FoundryIQ are?

📹 [43:13](https://youtube.com/watch?v=L7b_ppsJn2c&t=2593)

**Foundry IQ** is the higher-level search mechanism. It can both create and search its own indexes, and connect to different sources (including any MCP endpoint). Think of it as a higher-level search that sends queries to multiple sources in parallel, gets back results, and merges them using reciprocal rank fusion and semantic ranking models.

**Fabric IQ** has two main components:
- **Ontologies** — A graph representation of your data where you define entity types, relationships, and categories. You can send graph-like queries across the [ontology](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview), similar to SQL queries on top of your Fabric data.
- **[Data Agents](https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent)** — Higher-level than ontologies, these incorporate their own LLM to try to answer questions directly about your data.

Both need to be enabled at the Fabric tenant level by an admin.

**[Work IQ](https://github.com/microsoft/work-iq)** is an agent on top of your M365 read-only data (Teams chats, emails, calendar events). It's available as a CLI and an MCP server. It can query but not create/edit/delete. It's easier to integrate from a permissions perspective for querying M365. You can use it directly from the command line or point any MCP-supporting tool at its MCP server.

Links shared:

* [Fabric IQ Ontology overview](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview)
* [Fabric Data Agent concept](https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent)
* [microsoft/work-iq](https://github.com/microsoft/work-iq)

## Does Microsoft Agent Framework support a combination of checkpoints and session per agent in a handoff workflow?

📹 [47:54](https://youtube.com/watch?v=L7b_ppsJn2c&t=2874)

Pamela deferred this to the agent framework team since she wasn't sure of the answer. She pointed to the [banking assistant sample](https://github.com/Azure-Samples/agent-openai-python-banking-assistant/blob/main/app/backend/app/agents/azure_chat/handoff_orchestrator.py) by David Imo, which uses both checkpoint storage and thread IDs — it likely has a combination of session and checkpointing. David has done the most experimentation with that combination of features.

For further help, Pamela recommended posting in the [agent-framework discussions](https://github.com/microsoft/agent-framework/discussions) tab, as the team also runs their own office hours.

Links shared:

* [Banking assistant handoff orchestrator](https://github.com/Azure-Samples/agent-openai-python-banking-assistant/blob/main/app/backend/app/agents/azure_chat/handoff_orchestrator.py)
* [Agent framework discussions](https://github.com/microsoft/agent-framework/discussions)

## Announcements

📹 [0:00](https://youtube.com/watch?v=L7b_ppsJn2c&t=0)

**Claude models on Foundry:** Claude models (Sonnet, Haiku, Opus) are now available through Microsoft Foundry. See [aka.ms/claude/start](https://aka.ms/claude/start).

**GPT-5.5 in GitHub Copilot:** GPT-5.5 is now generally available for GitHub Copilot.

**GitHub Copilot pricing changes:** Sign-ups are paused and rate limits are now visible. Usage-based billing starts June 1st.

**Microsoft Agent Framework + Anthropic client:** The [agent framework](https://github.com/microsoft/agent-framework) now supports Anthropic models.

**OpenAI winding down fine-tuning:** OpenAI is [deprecating the self-serve fine-tuning API](https://community.openai.com/t/openai-is-winding-down-the-fine-tuning-api-and-platform-discussion-thread/1380522). Pamela was checking whether this also affects Azure OpenAI fine-tuning.

**PyCon US this week:** Pamela is running a [tutorial on building MCP servers](https://us.pycon.org/2026/schedule/presentation/2/) and presenting at the [EduSummit on AI-powered slides](https://us.pycon.org/2026/events/education-summit/).

**Build 2026:** A lab session on Foundry IQ is in development: [Build26-LAB532](https://github.com/microsoft/Build26-LAB532).

**New Mac M5 Max:** Pamela got a new Mac and is exploring local SLMs on it.
