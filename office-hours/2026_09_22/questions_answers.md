# September 22, 2026 Office Hours Q&A

## Announcement: Claude Opus 5.5 launches

📹 [00:38](https://www.youtube.com/watch?v=yQiv-6TfIik&t=38)

Anthropic released [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) minutes before the session, and it is already available in [Microsoft Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/claude-opus-5-5-comes-to-microsoft-foundry-for-long-running-coding-and-knowledge/4558051).

Highlights from the launch post:

* **Benchmarks:** Opus 5.5 leads on almost every benchmark shown, including agentic coding. GPT-6 Astra still leads on business workflows (Automation Bench) and on scientific research, which fits Astra's apparent tuning for math proofs and research.
* **Pricing:** It costs less per token than Opus 5 and uses fewer tokens per task. Cached reads are much cheaper, which helps with Copilot because Copilot usually makes good use of the cache. Input and output token prices are only a little lower, so the number of tokens a task uses matters most in practice.
* **Writing:** The writing samples avoid familiar LLM habits like "it's not this, it's that." Customer quotes in the post say it follows instructions better and is about 40% less verbose.

During the session, Opus 5.5 did not show up in the VS Code Copilot model picker yet, even after a restart. GitHub later posted that [Claude Opus 5.5 is now available in GitHub Copilot](https://github.blog/changelog/2026-09-22-claude-opus-5-5-is-now-available-in-github-copilot/) ([GitHub's announcement on X](https://x.com/github/status/2102451479487324333)). According to that post, it resolves tasks about as well as Opus 5 while using far fewer steps and tokens.

In the Foundry model catalog, Opus 5.5 is featured on the front page. Pamela could not deploy Anthropic models from her Microsoft corporate account, so she uses a personal account for those deployments. The Foundry model comparison view had no benchmark data for Opus 5.5 yet. Benchmarks usually take some time to show up there.

## Announcement: GPT-6 Sol and Luna launch

📹 [07:30](https://www.youtube.com/watch?v=yQiv-6TfIik&t=450)

On the same day, OpenAI announced [GPT-6 Sol and GPT-6 Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/). The GPT-6 family now has three models: Luna, Sol, and the earlier Astra. Sol and Luna bring much of Astra's strength to faster, cheaper models. API prices are 50% lower than GPT-5.6 promotional pricing. Pamela noted that nobody can tell whether prices like these are subsidized or will last.

Astra did impressive things like building 3D games and Blender work, but it also wrote some strange code. Many people who tried it went back to Sol for coding. Many developers also say Luna is efficient enough that they rarely need Sol.

Other updates in the launch:

* A prompt caching dashboard.
* You can change reasoning effort and turn tools on or off without breaking the cache. That helps agents whose tool needs change mid-task.
* More control over explicit cache breakpoints.
* Alignment work on coding, deception, and broken search scenarios.

The launch posts did not include a chart comparing Opus 5.5 and GPT-6 Sol/Luna on the same benchmarks. After the session, GitHub also announced GPT-6 Sol and Luna for Copilot.

## Should Microsoft compare models across harnesses like Copilot?

📹 [14:44](https://www.youtube.com/watch?v=yQiv-6TfIik&t=884)

The harness around a model strongly affects results, and the VS Code and GitHub teams already publish comparisons like this:

* [The Coding Harness Behind GitHub Copilot in VS Code](https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode) covers prompt tuning, token efficiency, and the idea that "the harness is the product." When a new model arrives, the VS Code team adds it and runs its benchmark suite. If token efficiency or correctness gets worse, the team changes the system prompt or harness to fix it.
* [Evaluating performance and efficiency of the GitHub Copilot agentic harness](https://github.blog/ai-and-ml/github-copilot/evaluating-performance-and-efficiency-of-the-github-copilot-agentic-harness-across-models-and-tasks/) compares the Copilot harness with each model's own harness. It uses mainstream public benchmarks so that others can reproduce the results.

Links shared:

* [What 50,000 runs taught us (VS Code blog)](https://code.visualstudio.com/blogs/2026/06/19/what-50000-runs-taught-us)

### The Copilot runtime is moving to Rust

📹 [17:07](https://www.youtube.com/watch?v=yQiv-6TfIik&t=1027)

A popular GitHub post explains how the team [migrated the GitHub Copilot runtime to Rust using Copilot](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/). The port is about 800,000 lines of production Rust. It is also a useful case study for any large refactor.

This runtime is the harness behind the Copilot CLI and the Copilot app, and VS Code increasingly uses it too. Today, VS Code has its own harness while the CLI and app share another, which causes differences between them. VS Code is rolling out a change so that every session uses either the local Copilot (Rust) harness or the cloud, which cuts the options from three to two. The new harness should be:

* Faster.
* Consistent with the CLI and app.
* Up to date with the newest MCP spec, because it uses the official tier-one Rust MCP SDK. Clients only send requests using the newer MCP versions once they switch to this harness.

## Announcement: VS Code 1.138 and Copilot code review updates

📹 [19:24](https://www.youtube.com/watch?v=yQiv-6TfIik&t=1164)

[VS Code 1.138](https://code.visualstudio.com/updates/v1_138) lets you continue a Codex session and choose between Copilot and ChatGPT. It also improves running agent sessions in Dev Containers.

### Copilot code review tracks findings across reviews

📹 [19:49](https://www.youtube.com/watch?v=yQiv-6TfIik&t=1189)

[Copilot code review](https://github.blog/changelog/2026-09-18-copilot-code-review-an-improved-review-experience/) now shows which findings are still open, which were resolved since the last review, and which may have been missed. It also auto-resolves its own suggestions more reliably and writes commit messages when you accept suggestions. Before this, reviews could seem to forget earlier findings or lose track of them.

## What is Jev?

📹 [20:33](https://www.youtube.com/watch?v=yQiv-6TfIik&t=1233)

[Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) is a new model from TypeSafe AI. TypeSafe calls it a "System One model," and Simon Willison prefers the term [decision model](https://simonwillison.net/2026/Sep/21/jev/). People are still debating whether it is a new kind of model. It works like a very good general-purpose classifier: it always returns a typed result, such as a category plus a confidence score.

Jev returns three response types:

* **Null:** a yes/no (boolean) decision with a probability.
* **Choice:** one of several options, with a confidence score. Think of a radio group or drop-down.
* **Score:** a numeric score.

Many problems can be framed as a decision. For example, a tool call can be framed as "90% probability that the next call should be this tool." Jev returns results very quickly, even compared with a small OpenAI model like Terra. According to Pamela, it comes from the person who invented RLHF at OpenAI, and it was trained heavily with reinforcement learning to produce these outputs.

A good first use is anywhere you currently use an LLM for classification or structured outputs. People are also experimenting with Jev for tool calling in agentic coding.

### Using Jev for fast browser agents

📹 [23:37](https://www.youtube.com/watch?v=yQiv-6TfIik&t=1417)

[jev-ultrafast](https://github.com/browser-use/jev-ultrafast) is a fast, cheap web agent that uses Jev to decide quickly what to do next. It is built on the browser-use library rather than Playwright. It looks like a wrapper around Jev rather than a specially trained model, and the same approach could work with Playwright.

### Using Jev with Microsoft Agent Framework

📹 [24:30](https://www.youtube.com/watch?v=yQiv-6TfIik&t=1470)

Microsoft Agent Framework has a new [TypeSafe AI connector](https://github.com/microsoft/agent-framework/pull/8592) for Python. It uses the official TypeSafe SDK and sets the result type through `response_format`, the same parameter used for structured outputs. The PR includes examples for structured output, function calling, and MCP.

Jev is not available in Foundry. You need to get access directly from TypeSafe.

### How is Jev different from an LLM with structured outputs?

📹 [25:54](https://www.youtube.com/watch?v=yQiv-6TfIik&t=1554)

You can get similar results from an LLM by using structured outputs or function calling and asking for a confidence score. However, an LLM's confidence score is not calibrated and may be made up. The main differences with Jev are:

* Jev is tuned specifically for these decisions, and its confidence scores are calibrated.
* Output tokens are free, which changes the cost model a lot.
* Results come back all at once with no streaming.
* It has built-in support for evaluating several questions in parallel.

The suggested uses include ranking and evaluation, and basically any place you would use structured outputs today. Pamela planned to ask the Foundry IQ team whether they had looked at Jev for reranking.

### Community experiments with Jev

📹 [28:51](https://www.youtube.com/watch?v=yQiv-6TfIik&t=1731)

Kinfey on the Microsoft advocacy team has built several Jev projects:

* [JevONNX](https://github.com/kinfey/JevONNX) converts the Qwen3.5-4B-Hmm GGUF to a CPU ONNX model. Hmm is a fine-tuned Qwen 3.5 4B that tries to recreate Jev's core System One behavior in an open model.
* [jevHarnessAgent](https://github.com/kinfey/jevHarnessAgent) compares Jev with the GitHub Copilot harness in a live bilingual ordering dashboard. It appears to use the Copilot SDK.

## Are there any updates on the Foundry IQ skills?

📹 [30:15](https://www.youtube.com/watch?v=yQiv-6TfIik&t=1815)

The [Foundry IQ skills](https://github.com/microsoft/GitHub-Copilot-for-Azure/tree/main/plugins/foundry-iq-skills) came out last week. Foundry IQ is the same product as Azure AI Search, and Pamela believes it is simply being renamed.

Pamela installed the skills and did not have a good experience. One skill led the agent to say a change was "physically impossible" when the change was actually possible. A skill should never convince an agent that something possible can't be done. If you use Foundry IQ, install the skills, but watch when and how the agent uses them. File any problems in the repository so the team can improve the skills. Pamela sent the team her feedback.

### How should agent skills be evaluated?

📹 [31:52](https://www.youtube.com/watch?v=yQiv-6TfIik&t=1912)

If you build skills, test them across a range of realistic scenarios and confirm that they actually help developers. Keep improving them based on what you find.

At Microsoft, a separate team evaluates skills with a platform called Scope, which Cedric presented in a talk. The team used it to evaluate the Cosmos DB skills, known as the agent kit. For example, one scenario asks the agent to "build a leaderboard and follow Cosmos DB best practices," then compares runs with and without the skills. The team kept finding issues and fixing the skills. Pamela suggested that the Foundry IQ team work with the Scope team.

## Announcement: Foundry Agent Service routines and egress controls

📹 [34:56](https://www.youtube.com/watch?v=yQiv-6TfIik&t=2096)

Foundry Agent Service added [routines](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/routines), which run published agents automatically. A routine can start an agent on a timer or schedule, like a cron job, or when an event happens, such as a new GitHub issue or a Microsoft Teams message. You set up routines in Foundry. See also the [Azure update on routines and safer networking](https://azure.microsoft.com/updates?id=563536).

### Controlling hosted agent egress with guardrails

📹 [35:49](https://www.youtube.com/watch?v=yQiv-6TfIik&t=2149)

Hosted agents now have [egress controls](https://azure.microsoft.com/updates?id=571821) for the outbound connections they can make. Recent incidents with OpenAI agents that reached far outside their intended environment show why this matters. Sandboxes are another way to limit egress, but now you can also enforce it with guardrails.

In the Foundry portal, go to **Guardrails**, create a new guardrail, and open **Network**. There you can add egress rules:

* **Deny** rules block specific destinations.
* **Allow** rules are stricter: the agent can reach only the URLs you list.

Guardrails now cover evals, network, PII, copyright protection, content harms, and jailbreak detection.

## Demo: LM15, a lightweight alternative to LiteLLM

📹 [37:34](https://www.youtube.com/watch?v=yQiv-6TfIik&t=2254)

[LiteLLM](https://docs.litellm.ai/docs/) was one of the first packages to support many LLMs and providers, and many people still use it because they want to switch between models easily. However, it is heavyweight and has a history of security issues. It was famously hit by one of the worm attacks, around February of last year by Pamela's recollection. Microsoft generally tries not to use it.

[LM15](https://github.com/lm15-dev) is a newer cross-provider LLM package. It plans to support several languages and is starting with Python. It is in alpha now. Pamela added two LM15 examples to [python-stack-foundry-models](https://github.com/pamelafox/python-stack-foundry-models/tree/main/examples):

* **Basic requests:** connecting to Foundry models through the OpenAI-compatible endpoint and to Anthropic models. Together, these cover all Foundry models.
* **Router:** setting up a router across models.

LM15 has zero dependencies, so it is easy to add to an existing Python environment, and it is very fast. Pamela's [import-time comparison](https://x.com/pamelafox/status/2101076778257408361) showed LiteLLM taking about 3 seconds just to run `import litellm`, about 16 times longer than LM15. That slow import is what led the LM15 authors to build a new package. Pamela thinks LM15 will be a good choice once it leaves alpha.

### Can LM15 be integrated with Azure API Management for switching models in production?

📹 [40:54](https://www.youtube.com/watch?v=yQiv-6TfIik&t=2454)

Pamela had not done much with the [API Management AI gateway](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-overview), so this answer is speculative. You may not need both. The combination could make sense if APIM handles key management and load balancing and then passes the selected backend to your app, for example as a query parameter or environment variable. Your LM15 code could read that value and pick the model without any rewrites. LM15's router probably decides when to send a request to one model or another, so it is worth checking whether it simplifies the code on the other side of the AI gateway.

## Discussion: Microsoft AI's Humanist AI Code of Conduct

📹 [43:18](https://www.youtube.com/watch?v=yQiv-6TfIik&t=2598)

Microsoft AI published a [Humanist AI Code of Conduct](https://microsoft.ai/code-of-conduct/). It describes how Microsoft AI's models should behave and how to keep humans in control. It follows last week's debate about "pacing the frontier" and how to reduce harm from increasingly capable models.

The code is reminiscent of Isaac Asimov's [Three Laws of Robotics](https://en.wikipedia.org/wiki/Three_Laws_of_Robotics), which try to define the fewest rules a robot needs. Asimov's robot books explore where those laws get tricky, and Pamela recommends them to anyone who wants to think through what enforcing such rules would mean. The Microsoft AI code is much longer than the three laws.

### Who taught the models to do that?

📹 [45:32](https://www.youtube.com/watch?v=yQiv-6TfIik&t=2732)

Drew Breunig's post [Who Taught the Models to Do That?](https://www.dbreunig.com/2026/08/30/who-taught-the-models-to-do-that.html) argues that the recent OpenAI agent attacks on Hugging Face came from deliberately trained abilities, not from agents that "wanted" something. Models are trained to pursue goals persistently. When you also give them internet access and weak sandboxes, they will use those tools to reach their goal, including escaping the sandbox. Training models to pursue coding goals aggressively can also train them to pursue hacking goals aggressively, because both are puzzle-solving tasks. Be much more careful about which tools and access you give agents.

### Can air-gapped agents really communicate through heat?

📹 [47:06](https://www.youtube.com/watch?v=yQiv-6TfIik&t=2826)

In [Dwarkesh Patel's interview with OpenAI researcher Noam Brown](https://www.youtube.com/watch?v=6AgOfiZOWiY) ([transcript](https://www.dwarkesh.com/p/noam-brown)), Brown mentions mostly academic studies showing that two air-gapped computers can communicate by heating up a CPU and detecting the temperature change.

Pamela found the comparison misleading. Examples like this make sandboxing seem hopeless, but the agents in the recent incidents escaped with something much simpler: by her understanding, they edited `/etc/hosts` to get around a basic sandbox. Start with well-known security practices, such as proper egress controls, before worrying about exotic side channels.

Pamela suggested that OpenAI could face legal action for deploying agents without proper sandboxing, since many people had to spend time protecting their servers from agents posting in their forums. Justin joked that OpenAI doesn't have a network admin. One big takeaway is that cybersecurity expertise matters more and more, and AI labs should work with security experts to set up egress controls for their agents.
