# Feb 10, 2026 Office Hours Q&A

## Announcement: New models available in GitHub Copilot and Foundry

📹 [0:00](https://youtube.com/watch?v=7LZ01lDzPIg&t=0)

This week was all about new models! Several have been released:

**Claude Opus 4.6** (and Opus 4.6 Fast):

- Available in VS Code Copilot
- General feedback: it's a good model, but feels like a slight incremental improvement over 4.5 (which was "game-changing")
- **Heads up**: Opus 4.6 is reportedly a "token hog" - even if it's better or faster, your token usage may go up. If you're paying by token, consider whether the improvement is worth the cost.

**GPT-5.3 Codex**:

- Now generally available for GitHub Copilot
- Available in VS Code already
- Not yet available in Azure Foundry (still waiting for 5.3 Codex there)

**Claude Code and Codex agents**:

- You can now use Claude Code or OpenAI Codex as agents directly in VS Code
- If you like those tools but also like VS Code, you can get the best of both worlds

**Kimmy K2.5**:

- Available on Foundry
- Known for being fast

**DeepSeek 3.2 Special**:

- A "high compute variant" that used reinforcement learning
- Claims reasoning on par with Gemini 3.0

Links shared:

- [GPT-5.3 Codex changelog](https://github.blog/changelog/2026-02-09-gpt-5-3-codex-is-now-generally-available-for-github-copilot/)

## How does the new GitHub Copilot agentic memory feature work?

📹 [6:36](https://youtube.com/watch?v=7LZ01lDzPIg&t=396)

GitHub Copilot now has an agentic memory feature in public preview. Here's how it works:

- **Enable memory** in your personal Copilot settings under Features → Memory
- **Repository-level memories** can be viewed and managed in repository settings under Copilot → Memory
- **Memory sources**: Copilot stores memories from code review sessions, coding agent interactions, and Copilot CLI usage
- **Where it's used**: Currently used by Copilot coding agent, Copilot code review, and Copilot CLI (and in VS Code as a *preview* feature, enabled in settings)

The memories are very specific facts about the codebase that Copilot learned. You can view them, delete individual memories, and the system helps avoid repeated feedback in code reviews (e.g., "I already told you this doesn't matter because...").

For deeper understanding, GitHub published an engineering blog post explaining how the memory system is implemented - useful both for understanding Copilot and for inspiration when building memory into your own agents.

Links shared:

- [Agentic memory for GitHub Copilot changelog](https://github.blog/changelog/2026-01-15-agentic-memory-for-github-copilot-is-in-public-preview/)
- [Building an agentic memory system for GitHub Copilot (engineering blog)](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)
- [About agentic memory for GitHub Copilot (docs)](https://docs.github.com/en/copilot/concepts/agents/copilot-memory)

### Does VS Code Copilot have memory support?

📹 [10:10](https://youtube.com/watch?v=7LZ01lDzPIg&t=610)

Yes! VS Code Copilot does have memory support, though it was only recently added and the documentation is catching up.

To enable it:

1. Go to VS Code settings
2. Look for the memory boolean setting and enable it
3. Once enabled, you'll see a new "Memory" tool available

To trigger memory storage, you can say "Remember that..." (e.g., "Remember that we always prefer sentence case for markdown headings in this repo").

**Important notes:**

- Memories are stored at the repository level (on GitHub)
- If you're working on a fork, memories get stored on your fork, not upstream - which may not be what you want for shared codebases
- Some memories are "institutional knowledge" (should be shared), some are private - this is a design challenge

Links shared:

- [VS Code January 2026 release notes - Copilot Memory](https://code.visualstudio.com/updates/v1_109#_copilot-memory-preview)


## Can I use Work IQ as an MCP server in VS Code?

📹 [14:37](https://youtube.com/watch?v=7LZ01lDzPIg&t=877)

Yes! If you have Work IQ working in Copilot CLI, you can add it to VS Code as an MCP server.

**Setup steps:**

1. Add a new MCP server in VS Code
2. Set it as a "command" server type
3. Command: `workiq`
4. Args: `mcp`
5. Save it globally (or per-workspace)

Work IQ is a standard input/output MCP server (runs locally), so you need it installed on your machine. Once configured, you can run `workiq ask` for a direct ask interface, or `workiq mcp` to start the MCP server.

**What Work IQ can access (read-only):**

- Calendar
- Email
- Teams chats
- SharePoint
- Online meeting transcripts
- People/contacts
- Channel messages

**Caveats:**

- Sometimes Copilot doesn't automatically choose to use the MCP server - you may need to explicitly prompt it (e.g., "use Work IQ MCP to find...")
- **Low recall issues**: Searching Teams chats is difficult because they're unstructured and long - Work IQ may not retrieve enough information to fully answer questions
- **No write operations**: Work IQ only has read access, but sometimes hallucinates that it can perform write operations

## What is Agentic DevOps on GitHub Copilot?

📹 [29:16](https://youtube.com/watch?v=7LZ01lDzPIg&t=1756)

"Agentic DevOps" refers to using AI agents (like GitHub Copilot) to automate parts of your development workflow. Here are practical examples:

**Assigning issues to Copilot:**

- For "boring" tasks you don't want to do, just assign the issue to Copilot
- Copilot creates a PR, you review and merge
- About a fifth of PRs in some repos are now authored by Copilot (entirely in the cloud)

**Using Plan Mode for complex tasks:**

- Use VS Code's plan mode to have Copilot analyze open PRs
- Ask: "Look at all open PRs, figure out which are obsolete, which can be merged, which need new PRs, which can be done in parallel"
- Copilot uses sub-agents to research all open PRs and CI failures
- It generates a plan you can file as an issue for your team
- The plan can then be assigned to different types of agents (local, background, cloud, CLI)

**Requirements for success:**

- Still requires supervision and "context engineering"
- Invest time in a good `AGENTS.md` file
- Configure appropriate settings and MCP servers
- Ensure Copilot has access to everything it needs (tests, documentation, etc.)

Links shared:

- [Agentic DevOps blog post](https://azure.microsoft.com/en-us/blog/agentic-devops-evolving-software-development-with-github-copilot-and-microsoft-azure/)
- [Video about sub-agents](https://youtu.be/GMAoTeD9siU)

## How do I connect Atlassian MCP to Azure Foundry?

📹 [36:11](https://youtube.com/watch?v=7LZ01lDzPIg&t=2171)

A community member asked about adding Atlassian's Rovo MCP Server to Azure AI Foundry agents, but kept getting 401 Unauthorized errors.

**The issue:** Azure Foundry currently only supports static bearer tokens and not complete OAuth flows, which Atlassian requires.

**Suggestions:**

- Check the MCP channel in Discord for ongoing discussions about this
- Reach out to **Liam Hampton**, who has connections to Atlassian and is working on MCP integrations

Links shared:

- [Microsoft Learn Q&A thread about Atlassian MCP issue](https://learn.microsoft.com/en-us/answers/questions/5699976/unable-to-connect-atlassian-rovo-mcp-server-from-a)

## How do I work through PR review comments in VS Code?

📹 [38:57](https://youtube.com/watch?v=7LZ01lDzPIg&t=2337)

When Copilot creates a PR and the code review completes, you may want to work through the review comments in VS Code. Here's a workflow:

1. Add a review prompt ([`review_pr.prompt.md`](https://gist.github.com/pamelafox/d7aff2ba68d96ee5993bb84b2341c3c8)) that tells Copilot to fetch PR comments
2. If Copilot says there are no comments when you know there are, push back: "No, you're wrong. There are definitely comments from Copilot". Sometimes you need to say "those are old comments" or be more specific
3. Copilot fetches and displays an overview of all comments
4. Copilot displays each comment one at a time, with its suggested change and reasoning
5. For each comment, tell Copilot: accept, iterate, or reject
6. Copilot can also reply and resolve to the inline PR comments, thanks to instructions in that prompt file. Instructions are needed since GitHub MCP server doesn't support this yet - you need to use the API endpoint or GitHub CLI.

## Can I transfer a Copilot session context to a different workspace?

📹 [42:30](https://youtube.com/watch?v=7LZ01lDzPIg&t=2550)

A community member asked about opening a workspace, having Copilot understand it, then transferring that knowledge to a different workspace (like resuming a session in a different repo).

**The answer:** While VS Code Copilot doesn't have this built-in, you can build it yourself using the **GitHub Copilot SDK**.

The Copilot SDK lets you:

- Start a copilot session programmatically
- Create sessions with specific models (including multimodal)
- Send messages with attachments
- Build skills that extend Copilot's functionality

**Example use case shared:** Creating a skill that extracts text from PDF images using the Copilot SDK with a multimodal model, because Copilot wasn't sending repo images as attachments (now fixed).

**Key insight:** Everything is just a series of messages. If you extract those messages using the SDK, you can create a new thread/session in a different repo with the same context. The Agent Framework demonstrates this pattern with their "thread example" - create a thread from existing messages, then run a new agent with that thread.

Links shared:

- [Agent Framework thread example](https://github.com/microsoft/agent-framework/blob/main/python/samples/concepts/threads/thread_with_messages.py)

## Tip: use prek as a faster alternative to pre-commit

📹 [48:24](https://youtube.com/watch?v=7LZ01lDzPIg&t=2904)

[prek](https://prek.j178.dev/) is a "better pre-commit alternative, re-engineered in Rust" - a faster alternative to the popular pre-commit framework.

**Key features:**

- Fully compatible with existing `.pre-commit-config.yaml` files
- Much faster than pre-commit (thanks to Rust)
- Has a cute crab mascot (following the Rust tradition)

**Who's using it:**

- [Agent Framework](https://github.com/microsoft/agent-framework/blob/main/python/.pre-commit-config.yaml) (Microsoft)
- FastMCP
- Ty (type checker)
- Various other projects

The discovery led to an "Agentic DevOps" discussion about programmatically creating issues across multiple repos to migrate them from pre-commit to prek.

Links shared:

- [prek website](https://prek.j178.dev/)
- [Agent Framework pre-commit config](https://github.com/microsoft/agent-framework/blob/main/python/.pre-commit-config.yaml)

## Announcements

📹 [47:27](https://youtube.com/watch?v=7LZ01lDzPIg&t=2847)

**Product updates:**

- GitHub Copilot in VS Code: Opus 4.6 (/Fast) and GPT-5.3 models available
- Claude Code and Codex agents available
- Optional memory feature now in public preview

**Articles discussed:**

- ["AI Doesn't Reduce Work—It Intensifies It"](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it) (Harvard Business Review) - Curious if others are experiencing this
- ["Where is AI Taking Us?"](https://www.nytimes.com/interactive/2026/02/02/opinion/ai-future-leading-thinkers-survey.html) (New York Times) - Survey of leading thinkers on AI's future

**Upcoming events:**

- [Python + Agents series](https://aka.ms/PythonAgents/series) - Building AI agents with Agent Framework
- [Microsoft AI Tour](https://aitour.microsoft.com/) - Going around different cities
- [PyAI in San Francisco](https://pyai.events/) - March 2026
- MVP Summit in Redmond - March 2026
- [MCP Dev Summit North America](https://events.linuxfoundation.org/mcp-dev-summit-north-america/) - April 2-3, 2026 in New York City
- [PyCon US 2026](https://us.pycon.org/2026/) - May in Long Beach
- Microsoft Build - Coming soon after PyCon

**Extensions mentioned:**

- AI Foundry extension and AI Toolkit extension for VS Code - Both have model catalogs, playgrounds, and deployment features. (They may eventually merge as they're quite similar.) AI Toolkit includes evaluation and tracing features.
