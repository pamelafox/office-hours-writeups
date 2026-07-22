# July 21, 2026 Office Hours Q&A

## Discussion: Generating synthetic evaluation data

📹 [3:35](https://youtube.com/watch?v=bsYGU6iWE4c&t=215)

Pamela has been testing Foundry's preview synthetic-data tooling for evaluation datasets in the Azure Search OpenAI demo. Single-hop questions are relatively straightforward and the SDK produces fairly natural examples. Multi-hop ground truth is harder: useful questions should require evidence from multiple documents, not merely combine two unrelated questions. The broader modernization plan for the [RAG solution](https://github.com/Azure-Samples/azure-search-openai-demo/) also includes evaluation and retrieval updates, with a move to Agent Framework planned.

### How do you prevent a system from learning the pattern used to generate synthetic evaluation data?

📹 [7:31](https://youtube.com/watch?v=bsYGU6iWE4c&t=451)

In an evaluation-only pipeline, no learning happens. One system uses an LLM and an Azure AI Search index to generate synthetic questions and ground-truth answers. The evaluation then sends each question to the application and compares its response with that ground truth. Neither the data generator nor the application can update its weights, system prompt, or other configuration from the result.

The risk appears when evaluation is used for optimization. A system such as [Foundry Agent Optimizer](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-optimizer-overview) can iteratively change an agent's system prompt, tool descriptions, and skills, evaluate each configuration, and choose the best performer. Optimizing repeatedly against the same synthetic questions can overfit the agent to that dataset while making it worse on unfamiliar production requests.

Use the same safeguards as a conventional machine learning workflow:

- Split the data into optimization and held-out validation sets. For example, optimize on 50% and use the other 50% to check whether the improvement generalizes.
- Keep adding real production questions to the evaluation set so it reflects what users actually ask rather than only the synthetic-data distribution.
- Make synthetic questions resemble realistic user prompts. Multi-hop questions are especially difficult because simply joining two unrelated trivia questions does not produce a natural query. Comparative questions that genuinely require information from multiple documents are better tests.

Agent Optimizer requires the parts it can change to be externalized as artifacts. The system prompt can live in Markdown, tools and their descriptions can use JSON schema, and skills can use their standard file format. Tool descriptions are effectively small prompts attached to tools, so they can be optimized along with the main instructions.

[DSPy](https://dspy.ai/) is another optimization option. It is particularly useful for structured output, entity extraction, and classification. Foundry Agent Optimizer is a better match for a complete agent whose behavior depends on a combination of prompts, tools, and skills.

## How can I use an LLM more effectively to help me become a millionaire?

📹 [36:13](https://youtube.com/watch?v=bsYGU6iWE4c&t=2173)

An LLM will usually default to conservative, conventional financial guidance. If the goal is to explore a particular investor's more aggressive strategy, ground the model in that person's material rather than expecting a generic goal prompt to supply the strategy. A focused knowledge base built from their articles or videos can make the source and assumptions explicit.

There is an important difference between getting advice and generating income. An agent cannot act on a financial account unless it has access to that account, and granting that access demands a very high level of trust. A safer workflow is to export the relevant data, ask the model to analyze it, and make any decisions and transactions yourself.

Pamela used that approach by exporting a CSV of bank transactions and sharing screenshots from investment accounts. The model helped categorize spending, explained cost basis, and suggested which shares might fit her stated cash needs and goals. The useful part was not a magic wealth goal; it was supplying concrete data, asking specific questions, and continuing to challenge explanations that were unclear.

For recurring monitoring, an MCP server or a browser automation with site-specific cookies could let an agent inspect an account and make periodic recommendations. Keep permissions narrowly scoped to the required site and task. Direct financial transactions carry much more risk than read-only analysis, so human review remains important.

The renamed [Gemini Notebook](https://notebooklm.google/) can support a research-oriented version of this workflow. During the session, it imported investment material and generated a mind map, flash cards, summaries, and follow-up answers. Those formats can help someone learn an unfamiliar domain, but the underlying sources and financial claims still need scrutiny.

## Announcement: New blog post on images and interactive apps from MCP servers

📹 [0:44](https://youtube.com/watch?v=bsYGU6iWE4c&t=44)

Pamela published [Beyond text: Returning images and interactive apps from MCP servers](https://techcommunity.microsoft.com/blog/AzureDevCommunityBlog/beyond-text-returning-images-and-interactive-apps-from-mcp-servers/4535865), a guide to MCP tools that return visual content and interactive interfaces instead of only plain text.

## Announcement: GitHub Copilot adds a model, metrics, and code review controls

📹 [16:33](https://youtube.com/watch?v=bsYGU6iWE4c&t=993)

[Gemini 3.6 Flash](https://github.blog/changelog/2026-07-21-gemini-3-6-flash-is-now-available-in-github-copilot) is available across GitHub Copilot surfaces as a medium-cost model. Repository-level Copilot usage metrics are generally available, and activity from the Copilot app is included in the metrics API.

[Copilot code review customization](https://github.blog/changelog/2026-07-17-copilot-code-review-customization-and-configurability-improvements) now includes head-branch custom instructions, YAML-based setup steps, firewall configuration, and runner controls. Custom setup steps are useful when review sessions repeatedly choose the wrong tools: the repository can define the environment the reviewer should use.

## Announcement: GitHub Copilot canvases provide interactive interfaces for agents

📹 [18:35](https://youtube.com/watch?v=bsYGU6iWE4c&t=1115)

A Copilot canvas is a JavaScript-powered interactive page that can be scoped to a session, repository, or global environment. Unlike a standalone web page, a canvas can access the agent and trigger anything that could otherwise be requested in chat.

The live demo turned a Markdown table of nanny-family candidates into a sortable and filterable interface. Another canvas provided controls for posting through a social-media MCP server; routing the action through the agent allowed it to diagnose and recover from API errors. Community examples, including a cross-repository Workhub dashboard, are available in [Awesome GitHub Copilot canvas extensions](https://awesome-copilot.github.com/extensions/).

Copilot automations complement canvases by running agent tasks on a schedule. Examples included checking new listings, collecting links from daily posts, and processing LinkedIn connection requests. They work like easier cron jobs, with an agent able to notice failures, adapt, and report next steps.

## Announcement: Foundry Toolbox connects hosted agents to Work IQ and other tools

📹 [31:25](https://youtube.com/watch?v=bsYGU6iWE4c&t=1885)

A Foundry hosted agent published to Teams used Work IQ through its A2A connection to search workplace content. Foundry Toolbox handles OAuth-backed connections and can combine web search, code interpreter, file search, remote MCP servers, OpenAPI tools, A2A services, and skills. The [Foundry Toolbox notebook](https://github.com/microsoft-foundry/forgebook/blob/main/notebooks/mastering-foundry-toolbox.ipynb) provides examples of the available integrations.

## Announcement: Gemma 4 visualization explores video token predictions

📹 [30:33](https://youtube.com/watch?v=bsYGU6iWE4c&t=1833)

A [Gemma 4 visualization](https://x.com/matthen2/status/2078818110597972114) sampled next-token predictions from raw video image patches to explore what a multimodal model might predict while watching video.

## Announcement: ChatGPT Work supports multi-step workflows

📹 [35:08](https://youtube.com/watch?v=bsYGU6iWE4c&t=2108)

[ChatGPT Work](https://openai.com/chatgpt-work/) targets multi-step workflows across connected apps and files.

## Announcement: NotebookLM is now Gemini Notebook

📹 [38:57](https://youtube.com/watch?v=bsYGU6iWE4c&t=2337)

NotebookLM has been renamed [Gemini Notebook](https://notebooklm.google/). The new name positions it as a more general-purpose product rather than a tool primarily for technical users.

During the live demo, Pamela used fast research to find and import an investor's material, then asked grounded questions such as which mutual funds that investor recommends. Gemini Notebook offered several ways to explore the sources, including an audio overview, slide deck, video overview, flash cards, and an interactive mind map. The mind map organized the investor's portfolio strategy and let Pamela open individual concepts for more detail, while the flash cards exposed terms that needed further study.

The demo showed how a notebook can turn a collection of videos and other sources into an explorable learning environment. Follow-up questions can relate unfamiliar ideas to concepts the learner already understands, but financial claims and generated summaries still need to be checked against the original sources.

## Announcement: Python + AI Office Hours news-generation skill is published

📹 [49:50](https://youtube.com/watch?v=bsYGU6iWE4c&t=2990)

The [Python + AI Office Hours news-generation skill](https://github.com/pamelafox/office-hours-writeups/blob/main/.agents/skills/python-ai-office-hours/SKILL.md) is also now published in the write-ups repository. It contains the workflow used to gather and generate the weekly news page and is updated as the desired output evolves.
