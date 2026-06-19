## What's new with Foundry IQ after Build 2026?

📹 [1:18](https://youtube.com/watch?v=CsC5OnBudiA&t=78)

[Foundry IQ](https://devblogs.microsoft.com/foundry/build-smarter-agents-faster-with-foundry-iq/) (also known as Azure AI Search) got two big updates at Build 2026:

**Serverless tier** (in preview): Previously, Azure AI Search required a dedicated search instance with a minimum of around $200/month. The new serverless offering makes pricing far more reasonable for variable workloads and getting started. Billing isn't enabled yet, so it's just for trial use to give feedback right now.

**New knowledge sources**: You can now connect Foundry IQ to Work IQ, Fabric IQ, and Web IQ (via an MCP endpoint). Microsoft now has four "IQs", which are different retrieval mechanisms:

* **Foundry IQ** — the generic retrieval mechanism (Azure AI Search), connects to lots of sources
* **Web IQ** — an agent-optimized Bing search index (very limited access; requires a $10k/month minimum spend)
* **Fabric IQ** — query data from Microsoft Fabric using an ontology, or build a "data agent"
* **Work IQ** — checks your Teams chats, emails, and Microsoft 365 content

Foundry IQ knowledge bases are now GA, with [research showing up to 54% better recall](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-iq-improve-recall-by-up-to-54-with-knowledge-bases/4524852) from agentic knowledge bases.

To see this all in action step-by-step, check out [Build Lab 532](https://github.com/microsoft/Build26-LAB532-from-data-to-context-agent-ready-knowledge-with-foundry-iq/), which walks through making an agentic knowledge base and adding Web IQ, Fabric IQ, and Work IQ.

### Does the serverless tier include all the premium features like agentic retrieval?

📹 [2:53](https://youtube.com/watch?v=CsC5OnBudiA&t=173)

Based on the [current preview limits](https://learn.microsoft.com/en-us/azure/search/search-limits-quotas-capacity), it appears that essentially all the features are supported on serverless — including semantic ranker and agentic retrieval. The preview limits are around things like the number of indexes and objects you can have, not which features are available. The idea is for you to try out everything, but not move production workloads to it until billing is enabled.

## What's it like to use Claude Fable 5?

📹 [7:24](https://youtube.com/watch?v=CsC5OnBudiA&t=444)

[Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) is Anthropic's first Mythos-class model released for public use. Benchmarks look very strong (with the usual caveat that models often learn the benchmarks over time). Anthropic published a detailed system card and a separate risk report — they appear to have invested heavily in safety reinforcement learning.

It's already available in the VS Code Copilot model picker as "Fable 5", and there's a setting for "thinking effort" you can configure.

A test run against a long-running thread with lots of context cost **407 credits (~$4)** for a single request — quite expensive, roughly double the price of Claude Opus 4.8 ($10/1M input tokens, $50/1M output tokens). It was fast, but you wouldn't want to use Fable 5 for everything.

A practical pattern: use Fable 5 for planning at the start of a session (when context is low), then switch to a cheaper model for implementation. You can also save money by lowering the thinking effort and by choosing the 200k context window over the 1M one.

## How do you mitigate risks when agents access untrusted external content like Web IQ?

📹 [12:19](https://youtube.com/watch?v=CsC5OnBudiA&t=739)

This question connects to Simon Willison's ["lethal trifecta"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — the dangerous combination of:

1. Access to private data
2. Ability to externally communicate
3. Exposure to untrusted content

Web search results are a classic source of untrusted content (a web page could contain a jailbreak or prompt poisoning). If you also have any MCP server with write access, the agent can externally communicate, which is genuinely bad.

Note that the current Work IQ used by Foundry IQ apparently has write access (it can send email), so it has the ability to externally communicate. But even "just answering a question" is itself a form of external communication — a poisoned web result could cause the agent to communicate an incorrect answer to the user.

The recommended mitigation is **[Foundry guardrails](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails?tabs=python)**. You can build a custom guardrail in the portal and enable:

* **Jailbreak detection** (direct attacks)
* **Indirect prompt injection** (checks tool responses — e.g. from Web IQ / Foundry IQ — for injected instructions)
* **Content harms**
* **Protected materials** (if you care about that)
* **Groundedness** as a guardrail (increases latency since it runs LLM evaluators inline)

The other key recommendation is to set up [AI red teaming](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/run-ai-red-teaming-cloud?view=foundry&tabs=python#create-a-run-in-a-red-team). Foundry has an **indirect jailbreak** attack strategy specifically designed for this scenario — make a red teaming run that uses it to test your agent.

### Will you get logs of all detected events if guardrails are enabled?

📹 [17:21](https://youtube.com/watch?v=CsC5OnBudiA&t=1041)

It depends on which mode you choose:

**Block mode**: You get an actual content filter error back from the Azure OpenAI responses API. You can catch this in your code and decide how to handle it (e.g. log it, show a friendly message to the user). If you don't catch it, it shows up in your error log with a recognizable shape noting it's a content filter.

**Annotate mode**: No error is raised. Instead, the response contains content filter annotations (a `content_filter` block and a `prompt_filter` block in the JSON). You'd need to be much more diligent — set up a custom dashboard that looks at the annotations in your OpenTelemetry data (easy to enable if you're using Agent Framework).

Pamela typically recommends **block** mode, then reviewing what got blocked to check if it's being too aggressive. (Sometimes content filters are over-aggressive — e.g. medical questions getting blocked as "sexual" — so you may need to tune blocking levels based on your app's domain.)

If you want the agent to access potentially unsafe content but only detect issues (not block), use annotate mode and wrap your agent calls with code that checks the content filter results on every response. You then decide what to do based on the detection — log it, show a warning, etc. This works well for scenarios like having an agent scan internet content for usable solutions (then running results in an isolated VM/sandbox for analysis).

Note: The current [view annotations docs](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails?tabs=python#view-annotations) use the older chat completions API; the team will update them soon to use the responses API.

## What is the openclaw-dev repo, and where can it be deployed?

📹 [24:39](https://youtube.com/watch?v=CsC5OnBudiA&t=1479)

[OpenClaw Dev](https://github.com/microsoft/openclaw-dev) is an OpenClaw agent hosted in the cloud for development, testing, and single-tenant use cases. It runs on standard [Azure Container Apps](https://azure.microsoft.com/en-us/products/container-apps) — *not* on the new [Azure Container Apps Sandboxes](https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-container-apps-sandboxes-secure-infrastructure-for-agentic-wor/4524131) that were announced at Build for secure, ephemeral agentic compute. Moving claw-dev onto ACA Sandboxes is being worked on, but it's currently blocked by some managed identity issues.

Arun (a maintainer of openclaw-dev) confirmed he hasn't gotten claw-dev working on Dev Box yet and thinks there may be similar issues on a [Windows 365 Cloud PC](https://www.microsoft.com/en-us/windows-365). He will work on it.

A related and already-usable tool from the OpenClaw team is **[gogcli](https://github.com/openclaw/gogcli)** — a command-line tool for Google Workspace (Gmail, Calendar, etc.) that works well with GitHub Copilot. Pamela used it yesterday to schedule her kids' summer camps on Google Calendar via a [custom skill](https://gist.github.com/pamelafox/e8aca757c8492313f21a0a5c474daf05).

## Should I focus on ML/DL fundamentals first, or jump straight into AI engineering (RAG, agents, LLMs)?

📹 [30:28](https://youtube.com/watch?v=CsC5OnBudiA&t=1828)

At this point, **everyone needs AI engineering** — incorporating LLMs into your code is a baseline skill for software engineers, similar to how we all needed to know regular expressions. Think of an LLM as a supercharged regex: very good at patterns. Whether you're building backend apps or automation scripts, there will be times when reaching for an LLM is the right architectural choice.

A "dedicated AI engineer" is someone whose main focus is building AI-centric workflows. **ML engineering** is a deeper specialty — fine-tuning models, working with PyTorch, understanding the math and training process. Pamela considers herself an AI engineer, not an ML engineer.

There's significant overlap in **evaluation** though. Just like we all had to learn unit tests and integration tests, we now all need to run evals and red teaming. That requires thinking a bit like a data scientist — e.g. when a new LLM comes out, you need to evaluate whether to switch to it. Ideally organizations have data scientists to partner with on eval workflows, but every engineer benefits from this skill.

Mushroom Man summed it up well in chat: "ML is much deeper in the mathematics of AI models. AI engineering is using models to solve problems in enterprise environments."

Links shared:

* [Microsoft ML for Beginners](https://github.com/microsoft/ML-For-Beginners) (Pablo)
* [Azure Machine Learning docs](https://learn.microsoft.com/en-us/azure/machine-learning/?view=azureml-api-2) (Pablo)
* [Create machine learning models learning path](https://learn.microsoft.com/en-us/training/paths/create-machine-learn-models/) (Pablo)
* [Cameron R. Wolfe on Substack](https://substack.com/@cwolferesearch) — good ML content (Mushroom Man)

## Are there any voice evals besides manually calling the agent?

📹 [34:48](https://youtube.com/watch?v=CsC5OnBudiA&t=2088)

Two main options to look at:

**[τ²-bench (tau2-bench)](https://github.com/sierra-research/tau2-bench)** from Sierra — a benchmark for full-duplex voice agents on real-world domains (airline, retail, telecom, banking). It's focused on customer support agents, which may not map perfectly to a generic voice agent, but worth trying. Agent Framework has [some integration with τ²-bench](https://github.com/microsoft/agent-framework), but it doesn't appear to support the voice variant yet.

**[Foundry's Voice Live evaluation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-voice-live-evaluate)** — if you're using [Voice Live](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/voice-live) (which appears to wrap on top of the real-time models), there's a built-in evaluator. Your dataset is actually a wave file; it transcribes the audio and then runs the standard evaluators (intent resolution, task adherence, etc.) on the transcript.

Open question for the product team: does Voice Live support [GPT Realtime 2](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/realtime-2) yet, or does the documentation just need updating?

Pamela also followed up after the session: **Foundry evals does support `audio_data`** for multimodal content — see [Evaluate generative AI app — multimodal content (preview)](https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app#multimodal-content-preview). It's not supported for online evals yet, since it's unclear where to store the audio data.

## Do you have a course or roadmap for learning AI engineering?

📹 [42:39](https://youtube.com/watch?v=CsC5OnBudiA&t=2559)

Pamela's go-to link is her blog post [How I learn about generative AI](https://blog.pamelafox.org/2025/08/how-i-learn-about-generative-ai.html), which has a mix of ML and AI engineering resources. Highlights:

* **For ML engineering**: [Sebastian Raschka](https://sebastianraschka.com/) and [Andrej Karpathy](https://karpathy.ai/) are the two essentials.
* **For AI engineering**: [AI Engineering by Chip Huyen](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) is a great book.
* Plus the many Microsoft video series.

## Have you tried TurboQuant for vector search?

📹 [43:35](https://youtube.com/watch?v=CsC5OnBudiA&t=2615)

[TurboVec](https://github.com/RyanCodrai/turbovec) is a vector index built on TurboQuant, written in Rust with Python bindings. Notable features:

* No training step — supports online ingest, so you can add new data on the fly
* Filtering, hybrid results, dense rerank
* Framework integrations with LangChain, LlamaIndex, Haystack, Agno

The repo's comparisons are against FAISS, which is mostly in-memory only and not really intended for production. For Azure production workloads, you'll get good performance from Azure AI Search's HNSW implementation which already implements quantization and Matryoshka representation learning compression, or from DiskANN which is used by Cosmos DB and Azure Database for PostgreSQL.

## What's new with PostgreSQL on Azure?

📹 [48:00](https://youtube.com/watch?v=CsC5OnBudiA&t=2880)

A few things worth checking out from the [Build 2026 PostgreSQL roundup](https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-new-security-maintenance-and-analytics-features-for-postgresql-at-mic/4524559):

* **[pg_durable](https://github.com/microsoft/pg_durable)** — PostgreSQL in-database durable execution from the Microsoft team. See also the related [Durable Functions in PostgreSQL post](https://techcommunity.microsoft.com/blog/adforpostgresql/introducing-durable-functions-in-postgresql/4526821) and [duroxide](https://github.com/microsoft/duroxide).
* **BM25 / [pg_textsearch](https://github.com/timescale/pg_textsearch)** — Azure Postgres appears to now support BM25 via TimescaleDB's pg_textsearch extension (docs to be confirmed with the team).
* **[azure-postgresql-auth](https://pypi.org/project/azure-postgresql-auth/)** — automatic Entra token refresh library for Python. Quite helpful for managed-identity-based connections.


## Announcements

📹 [50:59](https://youtube.com/watch?v=CsC5OnBudiA&t=3059)

* **Build 2026 master list**: See [Matt Hansen's comprehensive list of every Build 2026 announcement](https://github.com/matthansen0/matts-build-2026-list).
* **7 new MAI models** (Thinking-1, Code, Voice…) — [details on microsoft.ai](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/). Try the new MAI code models in VS Code.
* **GitHub Copilot Desktop App** got updates — you can now make custom canvases for custom UIs. See the [May releases changelog](https://github.blog/changelog/2026-06-03-github-copilot-in-visual-studio-code-may-releases/).
* **GitHub Copilot billing → usage-based AI Credits**: AI credits are roughly equivalent to one cent each, so they can burn fast. The VS Code team is exploring a "low cost / efficiency mode" — comment on [issue #320470](https://github.com/microsoft/vscode/issues/320470) if you have ideas. Different models have very different token efficiency (e.g. Gemini 3.1 Pro is one of the least token-hungry).
* **[Agents League Hackathon](https://info.microsoft.com/Agents-League-Hackathon-Registration.html)** — ends June 14th, lots of prizes.
* **Upcoming events**:
  * [Posette](https://posetteconf.com/2026/) (virtual PostgreSQL conference) — June 16–18, 2026. Pamela will have a talk.
  * [AI Engineer World's Fair](https://ai.engineer/worldsfair) — June 30 – July 2, San Francisco.
  * [DjangoCon US](https://2026.djangocon.us) — August 24–28, Chicago.
* **Microsoft IQ live stream series** — planned for end of July, covering Foundry IQ, Work IQ, and Fabric IQ. Stay tuned.
