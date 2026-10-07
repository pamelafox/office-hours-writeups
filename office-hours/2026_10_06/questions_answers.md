# October 6, 2026 Office Hours Q&A

## Announcement: OpenAI DevDay 2026 highlights

📹 [00:42](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=42)

OpenAI DevDay took place in San Francisco last week. It was the source of much of this session's news. The [DevDay 2026 recap](https://openai.com/index/devday-2026-recap/) lists more than 20 announcements. The ones most relevant to developers are summarized below. OpenAI also announced Codex Cloud, which runs Codex tasks remotely, similar to Copilot cloud agents.

### Sign in with ChatGPT

📹 [01:09](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=69)

Sign in with ChatGPT works like Sign in with Google. It lets users sign in to other apps, including coding agents such as T3 and OpenClaw, and spend their ChatGPT AI credits there. OpenAI wants people to use its credits beyond ChatGPT itself, which is a very different approach from Anthropic's. GitHub Copilot sits somewhere in between: it works with many models and across many surfaces, but there is Sign in with GitHub, not Sign in with GitHub Copilot.

### Pro 500 plan and Ultrafast

📹 [02:10](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=130)

OpenAI added Ultrafast, a premium speed tier that generates tokens up to 8× faster in Codex and up to 6× faster in the API. Because that speed costs more, Ultrafast comes with a new Pro 500 plan, which costs $500 a month and has the highest usage allowance. That is a lot of money, but it might be worth it, especially if your company pays.

### ChatGPT plugins extend MCP Apps

📹 [02:39](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=159)

