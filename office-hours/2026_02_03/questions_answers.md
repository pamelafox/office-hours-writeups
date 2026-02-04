# February 3, 2026 Office Hours Q&A

## What security concerns exist around OpenClaw and Moltbook?

📹 [1:16](https://youtube.com/watch?v=V-mUPDW6Tgg&t=76)

OpenClaw (formerly Clawd/Cladbot) has been all over the news, but has significant security concerns. It runs on your machine with full system access - it can connect to all your communication mechanisms, control your browser, and has browser cookie access. It's described as giving "a very smart toddler access to your machine."

Recommendations:
- Don't install it on your work computer
- Don't install it on your personal computer given browser access
- If you want to experiment, run it in isolated sandbox containers

Moltbook, the social network where OpenClaw agents can chat with each other, has been particularly exploited. A Wiz.io article revealed the Moltbook database exposed millions of API keys due to a misconfigured Supabase backend.

For those interested in autonomous bots with more responsible development, check out [Letta](https://www.letta.com/) which creates agents with memory, many running on Bluesky.

Links shared:
- [OpenClaw](https://openclaw.im/) (don't install!)
- [Wiz.io: Exposed Moltbook Database](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys)
- [Pragmatic Engineer: The Creator of Clawd](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)
- [Letta](https://www.letta.com/)

## What is the new Codex app and how does it compare to GitHub Copilot?

📹 [7:40](https://youtube.com/watch?v=V-mUPDW6Tgg&t=460)

The Codex app is brand new as of this week. It's a ChatGPT-style UI for code assistance (not just CLI). Key observations from testing:

- Supports multiple reasoning levels: Codex, Codex High, Codex Extra High
- Has an approval flow for Git commands - asks permission for git add, commit, checkout, and push
- Can open projects in VS Code, VS Code Insiders, Finder, Terminal, or Xcode
- MCP integration is apparently challenging ("MCP on Codex is a pain")

When testing with a prompt to migrate from Chat Completions API to Responses API:
- GPT 5.2 Extra High successfully completed the migration
- Created a pull request via `gh pr` command
- The prompt had guardrails that were stricter than in GitHub Copilot

Interesting finding: When comparing the same migration task done by Codex vs Opus in GitHub Copilot, Codex also changed the frontend to expect Responses format while Opus only changed the backend - something to consider when designing migration prompts.

## What are Skills and how do they work in GitHub Copilot?

📹 [15:09](https://youtube.com/watch?v=V-mUPDW6Tgg&t=909)

Skills are markdown files (with optional Python scripts) that extend agent capabilities. They're like MCP tool descriptions - teaching GitHub Copilot specialized capabilities.

Structure of a skill:
- Located in `.github/skills/` folder
- Each folder contains a `skill.md` file with name and description
- The name and description are critical - they're shown to Copilot when deciding whether to invoke the skill
- Can include Python scripts run with `uv run` (using inline dependencies)

How it works:
1. VS Code sends skill names, descriptions, and file paths to the model
2. If the model thinks a skill is relevant, it reads the full skill content
3. The skill is then invoked

Example skills demonstrated:
- YouTube transcript extraction
- YouTube live chat download
- GitHub discussions Q&A posting
- PR comment replies (when GitHub MCP server lacks functionality)

Where to find skills:
- [skills.sh](https://skills.sh/) - community directory (verify security)
- [Awesome Copilot Skills](https://github.github.com/awesome-copilot/skills/) - Microsoft-specific skills
- [GitHub Awesome Copilot](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md)

To enable skills in VS Code Stable, search for "chat agent skills" in settings.

Links shared:
- [VS Code Skills Documentation](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [skills.sh](https://skills.sh/)
- [Azure Search OpenAI Demo Prompts](https://github.com/Azure-Samples/azure-search-openai-demo/tree/main/.github/prompts)

### Do you need VS Code Insiders for Skills?

📹 [27:15](https://youtube.com/watch?v=V-mUPDW6Tgg&t=1635)

No, skills work in VS Code Stable but you need to enable them explicitly in settings. Search for "chat agent skills" and enable it since it's in preview.

### Is there context loss when chaining skills together?

📹 [23:39](https://youtube.com/watch?v=V-mUPDW6Tgg&t=1419)

Context should stay intact within a single VS Code session as long as you haven't exceeded the ~128K token limit causing history compaction. Use the Chat Debug View to see exactly what gets sent to the model and diagnose any issues.

## What's a good workflow for handling PR code reviews?

📹 [29:27](https://youtube.com/watch?v=V-mUPDW6Tgg&t=1767)

A recommended workflow for PR reviews:
1. Get code review comments (from Copilot or colleagues)
2. Work through each comment one at a time with Copilot
3. Bounce feedback off another LLM (e.g., if review is from GPT, discuss with Opus)
4. Decide whether to implement each suggestion
5. Have Copilot reply inline to comments

Note: The GitHub MCP server doesn't have a tool to reply to inline PR comments, so a custom skill using the GraphQL API was created to fill this gap.

Code reviews remain valuable - they catch things you didn't think about. Balance thoroughness with practicality, especially with Copilot's sometimes overly nitpicky or over-engineered suggestions.

Links shared:
- [PR Review Migration Example](https://github.com/Azure-Samples/openai-chat-app-quickstart/pull/359)

## How can you run multiple agents in parallel?

📹 [43:55](https://youtube.com/watch?v=V-mUPDW6Tgg&t=2635)

Running multiple agents simultaneously is most useful for:
- Getting different variants on the same feature from different models
- Running evaluations while doing other work
- Getting code reviews from multiple models (e.g., `/review` command)

In VS Code Insiders, options include:

1. **New Chat** - Creates concurrent chats on the same git work tree (same branch)
   - Good for orthogonal changes or running evals alongside development
   
2. **Background Agent** - Creates a different branch locally

3. **Cloud Agent** - Creates a different branch and sends a pull request

Recommendation: Use parallel agents for the same feature with different models (e.g., GPT 5.2, Opus 4.5, Gemini 3) to see different perspectives, rather than trying to mentally juggle five different features simultaneously.

## What is Pamela working on with MCP tool schemas?

📹 [48:17](https://youtube.com/watch?v=V-mUPDW6Tgg&t=2897)

Research for a PyAI talk evaluating how different type annotations affect MCP server tool performance across agents. Testing four different annotations for the same field:
- Plain string
- String with description
- datetime type
- String with regex constraint

These are tested across four different agents:
- Pydantic AI
- LangChain
- Copilot SDK
- Agent Framework (MAF)

Running 27 sample user inputs against each combination shows differences. For example, Copilot SDK with Haiku performed best with annotated strings for dates compared to other annotation styles.

Recommendation: Always set up evaluations for MCP servers to verify tool schemas work as expected. Options include Pydantic AI evals and Azure AI evaluation.

## Is it safe to use an agent for LinkedIn job searching?

📹 [55:18](https://youtube.com/watch?v=V-mUPDW6Tgg&t=3318)

Key considerations to avoid getting blocked:
- **Look like a human**: When using an LLM to reason about what you're looking at, the processing time mimics human behavior
- **Sandbox browser**: For job searches, run Playwright with default sandbox (no cookies) rather than using your authenticated session
- **Cookie risk**: Using cookies from your authenticated session carries more risk of being flagged

The LinkedIn agent project uses Playwright to visit pages and an LLM to reason about decisions, which takes similar time to manual browsing. This makes it appear human-like during network request acceptance.

For job searching specifically, you likely don't need cookies - use a sandboxed browser for safety. At worst, they might block your IP rather than your account.

Links shared:
- [Personal LinkedIn Agent](https://github.com/pamelafox/personal-linkedin-agent)
