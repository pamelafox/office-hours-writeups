# August 25, 2026 Office Hours Q&A

## Demo: Using @GitHub in Teams and Slack

📹 [04:02](https://www.youtube.com/watch?v=8YlDFQpiq30&t=242)

Pamela demonstrated using `@GitHub` to start Copilot coding-agent sessions from Slack and Teams, connect them to repositories, and create pull requests.

### How is GitHub Copilot usage in Slack or Teams billed?

📹 [04:02](https://www.youtube.com/watch?v=8YlDFQpiq30&t=242)

The integrations consume AI credits through usage-based billing. Pamela's best guess was that usage is attributed to the person who mentions `@GitHub` and starts the session, but she did not find confirmation during the session. The demo showed that the resulting cloud-agent session was associated with her GitHub account, which supports that interpretation without conclusively establishing the billing rule.

### Does your Slack email need to match your GitHub email?

📹 [13:46](https://www.youtube.com/watch?v=8YlDFQpiq30&t=826)

No. The connection is based on authenticating with GitHub through OAuth, not on matching Slack, Teams, and GitHub email addresses. The relevant GitHub app must also be installed for the personal account or organization whose repositories the bot should access; Pamela showed this in her [GitHub app installation settings](https://github.com/settings/installations).

### Are the Slack and Teams integrations using MCP?

📹 [31:49](https://www.youtube.com/watch?v=8YlDFQpiq30&t=1909)

No- These integrations use the native extension mechanisms provided by each platform: a Slack app and a Teams app. MCP could still be used internally by an agent session, but it is not the public integration layer demonstrated here.

### Why did a pull request appear to be authored by the user rather than Copilot?

📹 [34:11](https://www.youtube.com/watch?v=8YlDFQpiq30&t=2051)

Pull-request authorship depends on the context. In the Teams direct-message test, Copilot acted with the linked personal account's permissions, so the pull request appeared under Pamela's identity. In a shared context such as a channel, the integration uses the app identity; Slack creates a channel for these sessions, so the Slack pull request in the demo was authored by Copilot. This distinction can affect repository rules for human-authored versus Copilot-authored pull requests, and the [Teams integration documentation](https://docs.github.com/en/copilot/how-tos/copilot-integrations/integrate-cloud-agent-with-teams) explains the permission model.

## What is DeepSeek Harness, and are people discussing it?

📹 [44:27](https://www.youtube.com/watch?v=8YlDFQpiq30&t=2667)

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) is an open-source agent harness built around a plugin architecture. Pamela had heard more discussion of DeepSeek's models than of the harness itself, and more discussion of Grok Bot as an integrated agent product. She attempted to install the harness during the session, but the installation was slow, so the session did not reach a substantive evaluation of it. For Google Workspace access from different agents, she also mentioned the general-purpose [gogcli](https://github.com/openclaw/gogcli) command-line tool.

## Where is the documentation confirming that Microsoft Foundry hosted agents are generally available?

📹 [46:21](https://www.youtube.com/watch?v=8YlDFQpiq30&t=2781)

Pamela said [hosted agents in Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents) are generally available and noted that documentation explicitly labels features that remain in preview. For example, [resilience for long-running hosted agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/long-running-agent-resilience) was still marked preview. She could not find a dedicated GA blog post during the recording, but after the session she shared a broader [Microsoft Foundry announcement](https://azure.microsoft.com/en-us/blog/gpt-5-6-now-available-in-microsoft-foundry/) that lists production agents, hosted agents, toolboxes, and publishing to Microsoft 365 Copilot and Teams among the generally available updates.

## Demo: Playwright plus Pydantic AI agent

📹 [50:07](https://www.youtube.com/watch?v=8YlDFQpiq30&t=3007)

Pamela demonstrated the QA agent from her [browser automation with Pydantic AI and Playwright](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/browser-automation-with-pydantic-ai--playwright/4547971) article. The flexible agent repeatedly chooses Playwright SDK tools to inspect a website and produce a QA report.

### Where can I find more Playwright examples?

📹 [56:02](https://www.youtube.com/watch?v=8YlDFQpiq30&t=3362)

Pamela recommended using Playwright for end-to-end application tests and pointed to her [personal LinkedIn agent](https://github.com/pamelafox/personal-linkedin-agent) as a more structured workflow that uses Playwright with tighter control over what is sent to the model.

### How much does agentic browser automation cost?

📹 [56:49](https://www.youtube.com/watch?v=8YlDFQpiq30&t=3409)

The cost depends on model token pricing and how much context and tool output the workflow processes. Pamela had not calculated the final cost of the demonstrated run, but warned that its open-ended agent loop could be fairly expensive: it made many tool calls, gathered substantial context, and allowed up to 30,000 content tokens. A structured workflow can cost less by sending the model only the information needed for each decision.
