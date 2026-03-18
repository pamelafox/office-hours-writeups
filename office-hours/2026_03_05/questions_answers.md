# March 5, 2026 Office Hours Q&A

Note: This session was a follow-up Q&A after the [Python + Agents Session 5 livestream on human-in-the-loop workflows](https://developer.microsoft.com/en-us/reactor/events/26693/). Unfortunately, the recording only captured the first ~10 minutes, so answers beyond Q3 are reconstructed from Discord chat context only.

## What are some real-world use cases for the handoff with interaction pattern?

📹 [0:27](https://youtube.com/watch?v=FMi-SHU_55g&t=27)

The handoff pattern is designed for scenarios like a **phone tree** for customer service — where you have multiple specialist agents and the user gets routed to the right one. The key advantages over traditional phone trees:

- The **entire conversation history** gets passed between agents during handoff, so no context is lost.
- The **handoff is much faster** than waiting for a human to become available.

For handling offline users, you could use **database checkpoint storage** associated with the user. When a user revisits the site, you check if there's an in-progress workflow for them and resume it — similar to a chat history you can pick back up.

The important caveat is that handoff works best when specialist agents have **clearly defined, non-overlapping domains**. The banking assistant example works well because each agent has very specific responsibilities. The orders/returns demo was harder because those domains overlap too much, requiring significant prompt engineering to get the triage agent to route correctly.

Links shared:

* [Banking assistant sample (handoff with Foundry agents)](https://github.com/Azure-Samples/agent-openai-python-banking-assistant/tree/main/app/backend/app/agents/foundry_v2)
* [Handoff documentation](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff?pivots=programming-language-python)

## When building agents, does it make sense to use MCP or just use the underlying Python methods?

📹 [4:28](https://youtube.com/watch?v=FMi-SHU_55g&t=268)

This is an architectural decision. MCP is useful for **reusability and portability**, but you shouldn't make something an MCP server unless you plan to use it in **multiple contexts**.

Consider using MCP when:

- You want to reuse the same tools across **different agents or applications**
- You intend to use the tools in a **generic MCP client** like VS Code or Claude, where MCP capabilities beyond tools (like elicitations for asking users for more info) become valuable
- You want **portability across your organization**

If your agent just needs access to some API calls and you don't have reasons for portability, **keep them as plain tools**. When used solely from your own agents, you're likely only using the tools aspect of MCP anyway — you lose the benefit of the richer MCP protocol features like elicitations.

## How do you create a human-in-the-loop workflow in an API using checkpoints?

📹 [6:26](https://youtube.com/watch?v=FMi-SHU_55g&t=386)

Checkpoints are needed for **resuming workflows over time** (e.g., between process restarts or when a human is offline). If the human is present the whole time, you don't necessarily need checkpoints.

For workflows that occasionally need human intervention, the pattern is:

1. **Run the workflow** and detect when human input is needed
2. **Save a checkpoint** and exit when no human is available
3. Use an **inbox-style UI** to surface all paused workflows that need action
4. **Resume from checkpoint** once the human takes action

An example of this pattern is [LangChain's agent inbox](https://github.com/langchain-ai/agent-inbox), a React app that finds all interrupted agent threads and surfaces them for human action. A similar approach could be built for Agent Framework using database checkpoint storage, tracking workflow completion status, and displaying pending workflows.

There's also the [DBOS durable execution approach](https://docs.dbos.dev/python/examples/agent-inbox) for human-in-the-loop workflows, which handles durability differently.

## How do we find out what executors in a sequential workflow send to another executor?

You can monitor the messages using the events from a streaming worklow execution. When you run a workflow with `stream=True`, you get an event stream that includes messages sent between executors, and includes each time an output is added to the workflow outputs. Once the workflow ends, query `get_outputs()` for the final list of outputs.

Typically, the executors _inside_ a workflow will use `send_message`, and the final executor will use `yield_output`, but executors can also yield outputs along the way (in addition to sending messages).

## How do we protect our API keys and tokens from GitHub Copilot agent mode?

GitHub Copilot agent mode has access to your code, so you need to be careful about how you store secrets. It will generally not edit a `.env` file if you have one, but it can read from it and potentially expose secrets in generated code or during screen sharing.

- Consider using **keyless authentication** (like Azure managed identity / DefaultAzureCredential) to avoid needing API keys at all.
- For **local development**, storing tokens in a `.env` file (excluded via `.gitignore`) is acceptable. If you're uncomfortable with that, consider using a local secrets manager (e.g. the Python `keyring` library for Mac or [Infisical](https://github.com/Infisical/infisical).)
- For **production**, use a secrets manager like Azure Key Vault.
- To avoid **accidentally exposing secrets during screen sharing**, keep `.env` files closed and consider the VS Code [Camouflage extension](https://marketplace.visualstudio.com/items?itemName=KnisterPeter.camouflage). You can also move secrets to the very end of the file, after many blank lines, to reduce the chance of accidental exposure.

## What is your opinion on agent-skills (experimental) vs using workflows in Agent Framework?

Pamela has an example of using Microsoft Agent Framework with skills in her [presentation write-up repository](https://github.com/pamelafox/presentation-writeups/blob/main/agent_skills.py). Typically she uses GitHub Copilot agent with the repo's skills, but for further automation, she can use the Agent Framework agent with the same skills. This way, the skills can be shared between both approaches.

When an agent is given skills, it can be very creative and flexible in how it uses them, which is great for open-ended tasks. However, if you have a more structured process in mind, using the Agent Framework with defined workflows can give you more control over the orchestration and flow of the task.

Check the [MAF documentation on skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills?pivots=programming-language-python) for more examples and a good discussion of the pros and cons of each approach.