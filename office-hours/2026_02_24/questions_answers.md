# Feb 24, 2026 Office Hours Q&A

Note: This session was a follow-up Q&A after the [Python + Agents Session 1 livestream](https://developer.microsoft.com/en-us/reactor/events/26688/), focused on the Microsoft Agent Framework.

## How does middleware work in the Agent Framework?

📹 [0:01](https://youtube.com/watch?v=6HzauGnbRwA&t=1)

The Agent Framework supports three types of middleware, each operating at a different level:

- **Agent context middleware** — runs before and after `agent.run()`. You get access to the agent, messages, session (chat history), and options (e.g., whether streaming is enabled). You can override the result or modify options after the agent runs.
- **Function context middleware** — sits between the LLM calls and the tool/function calls. Useful for security-related concerns like permission checking, human-in-the-loop approvals, limiting the number of tool calls (e.g., cutting off a deep researcher after 12 tool calls), and tool retry logic.
- **Chat context middleware** — operates on the chat level, where you can override or filter the LLM's response (e.g., PII reduction).

All three middleware types let you mutate the result if needed. You can define middleware using simple functions or classes.

## Why do the tools in the demos have hard-coded return values?

📹 [4:01](https://youtube.com/watch?v=6HzauGnbRwA&t=241)

The demo tools return hard-coded values so they work without requiring API keys. For a real implementation, you'd replace the hard-coded returns with actual API calls (e.g., `requests.get()` to a weather API). Most weather APIs require keys, so the demos avoid that dependency.

## How does "context" differ across frameworks?

📹 [5:11](https://youtube.com/watch?v=6HzauGnbRwA&t=311)

The word "context" is extremely overloaded in the AI/agent space. In the Agent Framework specifically:

- **Context** (as in context providers) — information that always gets passed into the agent, as opposed to tools where definitions are passed but may or may not get called. This is covered more in the session on context and memory.
- **Middleware context** — the context object passed to middleware, giving it access to what it needs to operate (agent context, function context, chat context).

Every framework uses "context" differently, and even within a single framework it can mean different things depending on where it appears.

## What should I do if I get an "unavailable model" error with GPT-5 Mini?

📹 [6:52](https://youtube.com/watch?v=6HzauGnbRwA&t=412)

GPT-5 Mini access may be more restricted for some users on GitHub Models. Workarounds:

1. Check the [GitHub Marketplace models page](https://github.com/marketplace?type=models) to see if your account can access it
2. Create a `.env` file and set `GITHUB_MODEL` to a different model (e.g., `gpt-4o`)
3. Set the environment variable directly: `GITHUB_MODEL=gpt-4o`

All the examples in the repo check for a `GITHUB_MODEL` environment variable and fall back to a default. If deploying to Azure, GPT-5 Mini doesn't require an access request form and is available in many regions.

## Is it possible to see the full information sent to the LLM?

📹 [9:52](https://youtube.com/watch?v=6HzauGnbRwA&t=592)

Yes — set the logging level to debug:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

This shows the full HTTP request being sent to the chat completions endpoint, including the JSON data with the conversation, model, streaming settings, and tool definitions. Since the Agent Framework wraps the OpenAI SDK, setting debug logging will show what's sent to the LLM.

Seeing the **response body** is harder — the repo's AGENTS.md file has tips for how to inspect response bodies with various SDKs. Open Telemetry tracing (covered in the Thursday session) provides another way to see this information.

## Were these examples hand-coded or vibe-coded?

📹 [13:54](https://youtube.com/watch?v=6HzauGnbRwA&t=834)

A mix. The earlier examples shown in the session were mostly hand-coded. For later, more complex examples, the process was collaborative with GitHub Copilot:

1. Use **plan mode** in GitHub Copilot
2. Provide an outline and point the agent to the most similar existing examples
3. Do a lot of back-and-forth on the plan before implementing
4. Let the agent generate the code based on the agreed-upon plan

It's described as a collaborative process rather than pure "vibe coding."

## Do you recommend starting with a deployed model (Azure Foundry) for learning agents?

📹 [15:53](https://youtube.com/watch?v=6HzauGnbRwA&t=953)

Yes, deploying sooner is better because:

- **GitHub Models rate limits** are reached quickly with agent workloads since agents use a lot of tokens
- **Local small models** generally aren't good enough for reliable tool calling (at least on typical developer machines)
- **Frontier models** (GPT-5 Mini, GPT-4o, etc.) provide the best tool calling support

Even $20 worth of credits goes a long way. You can use Azure, OpenAI directly, or both. The repo's README has instructions for deploying to Azure with `azd login` and `azd provision`.

## Can you use local Ollama models with the Agent Framework?

📹 [17:49](https://youtube.com/watch?v=6HzauGnbRwA&t=1069)

Yes, technically. The question is whether they work well. Tips:

- Use a model that **supports tool calling** — filter for "tools" on [ollama.com](https://ollama.com) models page
- Recommended models for tool calling: **Qwen 3**, **GPT-4All** (if your machine can run it), **GLM models** (if you have sufficient VRAM)
- When running locally, connect via `http://localhost:11434/v1`
- When running inside a **dev container**, use `http://host.docker.internal:11434/v1` instead

A live demo showed Llama 3.1 successfully handling a basic agent example through Ollama.

## Are all the models you're using free?

📹 [25:11](https://youtube.com/watch?v=6HzauGnbRwA&t=1511)

No. The cost breakdown:

- **GitHub Models** — free (used by default in Codespaces), but has rate limits
- **Azure** — not free, but used to avoid rate limits. Uses keyless connections with `DefaultAzureCredential`
- **OpenAI** — not free
- **Ollama** — free (runs on your local machine)

## Does the tracing in Agent Framework work with OpenAI tracing?

📹 [28:00](https://youtube.com/watch?v=6HzauGnbRwA&t=1680)

Probably not directly. Agent Framework uses **Open Telemetry** for tracing, while OpenAI tracing appears to be its own thing (built specifically for the OpenAI Agents SDK). Since the Agent Framework wraps the OpenAI client, there might theoretically be a way to pass tracing info through, but it would likely not work out of the box. This topic is covered more in the Thursday session on Open Telemetry.

## How does the supervisor agent pattern work?

📹 [29:06](https://youtube.com/watch?v=6HzauGnbRwA&t=1746)

A supervisor agent manages multiple specialist agents by wrapping them as tools:

1. The supervisor has instructions describing it manages specialist agents and should decide which to call
2. Each specialist agent is wrapped as a tool function — e.g., `plan_meal` is a tool that runs the meal agent with a query and returns its response
3. The supervisor can potentially call multiple specialist agents, even in parallel

Key observations from the live demo:
- **Parallel tool calling** can happen — OpenAI models support suggesting multiple tool calls in a single response by default
- If the agent doesn't have enough information, it may ask follow-up questions instead of completing the task. You need either a conversation loop or enough detail in the initial prompt.
- Sub-agents are also useful for **reducing the context window**, which will be covered in the session on context and memory.

## Can you use GitHub Copilot models with the Agent Framework?

📹 [36:53](https://youtube.com/watch?v=6HzauGnbRwA&t=2213)

Yes. The Agent Framework has a GitHub Copilot provider:

1. Install the additional package: `agent-framework-github-copilot`
2. Import `GitHubCopilotAgent` instead of the regular `Agent` class
3. The Copilot CLI must be **installed and logged in** in the current environment

It works by wrapping the Copilot CLI binary. In the live demo, it was tricky to get working inside a dev container (required installing the Copilot CLI and logging in within the container). Once set up, you just swap `Agent` with `GitHubCopilotAgent`.

The GitHub Copilot team considers their agent runtime to be among the best available. Note that the Copilot CLI's agentic loop is actually different from VS Code's Copilot agentic loop — they implement things differently despite sharing the product name.

Links shared:

- [Agent Framework GitHub Copilot samples](https://github.com/Azure-Samples/python-agentframework-demos)

## Do you always use Codespaces or only for demos?

📹 [42:20](https://youtube.com/watch?v=6HzauGnbRwA&t=2540)

Lately, more local development instead of Codespaces. The main reason is that `azd login` (Azure Developer CLI login) is harder in Codespaces with the current tenant setup. Working locally (still in a dev container) makes it easier to stay logged into Azure. Codespaces is still liked in general, but the Azure authentication friction has pushed more work to local dev.

## What is YOLO mode in Copilot?

📹 [50:39](https://youtube.com/watch?v=6HzauGnbRwA&t=3039)

YOLO mode auto-approves all tool/command executions without confirmation. It's available both in the **Copilot CLI** and **VS Code** (search for "auto approve" in settings).

Caution: Even inside dev containers and Codespaces, authenticated tools (like the GitHub MCP server) can still perform real actions. The recommendation is to approve commands **per session** (per chat thread) rather than enabling full YOLO mode globally, since authenticated access to services like GitHub means an agent could make real changes.
