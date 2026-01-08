# January 6, 2026 Office Hours Write-up

## How do you set up Entra OBO (On-Behalf-Of) flow for Python MCP servers?

📹 [5:48](https://youtube.com/watch?v=LZLg_hQYk4I&t=348)

The demo showed how to use the Graph API with the OBO flow to find out the groups of a signed-in user and use that to decide whether to allow access to a particular tool.

The flow works as follows:

1. Get the access token from the middleware
2. Exchange that access token for a Graph API token using the OBO flow with a specific scope
3. Use the Graph token to call `graph.microsoft.com/v1/me/memberOf` to check group membership
4. Filter by the specific group ID you want to check (more efficient than getting all groups and paginating)
5. If the count returned is 1, the user is in the group; if 0, they're not

For the authentication dance, FastMCP handles the DCR (Dynamic Client Registration) flow since Entra itself doesn't support DCR natively.

To test from scratch:

1. Go to "Authentication: Remove Dynamic Authentication Providers" in VS Code
2. Clear the localhost authentication
3. Start the server
4. When you start, VS Code detects the 401, attempts DCR flow, gets the PRM, and sees the authorization server supports DCR
5. Allow access on the FastMCP consent screen
6. It briefly jumps to login.microsoftonline.com before returning

Links shared:

* [PR to python-mcp-demos to add Entra OBO](https://github.com/Azure-Samples/python-mcp-demos/pull/27)

## Which MCP inspector should I use for testing servers with Entra authentication?

📹 [20:24](https://youtube.com/watch?v=LZLg_hQYk4I&t=1224)

The standard MCP Inspector doesn't work well with Entra authentication because it doesn't do the DCR (Dynamic Client Registration) dance properly.

MCP Jam is recommended instead because it properly handles the OAuth flow with DCR. To set it up:

1. Install MCP Jam
2. Add a server over HTTP (e.g., localhost:8000/mcp)
3. Configure OAuth with your scopes
4. It will go through the full registration flow

MCP Jam also has nice features like:

* Saved requests for replaying the same request repeatedly during development
* An OAuth debugger with a diagram showing the whole flow
* A chat interface for testing your server with different models

One note: enum values in tools don't yet show as dropdowns in MCP Jam (issue to be filed).

Links shared:

* [MCPJam Inspector](https://github.com/MCPJam/inspector)

### What's the difference between MCP Jam and LM Studio?

📹 [34:19](https://youtube.com/watch?v=LZLg_hQYk4I&t=2059)

LM Studio is primarily for playing around with LLMs locally. MCP Jam has some overlap since it includes a chat interface with access to models, but its main purpose is to help you develop MCP servers and apps. It's focused on the development workflow rather than just chatting with models.

## How do you track LLM usage tokens and costs?

📹 [28:04](https://youtube.com/watch?v=LZLg_hQYk4I&t=1684)

For basic tracking, Azure portal shows metrics for token usage in your OpenAI accounts. You can see input tokens and output tokens in the metrics section.

You can also:

* Log custom metrics with OpenTelemetry
* Use Langfuse
* Use LiteLLM (mentioned by a community member)

If you use multiple providers, you need a way to consolidate the tracking. OpenTelemetry metrics could work but you'd need a way to hook into each system.

## How do you keep yourself updated with all the new changes related to AI?

📹 [30:32](https://youtube.com/watch?v=LZLg_hQYk4I&t=1832)

Several sources recommended:

* Company chat channels (e.g., generative AI chat, GitHub Copilot chat) for sharing what people are experimenting with
* Newsletters from LangChain, Pydantic AI, etc.
* LinkedIn, Hacker News
* Specific bloggers

Particularly recommended:

* [Elite AI Assisted Coding newsletter](https://elite-ai-assisted-coding.dev/) - Great for agentic coding tips, run by Isaac and Eleanor who experiment with everything
* [Drew Breunig's blog](https://www.dbreunig.com/) - A developer who writes thoughtful pieces about LLMs

Links shared:

* [How I learn about generative AI (blog post)](https://blog.pamelafox.org/2025/08/how-i-learn-about-generative-ai.html)

## How do you build a Microsoft Copilot agent in Python with custom API calls?

📹 [36:30](https://youtube.com/watch?v=LZLg_hQYk4I&t=2190)

For building agents that work with Microsoft 365 Copilot (which appears in Windows Copilot and other Microsoft surfaces):

1. Use the Agent Framework - it has a demo for M365 integration
2. Test locally using the agent playground
3. Deploy to Microsoft 365 using the deployment docs

The agent framework team is responsive if there are issues.

Links shared:

* [Blog post: Bring your own agents to M365 Copilot](https://devblogs.microsoft.com/microsoft365dev/bring-your-own-agents-into-microsoft-365-copilot/)
* [Learn Docs: Deploy agent to M365](https://learn.microsoft.com/en-us/microsoft-365/agents-sdk/deploy-azure-bot-service-manually)
* [Agent-framework + M365 sample](https://github.com/microsoft/agent-framework/tree/main/python/samples/demos/m365-agent)

## As a backend developer with a non-CS background, how do I learn about AI from scratch?

📹 [46:39](https://youtube.com/watch?v=LZLg_hQYk4I&t=2799)

Recommended approach:

1. Watch the Python + AI series from October (if you understand Python, it's at a good level)
2. Read the AI Engineering book by Chip Huyen
3. Build stuff - go back and forth between learning and doing

Links shared:

* [Python + AI series recap](https://techcommunity.microsoft.com/blog/educatordeveloperblog/level-up-your-python--ai-skills-with-our-complete-series/4464546)
* [Python + MCP series recap](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/learn-how-to-build-mcp-servers-with-python-and-azure/4479402)

## What's new with the RAG demo (azure-search-openai-demo) after the SharePoint data source was added?

📹 [49:50](https://youtube.com/watch?v=LZLg_hQYk4I&t=2990)

The main work is around improving ACL (Access Control List) support. The cloud ingestion feature was added recently, but it doesn't yet support ACLs. The team is working on making ACLs compatible with all features including:

* Cloud ingestion
* SharePoint Online document libraries
* ADLS (Azure Data Lake Storage Gen2)

A future feature idea: adding an MCP server to the RAG repo for internal documentation use cases, leveraging the Entra OBO flow for access control.

## Do you think companies will create internal MCP servers for AI apps to connect to?

📹 [53:53](https://youtube.com/watch?v=LZLg_hQYk4I&t=3233)

Yes, this is already happening quite a bit. Common use cases include:

* Internal documentation servers
* Data analytics access for non-developers
* Ticketing systems
* Debugging tools

A particularly valuable use case is data science/engineering teams creating MCP servers that enable less technical folks (marketing, PMs, bizdev) to pull data safely without needing to write SQL.

The pattern often starts with an engineer building an MCP server for themselves, sharing it with colleagues, adding features based on their needs, and growing from there.

Links shared:

* [Pragmatic Engineer: Building MCP servers in the real world](https://newsletter.pragmaticengineer.com/p/mcp-deepdive)
