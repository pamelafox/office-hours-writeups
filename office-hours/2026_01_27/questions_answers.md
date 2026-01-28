# January 27, 2026 Office Hours Q&A

## What is MCP Apps support in VS Code?

📹 [0:13](https://youtube.com/watch?v=3nlMoKu2g3Q&t=13)

MCP Apps (previously known as MCP UI) is the first official MCP extension. While not technically part of the core Model Context Protocol, it is an official extension that allows MCP servers to pass down rich interfaces instead of just text or binary files. The idea is that sometimes you need richer interaction than just text—you want actual user interfaces. This appears to work via iframes where you pass down an iframe with width, height, etc.

This could be the future of the web—instead of going to websites, we might do everything through agentic chat interfaces (like Microsoft Copilot, Claude, ChatGPT) with rich interaction coming into the chat terminal using MCP Apps. Kent C. Dodds has a great talk called "The Future of User Interaction" discussing this vision.

Links shared:

* [MCP Apps Support in VS Code blog post](https://code.visualstudio.com/blogs/2026/01/26/mcp-apps-support)
* [MCP Apps Playground demo repo](https://github.com/digitarald/mcp-apps-playground)
* [MCP Apps API docs](https://modelcontextprotocol.github.io/ext-apps/api/)
* [Kent C. Dodds - The Future of User Interaction](https://www.youtube.com/watch?v=gDSIxIGYk-o)

### Will MCP Apps be available in Teams/Copilot?

📹 [1:35](https://youtube.com/watch?v=3nlMoKu2g3Q&t=95)

Unknown at this time. VS Code is the most feature-complete MCP client out there, which is why it often has support for new features immediately. Other clients, including Teams Copilot, tend to lag behind in MCP support. There may also be additional security considerations for Teams/Copilot, though if the apps are iframed, that should relieve many security concerns.

### Is there a Python version of MCP Apps?

📹 [3:12](https://youtube.com/watch?v=3nlMoKu2g3Q&t=192)

Not yet. The current [MCP Apps playground repository](https://github.com/digitarald/mcp-apps-playground) is JavaScript-based. A Python version would need to be created. The FastMCP SDK doesn't appear to have support for apps yet—no open issues were found for MCP App or MCP UI support.

**Update:** FastMCP maintainer Jeremiah Lowin [confirmed](https://x.com/jlowin/status/2016233530670362842) they've been waiting to see the spec and absolutely want to add support—currently doing design work on it.

## What's new in VS Code Insiders?

📹 [7:58](https://youtube.com/watch?v=3nlMoKu2g3Q&t=478)

Follow Pierce Boggan for the latest VS Code Insiders updates. Recent additions include:

* **Agent HQ**: New dedicated agent management UX with "Chat: Open Agent Sessions Window"
* **200K context**: More context available for conversations
* **100 tool calls per session**: Increased tool call limits
* **Anthropic message API support**: Better support for Opus models
* **Claude SDK integration**: Direct integration for Claude users
* **Switch agent tool**: Helps you realize when you might want to use a different custom agent
* **Reads outside workspace**: VS Code can now read files outside the workspace if you approve
* **Isolated terminal sandbox**: Terminal commands can run in a sandbox for better security

Links shared:

* [Pierce Boggan tweet about Agent HQ](https://x.com/pierceboggan/status/2015910443395776647)

## What is the GitHub Copilot SDK and CLI?

📹 [11:07](https://youtube.com/watch?v=3nlMoKu2g3Q&t=667)

The **GitHub Copilot SDK** is a programmatic way to access GitHub Copilot. Key benefits:

* No need to deploy models—use the models built into the SDK
* Works like an agent framework without any deployment required
* If you already use GitHub Copilot, you can use similar prompts
* Can connect to MCP servers
* Can set up custom agents and sub-agents

The limitation is that you're currently restricted in model selection (e.g., can't use Opus, only Sonnet).

The **GitHub Copilot CLI** requires the CLI to be installed. From the CLI you can:

* Pick a model
* See your MCP servers
* Use tools like Work IQ

For an example of using the SDK to analyze pull requests, see the write-up from the January 26 live stream.

Links shared:

* [GitHub Copilot SDK](https://github.com/github/copilot-sdk)
* [January 26 Copilot experiments writeup](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_01_26_copilot/writeup.md)

## What developer hackathons are coming up?

📹 [19:06](https://youtube.com/watch?v=3nlMoKu2g3Q&t=1146)

Two hackathons were mentioned:

1. **AI Dev Days Hackathon** - Hosted by Microsoft Reactor
2. **Agent League** - An esports-style approach with battles:
   * Creative Apps Battle
   * Reasoning Agents Battle
   * Enterprise Agents Battle

Links shared:

* [AI Dev Days Hackathon](https://developer.microsoft.com/en-us/reactor/events/26647/)
* [AI Dev Days Hackathon GitHub repo](https://github.com/Azure/AI-Dev-Days-Hackathon)
* [Agent League series](https://developer.microsoft.com/en-us/reactor/series/s-1638/)

## Is this a good place to ask about Microsoft Foundry SDK or Agent Framework SDK?

📹 [20:53](https://youtube.com/watch?v=3nlMoKu2g3Q&t=1253)

Yes, you can ask questions about these here. The upcoming Python + Agents series will be diving deep into the Agent Framework SDK (which sometimes wraps the Foundry SDK). If you haven't registered for the agent series yet, definitely do that—it will cover the basics and go deeper into Agent Framework.

Links shared:

* [Python + Agents series](https://developer.microsoft.com/en-us/reactor/series/S-1631/)

## Are you using Spec-Driven Development (SDD) or SpecKit to guide coding agents?

📹 [21:59](https://youtube.com/watch?v=3nlMoKu2g3Q&t=1319)

Pamela had not used SpecKit before. For bigger projects, her approach has been to either:

* Use **Plan mode** in VS Code first to think through details
* Have it write a document first before coding
* Use Nicholas C. Zakas's **persona-based approach** to software development:
  * Start with a user-facing PRD (Product Requirements Doc) that a product manager would write
  * Then have an architect define design/technical choices
  * Finally have the implementer turn that into code

SpecKit seems good if you really know what you want versus being more experimental. Den, the original creator of SpecKit, has moved to Anthropic, but there is a new maintainer.

**Update:** Pamela tried out SpecKit in a [livestream later that day](https://youtube.com/live/8PjRfFluB2g). It worked pretty well, but may not be as necessary with newer models and GitHub Copilot features.

Links shared:

* [Nicholas C. Zakas's persona-based approach](https://humanwhocodes.com/blog/2025/06/persona-based-approach-ai-assisted-programming/)
* [SpecKit](https://speckit.org/)
* [SpecKit GitHub](https://github.com/github/spec-kit)

## What's new with the RAG demo - ACL support?

📹 [25:30](https://youtube.com/watch?v=3nlMoKu2g3Q&t=1530)

A new release was just made for the azure-search-openai-demo repo adding **ACL (Access Control List) support** for the cloud ingestion pipeline. This enables document-level security filtering in Azure AI Search.

How it works:

1. Point the repo at an **Azure Data Lake Storage** account (blob storage with access controls on each blob)
2. Azure Functions process the blobs and look at their ACLs
3. ACLs are converted into OIDs (individual user Entra IDs) and group IDs
4. When indexing, the OIDs and groups are added to the search index
5. When searching, only results the user has permission to view are returned

AI Search has built-in understanding for ACLs. You set up fields for user IDs and group IDs, mark them as such, and enable access control enforcement on the index.

Links shared:

* [azure-search-openai-demo ACL release](https://github.com/Azure-Samples/azure-search-openai-demo/releases/tag/2026-01-27)

### Can the RAG repo support ACLs from other identity providers like Okta?

📹 [31:01](https://youtube.com/watch?v=3nlMoKu2g3Q&t=1861)

Yes, but it requires custom implementation. You would need to:

1. Fork the repo
2. Add support for Okta (or other IDP)
3. Forward the token
4. Extract the OID and groups from the OAuth token
5. Check those against the index

AI Search only has built-in support for Entra. For other IDPs, you'd implement it similarly to how the repo worked before the built-in Entra support was added—by passing along the token and checking permissions manually.

## Have you tried memory tools in GitHub Copilot?

📹 [36:16](https://youtube.com/watch?v=3nlMoKu2g3Q&t=2176)

Pamela has not used memory tools in GitHub Copilot, but recently experimented with memory in Microsoft Copilot. To save a memory, you need to cue it up with "remember" - for example, "remember to never call me Pam, only call me Pamela."

You can view saved memories in Settings > Personalization and Memories > Manage Save Memories. Without explicitly using "remember," it doesn't seem to save memories automatically despite many conversations.

For VS Code, there are MCP servers for memory, though it's unclear which ones work well.

## When should I use Foundry IQ knowledge bases vs MCP tools?

📹 [45:25](https://youtube.com/watch?v=3nlMoKu2g3Q&t=2725)

**Foundry IQ** (the new name for Azure AI Search capabilities in Azure AI Foundry) provides:

* **Knowledge sources**: Index-based (search index, blob, SharePoint) or remote (SharePoint without copying data, web, and MCP in private preview)
* **Knowledge bases**: An agentic engine that can connect to multiple knowledge sources, do query planning, answer synthesis, hybrid search with semantic ranking, and iteration

**MCP as a knowledge source** is in private preview. If you want to use something like Elastic's MCP server as a knowledge source in Foundry IQ, you could request access to the private preview.

Additionally, there is an MCP endpoint for knowledge bases—meaning that if you create a knowledge base in AI Search, you can use it as an MCP server.

Note on naming: Azure Search → Azure Cognitive Search → Azure AI Search → Foundry IQ. The underlying Bicep/ARM resources still use "search services."

## What tools do you use to automate developer workflows?

📹 [38:48](https://youtube.com/watch?v=3nlMoKu2g3Q&t=2328)

Several approaches are being used:

1. **GitHub Copilot Skills**: Custom tools that can be invoked by agents. Examples:
   * YouTube transcript grabber
   * Live chat transcript fetcher
   * Discussion commenter (posts Q&A to GitHub Discussions)

2. **Python scripts**: For more structured, repeatable workflows. These can call the same functionality as skills.

3. **AGENTS.md files**: Give hints about what skills to use

4. **Prompt files**: Suggested prompts for common workflows

The flexibility is notable—you can pick whatever form of programmatic manipulation you want: custom agents, skills with prompts, Python scripts, or agent frameworks. Different approaches suit different needs.

One interesting use case: converting presentations to writeups, including automatic slide-to-timestamp alignment (which LLMs handle surprisingly well).

Links shared:

* [Office hours writeups repo](https://github.com/pamelafox/office-hours-writeups)
* [Presentation writeups repo](https://github.com/pamelafox/presentation-writeups)

## What is Work IQ?

📹 [17:09](https://youtube.com/watch?v=3nlMoKu2g3Q&t=1029)

Work IQ is a new command line tool and MCP server from Microsoft. It has read-only access to your Outlook, email, and Teams. You can:

* Use it as a chat tool
* Use it as an MCP server in VS Code

Example uses:

* Check calendar events
* Summarize industry news from specific channels/timeframes

The read-only access limits some usefulness, but it's helpful for information retrieval.

Links shared:

* [Work IQ MCP GitHub](https://github.com/microsoft/work-iq-mcp)