ChatGPT plugins are built on MCP, and they now integrate more deeply with the ChatGPT sidebar and full-screen view. They build on MCP Apps, which let an MCP server embed a website in an iframe. The [openai/mcp-extensions repo](https://github.com/openai/mcp-extensions) documents OpenAI's additions in its `spec.md`, such as:

* **Entry points:** Places in ChatGPT where an app can be invoked.
* **File extension handling:** An MCP server can declare which file types it handles.

Pamela talked with OpenAI's MCP team at DevDay. Some of these extensions may be proposed upstream as improvements to MCP itself, but they could also remain OpenAI-specific. If you build MCP servers or ChatGPT plugins, read through the spec.

### MCP events support

📹 [04:27](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=267)

ChatGPT is the first major client to support MCP events, even though events are not fully in the MCP specification yet. (Work on them is happening in the MCP [triggers and events working group](https://modelcontextprotocol.io/community/working-groups/triggers-events).) OpenAI added events early because it wanted triggers, events, and automations for plugins.

### Plugin discovery in chat

📹 [04:57](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=297)

ChatGPT can now suggest a relevant plugin mid-conversation. For example, it might recommend a hotel plugin when you try to book a hotel. It only recommends plugins that are clearly well used, highly ranked, and appropriate, so a high-quality plugin has a chance of being surfaced to users.

### Dots: always-on agents

📹 [05:37](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=337)

[Dots](https://openai.com/index/introducing-dots/) are long-running agents with memory, built on top of ChatGPT. They appear to be OpenAI's answer to Grok Bot and Muse. The closest Microsoft equivalent is Autopilot, which also has its own identity.

### GPT-6.1 Sol

📹 [06:10](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=370)

[GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol/) delivers near-Astra intelligence at one-fifth of Astra's standard input and output token prices. The main story is cost: if you liked Astra but not its price, try 6.1 Sol. It is already available in Microsoft Foundry and in [GitHub Copilot](https://github.blog/changelog/2026-09-29-gpt-6-1-sol-in-github-copilot/). The Azure OpenAI samples are being updated to use GPT-6.1 Sol.

### Decisions API as an answer to Jev

📹 [07:19](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=439)

[Jev from TypeSafe AI](https://docs.typesafe.ai/introduction) has been very popular over the last few weeks. It is a "System One" model that makes fast structured decisions. It can only pick an option from a list, give a score, or return a boolean. For many tasks that previously used structured outputs, it is very fast, appears accurate, and can be a good replacement. Other model providers now want an equivalent.

OpenAI's answer is the [Decisions API](https://developers.openai.com/api/docs/guides/decisions). It runs GPT-6 Luna with reasoning turned off and adds constrained decoding to make it faster, with an API shaped like Jev's. If you prefer to stay within the OpenAI model ecosystem or lack access to Jev, it is the closest equivalent. The Jev team has argued online that constrained decoding reduces accuracy and is not a good way to build this kind of model. It might still work for your scenario, so it is worth evaluating.

### Agents API

📹 [09:56](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=596)

The Agents API is essentially a managed Codex harness in the cloud. It is currently only on OpenAI. It might come to Azure eventually because it is somewhat like a successor to the Assistants API, though it does much more. If it does, it would be an alternative to Foundry hosted agents.

### GPT Live for real-time voice

📹 [10:41](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=641)

OpenAI showcased voice heavily with the [GPT Live](https://openai.com/index/introducing-gpt-live/) model, but the voice demos famously failed during the keynote. In a later session, attendees said it worked very well and looks like a compelling real-time voice model.

## Where should I start with Python + AI?

📹 [12:32](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=752)

Start with the [Python + AI series](https://aka.ms/pythonai/rewatch). It is a nine-part series on using generative AI models from Python, with recordings and resources for each session.

## Announcement: The new Microsoft Copilot with Home, Code, and Autopilot

📹 [13:01](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=781)

Microsoft launched [the new Copilot with Home, Code, and Autopilot](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/), which combines several apps into one. The rollout appears to be limited; Pamela did not have access yet.

* **Code** is the GitHub Copilot app with some features removed. Many people use the GitHub Copilot app for quick chats that aren't tied to a project, and some don't even have a GitHub account. The Code tab has features such as automations but doesn't depend on GitHub repos.
* **Autopilot**, previously called Scout, is an agent with its own identity, similar to Muse and Grok Bot. Besides this default autopilot in the app, developer can build custom autopilot agents for specific workflows and register them in the directory. Pamela and her colleague Ayça have been giving demos on how to build your own autopilot, like in [this Microsoft IQ talk](https://www.youtube.com/watch?v=B5ywcwSkvBA&t=10076s).

## Discussion: MCP gateways

📹 [15:03](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=903)

MCP gateways are a growing trend, with several approaches. [Uber announced an MCP management platform](https://x.com/UberEng/status/2106071967619322330) which includes an MCP gateway. Jiquan Ngiam, founder of MintMCP, spoke about their MCP gateway at MCP Community Connect SF the week before ([slides on enterprise MCP security](https://1drv.ms/b/c/b79cd1db3ada14c5/IQAm4bAkFsedQ4v_nXEILxDSAS_uT8-fZc2EmQpLalwtcdw?e=r6mo4a)).  On Azure, the options include the APIM AI gateway and Foundry Toolbox, which is essentially an MCP gateway.

## Discussion: DoorDash has an MCP server

📹 [16:06](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=966)

[DoorDash now offers MCP](https://developer.doordash.com/en-US/mcp/) and a CLI for agentic ordering. Ordering food for events is a common use case. Big consumer companies like DoorDash adding MCP servers shows how widespread MCP has become across the industry.

## Demo: Dynamic workflows in GitHub Copilot

📹 [17:17](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=1037)

[Dynamic workflows](https://github.blog/changelog/2026-10-01-dynamic-workflows-in-copilot-cli-and-the-copilot-app/) are now available in Copilot CLI, the GitHub Copilot app, and the Copilot SDK. A dynamic workflow defines in code how a task is carried out, so you get an auditable orchestration of agents. The [dynamic workflows concepts doc](https://docs.github.com/en/copilot/concepts/agents/dynamic-workflows#how-dynamic-workflows-differ-from-autopilot-and-fleet) explains how they differ from Autopilot and Fleet. The CLI requires experimental mode.

For the demo, Pamela asked the GitHub Copilot app in natural language to [create a dynamic workflow](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-dynamic-workflows#creating-a-dynamic-workflow) that lists the changes on a branch, reviews each change, and summarizes the results. The workflow is JavaScript built on an SDK, with phases and arguments. It can spawn subagents and run steps in parallel or independently. The app mostly hides the JavaScript and encourages natural language, but the code gives you a lot of control over the workflow.

### Aside: An agent-completion sound hook

📹 [19:34](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=1174)

Pamela uses a Copilot hook that plays a recording of her child giggling whenever an agent finishes. It's useful when she walks away from the computer: the giggle signals that it's time to come back and check the agent's work. A variant waits until she has been away for 60 seconds, then reads out the session title so she knows which session finished.

During the session, the hook's audio came through for viewers watching on Discord, even after Pamela muted her machine; it does not appear to be in the YouTube recording. Each of the workflow's subagents set it off, so Discord viewers heard many giggles.

### Running the workflow across hundreds of subagents

📹 [21:18](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=1278)

To run a workflow, ask for it by name in natural language ("Run the review-changed workflow"). The workflow runs in the background, and a new background activity tab shows its progress. The demo branch had about 300 changed files, so the workflow spawned about 300 subagents, one per file. That uses a lot of credits.

Each subagent appears as its own subsession with the review prompt. The UI shows the current phase and lets you pause or cancel the workflow. Pamela canceled it because the branch was mostly data changes that didn't need review. The workflow itself was still useful enough to keep, with a change to skip data files. The agent had even suggested reviewing that issue.

### Dynamic workflows versus skills

📹 [23:49](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=1429)

If you want to farm work out to subagents, dynamic workflows formalize that process. You could write a skill that says "use subagents for this," but a skill is just Markdown, so the agent may or may not follow it correctly. A workflow is JavaScript you can read and check, so the results are more deterministic. Dynamic workflows only work in the Copilot app and CLI. For a more portable approach, write a `SKILL.md` that tells the agent to create a subagent for each item; you may get similar results with less determinism.

### Viewing the workflow code

📹 [29:32](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=1772)

The docs on [reusing and sharing dynamic workflows](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-dynamic-workflows#reusing-and-sharing-dynamic-workflows) explain that you copy the workflow directory to make it available in all sessions. Pamela posted the [generated review-changed workflow JavaScript as a gist](https://gist.github.com/pamelafox/dd6c3ad66933105affcaf838f6a02f92). It is a Copilot SDK extension that calls `defineWorkflow` with metadata (name, description, phases, and an arguments schema) and a `run` function. The workflow has three phases:

1. **List changes:** Runs git commands to collect changed and untracked files, diffing against the merge base with `main` by default.
2. **Review:** Uses `ctx.parallel` to start one reviewer subagent per file with `ctx.agent`. Each reviewer is told not to modify files and returns findings that match a JSON schema with severity, line, title, and explanation.
3. **Summarize:** Sorts the combined findings by severity, counts them, and sends them to an agent to write a concise Markdown report.

Links shared:

* [Running a dynamic workflow from the command line](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-dynamic-workflows#running-a-dynamic-workflow-from-the-command-line)
* [Limiting a dynamic workflow](https://docs.github.com/en/copilot/concepts/agents/dynamic-workflows#limiting-a-dynamic-workflow)

## Announcement: Pamela's recent talks

📹 [32:38](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=1958)

Recordings, slides, and code from Pamela's recent talks are linked from her [talks page](https://pamelafox.org/talks/).

### Azure Container Apps sandboxes

📹 [32:51](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=1971)

The [Azure Container Apps sandboxes livestream](https://x.com/pamelafox/status/2105410713837859191) covered sandbox features that are especially useful for isolating agents and protecting against rogue agents. Resume and restore are particularly interesting: a sandbox can keep its disk, memory, and even running processes, then restore those processes later.

### A tour of Microsoft IQ

📹 [33:57](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=2037)

The Microsoft IQ talk condensed the IQ deep dive series into one hour. It gives a rapid-fire introduction to Foundry IQ (the same thing as Azure AI Search), Work IQ, Fabric IQ, and Web IQ.

### Parallelizing development with GitHub Copilot

📹 [34:37](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=2077)

The [WeAreDevelopers talk on parallelizing development with GitHub Copilot](https://pamelafox.github.io/parallelize-development-github-copilot/) covered subagents, the various Copilot surfaces, Git worktree strategies, hooks (including the giggle hook), background agents, automations, agentic workflows, and now dynamic workflows. It also covered Pamela's skill for using azd with worktrees, which lets her run azd across parallel agents. She shared a [repo of open-source agent skills](https://github.com/mattgotteiner/skills) that help with azd. She had added another skill to it the day before.

### GitHub Copilot, MCP, and skills workshop

📹 [36:12](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=2172)

The [GitHub Copilot, MCP, and skills workshop](https://pamelafox.github.io/github-copilot-mcp-skills-workshop/) is also available.

### Convergence with vectors at PyBay

📹 [36:32](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=2192)

At [PyBay](https://x.com/pamelafox/status/2106519693905519034), Pamela ran an improv game where two players try to say the same word at the same time. Each round, both players try to say a word between their two previous words, until they converge. The talk ran the game with both humans and embedding models. In the model version, players start from two random words and use vector embeddings to find a word in the middle. You can choose different operators and random models each round. In the live demo, the models went from "hawk" and "axe" to "hair" and "hair" in seven rounds. The [game is still deployed](https://ca-api-n7wptl6izdmcs.wonderfulplant-33a4a3ab.northcentralus.azurecontainerapps.io/web/play.html) for anyone to play.

The game shows how good open-weight embedding models have become, so you aren't limited to frontier embedding models. Local models will likely matter more and more. The [slides](https://pamelafox.github.io/convergence-with-vectors/) compare models on benchmarks and multilingual support. The two worth serious consideration are Microsoft's Harrier, which Web IQ uses and which helps make it fast, and Qwen3 Embedding. Both are multilingual and score well on benchmarks. Funnily enough, the models that did best on the benchmarks did worst in the game, though benchmarks measure very different things.

## Announcement: Rust for CPython

📹 [39:26](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=2366)

The [Rust for CPython](https://github.com/Rust-for-CPython/) project aims to formally support writing parts of CPython in Rust. That could make some parts of Python much faster, and many people want to contribute to CPython in Rust. If you're a Rust fan, check out the project.

## What can you say about A2A with Microsoft Agent Framework, Foundry, and Python?

📹 [40:12](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=2412)

Pamela hasn't done much with A2A yet. Work IQ supports A2A, and its A2A endpoint is increasingly the recommended way to use it. The [Work IQ A2A notebook](https://github.com/microsoft/iqdeepdive/blob/main/notebooks/workiq-a2a.ipynb) from the IQ deep dive shows the basic flow:

1. **Discover the agent card.** An agent card is a JSON document that describes the agent's identity, endpoint, capabilities, and skills. A2A defines its location under the `.well-known` path, a convention for standard locations. The notebook fetches it from the Work IQ gateway with a personal user token. The response includes the name, description, URL, provider, version, capabilities (streaming, but no push notifications), input and output modes, and JSON-RPC transports.
2. **Send a JSON-RPC request** with a method name and parameters, then read back the results.

The requests look a lot like MCP, where you send a tool name and parameters. The main differences seem to be discoverability and some additional capabilities, such as token streaming, which MCP servers don't usually do. Overall, MCP and A2A overlap heavily.

### Why do you have to send a method name to an agent?

📹 [42:58](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=2578)

A2A defines several kinds of requests, so the method name tells the agent which one you're sending. The [A2A specification](https://a2a-protocol.org/latest/specification/#312-send-streaming-message) lists methods such as send message, send streaming message, get task, list tasks, subscribe to a task, and push notifications. The two main concepts are messages and tasks. Tasks let you retrieve the current state of previously started work, which overlaps with [MCP tasks](https://modelcontextprotocol.io/extensions/tasks/overview) for long-running work that clients can poll for progress.

### How do you connect Foundry agents to A2A agents?

📹 [44:33](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=2673)

Foundry Toolbox has generic support for remote A2A agents, just as it supports remote MCP tools. The [Mastering Foundry Toolbox notebook](https://github.com/microsoft-foundry/forgebook/blob/main/notebooks/mastering-foundry-toolbox.ipynb) shows how to connect Toolbox to many kinds of tools, including A2A. The Learn guide on [connecting to an A2A agent endpoint from Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/agent-to-agent?pivots=python) has examples for prompt agents and hosted agents. The hosted agent example connects through Foundry Toolbox.

Pamela now uses Foundry Toolbox for most of her demos, including several of the agents in the [IQ deep dive repo](https://github.com/microsoft/iqdeepdive/tree/main/src). Once you move beyond a single MCP server, Toolbox is usually easier, and it simplifies passing user tokens around. To learn more, watch the MCP Live talk from Viswajeeet Balaji on [using Toolboxes in Microsoft Foundry as a unified MCP layer](https://www.youtube.com/watch?v=_VzwtDOqX0M&list=PLJ2a7YWJ3jxk&index=10&t=2s&pp=iAQB).

VK planned to try Foundry Toolbox.

## Discussion: Upgrading FastMCP servers

📹 [48:46](https://www.youtube.com/watch?v=M9IF-ymn5sU&t=2926)

Many developers build MCP servers on top of Azure. If you use [FastMCP](https://gofastmcp.com/), upgrade to v4. It supports the latest MCP SDK and has many other new features.

FastMCP has upgrade guides for each major version, such as [upgrading from FastMCP 3](https://gofastmcp.com/getting-started/upgrading/from-fastmcp-3). Find the guide for your current version and point your coding agent at it to handle the upgrade. AI is making upgrades and refactors much easier, which was the theme of Pamela's talk the next day on AI's effect on software engineering.

If you use the official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.3.0) directly, upgrade to v2. FastMCP depends on the official SDK and releases more often.