# November 10, 2026 Office Hours Q&A

## Announcement: Skills over MCP arrives in the GitHub Copilot harness

📹 [0:58](https://youtube.com/watch?v=LvVH3W4-xpg&t=58)

Skills over MCP ([SEP-2640](https://github.com/modelcontextprotocol/ext-skills)) is now supported in the GitHub Copilot harness. Any product built on that harness can add support, but each one needs its own way to turn it on. The Copilot CLI uses an environment variable, and [VS Code Insiders 1.146 adds experimental support](https://code.visualstudio.com/updates/v1_146#_november-4-2026). To try it in VS Code, search user settings for "MCP skills" and enable the chat agent host MCP skills setting. The setting was off by default during the office hours session. Since then, [a VS Code PR enabled MCP skills by default](https://github.com/microsoft/vscode/pull/347465), so it should be on by default in upcoming Insiders builds and later in VS Code stable.

### Demo: Loading skills from a remote authenticated MCP server

📹 [2:39](https://youtube.com/watch?v=LvVH3W4-xpg&t=159)

The demo used the [Descope](https://app.descope.com/gettingStarted) MCP server. Descope is an MCP auth provider, and the server was authenticated with a Descope account. Asking "what Descope skills are there?" showed one skill exposed by the server. When the agent first loads skills from an MCP server, VS Code asks for permission ("Allow skills from ..."), and you can allow them once. It was not yet clear whether VS Code will always show that prompt. The Descope FGA skill loaded and worked because it was a single `SKILL.md` with no supporting files.

### Demo: Serving local skills from a FastMCP server

📹 [4:03](https://youtube.com/watch?v=LvVH3W4-xpg&t=243)

A minimal FastMCP server can serve skills from a local folder with the skills provider. The demo server served only skills, and its one skill wrote release notes from merged pull requests using a `template.md` file. When Copilot was asked to draft release notes, it read the `SKILL.md` through the MCP server. It could not open `template.md` because it had no tool for reading MCP resources.

Many skills have no attached resources, but many do, so supporting files need to work too. The server exposes them as MCP resources, and the client needs a way to read them. Copilot filed [a VS Code issue for the supporting-files problem](https://github.com/microsoft/vscode/issues/347446) during the session, and the issue was shared with the VS Code team. The VS Code team fixed it later that day: [the fix lets MCP skills read their supporting files](https://github.com/microsoft/vscode/pull/347465). Bernhard pointed to an earlier issue about [supporting SEP-2640 in GitHub Copilot](https://github.com/microsoft/vscode/issues/338300).

Support across hosts is still early. The [ext-skills implementations list](https://github.com/modelcontextprotocol/ext-skills/blob/main/docs/implementations.md#hosts-including-agent-harnesses-ides-and-web-applications) tracks hosts, including MCPJam Inspector, and [caniuse.dev's host comparison](https://caniuse.dev/embed/host-compare?hosts=preset%3Achatgpt%2Cpreset%3Aclaude%2Cpreset%3Aclaude-desktop%2Cpreset%3Aclaude-code%2Cpreset%3Acodex%2Cpreset%3Acopilot%2Cpreset%3Acursor%2Cpreset%3Avscode%2Cpreset%3Aslack%2Cpreset%3Acursor-cli%2Cpreset%3Acopilot-cli&capability=skills-extension) still lists most hosts as unsupported. At the time of the session, VS Code was listed as unsupported because the feature was still behind a setting.

### How are skills over MCP different from the agent skills that Codex, Cursor, and other apps already bundle with MCP servers?

📹 [8:51](https://youtube.com/watch?v=LvVH3W4-xpg&t=531)

Bundling skills with MCP servers is what [agent plugins](https://agent-plugins.org/compatible-clients) do. Cursor, ChatGPT, VS Code, Kiro, OpenHands, and many others formally support the agent plugin spec, and other tools have their own bundling approaches. That approach still works.

Skills over MCP are more flexible because the server provides the skills. An authenticated server like Descope could, in theory, serve different skills based on your plan or data. A server could also generate `SKILL.md` files dynamically, for example with Jinja templates, instead of serving static files.

## Announcement: Azure OpenAI starter kit adds Decisions API samples

📹 [15:18](https://youtube.com/watch?v=LvVH3W4-xpg&t=918)

The [Azure OpenAI starter kit](https://github.com/Azure-Samples/azure-openai-starter) now includes [Decisions API](https://learn.microsoft.com/azure/foundry/openai/how-to/decisions) samples alongside the Responses API samples, in Python, TypeScript, Go, .NET, Java, and Ruby. Amazon reported large savings after moving a big internal LLM workload to Decisions. Look for places where your own app could save money the same way.

The samples can pass an image or plain text, ask questions about it, and use each answer's confidence to decide what to do next. The repo also includes infrastructure to deploy the model. The Decisions API runs on GPT-6 Luna, so it should work anywhere you can deploy GPT-6 Luna, though one East US region might be an exception.

In chat, Patrick shared that his team is experimenting with NVIDIA Sparks to run local models and save costs. Local models are a reasonable approach if you have the hardware.

## Announcement: Claude adds message threads

📹 [17:12](https://youtube.com/watch?v=LvVH3W4-xpg&t=1032)

[Claude message threads](https://claude.com/resources/articles/message-threads) make the Messages API look much like the Responses API. You create a thread, get back an ID, and then pass that ID instead of resending the whole conversation. The Responses API has always supported stateless or stateful use, while the Messages API was stateless until now. Message threads are also supported for Claude models in Microsoft Foundry, as documented under [context management for Claude models](https://learn.microsoft.com/azure/foundry/foundry-models/concepts/claude-models#context-management). [A pull request is adding message threads examples to the Azure-Samples/claude repo](https://github.com/Azure-Samples/claude/pull/77) across SDK languages.

## Announcement: OpenAI launches GPT-6 Cyber

📹 [18:31](https://youtube.com/watch?v=LvVH3W4-xpg&t=1111)

[GPT-6 Cyber](https://openai.com/index/introducing-gpt-6-cyber/) is tuned to find vulnerabilities. Since LLMs are already helping attackers find vulnerabilities, a defensive model like this is a way to fight fire with fire. It should outperform frontier models on cybersecurity tasks and likely has different guardrails. It is available through the API and Codex only to a select group of approved Daybreak Red customers. You can apply for [Daybreak](https://openai.com/daybreak), which has a Blue tier for defensive work and a Red tier for advanced red teaming.

## Announcement: AI coding startups consolidate

📹 [20:23](https://youtube.com/watch?v=LvVH3W4-xpg&t=1223)

There were several acquisitions last week:

* [OpenAI is acquiring Pierre](https://openai.com/index/openai-to-acquire-pierre/) for integration into Codex. Pierre was founded by people who created Twitter Bootstrap and worked on code review, code storage, and diffs.
* [Meta acquired Conductor](https://www.conductor.build/announcement), a tool for running parallel agents. This may help Meta's coding agent, [Muse Code](https://dev.meta.ai/products/muse-code), which costs $200 a month.
* [HumanLayer joined Factory](https://www.humanlayer.dev/blog/humanlayer-joins-factory), which works on software factories.

## Discussion: Security breaches and technology in healthcare

📹 [22:02](https://youtube.com/watch?v=LvVH3W4-xpg&t=1322)

Bernhard joked about the [European cold chain hacks](https://en.wikipedia.org/wiki/European_cold_chain_hacks). In those attacks, supermarket fridges were set to defrost mode, which destroyed tens of millions of euros of food. The login credentials were "admin" with the current date as the password. Hospital blood supplies were also affected.

[The Infinity Machine](https://www.amazon.com/dp/0593831845), a book about the creation of DeepMind, describes DeepMind's attempt to work with the UK's NHS. A hospital app aimed to streamline care, but the effort fell apart amid backlash against big tech in healthcare. Technology could make healthcare much more efficient, since doctors don't want to spend their time faxing documents, but deployments need to take security and patient privacy seriously. Patrick shared that he left healthcare tech because of slow technical progress.

## Discussion: The impact of AI on the CS curriculum

📹 [24:26](https://youtube.com/watch?v=LvVH3W4-xpg&t=1466)

Pamela gave a [talk on AI's impact on CS education](https://pamelafox.github.io/my-py-talks/impact-of-ai-on-cs-ed/) explains the current state of software engineering for K-12 and college teachers. The numbers show that AI is now the norm for coding: 70% of new code at Google is written by AI, 40% of code changes are started by agents, and more than half of engineers do most of their work with AI.

The talk's thesis is that agents now mostly write code and tests. Humans and agents both review, ship, and scale the work. Humans still handle problem design, specs, and managing agents. Nobody knows what this will look like in one or five years, which makes it hard for teachers to decide what to teach students who will join the industry eight to ten years from now.

### Should I still learn Python, or learn coding a different way?

📹 [26:24](https://youtube.com/watch?v=LvVH3W4-xpg&t=1584)

Learn one language well, enough to understand what a programming language is and what paradigms it uses. Learning many languages is less important than it used to be. Learning one language still helps you understand how computers work. Reading code and explaining what it does matters much more now than writing it or memorizing syntax. In Pamela's most recent job interview, she mostly read code and explained it.

Testing and verification are now the most important skills. If you can verify software, you can let agents loose on it. The testing trophy is a useful model:

* **End-to-end tests** check whole user flows. They matter most now because they should stay the same even if the implementation changes completely, such as a port from Python to Rust.
* **Property-based and fuzz tests** are important, especially for APIs.
* **Security and performance tests** are also very important.
* **Formal proofs** are becoming more common. They are currently being used to find bugs in the MCP SDKs. Formal proofs used to be an obscure skill, but they are the only way to guarantee correctness.

For each application, ask what your verification looks like. With full verification, coding agents can work freely. Without it, you need more manual QA, which gets frustrating and boring. Other skills are growing in importance too: understanding how computers and LLMs work behind the scenes, product judgment, and working with people.

## Announcement: GitHub and Azure updates

📹 [30:47](https://youtube.com/watch?v=LvVH3W4-xpg&t=1847)

* [Secret scanning now detects secrets in GitHub Actions workflow logs](https://github.blog/changelog/2026-11-09-secret-scanning-detects-secrets-in-github-actions-workflow-logs/). Workflow logs are a common place for leaked secrets. You can enable it under policies, in advanced security.
* [Copilot code review has new management APIs](https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates) that give you more control over reviews.
* [Four GPT-4o versions in Azure OpenAI are retiring](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirements#how-to-get-ready-for-model-retirements-and-version-upgrades). You should have moved off GPT-4o long ago.

## Demo: GitHub in Slack and Teams

📹 [31:51](https://youtube.com/watch?v=LvVH3W4-xpg&t=1911)

[GitHub Copilot in Slack and Teams is now generally available](https://github.blog/changelog/2026-11-06-github-copilot-in-slack-and-teams-is-generally-available/). It puts a GitHub agent in your Teams or Slack channel. The demo showed a Teams channel from an earlier alpha trial in September. To set it up, create a channel, say hi to GitHub, and set the channel's default repository to link the channel with a repo. The experience was rough in the alpha, so try it again now that it is GA.

## Announcement: Python 3.10 is end of life

📹 [33:17](https://youtube.com/watch?v=LvVH3W4-xpg&t=1997)

[Python 3.10 is now end of life](https://www.python.org/downloads/) and no longer receives security updates, so drop it if you haven't already. Python 3.11 is supported until next October, so your projects should require at least Python 3.11.

A GitHub Copilot app project can open upgrade PRs across many repos, so you can review them when you have time. [The upgrade PR for flask-db-quiz-example](https://github.com/pamelafox/flask-db-quiz-example/pull/118/changes) shows the usual changes: raise the minimum version in `pyproject.toml`, update the CI matrix, and pick up some typing improvements. That PR was merged during the session. A coding agent can handle this kind of upgrade.

## Announcement: Image and video models across the industry

📹 [35:05](https://youtube.com/watch?v=LvVH3W4-xpg&t=2105)

* [OpenAI Images 2.6](https://openai.com/index/introducing-images-2-6/) and MAI Image 2.6 share a version number, but as far as Pamela knows they are different models. Both seem good. Pamela uses MAI images.
* [Gemini Omni 1.2 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/) makes longer videos. Pamela hadn't tried the video tools and uses Opus for graphic design, which works very well.

## Announcement: Latest research into agent reasoning and hallucinations

📹 [35:39](https://youtube.com/watch?v=LvVH3W4-xpg&t=2139)

* [MCPHallu](https://arxiv.org/abs/2611.07689) studies hallucinations in agents that use MCP servers.
* [Another study](https://arxiv.org/abs/2611.07238) found that nearly half of agents' reasoning tokens were not useful.

## If an agent can only access what the asking user can access, how can Microsoft IQ use a company-wide knowledge graph to give good answers?

📹 [36:58](https://youtube.com/watch?v=LvVH3W4-xpg&t=2218)

That depends on how the agent is set up. There are two main models ([agent identity in Microsoft Agent 365](https://learn.microsoft.com/microsoft-agent-365/developer/identity)):

* **On behalf of the user:** The agent uses the user's token, so it can only access what the user can access. Work IQ, for example, makes Microsoft 365 calls with the user's permissions. The agent still helps because it has endless patience and will run many more searches than a person would.
* **Agent with its own identity:** The agent runs with its own Microsoft Entra user account, and even its own mailbox. Treat the agent like a new person: put it in the right Entra groups and decide which permissions it needs. This lets it see more, but be careful not to give it access to too much. Governance features let you monitor its permissions, and an agent blueprint defines the permissions that each new instance gets.

Building agents with their own identities is increasingly common among Pamela's colleagues who want more powerful agents.

### Can anyone in the company use an agent that has its own identity?

📹 [40:51](https://youtube.com/watch?v=LvVH3W4-xpg&t=2451)

Yes. Once you publish the agent and it is approved in the admin center, other people can create their own instances of it. This requires some administration. One of Pamela's colleagues recently got his agent approved, so others can now add instances of it.

### Will Microsoft and Google soon promote an all-knowing expert agent?

📹 [42:27](https://youtube.com/watch?v=LvVH3W4-xpg&t=2547)

Agents with their own identity are already a bigger focus because they are more capable and give clearer attribution. When an agent acts on your behalf, like Copilot filing the VS Code issue from earlier in the session, it becomes hard to tell what came from a colleague and what came from their agent. That reduces trust. When an agent has its own identity, it is clear that an email came from the agent. Agents with their own identity can also do more background work because they don't wait on token refreshes or consent flows and can act whether or not the user is present. That is why more demos use this approach.

## Will GraphRAG replace vector databases, or are they used together in a hybrid system?

📹 [44:08](https://youtube.com/watch?v=LvVH3W4-xpg&t=2648)

Knowledge graphs come in several kinds, even within GraphRAG, and they answer different kinds of questions:

* **Entity-relationship graphs** extract subject-predicate-object facts from your data, such as "this person did this thing in this location." They are good for questions about how things in your dataset connect.
* **Topic cluster graphs** group a knowledge base by topic so you can zoom in and out. They help with broad questions, such as which kinds of issues appear across the whole knowledge base.

Graphs will not replace vector search. Both graph approaches work best alongside vector search and rely on some vector math. Some questions are also better answered without either graph. That leaves a design choice: run all approaches in parallel, or use a router to pick between them.

Graphs will be a topic at Ignite, including the session [Foundry IQ: Knowledge graphs for better enterprise context](https://ignite.microsoft.com/en-US/sessions/1787856619636001E66J-1791588325591001CbDi).

### Should knowledge graphs be combined with hybrid search for cases like keyword searches for specific legal information?

📹 [49:13](https://youtube.com/watch?v=LvVH3W4-xpg&t=2953)

Pablo shared that a Neo4j presentation recommended combining hybrid search with knowledge graphs. Hybrid search covers cases that need semantic search or exact keyword matches, such as specific legal information. Neo4j has many talks on this topic. So far, the experience at Microsoft is that you need a mix of search types, run in parallel and/or chosen by a router.

### How does a chatbot use graph-based or RAG knowledge?

📹 [49:49](https://youtube.com/watch?v=LvVH3W4-xpg&t=2989)

It depends on the chatbot, but a common approach is to expose the knowledge through an MCP endpoint. Azure AI Search and Foundry IQ knowledge bases already have MCP endpoints. Otherwise, you can build an MCP server or expose the knowledge as tools. For example, a [developer knowledge base for GitHub Copilot](https://github.com/pamelafox/developer-kb-for-github-copilot) ([slides](https://pamelafox.github.io/developer-kb-for-github-copilot/#/23)) uses Foundry IQ and connects to Copilot over MCP. The agent sends queries to the knowledge base, gets results back, and uses them to answer.

### How do AI models perform specific tasks?

📹 [51:13](https://youtube.com/watch?v=LvVH3W4-xpg&t=3073)

AI agents use tool calling to perform tasks. The [Python + AI series](https://techcommunity.microsoft.com/blog/educatordeveloperblog/level-up-your-python--ai-skills-with-our-complete-series/4464546) has videos on how AI models work, with later videos covering agents and tool calls.

## Where should we start when building a SharePoint knowledge bot for our organization's data?

📹 [47:26](https://youtube.com/watch?v=LvVH3W4-xpg&t=2846)

There are three main options:

* **[Work IQ](https://learn.microsoft.com/microsoft-365/copilot/extensibility/work-iq/mcp/overview):** Accesses SharePoint documents on behalf of the user, so it requires the on-behalf-of flow.
* **[Microsoft 365 Copilot Retrieval API](https://learn.microsoft.com/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview):** Grounds your app in SharePoint, OneDrive, and Copilot connector content.
* **[SharePoint indexer for Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-index-sharepoint-online):** Still in preview, but expected to be generally available very soon.

The best choice depends on how fresh the data needs to be, how users access it, and which SharePoint features you use.
