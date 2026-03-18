# March 4, 2026 Office Hours Q&A

Note: This session was a follow-up Q&A after the [Python + Agents Session 5 livestream](https://developer.microsoft.com/en-us/reactor/events/26692/), focused on orchestrating advanced multi-agent workflows.

## How do you increase the performance (latency) of a multi-agent system?

📹 [0:30](https://youtube.com/watch?v=txskCy6Vmzc&t=30)

The first step is to set up **quality evaluations** with a ground truth baseline, so you can make performance changes and confirm quality doesn't regress. Once evaluations are in place, you can try several optimizations:

- **Use smaller/faster models**: Try quicker models or, if using a reasoning model like GPT-5.2 or GPT-5.3, set reasoning effort to "none" to save time.
- **Reduce input tokens**: Use context management techniques like sub-agents to keep context windows small. This was covered in the second session of the series.
- **Reduce output tokens**: Have the LLM output shorter responses (e.g., a one-sentence summary instead of a paragraph).

Always check evaluations after each change — sometimes a quality improvement causes latency to spike, making it not worth it. You need evaluations to reason about the latency/quality trade-off.

## How do you incorporate A2A protocols into model orchestrations to integrate other agent providers into Foundry orchestration?

📹 [3:47](https://youtube.com/watch?v=txskCy6Vmzc&t=227)

Microsoft Agent Framework has a sub-package specifically for A2A (Agent-to-Agent) integration. It lets you connect to an A2A agent and get responses from it. The documentation on [hosting your agent with A2A protocol](https://learn.microsoft.com/en-us/agent-framework/workflows/) covers this integration. However, the specifics depend on whether you're trying to communicate with an A2A agent or host one yourself.

## Are there limitations in workflow evaluation using Microsoft Foundry if you deploy your agent as a hosted agent?

📹 [5:48](https://youtube.com/watch?v=txskCy6Vmzc&t=348)

Pamela hasn't personally deployed an agent as a hosted agent yet and couldn't speak to specific limitations. If anyone has experience with hosted agents and evaluation, they were encouraged to share. A follow-up series about hosting agents may provide the opportunity to explore this.

## What evaluation framework do you recommend — DeepEval, Ragas, others?

📹 [6:42](https://youtube.com/watch?v=txskCy6Vmzc&t=402)

For workflows, the same principles as agent evaluation apply: evaluate the final output of the workflow against ground truth, but also evaluate each individual agent along the way.

Recommended options:

- **Azure AI Evaluation**: What Pamela primarily uses. The advantage of using it (or OpenAI Evals with Foundry projects) is that results show up in the Foundry portal.
- **OpenAI Evals**: Microsoft is moving towards using OpenAI Evals with Foundry projects — worth trying.
- **Agent Framework lab packages**: Includes TAU2 (specifically for customer service agent benchmarks) and GAIA (for agents and workflows), though documentation for GAIA is limited.
- **Custom evaluations**: Remember the core principles — you're either using an LLM as a judge (outputting yes/no or 1-5 with reasoning) or some other heuristic, then doing batch evaluation. You can ask GitHub Copilot to write a custom eval framework if existing ones don't fit your needs.

For .NET developers, [Agent Eval](https://github.com/) (a .NET evaluation framework) was recommended by another attendee — it includes latency and cost checking plus built-in red teaming.

Pamela also recommended subscribing to [Hamel Husain's blog](https://hamel.dev/) for everything related to LLM evaluation.

## Is there a more native way to access workflow context from middleware, rather than manually injecting it?

📹 [10:50](https://youtube.com/watch?v=txskCy6Vmzc&t=650)

This question was about middleware needing to save data to workflow shared state, but middleware doesn't have access to the workflow context. The attendee was manually injecting the context.

Pamela acknowledged this is a deep question and suggested posting it as a discussion on the [Agent Framework GitHub repo](https://github.com/orgs/microsoft-foundry/discussions/165), since the middleware story for workflows specifically may need improvement. The discussions and issues on the agent framework repo have been very helpful for getting answers from the team.

## How does tracing/logging work with workflows?

📹 [12:14](https://youtube.com/watch?v=txskCy6Vmzc&t=734)

It works the same way as with agents — just call `configure_otel_providers()` from agent framework. Pamela demonstrated this live by adding OpenTelemetry tracing to a workflow example and viewing the traces in DebUI.

The traces show parent spans for each workflow step: the agent execution, the edge (transition between agents), and each subsequent agent. So you can see the full workflow flow in the trace viewer. This also works with Aspire or App Insights. All you need is:

```python
from agent_framework import configure_otel_providers
configure_otel_providers()
```

## Will Microsoft Agent Framework be submitted to the AI Foundation (which has MCP, Goose, and agents.md)?

📹 [17:54](https://youtube.com/watch?v=txskCy6Vmzc&t=1074)

Pamela hasn't heard anything about this and isn't sure how projects get added to the foundation. Microsoft Agent Framework has a lot of Microsoft/Azure-specific integration, so it's unclear whether it would fit. Her observation is that protocols (A2A from Google, MCP from Anthropic) tend to come from companies developing frontier LLM models, and Microsoft doesn't have its own frontier models yet. Agent Framework tends to adopt emerging industry patterns (A2A, AGUI, MCP) rather than originating them. It would be nice if the industry agreed on common terminology, but terms like "magentic" originated from Microsoft (via AutoGen), while other frameworks like LangChain have their own orchestration concepts (e.g., Deep Agents).

## How should you version prompts and tool descriptions for agent systems?

📹 [23:21](https://youtube.com/watch?v=txskCy6Vmzc&t=1401)

Since tool descriptions are in code and are part of what the LLM processes, it's hard to separate prompt versioning from code versioning. Pamela's recommendation: keep prompts in your codebase. You can put system prompts in separate files (markdown or Jinja2 templates) and pull them in, but version them alongside your code.

Tie evaluations to your PRs — Pamela showed a GitHub Actions workflow that can be triggered on PRs to run evaluations against the local app inside the runner, upload results as artifacts, and summarize them. This way, changes to prompts or tools get evaluated as part of the normal code review process.

Links shared:

* [Python Agent Framework demos - GitHub Actions](https://github.com/Azure-Samples/python-agentframework-demos/actions)
* [Evaluation GitHub Actions workflow](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/.github/workflows/evaluate.yaml)

## What real-world problems do these workflow patterns solve architecturally?

📹 [33:31](https://youtube.com/watch?v=txskCy6Vmzc&t=2011)

Pamela acknowledged that while she can show the patterns, she can only speak to scenarios from her own job as an advocate. She plans to automate more of her own workflows with agent-framework in the future, possibly in conjunction with the Copilot SDK for coding tasks.

Known strong use cases:

- **Coding agents**: The best-proven use case for LLMs — code is structured, and LLMs know coding languages extremely well.
- **Fuzzy matching**: LLMs can be much better than regular expressions for fuzzy matching tasks.
- **New automation**: Some workflows may not have existed before and are only possible now with LLM access.

She encouraged attendees using workflows and agents in production to share what works and what doesn't to help inspire others.

## Can you use the OpenAI real-time API with Microsoft Agent Framework?

📹 [36:41](https://youtube.com/watch?v=txskCy6Vmzc&t=2201)

Pamela hasn't played with the newest OpenAI real-time models yet. Another advocate, Bruno Capuano, has a sample that combines real-time audio with agent framework in .NET, using whisper for speech-to-text and text-to-speech with voice activity detection. Pamela suggested reaching out to Bruno on LinkedIn for additional advice or samples, and noted that showing the overlap of agent framework with different communication modalities (WhatsApp, real-time audio) is a common request.

Links shared:

* [ElBruno.Realtime - Pluggable real-time audio conversation framework for .NET](https://github.com/elbruno/ElBruno.Realtime)
* [Azure OpenAI Realtime Audio SDK samples](https://github.com/Azure-Samples/aoai-realtime-audio-sdk)

## Can we get the full stack code for the AI finance agent?

📹 [40:50](https://youtube.com/watch?v=txskCy6Vmzc&t=2450)

Yes — the [Agentic AI Investment Analysis Sample](https://github.com/Azure-Samples/Agentic-AI-Investment-Analysis-Sample) is the full-stack repo. It uses React (with React Flow), Tailwind for the frontend, and FastAPI for the backend.

**Important caveat**: The repo currently uses an old version of agent framework and does not pin the version in requirements, so it's hard to run right now, unless you change requirements.txt to specify the old version `1.0.0b260212`. The team working on it said it should be updated within the next few weeks.

## Can you do breakpoint debugging with workflows in VS Code?

📹 [27:34](https://youtube.com/watch?v=txskCy6Vmzc&t=1654)

Yes! Pamela demonstrated this live. Key tips:

- Set breakpoints on the **first line of code** in edge functions — not on docstrings or function signatures (putting a breakpoint on a docstring moves it to the function signature, which doesn't work well).
- For agent-level debugging, you'd need to write debugging middleware since agents are just classes without a convenient place to break.
- At a breakpoint, you can inspect the agent response, see the text output, and examine the workflow state.
- If you have OpenTelemetry console exporter enabled, you'll see OTEL spans in the debug console output as well.

Tip: You could even ask GitHub Copilot to write VS Code debug middleware for you.
