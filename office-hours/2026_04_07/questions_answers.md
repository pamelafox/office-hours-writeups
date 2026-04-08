# April 7, 2026 Office Hours Q&A

## How did you generate the news slides using Copilot CLI and MCP servers?

📹 [0:56](https://youtube.com/watch?v=3cgN7X0fIB0&t=56)

Pamela demonstrated generating the weekly office hours news slides using Copilot CLI with three MCP servers connected: GitHub (built-in), X/Twitter (XMCP, running locally), and Work IQ. She asked Copilot to search the past seven days of activity across all three, then had it generate a PowerPoint slide summarizing the news. She iterated on the slide formatting and plans to turn this workflow into a reusable skill.

She showed her MCP config with Work IQ and Twitter configured. Work IQ is a command-line tool you authenticate once, and the Twitter/X MCP server is a Python server running locally that requires a developer account (~$20/month for API access). The Copilot CLI calls MCP server tools on her behalf using authenticated sessions — Work IQ (CLI-based auth), GitHub (built into Copilot), and Twitter (via developer API credentials in a `.env` file). Most of Pamela's data happens to be public, but the authentication allows access to private data too.

Links shared:

* [X MCP Server (XMCP)](https://github.com/xdevplatform/xmcp)

## When working with a multi-tool calling workflow, is generating a skill to guide the agent the right design?

📹 [3:40](https://youtube.com/watch?v=3cgN7X0fIB0&t=220)

Yes — Pamela demonstrated this with her comedy roast skill, which coordinates Work IQ, GitHub, and Twitter MCP servers to gather a week's activity and generate a comedy roast. A formal skill is helpful when you need to guide an agent through a specific multi-tool workflow — it specifies how to get work activity, GitHub activity, and Twitter activity, then how to deliver the output.

The drawback is that skills can be too prescriptive — if you specify exactly which tools to use, the skill won't adapt when better tools become available. There's a balance between giving direction and allowing flexibility.

She also showed installing skills via `npx skills add`, an npm package that makes it easy to share and install agent skills across repos and agents. For example, the Cosmos DB team published skills you can install with `npx skills add` that will review and critique your data model.

Links shared:

* [Comedy Roast Skill](https://github.com/pamelafox/comedy-roast-skill)
* [Comedy Roast output (Gist)](https://gist.github.com/pamelafox/0eb05c3498df1d940214559277801819)
* [npx skills package](https://www.npmjs.com/package/skills)
* [Cosmos DB Agent Kit](https://github.com/AzureCosmosDB/cosmosdb-agent-kit)

### Do you put skills in a repo or globally?

📹 [11:14](https://youtube.com/watch?v=3cgN7X0fIB0&t=674)

It depends on the skill's scope. Pamela usually installs skills globally now because she wants the same skill across all repos. Very specific skills (like generating office hours slides for this particular repo) go inside the repo in `.agents/skills/`. More generic skills that are useful everywhere (like her PR comment review skill) should be installed globally and ideally shared as standalone repos so others can install them with `npx skills add`.

## What's new with Agent Framework 1.0.0?

📹 [17:24](https://youtube.com/watch?v=3cgN7X0fIB0&t=1044)

Agent Framework is now 1.0.0 and Generally Available (GA), meaning companies that only allow GA packages can now use it. All the demo repos from the livestream series have been updated to 1.0.0.

One notable change: the new default API is the Responses API instead of Chat Completions API. This is generally better (more features, built-in tools like code interpreter), but there is one open issue that affected a sample when using Azure OpenAI endpoints or Foundry Direct models. If you were previously using Chat Completions, you might see some differences — file an issue on the repo if you run into problems.

Links shared:

* [Agent Framework on PyPI](https://pypi.org/project/agent-framework/#history)
* [Agent Framework Demo Repos](https://github.com/Azure-Samples/python-agentframework-demos/)
* [Agent Framework 1.0.0 livestream + demos](https://aka.ms/pythonagents/rewatch)

## GitHub Copilot now works on Dependabot PRs

📹 [19:55](https://youtube.com/watch?v=3cgN7X0fIB0&t=1195)

Pamela showed a Dependabot PR where CI failed after a prettier update. She commented `@copilot` on the PR asking it to fix the CI failure, and Copilot took over the PR, made the fix, committed it, and CI passed. This is especially useful for Dependabot PRs where about half tend to fail and the fixes are usually straightforward.

## New in VS Code: Copilot Chat Customizations viewer

📹 [23:21](https://youtube.com/watch?v=3cgN7X0fIB0&t=1401)

In VS Code (at least Insiders), clicking the gear icon now shows everything customizing your Copilot experience: agents, skills, instructions, prompts, hooks, MCP servers, and plugins. There are many ways to extend the coding agent experience now. Over time some may consolidate — for example, prompts may be deprecated in favor of skills since they're very similar.

Links shared:

* [VS Code Chat Customizations video by James Montemagno](https://youtu.be/os2eqa69gko)
* [VS Code Learn YouTube playlist](https://www.youtube.com/playlist?list=PLj6YeMhvp2S4l1_iP4-pS6p7lgyqKo-Ix)

## New in FastMCP 3.0: OpenTelemetry support

📹 [24:44](https://youtube.com/watch?v=3cgN7X0fIB0&t=1484)

FastMCP now has built-in OpenTelemetry support. The Python MCP demos repo was updated to remove custom middleware and use the built-in OTel support instead. It's been tested working with Aspire, App Insights, and Logfire.

Links shared:

* [FastMCP OpenTelemetry docs](https://gofastmcp.com/servers/telemetry)
* [Python MCP Demos](https://github.com/Azure-Samples/python-mcp-demos)
* [Blog: Building MCP servers with Entra ID auth](https://blog.pamelafox.org/2026/04/building-mcp-servers-with-entra-id-and.html)

## Are open models now viable for agent workloads? What about Gemma 4?

📹 [28:26](https://youtube.com/watch?v=3cgN7X0fIB0&t=1706)

LangChain shared data showing that open models are crossing the threshold for agent-capable workloads (GLM-5 scored 64% vs. Opus's 68% on agentic evals).

For **small local models**, Pamela's team tested Gemma 4 (E2B, ~8B parameters) as a replacement for Qwen 3.5:9B, which had issues like outputting Chinese and forgetting the original question. Gemma 4 performed notably better, especially on tasks involving the Microsoft Learn MCP server which returns large amounts of context — a challenging scenario for small models.

There is currently an [open bug in Ollama](https://github.com/ollama/ollama/issues/15250) affecting Gemma 4 usage that the team is working on. Once fixed, they plan to adopt Gemma 4 E2B as the recommended local model for their open source repos.

For **production use** of small models, Pamela recommended DSPy for prompt optimization. At the DSPy meetup, Shopify presented their journey using DSPy to optimize prompts for Qwen, achieving 75x cost savings. DSPy uses genetic algorithms to iteratively improve prompts for optimal results with smaller models.

Links shared:

* [Ollama Gemma 4 bug](https://github.com/ollama/ollama/issues/15250)
* [Ollama Gemma 4 model](https://ollama.com/library/gemma4)
* [Shopify's DSPy optimization journey](https://www.youtube.com/watch?v=bxToahwOVpY)
* [Mason Daugherty tweet on open models](https://x.com/masondrxy/status/2039776722220916762)

## How is Copilot CLI accessing the web browser so easily?

📹 [37:22](https://youtube.com/watch?v=3cgN7X0fIB0&t=2242)

Copilot CLI uses the Playwright MCP server for browser access. By default, Playwright opens a **separate** browser instance without your cookies/auth — which is more secure but means authenticated pages won't work.

To use your existing authenticated browser session, you need the **Playwright MCP Bridge** browser extension. Pamela demonstrated installing it from the Chrome Web Store (also available for Edge), then updating her MCP config to use the `--extension` argument. With the bridge extension, Playwright connects to her existing browser with all cookies and authentication intact.

**Security note**: This gives the agent access to any page in your authenticated browser, so use with caution.

Links shared:

* [Playwright MCP docs](https://playwright.dev/docs/getting-started-mcp#user-profile)
* [Playwright MCP Bridge (Chrome Web Store)](https://chromewebstore.google.com/detail/playwright-mcp-bridge/mmlmfjhmonkocbjadbfplnigmagldckm)

## What techniques does GitHub Copilot use to search large repos?

📹 [45:30](https://youtube.com/watch?v=3cgN7X0fIB0&t=2730)

GitHub Copilot uses semantic code search, which now works both on github.com and within VS Code. Previously, searches required exact text matches; now it uses vector-based semantic search. When you start a conversation, Copilot automatically indexes the workspace in the background.

The exact implementation details keep evolving. Pamela shared a blog post about their new embedding model and mentioned that the coding agent on github.com also has access to semantic code search (since March 2026). There may be a hybrid approach between local and remote indexing, but the details aren't fully clear as the implementation keeps changing.

Links shared:

* [Copilot coding agent semantic code search](https://github.blog/changelog/2026-03-17-copilot-coding-agent-works-faster-with-semantic-code-search/)
* [Repository indexing for GitHub Copilot](https://docs.github.com/en/copilot/concepts/context/repository-indexing)
* [GitHub Copilot's new embedding model](https://github.blog/news-insights/product-news/copilot-new-embedding-model-vs-code/)

## Would it be possible to do a Q&A with a VS Code team member?

📹 [51:01](https://youtube.com/watch?v=3cgN7X0fIB0&t=3061)

The VS Code team does internal office hours at Microsoft and runs a popular YouTube channel with frequent livestreams. The best opportunity to ask questions is during their release recap livestreams (next one around April 16th). Pamela said she'd ask the team about doing something more interactive or whether they have their own Discord channel.

Links shared:

* [VS Code YouTube channel](https://www.youtube.com/@code)
* [VS Code Live: April Recap](https://www.youtube.com/watch?v=I0bGJHsP6eA)

## Announcements

📹 [25:20](https://youtube.com/watch?v=3cgN7X0fIB0&t=1520)

* **MCP Dev Summit going global** — 7 new cities added. Check the [Linux Foundation events page](https://events.linuxfoundation.org/aaif-events/).
* **X (Twitter) MCP Server released** — [github.com/xdevplatform/xmcp](https://github.com/xdevplatform/xmcp)
* **Azure OpenAI → Microsoft Foundry migration** starting April 16.
* **Python 3.14** — add to CI matrices. [python.org/downloads](https://python.org/downloads)
* **PyCon 2026** — Pamela's MCP tutorial Thursday 9am. [us.pycon.org/2026/schedule/tutorials](https://us.pycon.org/2026/schedule/tutorials)
* **Podcast: "Is context engineering the new RAG?"** — [youtube.com/watch?v=wGpJdn8frYE](https://www.youtube.com/watch?v=wGpJdn8frYE)
* **Astral rethinking ruff/ty for agents** — [youtube.com/watch?v=DuCwaXTHtZo](https://www.youtube.com/watch?v=DuCwaXTHtZo)
* **"Revenge of the Data Scientist" by Hamel Husain** — [hamel.dev/blog/posts/revenge](https://hamel.dev/blog/posts/revenge)
* **Azure OpenAI to Responses API migration skill** — [github.com/Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses/tree/main/skills/azure-openai-to-responses)
