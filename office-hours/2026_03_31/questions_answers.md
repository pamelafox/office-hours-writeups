# March 31, 2026 Office Hours Q&A

## What is the GA version of agent framework? Can we install it now?

📹 [2:55](https://youtube.com/watch?v=02InkgJM8Do&t=175)

At Microsoft, "GA" (Generally Available) means a product is stable enough for production use — similar to what used to be called "beta" vs. "release." Some companies only adopt GA products. Agent framework is currently in public preview — you can definitely install and use it. There are many samples and an entire series built on it. However, the interface has been changing as the team incorporates feedback.

The framework has been progressing through release candidates (RC1 through RC6), with RC6 expected to be the last before the official 1.0.0 GA release. Once that ships, it won't be marked as a pre-release anymore.

Links shared:

* [agent-framework on PyPI](https://pypi.org/project/agent-framework/#description)

## What are some good local models for agents?

📹 [5:08](https://youtube.com/watch?v=02InkgJM8Do&t=308)

Pamela shared her experience trying to find good local models for agents on her Mac M1 with 16 GB RAM. Using [CanIRun.ai](https://www.canirun.ai/) to check hardware compatibility, her options were limited to Phi 3.18B and Qwen 3.5:9B.

She used Qwen 3.5:9B extensively and found it technically works for agents but with significant quality issues: it would sometimes output Chinese (likely due to training data), and would forget the original user question after making tool calls. The 27B version is reportedly much better but requires more memory.

She also shared a [SQL benchmark for LLMs](https://sql-benchmark.nicklothian.com/?utm_source=breadbox) that compares both frontier and local models on text-to-SQL tasks.

Links shared:

* [CanIRun.ai](https://www.canirun.ai/)
* [LLM SQL Benchmark](https://sql-benchmark.nicklothian.com/?utm_source=breadbox)

## What is GEPA's "Optimize Anything"?

📹 [7:30](https://youtube.com/watch?v=02InkgJM8Do&t=450)

Pamela attended a meetup where she met the creator of "Optimize Anything," which uses GEPA — a prompt optimizer based on genetic algorithms. Instead of trying every possible prompt variation, it intelligently decides what to try next, giving you efficient prompt optimization.

It's not just for prompts — people use it for structured outputs, and GEPA can even optimize skills (non-LLM tasks). Developers are reporting really good results from using GEPA to improve their LLM workflows.

Links shared:

* [GEPA: optimize_anything blog post](https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything)

## Has anyone at Microsoft tested TurboQuant for local models?

📹 [8:34](https://youtube.com/watch?v=02InkgJM8Do&t=514)

Pamela hadn't heard of TurboQuant before — it's a KV cache compression technique from Google published just 11 hours before the office hours. She said she'd ask colleagues about it. The discussion continued later in the session, with community members sharing that TurboQuant provides ~6x KV cache memory reduction and up to 8x faster attention computation on H100, with minimal accuracy loss at 3-4 bits.

The practical impact is primarily on inference serving rather than application development. It could potentially help when deploying models on serverless GPUs (like Azure Container Apps with serverless GPU using vLLM). Someone already created a [vLLM plugin for TurboQuant](https://github.com/Alberto-Codes/turboquant-vllm/tree/main).

Links shared:

* [TurboQuant blog post (Google Research)](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)
* [TurboQuant vLLM plugin](https://github.com/Alberto-Codes/turboquant-vllm/tree/main)

## Have you used the Work IQ MCP server?

📹 [11:39](https://youtube.com/watch?v=02InkgJM8Do&t=699)

Yes — Pamela has it configured in her Copilot CLI. She demonstrated it by asking "Do I have any meetings today?" and showed it querying Work IQ to check her calendar. Work IQ is a standard input/output MCP server (not HTTP), and you configure it in your `.copilot/mcp-config.json`.

Work IQ provides read-only access — it can read calendar events, search through Teams chats, and search SharePoint. It's similar to using Copilot in Teams but convenient because you can use it from any MCP client. You need to authenticate during setup, and then it works from there.

## Does Microsoft have anything to check agent skills for security and effectiveness?

📹 [16:48](https://youtube.com/watch?v=02InkgJM8Do&t=1008)

For **effectiveness**, Pamela recommended two tools from her colleague Shane:

- **[Sensei](https://github.com/spboyer/sensei)** — iteratively improves skills and recently added GEPA support. It checks for basic compliance issues, tests whether skills trigger correctly, and helps with skill collision (when multiple skills overlap). This is used for the [Azure Skills](https://github.com/microsoft/azure-skills) bundle.

- **[Waza](https://github.com/microsoft/waza)** — a CLI/framework for creating, testing, measuring, and improving skills. It generates new skills with evaluation scripts built in, checks for front matter adherence and token budget compliance. Good for building evaluation habits from the start.

For **security**, there's nothing specific she's aware of yet. She emphasized that security for agents should be enforced at the environment level — lock down what commands an agent can run and what credentials it can access, rather than relying on prompt instructions. Running skills in isolated Docker containers is safer than running directly on a machine with production credentials.

Links shared:

* [Sensei](https://github.com/spboyer/sensei)
* [Waza](https://github.com/microsoft/waza)
* [Azure Skills](https://github.com/microsoft/azure-skills)

## Have you seen the "Mirage" problem with multimodal LLMs?

📹 [23:22](https://youtube.com/watch?v=02InkgJM8Do&t=1402)

Pamela shared a paper called "MIRAGE: The Illusion of Visual Understanding" which found that multimodal LLMs sometimes hallucinate image understanding — they respond as if they've analyzed an image even when no image was provided. For example, when asked to identify tissue in a histology slide with no image attached, the LLM would confidently describe "cardiac muscle tissue."

The researchers also found that some benchmark successes weren't actually due to image understanding. They cleaned benchmarks by removing compromised questions and re-evaluated vision-language models, finding performance dropped across the board.

Relatedly, Pamela discussed Azure AI Vision (Florence model) being deprecated, with image analysis service retiring in 2028. Microsoft is moving away from dedicated vision models toward generic multimodal LLMs and embedding models like Cohere Embed.

For multimodal RAG, Pamela noted a quirk: when providing both an image and its text description to an LLM, the model strongly prefers referencing the text description over actually looking at the image. You may need to explicitly prompt it to examine the image itself.

Links shared:

* [MIRAGE paper](https://arxiv.org/abs/2603.21687)
* [Azure AI Vision migration options](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/migration-options)

## Why are people saying MCP is dead? Is it because of skills?

📹 [29:33](https://youtube.com/watch?v=02InkgJM8Do&t=1773)

Pamela referred back to the previous week's extensive discussion and reiterated: MCP is not dead (though there's a tongue-in-cheek funeral for it on April 1st in NYC). Skills are useful for coding agents, but MCP is particularly valuable when authentication is involved, when you're in deployed environments across organizations, and for features like elicitations and destructive tool decorators.

The MCP protocol has a working group exploring how to make skills a first-class concept discoverable from MCP servers, alongside tools, resources, and prompts. All major agent frameworks now support both skills and MCP.

Links shared:

* [MCP experimental ext-skills repo](https://github.com/modelcontextprotocol/experimental-ext-skills)

## What are some recommended talks from the Py AI conference?

📹 [33:00](https://youtube.com/watch?v=02InkgJM8Do&t=1980)

The talks from the Py AI conference are being uploaded to YouTube. Pamela highlighted several:

- **Till from Mother Duck** — built an MCP server for Mother Duck, showed its evolution, and is part of the MCP skills working group
- **Jeremiah (FastMCP maintainer)** — gave a talk on FastMCP
- **Hamel Husain** — "Revenge of the Data Scientist," about evaluation (also available as a blog post)
- **Open Source in the Age of AI panel** — quite interesting

Links shared:

* [Pydantic YouTube channel (Py AI talks)](https://www.youtube.com/@Pydantic)
* [Hamel's "Revenge of the Data Scientist" blog post](https://hamel.dev/blog/posts/revenge/)

## Ollama now powered by MLX on Apple Silicon?

📹 [36:44](https://youtube.com/watch?v=02InkgJM8Do&t=2204)

Ollama announced preview support for MLX on Apple Silicon, promising faster local model inference on Macs. However, the current requirement is a Mac with 32+ GB of unified memory, which means it doesn't help Pamela (16 GB M1). If you have a newer Mac with sufficient memory and GPU neural accelerators (especially M5), it's worth trying.

Links shared:

* [Ollama MLX on Apple Silicon blog post](https://ollama.com/blog/mlx)

## When can we see agent framework durable agents in an Azure Functions series?

📹 [40:04](https://youtube.com/watch?v=02InkgJM8Do&t=2404)

Pamela hasn't had a chance to play with durable execution yet. The durable task extension for Microsoft Agent Framework provides serverless hosting, session management, deterministic multi-agent orchestrations with automatic checkpointing, and human-in-the-loop support.

She noted it's not yet compatible with Foundry hosted agents — you'd deploy on Azure Functions to get durability. She offered to invite Nick (from the durable team) to a future office hours to demo it.

Links shared:

* [Bulletproof agents with durable task extension blog post](https://techcommunity.microsoft.com/blog/appsonazureblog/bulletproof-agents-with-the-durable-task-extension-for-microsoft-agent-framework/4467122)

## Is private networking supported for Foundry hosted agents?

📹 [43:18](https://youtube.com/watch?v=02InkgJM8Do&t=2598)

Currently, you cannot create hosted agents within network-isolated Foundry projects. Pamela said she'd check with colleagues and hoped this limitation would be addressed soon, given how important private networking is for Microsoft's enterprise customers.

Links shared:

* [Foundry hosted agents documentation](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents)
* [Foundry virtual networks configuration](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/virtual-networks)

## Any tips to maximize GitHub Copilot Auto output quality with the Codex model?

📹 [48:16](https://youtube.com/watch?v=02InkgJM8Do&t=2896)

Pamela doesn't use Auto mode herself (she uses Opus). She recommended reaching out to Burke Holland and Pierce Boggan on Twitter/X — they're VS Code advocates who are more familiar with Auto mode.

**Update posted after office hours:** Pierce (from the VS Code team) responded: "It should do better in Insiders, where our task detection model is now at 100% as of today. Based on those results, we'll roll to stable. Today, Auto is based purely off available capacity and uptime, so the model mix can be quite static in how it's applied."

Links shared:

* [Burke Holland on X](https://x.com/burkeholland)
* [Pierce Boggan on X](https://x.com/pierceboggan)

## How to start learning AI? What about the "AI Engineering" book?

📹 [49:49](https://youtube.com/watch?v=02InkgJM8Do&t=2989)

Pamela recommended starting with the Python AI series before reading Chip Huyen's "AI Engineering" book. She shared her blog post on how she learns about generative AI, which covers the AI Engineering book, AI news sources, hands-on practice, and Microsoft's video series.

Links shared:

* [How I learn about generative AI (blog post)](https://blog.pamelafox.org/2025/08/how-i-learn-about-generative-ai.html)

## Announcements

📹 [0:39](https://youtube.com/watch?v=02InkgJM8Do&t=39)

**Agent Framework RC6 released:** Release candidate 6 for the Python agent-framework is out and expected to be the last RC before GA 1.0.0.

**GitHub Copilot privacy policy change:** GitHub updated its privacy statement so that Copilot Free, Pro, and Pro Plus users' interaction data (inputs, outputs, code snippets) will be used to train and improve AI models unless users opt out. Enterprise and organization users with private repos are not affected by this change.

Links shared:

* [GitHub privacy statement update](https://github.blog/changelog/2026-03-25-updates-to-our-privacy-statement-and-terms-of-service-how-we-use-your-data/)
* [FAQ on Copilot data use](https://github.com/orgs/community/discussions/188488)

**Host Your Agents on Foundry series:** A new three-part live stream series starting end of April covering hosting agent framework, LangChain/LangGraph on Foundry, and quality/safety evaluations. Includes office hours after each session.

Links shared:

* [Host your agents on Foundry series](https://aka.ms/AgentsOnFoundry/series)

**Upcoming events:**

* [Microsoft AI Tour (Global)](https://aitour.microsoft.com/flow/microsoft/aitour/landing/page/home)
* [MCP Summit (NYC)](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)
* [Azure Cosmos DB Conf (Online)](https://developer.azurecosmosdb.com/conf/)
* [PyCon 2026 (LA, CA)](https://us.pycon.org/2026/)
* [Posette (Online)](https://posetteconf.com/2026/)
* [Code with Claude (SF, NY, Tokyo)](https://claude.com/blog/code-with-claude-san-francisco-london-tokyo)
* [Build 2026 (SF)](https://build.microsoft.com/)
