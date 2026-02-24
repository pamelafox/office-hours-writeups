🐍 This week's Python + AI Office Hours was full of great questions and announcements!

Topics we covered:

🤖 Claude Sonnet 4.6 is here: Now available in Azure Foundry and rolling out to GitHub Copilot today. It has a 1 million token context window, excels at financial analysis and long-horizon planning, and is cheaper and faster than Opus 4.6.

🌐 WebMCP early preview: A new standard co-authored by Google and Microsoft that lets websites expose themselves as MCP servers - so agents can interact with them through structured tools instead of fragile browser automation.

🧩 Agent skills vs. system prompts: Skills are modular and lazy-loaded - only the front matter is sent to the LLM on every request, and the full content is fetched on demand. Great for reusable capabilities across multiple prompts. Keep your AGENTS.md minimal - research shows LLM-generated files that are too long actually hurt agent performance!

⚙️ GitHub Agentic Workflows: A new preview feature that lets you define repo automations in a markdown file (with front matter for guard rails) instead of writing full GitHub Actions YAML. Start with low-risk outputs like comments and drafts.

🔧 When to build a custom agent: Start with the lightest weight option - prompt, then skill, then agentic workflow, then Copilot SDK, then Agent Framework. Only reach for more complexity when you hit the limits of the simpler approach.

Also discussed: use cases for Microsoft Agent Framework, mixed-media RAG reranking, online evals for Agent Framework agents, and Foundry Hosted Agents infrastructure.

Join us live every week: http://aka.ms/pythonai/oh

See the recording and questions here:
https://github.com/orgs/microsoft-foundry/discussions/280

#Python #AI #GenerativeAI #MCP #AgentFramework #GitHubCopilot
