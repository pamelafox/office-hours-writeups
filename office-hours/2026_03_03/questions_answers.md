# March 3, 2026 Office Hours Q&A

Note: This session was a follow-up Q&A after the [Python + Agents Session 4 livestream](https://developer.microsoft.com/en-us/reactor/events/26691/), focused on workflows (conditional, switch-case, state management). The recording cut out near the end due to internet issues, so the final questions were reconstructed from Discord chat.

## How do you stop an agent from outputting an old value in its context rather than re-running a function tool or an API call?

📹 [0:00](https://youtube.com/watch?v=UDZ8oACh_1g&t=0)

This comes up when an agent has a long conversation history and decides to use cached tool call results instead of re-calling the function — for example, an exchange rate agent returning stale rates.

The recommended approach is to use **middleware** to invalidate old tool call returns. You can base it on the summarization middleware pattern: look back at the tool call history, and if a particular tool call's result is too old (e.g., 10 minutes, an hour, 3 days — whatever makes sense for your use case), remove that tool call from the history. This forces the agent to re-call the function.

This needs to be agent-level or chat-level middleware, not function-level middleware, since the problem is that the agent isn't calling the function at all. You can also add prompt instructions telling the agent to check how old a value is, but agents don't always respect prompts, so middleware is the more reliable solution.

## How do you prevent malicious prompts from proliferating your workflows?

📹 [3:40](https://youtube.com/watch?v=UDZ8oACh_1g&t=220)

There are multiple risk mitigation layers to consider:

1. **System message and grounding**: Helpful but has limitations — prompts can only go so far.
2. **Model safety training**: Use frontier-level models that have been through rigorous RLHF (Reinforcement Learning from Human Feedback) specifically for safety. Check the model card for any new model to see what safety red teaming was done. Avoid models without published model cards.
3. **Content safety system**: On Azure, the content safety system lets you configure what gets blocked, including two kinds of jailbreak detection and protected materials detection. Models hosted on Foundry (formerly Azure AI) include these filters by default at a "medium" threshold, which you can adjust higher or lower.

The recommendation is to use Azure-deployed models since they include built-in safety layers, rather than relying solely on prompt-based protections.

## What is the recommended approach for integrating the GitHub Copilot CLI and SDK in a DevOps workflow?

📹 [7:26](https://youtube.com/watch?v=UDZ8oACh_1g&t=446)

The specific question was about analyzing CVEs in dependencies and making corrective actions on PRs.

For CI/CD automation with LLMs, [GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/) is the recommended starting point. These let you write workflows in plain text with security YAML front matter (specifying permissions, allowed outputs, and tools like the GitHub MCP server), and it generates the GitHub Actions workflow file for you. This is much easier than writing workflows from scratch.

For analyzing CVEs on PRs specifically, you could set up an agentic workflow that triggers on pull requests, reads the PR contents, and analyzes dependencies — with custom MCP servers if needed.

Links shared:

* [GitHub Agentic Workflows blog post](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/)
* [Copilot SDK experiments branch](https://github.com/Azure-Samples/azure-search-openai-demo/compare/main...pamelafox:azure-search-openai-demo:sdkexperiments)

## Have you tried building MAF applications using Claude Code or Codex?

📹 [12:26](https://youtube.com/watch?v=UDZ8oACh_1g&t=746)

Pamela has only used Codex once (when the Mac desktop app came out) and found it quite good, but hasn't used Claude Code. All the demo examples were built using GitHub Copilot.

The key is having a good [`AGENTS.md`](https://github.com/Azure-Samples/python-agentframework-demos/blob/main/AGENTS.md) file that tells the coding agent about the framework, repo structure, and relevant resources — Pamela shared her configuration for the demo repo, which specifies the framework, Python version, changelog location, and available MCP servers. This kind of configuration is useful regardless of which coding agent you use.

## How likely is it that a conditional workflow gets stuck in an infinite revision loop, and how do you prevent it?

📹 [14:06](https://youtube.com/watch?v=UDZ8oACh_1g&t=846)

This is very possible. Pamela experienced it herself and had to make the reviewer less critical and increase `max_iterations` (from 8 to 20 in one example). The default max iterations is 100.

Best practices for handling this:

1. **Set `max_iterations`** on your workflow to a reasonable limit.
2. **Catch the exception**: When max iterations is exceeded, the framework raises a `WorkflowConvergenceException` ("Runner did not converge"). Wrap your workflow execution in a try/except to handle this gracefully — e.g., log it, mark it for human review, or investigate which stage was too critical.
3. **Use workflow state**: You can use `set_state`/`get_state` to track revision counts and break loops intentionally via conditional edges.
4. **Design fallback edges**: Ensure conditional edges have a default fallback path that guarantees termination.
5. **Instruct the agent**: Include guidance in the system prompt about when to stop revising.

At the agent level (as opposed to the workflow level), you can use middleware to detect when an agent is making too many tool calls and intervene.

### Does the executor context include iteration count?

📹 [19:27](https://youtube.com/watch?v=UDZ8oACh_1g&t=1167)

The workflow does track iteration count internally, but it may not be directly accessible from the workflow context. If you can't access it naturally, you can use `set_state`/`get_state` to track iteration count yourself and use it in conditional edges to break out of loops.

## The switch-case workflow throws an unhandled exception when running with DevUI — is it an environment issue?

📹 [22:21](https://youtube.com/watch?v=UDZ8oACh_1g&t=1341)

It's not just your environment — Pamela hit the same bug. The error (`'NoneType' object has no attribute 'category'`) occurs when running with `--devui` but not via CLI. Multiple attendees confirmed that several switching/conditional workflows don't complete under DevUI but work fine from the command line. It was a recent regression related to how structured outputs are handled. The bug was [filed on GitHub](https://github.com/microsoft/agent-framework/issues/4437) and has already been resolved in main.

## Is there a certification about agents from Microsoft?

📹 [30:13](https://youtube.com/watch?v=UDZ8oACh_1g&t=1813)

There isn't a specific "agents" certification, but several related ones exist:

* [Azure AI Fundamentals (AI-900)](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/) — the fundamentals-level certification
* [Azure AI Engineer Associate (AI-102)](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/) — the associate-level certification, frequently recommended
* [Applied Skills: Create an AI Agent](https://learn.microsoft.com/en-us/credentials/applied-skills/create-an-ai-agent/) — a targeted applied skills credential

Links shared:

* [Azure AI Engineer Associate certification](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/)
* [Azure AI Fundamentals certification](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/)
* [Applied Skills: Create an AI Agent](https://learn.microsoft.com/en-us/credentials/applied-skills/create-an-ai-agent/)

## What LLMs or SLMs do you recommend for running workflows locally?

This question was asked in Discord chat near the end of the session but the recording cut out before it could be answered on stream. [Foundry Local](https://learn.microsoft.com/en-us/azure/foundry-local/get-started) is a tool for running models locally, available on [GitHub](https://github.com/microsoft/Foundry-Local).

## Where can I find all the course series?

This question was asked in Discord chat. Links shared:

* [Python + AI series resources](https://aka.ms/pythonai/resources)
* [Python + MCP series resources](https://aka.ms/pythonmcp/resources)
* [Python + Agents series resources](https://aka.ms/pythonagents/resources)
* [Pamela's talks page](https://pamelafox.org/talks/)
* [Pamela's Python talks slides](https://pamelafox.github.io/my-py-talks/)

## What is the status of Foundry Local for Linux?

Currently, [Foundry Local](https://github.com/microsoft/Foundry-Local) only supports Mac and Windows. There are open discussions about Linux support on the GitHub repo.
