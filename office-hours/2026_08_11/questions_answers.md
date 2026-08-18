# August 11, 2026 Office Hours Q&A

## How much Python should you know for AI, and are data structures and algorithms important for machine learning?

📹 [2:47](https://youtube.com/watch?v=lYeRqOvohxk&t=167)

Even with agentic coding, you should be able to read a program, explain what each line does, and judge whether generated code is sound. Models can produce code that reaches the goal but is overly complex, uses odd techniques such as monkey-patching, or otherwise fails to follow best practices. Recognizing those code smells requires a working understanding of Python.

Machine learning depends more directly on discrete mathematics than on data structures and algorithms, but DSA becomes important when making a system efficient. An early implementation only needs to work; production work also needs suitable data structures and algorithms to reduce execution time, memory use, and energy consumption.

## Demo: Using the chat debug view in VS Code

📹 [37:26](https://youtube.com/watch?v=lYeRqOvohxk&t=2246)

After starting a chat, open the three-dot menu in the chat header and select **Show Chat Debug View**. It exposes the LLM requests and responses, including system instructions, available skills and subagents, tool definitions, and tool-loading behavior. Pamela believed the view was available by default and did not identify a setting that had to be enabled. **Agent Debug Logs** is available from the same area and provides a higher-level debugging view.

## Does the Copilot app automatically use reviewer agents or multiple models for complex requests?

📹 [41:02](https://youtube.com/watch?v=lYeRqOvohxk&t=2462)

Not for general requests, as far as Pamela knew. Auto mode may choose a stronger model for one task, but she was not aware of a mode that automatically sends ordinary work to several models.

You can request that behavior explicitly. In the demo, Pamela named two models and asked both to propose a skill; Copilot created a subagent for each model and ran them in parallel. A repeatable skill could encode the same pattern so the model names do not have to be entered each time.

For code review, the `/review` workflow can also be given multiple models. Pamela described that as a useful first check, while finding the Copilot cloud agent's review stricter and more selective. The broader point was that parallel multi-model work is easy to ask for, but it is user-directed rather than a hidden default architecture.

## What are good practices for projects with many Markdown documentation and project-management files?

📹 [52:44](https://youtube.com/watch?v=lYeRqOvohxk&t=3164)

Pamela had not explored a mature system based on OKF, schemas, Obsidian, or automatic wikis, so she framed her advice as early experience rather than settled best practice. Product managers she knows are increasingly using agent skills to govern this kind of documentation.

In one cross-platform comparison, a skill maintained a consistent set of files such as an ease-of-use journey, working diary, and todo list. The skill defined how to initialize, link, and update those records, and was referenced at the start of each agent thread. A repository-level `AGENTS.md` can similarly tell agents to check and update documentation before publishing changes.

The central design decision is whether the files are traces primarily for later LLM analysis or documents people must comfortably read. Models tend to produce verbose, unnecessarily technical prose, so human-readable documentation needs active review and prompts to explain things more simply. Agent-maintained Markdown can preserve a great deal of detail, but that detail may need a separate summarization pass.

## Announcement: GitHub stacked pull requests entered public preview

📹 [0:48](https://youtube.com/watch?v=lYeRqOvohxk&t=48)

[Stacked pull requests](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/) organize dependent changes as a sequence of smaller PRs. They are especially useful in collaborative repositories when authors produce changes faster than reviewers can review them, because each change can remain focused without blocking later work.

## Announcement: Agent Plugins bundle skills and MCP servers

📹 [5:42](https://youtube.com/watch?v=lYeRqOvohxk&t=342)

The [Agent Plugins specification](https://agent-plugins.org/) defines a bundle that can include both agent skills and MCP servers. A plugin has a root `plugin.json` manifest, discovers skills from a skills directory, and declares MCP servers in `mcp.json`. Client-specific additions can also live alongside the portable parts; for example, VS Code hooks were not yet part of the shared specification.

The specification was developed with participation from Amazon, Cursor, Microsoft, OpenAI, and Vercel. The [canonical example repository](https://github.com/agentplugins/agent-plugins-example) is a useful starting template, and the [Agentic AI Foundation announcement](https://aaif.io/blog/from-skills-and-tools-to-portable-agent-plugins) explains the portability goal.

### Are agent plugins framework-agnostic?

📹 [9:40](https://youtube.com/watch?v=lYeRqOvohxk&t=580)

The format is intended to be a cross-client standard, but actual support depends on the client and on which plugin components it implements. A compatibility table may claim support while a particular installation path or component still has issues, so the practical answer is to test the complete plugin in every target client.

### Demo: Developing and installing a new agent plugin

📹 [13:38](https://youtube.com/watch?v=lYeRqOvohxk&t=818)

Pamela forked the example plugin, added an `mcp.json` entry for the Microsoft Learn MCP server, and tried to install the resulting bundle in several clients. The goal was to verify that one install could deliver both the MCP server and the plugin's skills. This is useful when the skills provide instructions that teach an agent how to use the accompanying tools effectively.

The results were mixed:

* VS Code's **Install Plugin from Source** flow worked. Both the MCP server and skill appeared with the plugin as their source.
* The Copilot CLI reported that the direct repository install succeeded, but the plugin did not appear in `copilot plugin list`. The CLI also warned that direct installs were deprecated in favor of marketplaces.
* The ChatGPT installation path remained unclear during the demo. A participant later reported that their plugin's skill imported but its MCP server did not.

The experiment exposed a need for clearer development-time documentation, especially for testing a plugin directly from a repository before publishing it to a marketplace. The [VS Code agent plugin documentation](https://code.visualstudio.com/docs/agent-customization/agent-plugins?plugin-marketplace=agent-customizations#_discover-and-install-plugins) includes its source-install flow.

### Do plugins reduce initial context loading?

📹 [29:32](https://youtube.com/watch?v=lYeRqOvohxk&t=1772)

Not inherently. Installing a plugin can increase available context because it adds skills and MCP tools together. Skill names and descriptions are currently placed in the initial context so the model can decide whether to load their full instructions.

Tool cost depends on the model and client. In the demo, one smaller model received every tool definition up front, while GPT-5.6 Sol received a small built-in set plus a tool-search capability for loading deferred tools only when needed. Good, descriptive tool names matter because the model uses them to decide what to search for. An Anthropic-model test showed both tool-search instructions and many tool definitions, possibly because that session used a much larger context window; Pamela presented that as a hypothesis rather than a confirmed rule. The [VS Code token-efficiency article](https://code.visualstudio.com/blogs/2026/06/17/improving-token-efficiency-in-github-copilot#_efficiency-wins-for-anthropic-models) describes related tool-search approaches.

## Announcement: Meta released the Muse Glimmer open-weight model

📹 [46:47](https://youtube.com/watch?v=lYeRqOvohxk&t=2807)

[Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) attracted interest as a new open-weight model. Pamela considered trying its [Ollama distribution](https://ollama.com/library/muse-glimmer), but its roughly 18 GB download and her earlier hardware trouble with a 20B model made local testing uncertain. An MLX build may be better suited to a Mac, but she did not complete an inference test during the session.

## Announcement: The Hugging Face incident reinforced the need for real sandboxing

📹 [50:08](https://youtube.com/watch?v=lYeRqOvohxk&t=3008)

A Black Hat talk prompted renewed discussion of the Hugging Face compromise; Simon Willison published a [timeline of the incident](https://simonwillison.net/2026/Aug/7/openai-timeline/). Pamela's practical takeaway was to verify that systems described as sandboxes are genuinely isolated. The later discussion also cautioned against turning security incidents into model marketing instead of conducting responsible retrospectives.

## Announcement: Pamela built a PydanticAI Playwright agent

📹 [50:40](https://youtube.com/watch?v=lYeRqOvohxk&t=3040)

Pamela shared a [PydanticAI Playwright agent sample](https://github.com/pamelafox/pydanticai-playwright-agent) based on Playwright support that was still awaiting release. She planned to update the sample when the upstream capability shipped.

## Announcement: Pamela is comparing Gemini and Foundry agent development

📹 [50:59](https://youtube.com/watch?v=lYeRqOvohxk&t=3059)

Pamela has been experimenting with a Gemini agent so she can compare its developer experience with Foundry. The goal is to understand both the similarities and the important differences for developers working across clouds.