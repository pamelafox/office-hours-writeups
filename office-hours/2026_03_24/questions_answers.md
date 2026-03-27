# March 24, 2026 Office Hours Q&A

## What's the difference between the chat completions API and the responses API?

📹 [9:19](https://youtube.com/watch?v=Uufh7cPUnmQ&t=559)

Someone asked Pamela to explain the differences, since she'd been discussing her effort to port all her repos from chat completions to responses API. The code looks very similar — the key differences:

- **Syntax**: Instead of `chat.completions.create`, you use `responses.create` with an `input` parameter instead of `messages`.
- **Stateful mode**: The responses API has a `store` parameter. With `store=True`, the API creates a thread ID and stores conversation history server-side (on Azure servers, retained for 30 days by default). For multi-turn conversations, you can pass `previous_response_id` instead of rebuilding the full message history. You can set `store=False` for stateless behavior like chat completions.
- **Built-in tools**: You can enable code interpreter (runs in a sandboxed Azure Container Apps environment) and web search with a single line of code. You can also point it at remote MCP servers with built-in support.
- **Model support**: Once on the responses API, your code can support DeepSeek, Llama, and all Azure direct models.
- **Encrypted reasoning items**: When using reasoning models in stateless mode, you need to retrieve and pass back encrypted reasoning items to preserve reasoning context across turns.
- **Compaction**: The API has built-in `client.responses.compact` as well as server-side compaction for managing conversation length.

One downside: GitHub Models only supports chat completions, so porting to responses API means losing that path. But the benefits outweigh the loss.

Pamela has been using a [custom Copilot agent](https://github.com/Azure-Samples/azure-openai-to-responses) with skills that automates the port — you open your repo in VS Code, add the porting repo to the workspace, and run the agent prompt. For new projects, she recommends the [ai-model-start](https://github.com/Azure-Samples/ai-model-start) repo which already uses the responses API.

Links shared:

* [Azure OpenAI to Responses porting agent](https://github.com/Azure-Samples/azure-openai-to-responses)
* [AI Model Start template](https://github.com/Azure-Samples/ai-model-start)
* [Responses API documentation](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses)
* [Example porting PR (FastAPI chat backend)](https://github.com/Azure-Samples/openai-chat-backend-fastapi/pull/95)
* [Repo porting tracker gist](https://gist.github.com/pamelafox/e4f0817f79460c49425caf2c9706a847)

## Can VS Code skills be a replacement for MCP servers?

📹 [14:37](https://youtube.com/watch?v=Uufh7cPUnmQ&t=877)

Skills and MCP serve different purposes — they're not a direct replacement for each other. (And no, MCP is not dead — the Fast MCP maintainers are even hosting a [tongue-in-cheek funeral for MCP](https://luma.com/htkxoidx) on April 1st in NYC.)

**When to use skills:** For local coding agent workflows with repeatable tasks. Skills are lighter weight — only the tool name and description go into the LLM context, whereas MCP servers can have many tool descriptions that overwhelm the context window. Skills support progressive loading, making them more selective. They're great for functionality like converting slides, extracting transcripts, or anything you'd write a Python script for.

**When to use MCP:** For authenticated data access (MCP has built-in OAuth support and VS Code handles authentication), agent-to-agent communication, and organization-wide tool exposure. Organizations use MCP servers to expose service data in a structured way with proper authentication. Pamela prefers the GitHub MCP server over the GitHub CLI specifically because it handles authentication better.

**How to create skills:** Ask Copilot to write a skill, and tell it to use Python inline dependencies (PEP 723) so scripts can be run with `uv run`. After successfully completing a task, tell the agent to make a skill based on the conversation. Skills can be stored in `.github/skills`, `.agent/skills` (the standard location), or globally in `~/.agents/skills` for use across all repos.

The MCP protocol also has a skills working group exploring how MCP servers can expose skills, so the two approaches may converge.

Links shared:

* [VS Code Skills documentation](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
* [Azure Skills plugin](https://github.com/microsoft/azure-skills)
* [Waza — CLI to evaluate skill quality](https://github.com/microsoft/waza)
* [Sensei — iteratively improve skills using RALF loop](https://github.com/spboyer/sensei)

## What happened with the LiteLLM supply chain attack?

📹 [26:12](https://youtube.com/watch?v=Uufh7cPUnmQ&t=1572)

Zach raised concerns about the LiteLLM supply chain attack that happened the same day. LiteLLM, a popular Python gateway package, was compromised by a threat actor ("Team PCP") who published malicious versions that harvest SSH keys, cloud credentials, environment variables, and crypto wallets. There was approximately a 3-hour exposure window before PyPI quarantined the compromised packages.

If you had your dependencies pinned (e.g., to version 1.58.2.6 or earlier), you were fine. If you used an unpinned dependency and pulled the latest during that window, your environment may have been compromised.

**Best practices for dependency security:**

- **Always pin dependencies.** With UV, use `uv sync` which creates a lock file that you explicitly update. With pip, use `pip-compile` to generate a pinned `requirements.txt` from your `pyproject.toml`.
- **Enable GitHub code alerts and Dependabot** on your repositories. Dependabot will notify you of CVEs in pinned packages and create PRs to update them.
- **Check PyPI maintainers.** Official Microsoft packages list "Microsoft" as a maintainer and go through strict security requirements before publishing.
- **Consider alternatives.** If you're an Azure user, the responses API now serves as a common gateway to all Azure models, potentially replacing what LiteLLM does.

Links shared:

* [LiteLLM supply chain attack timeline](https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/)

## Is there a way to host agents in AKS and use Foundry orchestrations?

📹 [40:04](https://youtube.com/watch?v=Uufh7cPUnmQ&t=2404)

Foundry hosted agents currently deploy to Azure Container Apps behind the scenes (not AKS), using a specific deployment process that wraps your agent in instrumentation for tracing and evaluation.

If you want to run on AKS, you can use the agent framework workflow YAML approach: create your workflow in Foundry (sequential, group chat, etc.), export the YAML, and run it with agent framework on AKS. The YAML is just standard agent framework configuration.

However, you lose the key Foundry hosted agent benefits: continuous evaluation (sampling and evaluating live agent requests), evaluation alerts, and scheduled evaluations. Those require the Foundry-specific deployment with adapters for agent framework or LangChain/LangGraph. At the moment, there are only two adapters (agent framework and LangChain), though it may be possible to write a custom adapter for other frameworks.

Logic App connectors have also been added as built-in tools in Foundry, available under "Discover Tools" for both Foundry agents and hosted agents.

## Do you have recommendations for getting started with evals?

📹 [48:39](https://youtube.com/watch?v=Uufh7cPUnmQ&t=2919)

Start with the **built-in evaluators** using the OpenAI eval SDK (the new approach, replacing the older Azure AI Evaluation SDK):

- **Task adherence** and **intent resolution**: General evaluators that check how well the agent handled the user's request.
- **Groundedness** and **relevance**: The best built-in evaluators for RAG scenarios.

Then **move to custom evaluators** as a best practice:

1. Look through your data and have humans identify good and bad examples.
2. Identify specific failure patterns in your agent's behavior.
3. Build custom "LLM-as-a-judge" evaluators targeting those failure patterns, or regex-based evaluators for simpler checks.
4. Distinguish between evals with **ground truth** (where you can check exact tool calls and arguments at every step) vs. evals on **live data** (where you need general failure-case detection).

For learning more about evals, Pamela highly recommends subscribing to [hamel.dev](https://hamel.dev). Hamel Husain runs courses on evals and his blog posts — especially the [LLM Evals guide](https://hamel.dev/blog/posts/evals/) — are excellent resources.

Links shared:

* [Quality eval example script](https://github.com/pamelafox/python-foundryagent-demos/blob/main/scripts/quality_eval.py)
* [hamel.dev](https://hamel.dev)

## Announcement: New agent-framework release candidate (RC5)

📹 [0:49](https://youtube.com/watch?v=Uufh7cPUnmQ&t=49)

Agent framework (the successor to Semantic Kernel and AutoGen) published release candidate RC5 on March 19th. Microsoft is doing a big internal bug bash, and GA is expected around end of March / early April. You can test the release candidate yourself if you're already developing with agent framework.

Links shared:

* [agent-framework on PyPI](https://pypi.org/project/agent-framework/)

## Announcement: Deploy agents to Foundry with azd

📹 [1:51](https://youtube.com/watch?v=Uufh7cPUnmQ&t=111)

A new blog post explains how to deploy your own agents (built with agent framework or LangChain) to Microsoft Foundry as "hosted agents." Hosted agents provide online evaluations (sampling live traces), scheduled evaluations, and red teaming scans. Not everything works perfectly yet, but improvements are ongoing.

Links shared:

* [From code to cloud: Deploy an AI agent to Microsoft Foundry in minutes with azd](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/)

## Announcement: Upcoming live stream series on Foundry Hosted Agents (April 28–30)

📹 [3:07](https://youtube.com/watch?v=Uufh7cPUnmQ&t=187)

A three-part live stream series on Foundry hosted agents:

- Day 1 (April 28): Microsoft Agent Framework
- Day 2 (April 29): LangChain and LangGraph
- Day 3 (April 30): Quality and safety evaluations

Registration pages coming soon.

## Demo: Foundry Agent Service

📹 [35:17](https://youtube.com/watch?v=Uufh7cPUnmQ&t=2117)

Pamela demoed Foundry Agent Service at Nvidia GTC the previous week. The demo code creates 20+ Foundry prompt agents, an agent grounded in a Foundry IQ knowledge base (Azure AI Search), runs quality evaluations, red teaming scans, continuous evaluation, scheduled evaluations, and uses Locust for simulating user traffic. All code is available in the demo repo.

Links shared:

* [python-foundryagent-demos](https://github.com/pamelafox/python-foundryagent-demos)
