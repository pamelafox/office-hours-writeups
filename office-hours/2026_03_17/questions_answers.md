# March 17, 2026 Office Hours Q&A

## Announcement: Foundry Agent Service goes GA

📹 [0:26](https://youtube.com/watch?v=8y00vfyIlrA&t=26)

The Foundry Agent Service is now generally available. The GA release includes compatibility with many models, private networking, connection to tools and MCP servers, MCP authentication, and evaluations using the OpenAI SDK combined with the Azure AI Project SDK. Features still in preview include Voice Live (real-time text-to-speech), continuous evaluations, and hosted agents.

If you've been using Foundry Agents, this is good news for stability. If you've been waiting for GA before adopting them, now is the time. All the examples in the blog post are in Python, though other languages are supported.

## Announcement: What's new with GitHub Copilot

📹 [2:56](https://youtube.com/watch?v=8y00vfyIlrA&t=176)

Several GitHub Copilot updates in the last few weeks:

**GPT-5.4-mini in VS Code**: Now rolling out with a 0.33x multiplier, making it very cheap. Good for searching and light refactoring tasks, though not necessarily for heavy coding.

**Copilot CLI is GA** (since February 25th): Useful for quick terminal tasks — Pamela used it to stitch images together as a Photoshop alternative. It can also connect to MCP servers, e.g., a Foundry IQ knowledge base backed by Azure AI Search.

**Copilot Metrics is GA**: Provides usage metrics, especially useful for enterprises wanting to track how employees are using GitHub Copilot.

**Copilot Coding Agent can skip approvals**: Previously, the coding agent's PRs required manual CI approval each time, making it impractical. Now there's a repository setting under Settings > Code and Automation > Copilot > Coding Agent where you can disable the "require approval" setting. This makes the coding agent much more practical for automated workflows.

Pamela demonstrated setting this up live and assigning [an issue to Copilot](https://github.com/Azure-Samples/azure-search-openai-demo/issues/3005), which immediately creates a draft PR and starts working. She also has a [repo maintainer agent](https://github.com/pamelafox/github-repo-maintainer-agent) that auto-assigns issues to Copilot across hundreds of repos, which she had stopped using due to the CI approval friction, but can now resume using.

Links shared:

* [Configuring Copilot Coding Agent settings](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/configuring-agent-settings)
* [Skip approval announcement](https://github.blog/changelog/2026-03-13-optionally-skip-approval-for-copilot-coding-agent-actions-workflows/)
* [GitHub Repo Maintainer Agent](https://github.com/pamelafox/github-repo-maintainer-agent)
* [azure-search-openai-demo issue #3005](https://github.com/Azure-Samples/azure-search-openai-demo/issues/3005)

## Does OpenAI/Azure OpenAI see your data?

📹 [10:01](https://youtube.com/watch?v=8y00vfyIlrA&t=601)

When using Azure OpenAI, the [data privacy policy](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy?tabs=azure-portal) states that your prompts, completions, embeddings, and training data are not available to other customers, not available to OpenAI, and are not used to train models. This is different from GitHub Copilot's code training (public repos on GitHub may be used for training).

## Can you talk about Claude and Claude Code?

📹 [10:57](https://youtube.com/watch?v=8y00vfyIlrA&t=657)

Pamela's default model for coding is Claude Opus 4.6 (with a 3x multiplier) via GitHub Copilot. She doesn't pay separately for ChatGPT, Claude, or Copilot — Microsoft pays for her Copilot.

She briefly explored Claude Code (which requires a paid Claude subscription) but doesn't use it since GitHub Copilot covers her needs. She also uses a [Responses API chat wrapper](https://mattgotteiner.github.io/responses-chat/) deployed with a GPT model, which gives access to web search and code interpreter — two very compelling built-in tools.

## How do web search and code interpreter work with the Responses API?

📹 [16:08](https://youtube.com/watch?v=8y00vfyIlrA&t=968)

**Web Search**: Uses Bing under the hood (same as Bing grounding). The responses API can send multiple queries, and you get back citations/URLs and the final answer — but not the full web page snippets, due to Bing licensing. This differs from services like Tavily or Perplexity where you may get the actual snippets. It works on both Azure OpenAI and OpenAI (with different configuration). Web search also supports domain filtering.

**Code Interpreter**: Runs code in a sandboxed environment. It can generate charts (via matplotlib), work with files, upload/download files, and handle calculations. 

### What does Bing web search cost?

📹 [21:03](https://youtube.com/watch?v=8y00vfyIlrA&t=1263)

$14 per 1,000 transactions. For comparison, Tavily is roughly half the price, Exa is about $7 per query at higher tiers, and Google is about $5 per 1,000 queries (roughly a third of Bing's price). Microsoft won't always be the cheapest option due to enterprise controls, but it's not an order of magnitude more expensive — roughly 2x compared to alternatives.

Links shared:

* [Tavily pricing](https://www.tavily.com/pricing)
* [Exa pricing](https://exa.ai/pricing)
* [Google Custom Search pricing](https://developers.google.com/custom-search/v1/overview#pricing)

### Are the API keys safe in a front-end-only app?

📹 [30:14](https://youtube.com/watch?v=8y00vfyIlrA&t=1814)

This question pertains to the [Responses API chat wrapper](https://mattgotteiner.github.io/responses-chat/), which is a front-end-only JavaScript app that interacts directly with the Azure OpenAI Responses API. The API keys are stored in localStorage and sent as bearer tokens over HTTPS.

The keys are stored in localStorage (currently unencrypted) and sent as bearer tokens over HTTPS. While HTTPS is secure in transit, the remaining concerns are: keys are visible in browser DevTools, the keys could leak through logs/error reporting/screen sharing, and they're long-lived (unlike short-lived tokens). It would be better to use Entra authentication with short-lived tokens rather than API keys. The app could also encrypt keys in localStorage.

## How important is system design for multi-agent systems?

📹 [33:34](https://youtube.com/watch?v=8y00vfyIlrA&t=2014)

System design matters because there are many ways to coordinate agents — supervisor/sub-agent (agent as tools), handoff orchestration, conditional routing, etc. Key considerations include:

- **Context management**: Who's in charge? How much context does each agent get? Are you controlling context window limits?
- **Control flow**: Which agent decides what happens next? Is the control predictable or chaotic?

The recommendation is to build your system first, then evaluate it to identify actual issues (too much context? control flow problems?) rather than prematurely choosing an architecture. Reference the [agents series slides](https://aka.ms/pythonagents/resources) for different orchestration patterns.

## What is your opinion about RL (reinforcement learning) on the agent layer?

📹 [36:39](https://youtube.com/watch?v=8y00vfyIlrA&t=2199)

Reinforcement learning has been one of the most effective techniques in generative AI — it's responsible for improvements in tool calling, structured outputs, safety, and reduced hallucinations. As Andrej Karpathy noted, RL has many issues but is surprisingly effective.

The specific paper discussed proposes collapsing the boundary between deployment and training, where every interaction becomes both useful work and a potential training example ("online RL"). This involves asynchronous background training — logging interactions, using LLM-as-judge for reward signals, and periodically serving updated checkpoints. It's more expensive due to fine-tuning costs, but could be valuable for very domain-specific use cases.

Generally, approaches requiring fine-tuning see less adoption. But if base LLM performance isn't sufficient for your use case and fine-tuning becomes easy/affordable enough, it could be worthwhile.

## What's your opinion on SaaS providers offering agents instead of direct data access?

📹 [43:32](https://youtube.com/watch?v=8y00vfyIlrA&t=2612)

More SaaS providers are wrapping their data in agents rather than exposing direct API/MCP access. As a developer, this is frustrating because:

- You lose access to raw data — you only get an LLM-generated answer
- You don't control the system prompt the agent uses
- There's added lossiness and hallucination risk from the extra LLM layer
- It's less flexible than direct tool/API access

A concrete example is the Work IQ MCP server in VS Code — it's an MCP server wrapping an agent, which means you don't get direct Graph API access. It works well for straightforward queries (like calendar events) but struggles with fuzzier tasks (like searching chats) where hallucination from the internal LLM is more likely.

The ideal approach: companies should offer direct tools/APIs alongside their agents, so developers have the flexibility to choose.

## What are your go-to resources for system design interviews?

📹 [47:02](https://youtube.com/watch?v=8y00vfyIlrA&t=2822)

Pamela's primary related experience is interviewing candidates for full-stack web developer roles (front end, backend, cron jobs, messaging systems). Key areas to be familiar with for system design: messaging systems, cron jobs, queuing, deferred tasks, and handling variable production load.

## Can auto-research be used to improve MCP servers or agents?

📹 [49:57](https://youtube.com/watch?v=8y00vfyIlrA&t=2997)

Referencing [Andrej Karpathy's auto-research](https://github.com/karpathy/nano-gpt) approach (where agents iteratively improve parameters), this concept can be applied to MCP servers. The key requirement is having a validation/evaluation loop.

Pamela demonstrated MCP server evaluation in her [PyAI talk](https://blog.pamelafox.org/2026/03/do-stricter-mcp-tool-schemas-increase.html) — she set up an MCP server with different tool schemas, pointed agents at it, defined expected outputs for test prompts, and ran evaluations to see which schema produced the best results. For Pamela's experiment, she came up with the different tool schemas herself. In theory, an LLM could iterate on tool names, descriptions, parameters, and return values to optimize eval scores.

Related tools mentioned:

* **[Lightning](https://github.com/microsoft/agent-framework/tree/main/python/packages/lab/lightning)**: An optimization framework in agent framework — "optimize any agent with any framework"
* **[Waza](https://github.com/microsoft/waza)** (by Shane Boyer): A CLI for evaluating GitHub Copilot skills
* **[Sensei](https://github.com/spboyer/sensei)** (by Shane Boyer): A skill for iteratively improving SKILL.md frontmatter compliance

Links shared:

* [Do stricter MCP tool schemas increase agent reliability? (blog post)](https://blog.pamelafox.org/2026/03/do-stricter-mcp-tool-schemas-increase.html)

## Upcoming events (Online and in-person)

📹 [55:46](https://youtube.com/watch?v=8y00vfyIlrA&t=3346)

* [Foundry IQ Series (Online)](https://aka.ms/iq-series) — first one is March 18th
* [Microsoft AI Tour (Global)](https://aitour.microsoft.com/flow/microsoft/aitour/landing/page/home)
* [MVP Summit (Redmond, WA)](https://summit.microsoft.com/) — Pamela will be there next week but plans to still hold office hours from the Microsoft Redmond office
* [MCP Summit (NYC)](https://events.linuxfoundation.org/mcp-dev-summit-north-america/program/cfp/)
* [Azure Cosmos DB Conf (Online)](https://developer.azurecosmosdb.com/conf/)
* [PyCon 2026 (LA, CA)](https://us.pycon.org/2026/)
* [Posette (Online)](https://posetteconf.com/2026/)
