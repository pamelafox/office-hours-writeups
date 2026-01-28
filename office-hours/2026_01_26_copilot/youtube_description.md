We explored the GitHub Copilot CLI and GitHub Copilot SDK for Python, testing various features and discovering a few issues along the way.

Links:

- GitHub Copilot CLI: https://github.com/github/copilot-cli
- GitHub Copilot SDK: https://github.com/github/copilot-sdk
- CLI docs: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli
- Follow Evan Boyle for CLI updates: https://x.com/_Evan_Boyle
- SDK experiments branch: https://github.com/Azure-Samples/azure-search-openai-demo/compare/main...pamelafox:azure-search-openai-demo:sdkexperiments

Timestamps:
0:00 Intro - What we're exploring today
2:11 Installing/upgrading GitHub Copilot CLI
7:00 CLI updated to v0.0.395, staff mode, model selection
8:20 Using /review to review code changes
13:00 Multi-model review with Opus, Gemini, and GPT-5.2
16:06 Queueing prompts with Ctrl+D
18:01 Exploring CLI documentation and commands
19:30 Adding MCP servers (Ctrl+S doesn't work on Mac!)
24:30 Testing custom agents (/triagger)
26:00 Bug: Custom agents can't close issues despite tool permissions
29:47 Switching to the GitHub Copilot SDK
31:00 PR visualization example from cookbook
33:00 Fixing outdated SDK example code (types changed)
38:00 Bug: Event type enum comparison doesn't work with strings
42:00 PR visualization working - getting shamed for old PRs
45:50 Bug: Can't use Opus 4.5 model in SDK
49:00 Setting up MCP server with SDK
55:00 Bug: MCP servers need explicit tools=["*"] to work
58:00 Trying to use custom agent.md files with SDK
1:03:30 Bug: No factory method to load existing agents
1:06:00 Getting triagger agent to work with SDK
1:13:30 Successfully closing a stale issue via SDK
1:17:00 Pushing SDK examples to branch
1:18:30 Wrap-up and thoughts on agentic coding automation
