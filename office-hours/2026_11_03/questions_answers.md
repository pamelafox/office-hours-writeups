# November 3, 2026 Office Hours Q&A

## Announcement: Azure OpenAI now has the Decisions API

📹 [0:31](https://youtube.com/watch?v=6Vu0_W1OzWk&t=31)

The [Decisions API is now available in Azure OpenAI](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/decisions?tabs=python), after previously being available only from openai.com. It is based on the GPT-6 Luna model, so it is multimodal and has a 1 million token context window. A [pull request in azure-openai-starter](https://github.com/Azure-Samples/azure-openai-starter/pull/20/changes) adds Decisions samples across multiple languages.

The Python sample connects to the Azure OpenAI `/openai/v1` endpoint with the OpenAI client, using either keyless authentication with `DefaultAzureCredential` or an API key. It then calls the client to create a decision from a user input (optionally with a photo) and a set of questions. In the demo, the input "I was charged twice for order 123" returned answers for whether a refund was requested, which department should handle it, and the severity. Each answer comes back with a value and a confidence, which is how decision models work. Pamela gave feedback that the sample is confusing because it tries to do too many things at once.

There are now two decision model options in Foundry:

* **[Microsoft Decision-1](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/):** Smaller context window and not multimodal, but it might be faster, and its listed token pricing looked much cheaper.
* **Azure OpenAI Decisions API:** Choose it when you need the longer context or multimodal input. Its pricing appeared to match [GPT-6 Luna pricing](https://azure.microsoft.com/en-us/pricing/details/azure-openai/), since the pricing page had no separate Decisions entry.

Decision models are useful for routing, classification, and judge-style evaluation, as long as you calibrate them and verify that they work well for your task.

## Announcement: GitHub Universe brings GitHub Copilot Fusion

📹 [5:46](https://youtube.com/watch?v=6Vu0_W1OzWk&t=346)

[GitHub Universe](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) had a modest number of announcements. One is [Copilot Fusion](https://docs.github.com/en/copilot/concepts/models/copilot-fusion), previously called Hydrafusion. Instead of sending a task straight to a single model, a router model inspects the task and chooses an execution pattern: single, cascade, or critique. The [Project Hydrafusion blog post](https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/) has a helpful visualization of that flow. Fusion is available wherever you use GitHub Copilot.

### Does GitHub Copilot Fusion conflict with existing agent skills or instructions that do orchestration?

📹 [12:05](https://youtube.com/watch?v=6Vu0_W1OzWk&t=725)

Fusion combines picking the right model with picking the right orchestration. It is aimed at the many people who have not set up their own orchestration. If you already have custom orchestration (such as a coordinator with subagents) and it works well, you probably don't need Fusion.

## Announcement: GitHub Copilot app projects for cross-repo work

📹 [7:12](https://youtube.com/watch?v=6Vu0_W1OzWk&t=432)

[Projects are new in the GitHub Copilot app](https://github.blog/changelog/2026-10-28-github-copilot-app-universe-releases/). They turn a goal into coordinated work, running parallel sessions across repos while keeping context and results together. That makes them most useful for cross-repo and multi-session work.

### Demo: Running cross-repo projects

📹 [7:43](https://youtube.com/watch?v=6Vu0_W1OzWk&t=463)

Good fits for projects include upgrading many repos (such as moving to Python 3.11), checking whether data shared across several repos is in sync, and exploring multiple website redesigns in parallel. Tips from the demo:

* **Ask for child sessions explicitly.** The agent may do all the work in one session instead. A prompt like "can you do it in child sessions?" gives you the project overview, where you can follow the parallel work and dig into each child session. Whether it splits the work on its own may depend on the model.
* **Check permissions first.** Child sessions can fail with errors like "this session is not allowed to write files." Review the app's tool permission settings, and switch sessions to autopilot if you want them to run without approvals.

## Announcement: GitHub Copilot automations are easier to create

📹 [14:16](https://youtube.com/watch?v=6Vu0_W1OzWk&t=856)

[Copilot automations](https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-automations) run Copilot cloud agent automatically on a schedule, in response to repository events, or via the API. They are now much easier to create. You can manage them from the repository's **Agents** tab, the Copilot app, the VS Code Agents window, or the REST API. See [Using automations in the GitHub Copilot app](https://docs.github.com/en/copilot/how-tos/github-copilot-app/using-automations) for setup steps, including the prerequisites for cloud automations.

### Demo: Creating automations in the GitHub Copilot app

📹 [14:25](https://youtube.com/watch?v=6Vu0_W1OzWk&t=865)

Describe what you want, such as "every day at 10 p.m., check daily issues for this repo," select the repo, and an LLM writes a more formal automation definition with an appropriate trigger.

**Create manually** is a great way to discover all the available triggers. Besides schedules, triggers include new issues, automation failures, code scanning alerts, Dependabot alerts, discussion comments, pull requests, secrets, and GitHub Actions workflow completions. You can also add multiple triggers to one automation. Most trigger types can run in the cloud (Dependabot alerts default to cloud), which means they run even when your machine is off. For automations that are useful to everyone on a repo, run them in the cloud.

### Can the cron trigger switch to a webhook?

📹 [17:30](https://youtube.com/watch?v=6Vu0_W1OzWk&t=1050)

The cron trigger accepts standard cron syntax, but it did not offer the cloud option, so it presumably only runs locally. The daily, weekly, and hourly triggers can run in the cloud. There is no generic webhook trigger, so arbitrary non-GitHub webhooks are not supported right now. The GitHub-specific triggers may correspond to GitHub webhooks. Pamela planned to file a feature request with the app team.

### Are automations a parallel mechanism to GitHub Agentic Workflows?

📹 [19:15](https://youtube.com/watch?v=6Vu0_W1OzWk&t=1155)

[GitHub Agentic Workflows](https://github.github.com/gh-aw/) are still supported, but the lines are blurring because you can build similar things with automations. Automations have a much lower barrier to entry, so try them first. Move to Agentic Workflows when you need more control and complexity. Agentic Workflows are also checked into your repo, so you can reason about them and code review them, which makes them more team-friendly when a repo has multiple team members.

### Does GitHub Copilot support the MCP events spec?

📹 [20:51](https://youtube.com/watch?v=6Vu0_W1OzWk&t=1251)

Almost certainly not yet. Justin noted that events work really well in Codex with the beta spec from the [MCP Tasks and Events working group](https://modelcontextprotocol.io/community/working-groups/tasks-events). Pamela pinged the GitHub Copilot MCP team to request support.

### Why are GitHub Actions cron triggers running hours late?

📹 [23:39](https://youtube.com/watch?v=6Vu0_W1OzWk&t=1419)

GitHub Actions scheduled workflows use a different mechanism from Copilot automations ([events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)). Nnamdi reported cron triggers running 4–5 hours late. The default time zone is UTC, so rule out time zone confusion first. Adam had seen recent improvements, though cron triggers were unreliable for him 1–2 months earlier.

The [GitHub Community discussions](https://github.com/orgs/community/discussions) site is the place for product feedback and ideas. A [discussion about scheduled runs starting 3–6.5 hours late](https://github.com/orgs/community/discussions/211921) matches this issue. If you're affected, add more details to the discussion.

### How do shared automations work?

📹 [27:09](https://youtube.com/watch?v=6Vu0_W1OzWk&t=1629)

Teams can now [share Copilot automations](https://github.blog/changelog/2026-10-28-build-shared-workflows-for-your-team-with-copilot-automations/). Shared automations are visible to the team, belong to the repository owner, and act as Copilot so their actions are attributed to Copilot. Choose **Shared** under **Type** when creating the automation. The shared option is only available when the automation runs in the cloud. It's unclear whether you can change an existing automation to shared afterward.

Automations can also be run via an API, and you can set AI credit limits to create a budget for each automation. Justin liked the credit limits, since some friends have automations that drain their credits. Shared automations appear in the repository's **Agents** tab under **Automations**, where everyone with access to the repo can see their runs.

## Discussion: GitHub Copilot cloud agents have improved

📹 [32:00](https://youtube.com/watch?v=6Vu0_W1OzWk&t=1920)

GitHub Copilot cloud agents have gotten much better. The Copilot tab in the GitHub mobile app can start sessions that are tied to a repo, or not tied to any repo for arbitrary work. Once you're back at a computer, those sessions show up at [github.com/copilot](https://github.com/copilot), where you can resume them and keep chatting.

Cloud agents give you portability across devices, and sessions started from Copilot in Teams or Slack become shared sessions that anyone in that conversation can see. They take a bit more setup, such as configuring MCP servers, and you can't yet configure the base image, but that should improve over time.

## Announcement: VS Code now uses the Microsoft Copilot harness

📹 [35:07](https://youtube.com/watch?v=6Vu0_W1OzWk&t=2107)

[VS Code now defaults to the Copilot harness](https://code.visualstudio.com/updates/v1_144) rather than its older local harness. Previously, VS Code and the Copilot app and CLI used different harnesses, so the same task could give different results, and maintaining both harnesses duplicated engineering work. VS Code is deprecating its old harness. Some features of the old harness are not supported in the new one, so watch for missing features and report any you need.

### What is a harness, and why does it matter?

📹 [36:46](https://youtube.com/watch?v=6Vu0_W1OzWk&t=2206)

A harness is the coding agent logic that wraps the model. The GitHub harness is now the [Microsoft Copilot harness](https://blogs.microsoft.com/blog/2026/10/28/introducing-the-microsoft-copilot-harness-unlocking-the-potential-of-truly-multi-model-agentic-work/), a shared foundation used by the Copilot CLI, the Copilot app, VS Code, and Copilot in apps like PowerPoint and Excel. The [Copilot SDK](https://github.com/github/copilot-sdk) uses the same Rust-based harness behind the scenes. As a result, the many products named Copilot should behave increasingly alike. Not all of them use it yet: Pamela had heard that Copilot in Edge, and maybe Teams, had not switched over.

### Who is the pilot: the agent or the human?

📹 [37:59](https://youtube.com/watch?v=6Vu0_W1OzWk&t=2279)

Increasingly, that is changing. Using Opus 5.5 is convincing many developers that the job is shifting, since it writes good code, perhaps better than most people do. Pamela is preparing for a world where we assume LLMs write good code, and the human's job is to check whether the output matches expectations. We're not quite there yet, but it's getting close.

## Demo: Agents Hangout and the Cure MS research lab

📹 [38:58](https://youtube.com/watch?v=6Vu0_W1OzWk&t=2338)

Justin shared [Agents Hangout](https://agentshangout.com/h/fcrkZH62LSwc3gmX), a SimCity-like world where AI agents and their people hang out in shared rooms and build together in the open. In its research lab, agents are working on a public, open-source effort to research multiple sclerosis, with work tracked in [Cure-MS issues](https://github.com/AgentsHangout/Cure-MS/issues) and pull requests. Pamela also mentioned a talk about someone who used LLMs to research and design a custom vaccine for their dog's cancer, which suggests agents are increasingly being used for custom vaccines. If you have done work related to MS, consider joining.

## Announcement: Skills over MCP lands in the GitHub Copilot SDK for Rust

📹 [42:15](https://youtube.com/watch?v=6Vu0_W1OzWk&t=2535)

The VS Code Copilot team reported that skills over MCP is now in the Rust SDK, likely the [Copilot SDK for Rust](https://github.com/github/copilot-sdk/tree/main/rust). Since the Copilot harness is built on a Rust binary, skills over MCP will likely arrive in Copilot before MCP events. Pamela didn't know of any agents that supported skills over MCP yet, so Copilot could lead the way.

The [Developer knowledge base workshop from GitHub Universe](https://github.com/pamelafox/developer-kb-for-github-copilot) is also open source. It covers connecting GitHub Copilot first to the GitHub MCP server and then to the Foundry IQ MCP server.

## Discussion: LLMs can read and write neural network weights

📹 [43:36](https://youtube.com/watch?v=6Vu0_W1OzWk&t=2616)

[Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) finds that a general-purpose LLM can read and write a neural network's weights directly, without gradient descent or an optimizer. It can inspect weights to identify traits, such as recognizing that a network was trained on Breakout or predicting what a diffusion model will generate. The result that excited people most was an LLM editing weights to make a model better at math.

As Nnamdi summarized in chat, training normally nudges weights through gradient descent and backpropagation, while here the LLM looked at the weights and essentially guessed what to change, which is probably much faster. This could improve interpretability, since an LLM that understands weights might help humans understand them too. It might also become an alternative to fine-tuning, such as tweaking weights to prioritize accuracy over hallucinations for RAG. You would still pay to run a custom model, but it might be more efficient than fine-tuning.

Justin hoped that models can't tweak their own weights in real time without good oversight. Pamela assumed they can't, given how inference engines like vLLM run models.

## Discussion: More industry news

📹 [46:43](https://youtube.com/watch?v=6Vu0_W1OzWk&t=2803)

* **DeepSeek open-sourced [DeepInfer](https://github.com/deepseek-ai/DeepInfer):** Its inference engine is optimized for DeepSeek models.
* **Cloudflare bought Deno:** The acquisition was mostly for its serverless technology, and Deno is winding down. If you use Deno as an alternative to Node or Bun, plan to migrate.
* **OpenAI launched [GPT-6.1 Terra](https://openai.com/index/introducing-gpt-6-1-terra/):** Terra has been the in-between model next to the cheap Luna and the strong Sol, but OpenAI says 6.1 Terra is particularly good at visual understanding and action. Pamela had not tried Terra.

## Can you have a strong model use cheaper models for subagents?

📹 [50:27](https://youtube.com/watch?v=6Vu0_W1OzWk&t=3027)

Yes. Justin likes prompting a strong model to use subagents and assign cheaper models to them, such as Astra controlling Terra, Luna, and Sol. This is easy in the Copilot app. For example, asking it to "use a different GPT model for each redesign in a child session" started child sessions using GPT-6.1 Sol, GPT-6 Luna, and GPT-5.3 Codex.

Design is a great use case for multiple child sessions, since different models give more variation. Pamela often asks for a gallery or contact sheet to compare outputs, such as logo options for a fake chocolate company. The hard part then becomes taste: narrowing many good designs down to the one that is actually best.

## Does FastMCP support skills over MCP?

📹 [53:47](https://youtube.com/watch?v=6Vu0_W1OzWk&t=3227)

Yes. Bernhard shared that [FastMCP supports the skills over MCP extension](https://gofastmcp.com/servers/skills), so MCP servers built with FastMCP can serve skills. The MCP features released since the last MCP livestream could fill another livestream. A FastMCP event with the team is planned in person in December, and one talk is expected to cover skills.
