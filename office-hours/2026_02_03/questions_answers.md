# February 3, 2026 Office Hours Q&A

## What is OpenClaw and is it safe to install?

📹 [1:16](https://youtube.com/watch?v=V-mUPDW6Tgg&t=76)

OpenClaw (formerly known as Clawd/Cladbot) is a very powerful autonomous agent that has been all over the news. It runs on your machine, can connect to all your communication mechanisms, control your browser, and has full system access. Pamela has **not** installed it and recommends against it for security reasons — it's like giving a very smart toddler access to your machine.

If you must try it, run it in isolated sandbox containers rather than on your work or personal computer, since it has browser access and your browser is logged in with your cookies.

**Moltbook**, a related social network where OpenClaw agents can chat with each other, was not created by the same developer but has been heavily exploited. A Wiz.io analysis revealed that Moltbook's database exposed millions of API keys due to a misconfigured Supabase backend.

The creator of OpenClaw claims to run 5-10 agents simultaneously and says "code reviews are dead" for this workflow, replaced by architecture discussions. While interesting, this approach may only be appropriate for personal repos, not open source or shared codebases.

If you're interested in autonomous bots on social media, check out **Letta** instead — they build agents with long-term memory and operate more responsibly. Cameron, a developer advocate at Letta, runs several bots on Bluesky (Comind, Void, Grunk) that experiment with agent memory and learning.

Links shared:

* [OpenClaw](https://openclaw.im/)
* [Wiz.io: Hacking Moltbook - AI Social Network Reveals 1.5M API Keys](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys)
* [Pragmatic Engineer: The creator of Clawd - "I ship code I don't read"](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)
* [Letta](https://www.letta.com/)

## What is the new Codex app and how does it compare to VS Code Copilot?

📹 [7:40](https://youtube.com/watch?v=V-mUPDW6Tgg&t=460)

The **Codex app** is a brand-new (as of this week) web-based UI from OpenAI for coding tasks. It's similar to GitHub Copilot's chat interface but runs outside VS Code in a ChatGPT-like UI. It offers three reasoning levels: Codex, Codex High, and Codex Extra High. It can also open projects directly in VS Code, Finder, Terminal, or Xcode.

Pamela tested it live by pasting in her Chat Completions to Responses API migration prompt. Using GPT 5.2 with Extra High reasoning, Codex successfully migrated a simple chat app — though it was noticeably slow due to the high reasoning level.

One issue encountered: the migration prompt included guardrails saying "do not run git commands," which Codex followed very strictly (unlike GitHub Copilot, which ignored them). When asked to bypass the guardrails, Codex struggled, showing it enforces prompt-level guardrails more rigidly than Copilot.

Codex also has an explicit approval flow for git operations (git add, commit, checkout, push each require separate approval), which is more cautious than VS Code's approach.

On the news front, there were reports about OpenAI acquiring/acqui-hiring Cline, though Cline later clarified there was no acquisition — the situation was confusing.

Links shared:

* [Cline acqui-hire clarification](https://blog.kilo.ai/p/cline-just-acqui-hired)

## What are GitHub Copilot Skills and where can you find them?

📹 [15:07](https://youtube.com/watch?v=V-mUPDW6Tgg&t=907)

**Skills** are markdown files (with optional associated scripts) that teach GitHub Copilot new capabilities. A skill consists of a `SKILL.md` file with a name, description, and instructions. Think of it like an MCP tool description — the name and description determine when Copilot decides to use the skill.

Two directories for finding skills:

1. **[skills.sh](https://skills.sh/)** — A community-built directory, though you should vet skills for security
2. **[Awesome Copilot](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md)** — Microsoft-specific skills, with a [website version](https://github.github.com/awesome-copilot/skills/) for browsing

How skills work internally: VS Code only sends the skill **name** and **description** to the model initially. If the model decides a skill is relevant, it then reads the full `SKILL.md` file. This means putting effort into your name and description is crucial — similar to writing good MCP tool descriptions.

For Python-based skills, the recommendation is to use **uv** with inline script metadata to declare dependencies. This way each skill is standalone — no need to set up a full project. This follows the Python standard (PEP 723) for declaring dependencies in a single file.

Links shared:

* [skills.sh](https://skills.sh/)
* [Awesome Copilot skills list](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md)
* [Awesome Copilot skills website](https://github.github.com/awesome-copilot/skills/)
* [Using Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills)

### Is there context loss when chaining skills together?

📹 [23:39](https://youtube.com/watch?v=V-mUPDW6Tgg&t=1419)

A viewer noted context loss when skills invoke other skills. Pamela's take: within a single VS Code session, context should persist as long as you haven't exceeded the token limit (e.g., 128K). If you go over the context window, history compaction can cause context loss.

If you're experiencing unexpected context loss, use the **Chat Debug View** in VS Code to see exactly what's being sent to the model. This shows the full payload including transcripts, skill contents, and tool calls — invaluable for debugging what the model actually receives.

### Do you need VS Code Insiders to use skills?

📹 [27:13](https://youtube.com/watch?v=V-mUPDW6Tgg&t=1633)

No. Skills are available in **stable VS Code** as a preview feature. You do need to explicitly enable it by searching for "chat agent skills" in settings. You can also click the setting link directly from the VS Code documentation page.

### What's a practical use case for skills beyond documentation?

📹 [28:34](https://youtube.com/watch?v=V-mUPDW6Tgg&t=1714)

Pamela shared her PR comment reply workflow: when she gets code review comments on a pull request, she works through each comment one at a time with Copilot, deciding whether to implement the suggestion or not. Then she has Copilot reply inline to each comment.

The problem: the **GitHub MCP server** doesn't have a tool for replying to inline PR comments. So she created a skill that teaches Copilot to use the **GraphQL API** instead. This is a great use case for skills — filling gaps in existing MCP server functionality.

She also emphasized the value of getting code reviews from multiple sources. She typically gets Copilot reviews (which tend to use a GPT model) and then discusses the suggestions with a different model (like Opus) to get different perspectives. Sometimes she even bounces suggestions off a human colleague. Code reviews are important because they catch things you didn't think about, but there's a balance — Copilot can be overly critical and nitpicky, sometimes wanting to over-engineer things like exception handling.

Links shared:

* [azure-search-openai-demo prompts](https://github.com/Azure-Samples/azure-search-openai-demo/tree/main/.github/prompts)

## How did Codex compare to Opus for the same migration task?

📹 [32:08](https://youtube.com/watch?v=V-mUPDW6Tgg&t=1928)

After running the same Chat Completions → Responses API migration prompt on both **Codex (GPT 5.2 Extra High)** and **Opus**, interesting differences emerged:

* The **Codex version** changed both the backend AND the frontend to expect Responses API events
* The **Opus version** only changed the backend, leaving the frontend unchanged
* The frontend change was actually a good call — something worth considering for the prompt

This highlights the value of trying the same prompt across multiple models to get different perspectives and identify decisions you might not have considered.

Links shared:

* [Codex PR #359](https://github.com/Azure-Samples/openai-chat-app-quickstart/pull/359)
* [Opus PR #358](https://github.com/Azure-Samples/openai-chat-app-quickstart/pull/358)

## What's the best approach for running multiple agents in parallel?

📹 [43:55](https://youtube.com/watch?v=V-mUPDW6Tgg&t=2635)

The most practical use case for running agents in parallel isn't working on 5 different features simultaneously (too much cognitive load), but rather getting **different model perspectives on the same feature**. For example, run GPT 5.2, Opus 4.5, and Gemini 3 on the same task and compare results. The GitHub Copilot CLI's `/review` command already does this — getting reviews from multiple models at once.

In VS Code Insiders, you have three options:

1. **New Chat** — Creates a concurrent chat on the same git work tree/branch. Good for orthogonal changes that won't conflict, or for running evals alongside development
2. **Background Agent** — Creates a separate branch. Good when you want isolated git work trees
3. **Cloud Agent** — Also creates a separate branch and sends a pull request. Best for fully independent work

The key question is: do you want a clean PR? If you're doing a prototype/hobby project, stuff it all in. For a shared codebase with colleagues, keep PRs clean.

## How do MCP tool type annotations affect agent performance?

📹 [48:17](https://youtube.com/watch?v=V-mUPDW6Tgg&t=2897)

For an upcoming PyAI talk, Pamela is evaluating how different type annotations for MCP tool parameters affect agent performance. She tested four annotation styles for a date field:

1. **Plain string** — No additional info
2. **String with description** — Adds a text description
3. **datetime** — Uses Python's datetime type
4. **String with regex constraint** — Adds a format pattern

These were tested across **4 agent frameworks** (Pydantic AI, LangChain, Copilot SDK, Agent Framework) with **27 sample user inputs** and multiple models.

Results vary significantly by model and agent:
* **GPT 5.2** did well across all annotation styles (100% on date formatting)
* **Copilot SDK with Haiku** showed more variation — the **annotated string** performed best, while other approaches had lower success rates (e.g., 89% vs higher)

The takeaway: always set up evaluations for your MCP tool schemas. Different schemas can meaningfully impact how well agents handle your tools, and the best approach varies by model and framework. Pamela uses Pydantic AI evals but noted Azure AI Evaluation works as well.

## Is it safe to use a Playwright agent for LinkedIn job search?

📹 [55:16](https://youtube.com/watch?v=V-mUPDW6Tgg&t=3316)

A viewer asked about using automation for LinkedIn job search after seeing Pamela's LinkedIn agent project (which uses Playwright to accept network connection requests).

The key to not getting blocked: **look like a human**. Pamela's agent works because:

1. It uses an LLM to reason about each page/decision, which takes roughly the same time a human would take
2. It runs via her cookies in a local browser, making it indistinguishable from manual browsing

For job searching specifically, you likely **don't need cookies** — use Playwright's default sandboxed browser (no cookies). This is safer since:
* They can't tie the activity to your account as easily
* They might block your IP, but probably won't
* The LLM reasoning time still makes you look human

Advice: don't spam companies with applications. Use automation for more efficient searching, not mass applying.

Links shared:

* [Personal LinkedIn Agent](https://github.com/pamelafox/personal-linkedin-agent)
