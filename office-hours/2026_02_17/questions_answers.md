# Feb 17, 2026 Office Hours Q&A

## Announcement: Claude Sonnet 4.6 Availability

📹 [1:26](https://youtube.com/watch?v=c4_sjAwFNAY&t=86)

Claude Sonnet 4.6 is a new model from Anthropic — smaller and faster than Opus 4.6 but still highly capable, and likely cheaper. What is known about Sonnet 4.6:

- Available in Azure Foundry models (and rolling out to GitHub Copilot today)
- Has a **1 million token context window** — confirmed even on Foundry
- Benchmarks show it excels at financial analysis and office tasks (though benchmarks should always be taken with a grain of salt and tested against your specific use case)
- Cheaper and faster than Opus 4.6, though Opus generally scores higher on most benchmarks
- Claude's own announcement says it's better at long-horizon planning

Links shared:

- [Claude Sonnet 4.6 on Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/how-to/use-foundry-models-claude)
- [Claude Sonnet 4.6 now GA in GitHub Copilot](https://github.blog/changelog/2026-02-17-claude-sonnet-4-6-is-now-generally-available-in-github-copilot/)

## Any update on Anthropic models available over Azure for CSP clients?

📹 [4:29](https://youtube.com/watch?v=c4_sjAwFNAY&t=269)

As of now, **Cloud Solution Provider (CSP) accounts are restricted** from using Anthropic Claude models in Azure Foundry. To use Claude models in Azure Foundry, you need a paid Azure subscription from a billing account in a country or region where Anthropic offers models — CSP accounts don't qualify.

For the current status, the recommendation is to check with the Azure product team directly, as this may change.

## Can students or free accounts access Foundry models?

📹 [11:28](https://youtube.com/watch?v=c4_sjAwFNAY&t=688)

Creating a Foundry resource with a student or free Azure plan is generally restricted, and access to GenAI features is very limited (e.g., 1 million tokens/month on the free tier). 

**Workaround: GitHub Marketplace Models** — these are essentially Foundry-equivalent models available for free with rate limits. They're used for live streams and workshops specifically because of their free access. Limitations:

- May not include the newest models right away
- Cannot access Foundry-specific features like agents

Links shared:

- [GitHub Marketplace Models](https://github.com/marketplace?type=models)

## What is WebMCP and how does it work?

📹 [12:39](https://youtube.com/watch?v=c4_sjAwFNAY&t=759)

WebMCP (Web Machine Context Protocol) is an early-preview standard **co-authored by Google and Microsoft** that allows websites to expose themselves as MCP servers so AI agents can interact with them through defined JavaScript tools — rather than fragile browser automation (Playwright/Selenium).

How it works:

- Websites implement specific JavaScript functions as "tools" that agents can call
- These tools represent common actions agents might want to perform (e.g., "list notifications")
- Agents get a structured, deliberate API instead of trying to scrape or click through a page

Key points from the discussion:

- Websites that implement WebMCP would also need to adjust their bot detection/rate limiting to allow legitimate agent usage
- It requires deliberate adoption from each website — it's not automatic
- Compared to [NLWeb](https://github.com/nlweb-ai/NLWeb) (a prior Microsoft initiative for making sites searchable by AI), WebMCP benefits from the now-standardized MCP protocol
- **Edge doesn't support WebMCP yet**, even though Microsoft co-authored it

Links shared:

- [WebMCP early preview blog post](https://developer.chrome.com/blog/webmcp-epp)
- [WebMCP GitHub repo](https://github.com/webmachinelearning/webmcp)
- [NLWeb GitHub repo](https://github.com/nlweb-ai/NLWeb)

## What are good use cases for Microsoft Agent Framework?

📹 [20:47](https://youtube.com/watch?v=c4_sjAwFNAY&t=1247)

A great use case for an agent is anything where a tool loop helps achieve a goal that requires non-trivial exploration. Top current recommendations:

1. **Agentic coding** — already replacing most coding tasks; excellent reliability
2. **Research and triage** — give an agent access to documentation, issues, support tickets, etc. and have it research a bug report or customer issue. This is great because:
   - Output is a summary with citations, so a human can verify
   - You inherently have a human in the loop
3. **Personal planning** — weekend planners, event lookups, etc. — low risk, good for hobbyist agents

For agents that take actions (posting to social media, emailing, etc.) you need much higher confidence or an explicit human-in-the-loop approval step.

The upcoming **Python + Agents series** (starting next week) will cover many agent patterns with 60+ example agents across different use cases.

Links shared:

- [Python + Agents series](https://aka.ms/PythonAgents/series)

## What are GitHub Agentic Workflows?

📹 [26:53](https://youtube.com/watch?v=c4_sjAwFNAY&t=1613)

GitHub Agentic Workflows (GH AW) is a preview feature that lets you define repository automation tasks using a **markdown file with front matter** instead of writing full GitHub Actions YAML. You install the CLI extension with:

```
gh extension install github/gh-aw
```

How it works:

- Write a `.md` file with front matter specifying: schedule, permissions, allowed outputs, and allowed MCP tools (e.g., GitHub MCP server)
- Run `ghaw compile` to generate a full GitHub Actions workflow — treat the generated file as a lock file and don't edit it directly
- The programmatic guard rails (permissions, allowed outputs) live in the front matter; the natural language description drives what the agent actually does

Design guidance from the GH AW docs:

- **Start with low-risk outputs** like comments, drafts, and reports — not pull requests
- **Never auto-merge PRs** — always require human review
- Avoid using it as a full replacement for all workflows

Links shared:

- [GitHub Agentic Workflows blog post](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/)

## How are agent skills different from system prompts? What should go in AGENTS.md?

📹 [31:15](https://youtube.com/watch?v=c4_sjAwFNAY&t=1875)

**AGENTS.md** is a repository-level context file that coding agents (like Copilot or Claude) read to better understand your repo. It should contain only the information your agent needs to do its job better — not an info dump. A recent research paper found that LLM-generated AGENTS.md files tend to be too long, causing agents to over-explore and fail to reach goals.

Best practice: add something to AGENTS.md, try a task, see if it helps — be empirical about what goes in.

**Skills** are modular, lazy-loaded instructions:

- Stored in `.github/skills/` or `agent.skills/` — the latter is the emerging standard
- Each skill folder has a `skill.md` and optional associated Python files
- **Only the front matter (name + description) is sent to the LLM on every request**
- The full skill content is only loaded when the agent decides to invoke that skill
- This means you can have detailed instructions and associated assets without bloating the context window every time

**Comparison to system prompts:**

| | System Prompt | Skills |
|---|---|---|
| Always in context | ✅ Full content | ✅ Front matter only |
| On-demand detail | ❌ | ✅ Full content on invocation |
| Reusable across prompts | ❌ | ✅ |
| Best for | Always-needed instructions | Optional, reusable capabilities |

When to use each:

- If you'll use it in exactly one prompt — just inline it
- If you'll use it across multiple prompts/tasks — make it a skill
- Use **prompt files** (`.prompt.md`) to enforce a specific model for a task (e.g., GPT 5.2 was found to be better for Spanish translations)

Links shared:

- [microsoft/skills — Skills for Microsoft technologies](https://github.com/microsoft/skills)
- [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/abs/2602.11988)
- [SkillsBench: Benchmarking how well agent skills work across diverse tasks](https://arxiv.org/pdf/2602.12670)

## When should you build a custom agent vs. use lighter weight tools?

📹 [39:53](https://youtube.com/watch?v=c4_sjAwFNAY&t=2393)

With so many options — prompts, skills, GitHub Agentic Workflows, Copilot SDK, Microsoft Agent Framework — the recommendation is to **start with the lightest weight thing that works**:

1. **Prompt** — simplest, works for one-off tasks
2. **Skill** — reusable capability across prompts
3. **GitHub Agentic Workflow** — scheduled or event-driven repo automation
4. **Copilot SDK** — general agent harness, can do much of what Agent Framework does for agent tasks (but less ideal for workflows)
5. **Agent Framework** — full-featured agents and workflows for production deployment

The deciding factor: only reach for more complexity when you hit the limitations of the simpler approach. The maintenance cost of a full agent script is high — avoid it unless you need it.

## Are Foundry Hosted Agents running on Microsoft-managed infrastructure expected?

📹 [44:47](https://youtube.com/watch?v=c4_sjAwFNAY&t=2687)

A community member noted that Foundry Hosted Agents appear to run on Microsoft-managed infra rather than directly within their subscription's resource group. This came as a surprise.

The discussion didn't reach a definitive answer — it's possible the hosted agent runtime isn't co-located with the user's resource group even when deployed to a specific region. Pamela asked the product team for clarification during the session.

**Suggested next steps:** Check the [hosted agents documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/hosted-agents?view=foundry) and follow up in the Microsoft Foundry Discord.

Links shared:

- [Hosted agents in Foundry Agent Service (preview) docs](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/hosted-agents?view=foundry)

## Is anyone actually solving reranking for mixed-media RAG?

📹 [46:25](https://youtube.com/watch?v=c4_sjAwFNAY&t=2785)

Current state of mixed-media reranking (text + images in a single index):

- **Text-only rerankers** (like Cohere Rerank or AI Search's built-in reranker) only operate on text
- The recommended workaround: **add media descriptions to your ingestion pipeline** — generate text captions/descriptions for images so text-based rerankers can score them

Example from the azure-search-openai-demo repo: for every figure, an LLM-generated description is added to the text chunk, enabling reranking to work on that description.

**Cohere Rerank 4.0** is multilingual, but does not appear to be multimodal. There is no known dedicated multimodal reranker at this time. The HNSW graph filtering issue affects all document types equally, so the current pragmatic options are:

1. **Add media descriptions** and use a text reranker on those descriptions
2. **Multimodal LLM as reranker** — experimental but possible
3. **Split into separate sources** — keep text and image indexes separate and merge results

Pamela planned to ask the AI Search team for their current thinking on this.

Links shared:

- [azure-search-openai-demo multimodal release](https://github.com/Azure-Samples/azure-search-openai-demo/releases/tag/2025-11-12)

## How do you get an agent built with Agent Framework to use online evals in Azure Foundry?

📹 [49:38](https://youtube.com/watch?v=c4_sjAwFNAY&t=2978)

**Online evaluations** continuously run LLM-based evaluators on every agent request in production — checking for groundedness, completeness, etc. — without needing a pre-built test dataset.

For agents built with Microsoft Agent Framework (rather than the hosted Foundry Agent Service), it was unclear during the session whether online evals are directly available — but **Anthony Shaw confirmed after the stream that it should work**. Reach out to him on [LinkedIn](https://www.linkedin.com/in/anthonypshaw/) if you have questions.

**Where to look:**

- [Agent Framework observability docs](https://learn.microsoft.com/en-us/agent-framework/agents/observability?pivots=programming-language-python)
- [Azure AI Evaluation SDK samples for agent evaluators](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/evaluation/azure-ai-evaluation/samples/agent_evaluators/intent_resolution.ipynb)
- The upcoming **Model Mondays** event covers Foundry Agents hands-on

Links shared:

- [Model Mondays - Hands on with Claude + Microsoft Foundry Agent](https://developer.microsoft.com/en-us/reactor/events/26811/)
- [Agent Framework agent evaluation example](https://github.com/Azure-Samples/python-agentframework-demos/blob/main/examples/agent_evaluation.py)

## Announcements

📹 [0:00](https://youtube.com/watch?v=c4_sjAwFNAY&t=0)

**Product updates:**

- **Claude Sonnet 4.6** is now available in Azure Foundry models, and is rolling out to GitHub Copilot today
- **GitHub Agentic Workflows** (preview) — define repo automations in markdown, compiled into GitHub Actions
- **microsoft/skills** — a new repo of ready-made skills for Microsoft technologies (AZD deployment, GitHub issue creator, Copilot SDK, MCP builder, skill creator/evaluator, and more)

**Research papers discussed:**

- ["SkillsBench: Benchmarking how well agent skills work across diverse tasks"](https://arxiv.org/pdf/2602.12670)
- ["Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"](https://arxiv.org/abs/2602.11988) — Key finding: LLM-generated AGENTS.md files tend to be too long and hurt agent performance

**Upcoming events:**

- [Python + Agents series](https://aka.ms/PythonAgents/series) — starts next week (Tue/Wed/Thu at 11:30 AM for the first two weeks)
- [Microsoft AI Tour](https://aitour.microsoft.com/)
- [Py AI in San Francisco](https://pyai.events/) — March 10th (with Guido van Rossum and others)
- [MCP Dev Summit North America](https://events.linuxfoundation.org/mcp-dev-summit-north-america/) — April, New York City
- [PyCon US 2026](https://us.pycon.org/2026/) — May, Long Beach (MCP tutorial accepted: building your first Python MCP server with FastMCP + Keycloak)
- MVP Summit — March ~25th, Redmond (MCP workshops at the ACD booth)
