# July 29, 2026 Office Hours Q&A

These office hours followed session 2 of the [Microsoft IQ Deep Dive](https://aka.ms/iqdeepdive/resources) series, which covered Work IQ.

## What are the best practices for structuring and maintaining IQ deployments in a larger environment?

📹 [5:23](https://youtube.com/watch?v=69IFV1zZEdA&t=323)

A deployment spanning Foundry IQ, Work IQ, and Fabric IQ is not one service. It crosses several workloads and usually needs people with expertise in Foundry, Microsoft 365, and Fabric to handle deployment and governance.

[Microsoft Agent 365](https://www.microsoft.com/en-us/microsoft-agent-365) can help govern agents and tools by showing what data and tools an agent can access and by supporting monitoring and inspection. Work IQ itself preserves the user's existing Microsoft 365 permissions and DLP controls, so a user only receives content they are already allowed to see.

The larger risk is what an agent can do after retrieval. An agent or multi-agent system that can read private organizational data and publish externally could leak that data even though Work IQ retrieved it correctly. Limit each agent to the tools it needs, pay particular attention to write or publishing tools, and use Agent 365 for governance and monitoring.

## How should we evaluate data retrieved by Work IQ separately from the agent using it?

📹 [10:25](https://youtube.com/watch?v=69IFV1zZEdA&t=625)

Evaluate Work IQ by data type because retrieval difficulty varies substantially. Calendar data is relatively structured, while long email threads and Teams chats are messy, conversational, and prone to missed results or speaker misattribution. A realistic test tenant should reproduce the length, slang, multiple languages, and ambiguity of production data rather than containing only clean examples.

For retrieval-specific evaluation, build a ground-truth set that maps each query to the expected source attributions. Then measure recall and precision: whether Work IQ found all expected sources, missed some, or returned irrelevant extras.

Also evaluate the complete agent separately. The agent may rewrite the user's query, select the wrong Work IQ tool, or supply incorrect arguments even when retrieval itself works well. Useful agent-level measures include groundedness, relevance, tool-selection accuracy, and argument accuracy. Repeated evaluations showed a noticeable improvement in accuracy when the agent's available tools were restricted to only those it needed. The linked [Foundry hosted-agent evaluation example](https://github.com/Azure-Samples/foundry-hosted-agentframework-demos/blob/main/scripts/quality_eval.py) demonstrates quality and tool-call evaluation.

## How can we debug a declarative agent and inspect its MCP tool calls?

📹 [17:34](https://youtube.com/watch?v=69IFV1zZEdA&t=1054)

In Microsoft 365 Copilot chat, send `-developer on`, then run the declarative agent. The developer information can show which tools were considered, which tool was invoked, and the low-level request and response. Send the corresponding command to turn developer mode off when finished. The full workflow is documented in [debugging agents in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/debugging-agents-copilot-studio).

## Can one AI agent use Work IQ across different customer tenants?

📹 [20:00](https://youtube.com/watch?v=69IFV1zZEdA&t=1200)

Technically, an external agent can call Work IQ for different tenants if it can obtain the correct delegated user access token for each target tenant. Work IQ does not support app-only tokens for its A2A, MCP, or REST APIs; every request must represent a particular user and can only retrieve what that user may access.

The application surface is therefore important. A custom web interface could use a multitenant Entra application to let each customer sign in and pass their delegated token. The one-click Foundry hosted-agent publishing flow for Teams is tenant-specific and does not by itself produce an app that customers in arbitrary tenants can install.

There is also an important architecture distinction: one running agent with simultaneous access to several tenants has a larger security risk than deploying the same agent separately into each tenant. The latter keeps each deployment and its Work IQ access scoped to that tenant.

### How can the same agent be deployed as a Teams app to multiple tenants?

📹 [24:19](https://youtube.com/watch?v=69IFV1zZEdA&t=1459)

The portal's one-click publishing path for a Foundry hosted agent was confirmed not to support this scenario. Use the standard Microsoft 365 and Teams publishing process instead. Declarative agents and Copilot Studio agents can also be exported and deployed to multiple environments or customer tenants, with each deployment configured for its own tenant.

Links shared:

* [Publish an app to the Microsoft Teams Store](https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/appsource/publish)
* [Building and deploying Microsoft hosted agents to Microsoft Teams](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/building-and-deploying-microsoft-hosted-agents-to-microsoft-teams/4540376)

## How do Copilot Studio agents relate to Foundry agents?

📹 [22:47](https://youtube.com/watch?v=69IFV1zZEdA&t=1367)

They are not mutually exclusive. A Copilot Studio agent can connect to other agents through A2A, including a Foundry agent, and Copilot Studio also has a dedicated option for connecting to Foundry agents. This allows a multi-agent architecture in which low-code agents use Power Automate and other Copilot Studio features while code-first agents use Foundry capabilities.

## What security checks can catch risky agent actions before publishing?

📹 [27:06](https://youtube.com/watch?v=69IFV1zZEdA&t=1626)

Foundry guardrails can protect the model used by an agent with checks for jailbreaks, indirect prompt injection, harmful content, protected material, PII, task adherence, and groundedness. They do not replace tool-level authorization.

Start by exposing only the tools the agent needs. If it should be read-only, allow Work IQ retrieval tools such as Ask and Fetch but not action tools. When an agent does need write actions, Agent Framework middleware can intercept proposed tool calls and enforce deterministic policies, such as rejecting an email addressed to more than a permitted number of recipients.

### Is there a static analyzer for agent risks at build time?

📹 [30:12](https://youtube.com/watch?v=69IFV1zZEdA&t=1812)

There is not yet a general-purpose static analyzer specifically for agent risks. You can start with more general risk checking. For example, the Microsoft Agent Framework team uses [Bandit](https://pypi.org/project/bandit/) and [GitHub code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/code-scanning) as automated security measures for their code, though neither looks for agent-specific vulnerabilities.

For an agent-focused review, a practical starting point is to create a coding-agent security skill based on the [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html), or point GitHub Copilot at that guidance and the codebase and ask it to identify relevant risks. This is not a replacement for a purpose-built analyzer, but it can provide a structured review while more specialized tooling is still being investigated.

## How can a team get standardized, reliable Work IQ results when each user can access different data?

📹 [32:00](https://youtube.com/watch?v=69IFV1zZEdA&t=1920)

Security takes priority over identical answers: Work IQ should not bypass source permissions merely to make every user receive the same result. Standardize access-control lists and governance for content intended to be shared broadly, while preserving legitimate differences for restricted content.

Test against the messiest permitted data and account for differences such as chat volume, conversational style, and language. For more repeatable behavior, consider lower-level Work IQ tools that do not use an LLM. This removes one source of nondeterminism and gives the application more control, but may require the application to orchestrate and parallelize calls across email, Teams, and calendar itself.

## Should an agent query SharePoint, Outlook, and Confluence through Microsoft Graph or Work IQ?

📹 [43:38](https://youtube.com/watch?v=69IFV1zZEdA&t=2618)

Use Microsoft Graph when the application needs specific raw Microsoft 365 objects and their properties, such as individual email messages. Use Work IQ when the agent needs organizational context synthesized across emails, Teams conversations, and SharePoint documents. Work IQ can return a focused, synthesized answer instead of forcing the agent to retrieve and process a large volume of raw objects, which can reduce downstream model-token usage.

Confluence is outside the Microsoft 365 data described in this answer, so it would still need its own connector or retrieval path. The choice should follow the questions the agent needs to answer rather than assuming one interface covers every source.

## Are Work IQ MCP results truncated differently in Copilot Studio and Foundry agents?

📹 [46:10](https://youtube.com/watch?v=69IFV1zZEdA&t=2770)

Work IQ exposes the same MCP server and response regardless of the consuming orchestrator. The speakers could not confirm whether Copilot Studio applies its own payload limits or truncation after receiving that response.

A Foundry hosted agent runs the developer's code in a container, so Foundry does not impose an additional hosted-agent truncation step. The model context window remains a limit, and exceeding it without management can produce an error. Developers can add summarization or tool-call middleware, or use the Agent Framework [agent harness](https://learn.microsoft.com/en-us/agent-framework/agents/harness), which includes compaction support.

## Does every user of a shared WorkMate autopilot need a separate E5 license?

📹 [49:46](https://youtube.com/watch?v=69IFV1zZEdA&t=2986)

No. A single WorkMate instance shared by several users needs one E5 license for that instance. If the scenario requires multiple WorkMate instances, each instance needs its own E5 license.

## If Work IQ summarizes data, does it still enforce each user's document permissions?

📹 [51:27](https://youtube.com/watch?v=69IFV1zZEdA&t=3087)

Yes. Work IQ evaluates access using the delegated user's token before returning content, so summarization does not expose tenant-wide data to that user. Work IQ may be capable of reaching data across the tenant, but each request only returns information the represented user is authorized to access.

## Will Work IQ behave differently in Copilot Studio, Foundry, or another agent framework?

📹 [53:01](https://youtube.com/watch?v=69IFV1zZEdA&t=3181)

Yes. Work IQ itself is the same service, but the surrounding agent harness, model, prompt, available tools, query decomposition, filtering, and middleware can all change reasoning quality, tool-call sequences, latency, and final answers. If tool use is disappointing, compare models and harnesses, narrow the tool list, improve the prompt, and evaluate each configuration instead of assuming the retrieval service alone determines the result.
