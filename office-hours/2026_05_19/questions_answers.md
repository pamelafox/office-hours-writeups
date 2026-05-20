## Which TTS model do you recommend using locally (offline)?

📹 [22:32](https://youtube.com/watch?v=p9qYDwLWcJs&t=1352)

Pamela hasn't used local TTS models much herself, but noted that most people recommend Whisper or using Whisper inside some kind of harness for offline speech. She mentioned that she just got a computer with 64 GB of RAM, so she's hoping to start experimenting more with local models. She also checked [CanIRun.ai](https://canirun.ai) but it doesn't seem to list TTS models. She encouraged others in the chat to share their recommendations for offline TTS.

## How can I experiment with generative UI / A2UI?

📹 [24:08](https://youtube.com/watch?v=p9qYDwLWcJs&t=1448)

For generative UI, there are a few options depending on what you're building:

- **FastMCP** already supports [generative UI](https://gofastmcp.com/apps/generative), where an MCP server can respond to requests with UI components on the fly (constrained to prefab components for safety). This is a good starting point if you're building MCP servers that output apps.

- **AG-UI** is the protocol that [Agent Framework (MAF)](https://github.com/microsoft/agent-framework/tree/main/python/packages/ag-ui) integrates with for front-end/back-end agent communication.

- **A2UI** (from Google) is a declarative, LLM-friendly generative UI spec. Support for A2UI in Agent Framework Python is [currently in progress](https://github.com/microsoft/agent-framework/discussions/2954) — an engineer on the MAF team confirmed this in a discussion thread. No PR has been pushed yet, so subscribing to that discussion is recommended.

- **CopilotKit** is the open-source team behind the AG-UI protocol. There's a [DeepLearning.ai course](https://www.deeplearning.ai/courses/build-interactive-agents-with-generative-ui) on building interactive agents with generative UI using CopilotKit that could be a good learning resource.

Links shared:

* [FastMCP Generative UI](https://gofastmcp.com/apps/generative)
* [AG-UI in Agent Framework](https://github.com/microsoft/agent-framework/tree/main/python/packages/ag-ui)
* [A2UI discussion in Agent Framework](https://github.com/microsoft/agent-framework/discussions/2954)
* [AG-UI Generative UI specs](https://docs.ag-ui.com/concepts/generative-ui-specs)
* [CopilotKit](https://www.copilotkit.ai/)
* [DeepLearning.ai: Build Interactive Agents with Generative UI](https://www.deeplearning.ai/courses/build-interactive-agents-with-generative-ui)

## What is Pydantic Monty and how can it be used with agents?

📹 [29:46](https://youtube.com/watch?v=p9qYDwLWcJs&t=1786)

[Pydantic Monty](https://github.com/pydantic/monty) is a sandboxed Python runtime (re-implemented in Rust) that lets you run a subset of Python safely. There are two main use cases for agents:

**1. Code mode (reducing tool-calling overhead):** Instead of the traditional back-and-forth of many individual tool calls, the LLM writes Python code that calls tools as if they were functions. This code can do sequences, for loops, async gathers, etc. — all in one shot. This dramatically reduces tokens and round trips. If you're using Pydantic AI, it's one line of code to add Monty as a code mode backend. For Agent Framework, there's a [PR in review](https://github.com/microsoft/agent-framework/pull/5915) that adds Monty as a CodeAct provider.

**2. Code execution tool:** You can add a code execution tool to your agent that uses Monty for fast, safe computation. For example, giving an agent the ability to do date/time math or calculations without relying on the LLM's (often unreliable) arithmetic. You could even have two code execution tools: a fast Monty tool for datetime/math, and a slower hosted code interpreter (with access to pandas, numpy, etc.) for more complex tasks.

Samuel Colvin (Pydantic's creator) gave an extended talk about Monty at PyCon US, explaining how they re-implemented Python in Rust. There's also a "Hack Monty" competition with a $10,000 bounty to find security issues, which helps validate the sandbox's safety.

Links shared:

* [Pydantic Monty](https://github.com/pydantic/monty)
* [Agent Framework Monty PR](https://github.com/microsoft/agent-framework/pull/5915)
* [Samuel Colvin's PyCon talk](https://us.pycon.org/2026/schedule/presentation/27/)
* [AgentCon talk: Your agent needs a sandbox, not a desert](https://www.youtube.com/watch?v=u5X7TlmR0sY)

## Can I use GitHub Copilot (VS Code) with a model deployed in Foundry?

📹 [38:22](https://youtube.com/watch?v=p9qYDwLWcJs&t=2302)

Yes! You can add Foundry models to VS Code via **Manage Language Models** (in the model picker dropdown). This creates a `chatLanguageModels.json` file in your user settings directory. The [main documentation](https://code.visualstudio.com/docs/copilot/customization/language-models) covers the Azure vendor option, which works for OpenAI models. For non-OpenAI models (like Claude), you need VS Code Insiders and the [custom endpoint](https://github.com/microsoft/vscode-docs/blob/vnext/docs/copilot/customization/language-models.md#add-a-custom-endpoint-model) vendor.

During the session, Pamela had trouble getting the "Azure" provider option to work. After live-debugging with attendees and reading the [VS Code source code](https://github.com/microsoft/vscode/blob/f5af6b8a1d3eb8107cc2e2a2973f36501c114ae7/extensions/copilot/src/extension/byok/vscode-node/azureProvider.ts#L8), she discovered the Azure provider only recognizes URLs containing `models.ai.azure.com` or `openai.azure.com`. This means it works for Azure OpenAI models, but not for non-OpenAI models deployed on Foundry (which use `services.ai.azure.com`). This is what she got working after the livestream:

**Option 1: Azure vendor (for Azure OpenAI models only)**

For OpenAI models on Foundry, you can use `"vendor": "azure"` with either key-based or Entra authentication. The URL should be just the base endpoint (without path suffixes):

```json
{
    "name": "Work Foundry",
    "vendor": "azure",
    "models": [
        {
            "id": "gpt-5.2",
            "name": "gpt-5.2-work",
            "url": "https://YOUR-ACCOUNT.openai.azure.com",
            "toolCalling": true,
            "vision": true,
            "maxInputTokens": 128000,
            "maxOutputTokens": 16000
        }
    ]
}
```

**Option 2: Custom endpoint vendor (for ANY model, including non-OpenAI — requires API key)**

For non-OpenAI models (like Claude) or if you want a single configuration for all models, use `"vendor": "customendpoint"` instead, which works with any URL. Note that this option requires an API key and does not support keyless/Entra authentication:

```json
{
    "name": "Personal Foundry",
    "vendor": "customendpoint",
    "apiKey": "${input:chat.lm.secret.YOUR_SECRET_ID}",
    "apiType": "responses",
    "models": [
        {
            "id": "gpt-5.4",
            "name": "gpt-5.4-mine",
            "url": "https://YOUR-FOUNDRY.openai.azure.com/openai/v1/responses",
            "apiType": "responses",
            "toolCalling": true,
            "vision": true,
            "maxInputTokens": 128000,
            "maxOutputTokens": 16000
        },
        {
            "id": "claude-sonnet-4-6-DEPLOYMENT",
            "name": "claude-sonnet-mine",
            "url": "https://YOUR-FOUNDRY.services.ai.azure.com/anthropic/v1/messages",
            "apiType": "messages",
            "toolCalling": true,
            "vision": true,
            "maxInputTokens": 128000,
            "maxOutputTokens": 16000
        }
    ]
}
```

Key details:
- Use `"apiType": "responses"` for OpenAI models and `"apiType": "messages"` for Anthropic models
- The `id` should match your deployment name in Foundry
- The URL format differs: `openai.azure.com/openai/v1/responses` for OpenAI models, `services.ai.azure.com/anthropic/v1/messages` for Anthropic models

Links shared:

* [VS Code: Language Models documentation](https://code.visualstudio.com/docs/copilot/customization/language-models)
* [VS Code custom endpoint docs (Insiders)](https://github.com/microsoft/vscode-docs/blob/vnext/docs/copilot/customization/language-models.md#add-a-custom-endpoint-model)
* [VS Code Azure provider source code](https://github.com/microsoft/vscode/blob/f5af6b8a1d3eb8107cc2e2a2973f36501c114ae7/extensions/copilot/src/extension/byok/vscode-node/azureProvider.ts#L8)
* [Related VS Code issue](https://github.com/microsoft/vscode/issues/294841)

## Announcements

📹 [0:00](https://youtube.com/watch?v=p9qYDwLWcJs&t=0)

**PyCon US recap:**

- Pamela ran an [MCP tutorial](https://pamelafox.github.io/pycon2026-mcp-tutorial/) covering elicitations and MCP apps (newer parts of the protocol), with [self-paced exercises](https://github.com/pamelafox/pycon2026-mcp-tutorial#exercises) for learning to build MCP servers in Python.
- She gave a talk at the EduSummit about [making slides using Reveal.js and GitHub Copilot](https://pamelafox.github.io/ai-powered-presentation-workflow/), with tips on using VS Code's integrated browser for rapid front-end iteration. The related [presentation-skills repo](https://github.com/pamelafox/presentation-skills) contains skills for AI agents to process presentations.

**GitHub Copilot App (desktop technical preview):**

📹 [4:57](https://youtube.com/watch?v=p9qYDwLWcJs&t=297)

The new [GitHub Copilot App](https://github.com/github/app) is a desktop app wrapping the Copilot CLI, available for Enterprise and Business subscribers. Key features demonstrated:
- Better UI for viewing sessions, repos, inline diffs, and PRs
- MCP server and skills integration (same as CLI)
- Agent merge for automated CI fixing
- **Workflows**: scheduled personal automations (daily issue triage, weekly recaps, etc.) with a gallery of templates
- Web search tool built in
- Repo-less chats for general questions

**New MAI models in Foundry:**

📹 [11:46](https://youtube.com/watch?v=p9qYDwLWcJs&t=706)

Three new MAI models are available:
- **MAI-Image-2E**: An image generation model that excels at facial likeness preservation and photo-realistic output. Pamela demonstrated using it at the PyCon booth to generate images from source photos. The [model card](https://microsoft.ai/pdf/MAI-Image-2-Model-Card.pdf) details evaluation categories, red teaming, and training data.
- **MAI-Transcribe-1**: For transcription
- **MAI-Voice-1**: For voice generation

Links shared:

* [MAI models announcement](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/)
* [MAI-Image-2 Model Card](https://microsoft.ai/pdf/MAI-Image-2-Model-Card.pdf)
* [MAI-Image-2 Data Summary](https://microsoft.ai/pdf/MAI-Image-2-Data-Summary.pdf)
