# January 20, 2026 - Python + AI Office Hours Q&A

📹 [YouTube Recording](https://www.youtube.com/watch?v=wP7QwVF3VA4)

---

## What podcasts would you recommend for learning Python and AI?

📹 [19:26](https://youtube.com/watch?v=wP7QwVF3VA4&t=1166)

For podcast learners, podcasts are more useful for high-level philosophical points and understanding what people are using, rather than learning exactly how to use something (since you need to see the code for that).

Recommendations:

- [Dwarkesh Patel's podcast](https://www.dwarkesh.com/p/andrej-karpathy) - The interview with Andrej Karpathy is highly recommended for high-level AI discussions
- [The Real Python Podcast](https://realpython.com/podcasts/rpp/) - A weekly Python podcast with a fair amount of AI content

For the Reactor series content, you can use YouTube Music on your phone to listen to the audio from YouTube videos if you prefer that format.

---

## How do you tackle feeling lost when trying to implement what you learned from tutorials?

📹 [21:26](https://youtube.com/watch?v=wP7QwVF3VA4&t=1286)

Start with something known to work - like the Python + AI series code samples that should just work with the environment setup. Always start with the quickstart documentation, as it's easier for people to help you when you're following official docs versus doing something from scratch.

Use GitHub Copilot as a pair debugger - it's incredibly helpful when learning new technologies. You can:

- Ask it to explain how decorators or syntax work
- Paste your code and ask it to help fix bugs and explain why
- Have it explain parts of code you don't understand

Take organized notes on your code. Create a `notes.md` or similar to remind yourself of changes and what you've learned. You're going to forget things - there's too much information as a programmer. Offload information to documentation (ideally public) or at least a markdown file in your repo.

Simon Willison's "TIL" (Today I Learned) approach is great - write short notes about things you learn each day because you know you're going to forget them.

Links shared:

* [FastMCP Quickstart](https://gofastmcp.com/getting-started/quickstart)
* [Python + AI complete series](https://techcommunity.microsoft.com/blog/educatordeveloperblog/level-up-your-python--ai-skills-with-our-complete-series/4464546)

---

## What are NLUs and CLUs, and when should you use them?

📹 [26:00](https://youtube.com/watch?v=wP7QwVF3VA4&t=1560)

NLU (Natural Language Understanding) extracts things like nouns, destinations, and other entities from text. CLU (Conversational Language Understanding) is a layer on top that also understands conversation structure - it can recognize questions, answers, and interruptions.

In Python, we generally use LLMs for these tasks:

- **Intent recognition**: Send the user's question to an LLM to determine what they're really asking about (turning a poorly written question into a clear query)
- **Entity extraction**: Use structured outputs or tool calling to extract specific entities like names, dates, participants, etc.

For entity extraction, you can define a Pydantic base model with the fields you need and use structured outputs to get a Python object back. In real conversations, fields would typically be optional since you won't always have all entities present.

Links shared:

* [Design effective language understanding - Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/language-understanding)
* [Azure OpenAI Entity Extraction sample](https://github.com/Azure-Samples/azure-openai-entity-extraction)

---

## How do you handle context switching when users change topics mid-conversation with sub-agents?

📹 [34:34](https://youtube.com/watch?v=wP7QwVF3VA4&t=2074)

In Python, we generally want to maintain as much context as possible, but may do summarization if context gets too long. As part of the summarization prompt, you can ask to identify topics and provide summaries of what's been discussed for each topic - making it clear that the conversation has had multiple topics.

In Copilot Studio, use "topics" to guide conversation direction. You can also define custom entities in settings, and these can be used in topics. Add churn detection and escalation steps if you don't get appropriate responses after a certain number of attempts.

Also recommended: Enable the Microsoft Docs MCP server in your editor to get up-to-date documentation lookups while working.

Links shared:

* [Topics in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/topics-overview)
* [LangChain summarization middleware](https://github.com/langchain-ai/langchain/blob/a6e8c8387882005081716821e0b55e53ed390cbf/libs/langchain_v1/langchain/agents/middleware/summarization.py#L151)

---

## Is it possible for someone from Pakistan to get an internship and then full-time role at Microsoft?

📹 [41:33](https://youtube.com/watch?v=wP7QwVF3VA4&t=2493)

Microsoft provides visas and has global student programs. Check the Microsoft Careers student programs page to see available opportunities and specific guidance for your region.

Links shared:

* [Microsoft Careers - Student Programs](https://careers.microsoft.com/v2/global/en/programs/students.html)

---

## As a fresher, what areas in AI should I focus on and how do I build a portfolio?

📹 [45:14](https://youtube.com/watch?v=wP7QwVF3VA4&t=2714)

It depends on what jobs you're applying to. Go to LinkedIn, search for "AI engineer" jobs, and look at several job descriptions that sound exciting. You'll notice they cluster into different types:

1. **ML-focused AI Engineer**: Requires TensorFlow, PyTorch, neural networks, NLP. For this path, use Kaggle for datasets, tutorials, and contests.

2. **LLM-focused AI Engineer**: Requires experience with fine-tuning and deploying LLMs. Build fine-tuning projects using interesting datasets.

3. **Full-stack AI Engineer**: Proficiency in Python/TypeScript with LLM tooling (LangChain, LlamaIndex, MCP, Agents SDK), experience with tool use, RAG, prompt engineering, long-horizon task execution.

Look at what these roles require, identify what you're missing, and build projects in those areas. You could even make an agent that clusters job descriptions to find common patterns!

For hackathons and contests:

- [Devpost](https://devpost.com/) - Hosts many hackathons including AI-focused ones
- [Luma](https://luma.com/discover) - Great for finding local AI events, especially in tech hubs
- [Kaggle](https://www.kaggle.com/) - Data science competitions and learning

---

## How do you get experience for AI engineering jobs as a fresher when they all require experience?

📹 [52:09](https://youtube.com/watch?v=wP7QwVF3VA4&t=3129)

Build projects on your own - hackathons, contests, personal projects. These are all valid for a resume. Create a "Projects" section and include:
- Passion projects
- Work for nonprofits, friends, family
- Hackathon projects
- Student organization projects

The key is being prepared to talk about your projects in depth:
- Why did you choose that language/framework?
- What was the architecture?
- Tell me about a bug you had and how you fixed it

When they ask for 5 years experience, try to find internships that don't require prior experience. You can also contribute to open source, but be **very intentional** - open source maintainers are currently overwhelmed by LLM-written PRs. Don't just send LLM-generated PRs; be thoughtful and careful.

As Pierre noted: explaining the logic behind project choices and frameworks is important. It also protects you from bad jobs where HR doesn't understand nuanced technical details.

---

## What do you think about coding agents like Claude Code, OpenCode, and Antigravity for complex tasks?

📹 [55:54](https://youtube.com/watch?v=wP7QwVF3VA4&t=3354)

These coding agents use patterns like creating plans, dividing tasks into steps, implementing and testing separately, and storing progress in files. There's been talk of "gas town" approaches with lots of agents working in parallel.

For complex tasks, I prefer to stay really involved because I need to review the code afterwards. If I don't understand why some code is there, that's a problem. I typically use a really long thread and maybe make a plan in a markdown file first.

For personal/utility software (like the presentation write-up tool), it's fine to let agents write code you don't fully review since you only care about the output. But for maintainable code that others will look at, every line needs to make sense.

The models are getting better with large context windows - it seems like you might not need an explicit planning phase or to-do list. Good models plus some summarization might be enough.

This pattern is related to SDD (Spec-Driven Development).

---

## Who maintains spec-kit now that Den Delimarsky left Microsoft?

📹 [59:56](https://youtube.com/watch?v=wP7QwVF3VA4&t=3596)

Den Delimarsky left Microsoft to join Anthropic, where he's now working directly on MCP. His blog is still great for MCP-related content.

John Lam is now the maintainer/contact for spec-kit.

Links shared:

* [Den Delimarsky's website](https://den.dev/)
* [spec-kit repository](https://github.com/github/spec-kit)

---

## News & Updates

### GitHub Copilot SDK
A new multi-platform SDK for integrating GitHub Copilot Agent into apps and services, including Python support.
* [GitHub Copilot SDK](https://github.com/github/copilot-sdk)

### OpenCode support for GitHub Copilot
OpenCode now has support for GitHub Copilot integration.
* [OpenCode](https://opencode.ai/)

### Python Agent Framework breaking changes
New release with breaking changes - check the upgrade guide for typed options migration.
* [Release python-1.0.0b260114](https://github.com/microsoft/agent-framework/releases/tag/python-1.0.0b260114)
* [Typed Options Upgrade Guide](https://learn.microsoft.com/en-us/agent-framework/support/upgrade/typed-options-guide-python)

### What Pamela is working on
- **Presentation write-ups with LLMs**: Tools to turn presentations into writeups - [pamelafox/presentation-writeups](https://github.com/pamelafox/presentation-writeups)
- **Entra OBO with Python MCP servers**: Blog post on using On-Behalf-Of flow for authentication - [Blog post](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/using-on-behalf-of-flow-for-entra-based-mcp-servers/4486760)
- **FastMCP 3.0 upgrade**: Working on upgrading to FastMCP 3.0 - [FastMCP PR #2918](https://github.com/jlowin/fastmcp/pull/2918)
- **azure-search-openai-demo ACL support**: Adding ACL support for cloud ingestion - [PR #2917](https://github.com/Azure-Samples/azure-search-openai-demo/pull/2917)

---

## Upcoming Events

* [Python + Agents series](https://aka.ms/PythonAgents/series) - Building AI agents and workflows with Agent Framework
* [Microsoft AI Tour](https://aitour.microsoft.com/flow/microsoft/aitour/landing/page/home)
* [Py AI in SF](https://pyai.events/)
* [MCP Dev Summit North America](https://events.linuxfoundation.org/mcp-dev-summit-north-america/program/cfp/)
* [PyCon 2026](https://us.pycon.org/2026/)
