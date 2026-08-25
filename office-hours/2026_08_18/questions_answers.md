# August 18, 2026 Office Hours Q&A

## How can you build production-grade AI applications while balancing safe code execution with agent autonomy?

📹 [11:02](https://youtube.com/watch?v=PfGP_fnKvy8&t=662)

For a production agent that generates or executes code, run that code in a sandbox rather than in the agent's own environment. This matters especially when the production agent has RBAC permissions or access to other resources: arbitrary generated code should not inherit those privileges. Pamela demonstrated Foundry's code interpreter, which runs Python and common data-analysis packages in an isolated environment and returns generated assets such as charts.

Coding agents used during development are a different case. VS Code and GitHub Copilot provide controls such as workspace isolation, command permissions, sandboxing, and tool approval. Pamela often uses permissive modes in a local setup she trusts, but emphasized that the right setting depends on the task. Her practical distinction was: use strong sandboxing for production code execution, and deliberately choose workspace isolation, approvals, and permissions for local agentic coding.

## Demo: Exploring WebMCP with browsers and coding agents

📹 [16:31](https://youtube.com/watch?v=PfGP_fnKvy8&t=991)

[WebMCP](https://webmcp.dev/) is a proposed browser standard that lets a web page register structured tools for AI agents. Each tool has a name, description, input schema, and implementation, much like a server-side MCP tool, but it can update the page UI or call the site's APIs from within the browser. This could give agents a more efficient and intentional way to interact with sites than scraping pages or manipulating arbitrary DOM elements.

Adoption was still early. Chrome exposed experimental WebMCP support, but agent clients did not consistently discover and call the tools automatically. In the live demo, Pamela enabled the browser feature and successfully called tools on the [WebMCP pizza demo](https://googlechromelabs.github.io/webmcp-tools/demos/pizza-maker/). GitHub Copilot could reach them through the [Chrome DevTools MCP server](https://github.com/ChromeDevTools/chrome-devtools-mcp), but it initially manipulated the DOM instead; an explicit instruction to use the registered WebMCP tool was needed.

The experiment showed both the promise and the current gap: the programmatic tool interface is useful, but broader browser and agent support is needed, ideally with a way to constrain an agent to the site's declared tools instead of giving it unrestricted DOM access.

### Could an agent generate the interface at runtime instead of developers building a fixed UI?

📹 [32:58](https://youtube.com/watch?v=PfGP_fnKvy8&t=1978)

Yes, generative UI is a related approach. Instead of hard-coding every interface, an LLM can build a UI over the available data and tools at runtime. Pamela pointed to [FastMCP's generative UI support](https://gofastmcp.com/apps/generative) for Python MCP servers as one example of that possible future.

### What security precautions should you take when giving an agent browser access?

📹 [35:55](https://youtube.com/watch?v=PfGP_fnKvy8&t=2155)

Treat browser access as a powerful permission. The Chrome DevTools MCP server starts a new Chrome instance with a dedicated profile by default, which kept the demo separate from Pamela's signed-in browser. It can be configured to connect to an existing browser through remote debugging, but doing so may expose sessions and sensitive sites. Do not browse sensitive sites while that debugging port is open, and avoid giving an agent unrestricted access to a fully authenticated profile.

Broad browser automation can also uncover and exploit application weaknesses. After discussing a report about an agent abusing a gym-booking flaw, Pamela recommended red-teaming sites before outside agents do. Her [PydanticAI Playwright agent sample](https://github.com/pamelafox/pydanticai-playwright-agent) demonstrates automated website testing and could be given more security-focused instructions; Chrome DevTools MCP can support a similar exercise.

### Does WebMCP work in Microsoft Edge?

📹 [45:11](https://youtube.com/watch?v=PfGP_fnKvy8&t=2711)

Edge is Chromium-based and Pamela was able to call a WebMCP tool through its developer tools during the session. However, the [Edge release-note flow for trying WebMCP](https://learn.microsoft.com/en-us/microsoft-edge/web-platform/release-notes/151) appeared to require an origin trial for a live site, and its registration page returned an error during the demo. Her tentative conclusion was that Edge support seemed earlier and involved more setup than Chrome support. She also could not determine whether the successful inspector test came from Edge itself or shared Chromium functionality, so agent integration still needed further testing.

## How granular should permissions be for agents that can control computers or connected services?

📹 [52:36](https://youtube.com/watch?v=PfGP_fnKvy8&t=3156)

Giving an agent access to an entire service is usually too broad, but approving every individual action creates too much friction. Pamela described an approach shown at the [WorkOS Agent Night](https://www.youtube.com/watch?v=wcYdO0v1K1k): combine deterministic policy checks with contextual evaluation, then request human approval only when an action falls outside the allowed policy.

For example, permission to use Gmail or even its send-email tool may still be excessive. A more precise rule could allow messages only to people the user has emailed before, reject distribution lists, and prompt for approval in Slack when a recipient falls outside that boundary. The principle also applies to remote-management agents such as [FlowRMM](https://flowrmm.com/): define narrow roles around the actual action and target, retain approval for exceptions, and keep an audit trail rather than treating tool access as blanket authorization.

## Announcement: MAI models are available in Microsoft Foundry

📹 [3:09](https://youtube.com/watch?v=PfGP_fnKvy8&t=189)

Pamela demonstrated MAI-Image-2.5-generated images used in synthetic PDF test data and found the photographic results strong, though fine text and small details could still be imperfect. She also deployed [MAI-Thinking-1](https://microsoft.ai/news/introducing-mai-thinking-1/) in Foundry and noted that the available deployment used Chat Completions rather than the Responses API. MAI-Code-1.1-Flash was another lower-cost option she suggested trying for plan-driven refactoring work.

## Announcement: Azure App Service can return agent-friendly Markdown

📹 [14:35](https://youtube.com/watch?v=PfGP_fnKvy8&t=875)

The [App Service Markdown preview](https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-public-preview-markdown-for-agents-in-azure-app-service/4537023) lets an enabled Windows App Service app convert its HTML response to Markdown when a request includes an `Accept: text/markdown` header. Linux support was expected later. Pamela presented this as one way to make a site easier for agents to consume, while noting that publishing developer tools in a public GitHub repository may also help models learn about them during training.

## Announcement: Grok 4.6 and Gemini 3.7 Flash arrive in GitHub Copilot

📹 [41:44](https://youtube.com/watch?v=PfGP_fnKvy8&t=2504)

GitHub Copilot added Grok 4.6 and Gemini 3.7 Flash. Pamela reviewed the [Grok 4.6 model card](https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf) and welcomed the published benchmark and safety information, but cautioned that model-card results do not replace testing with your own tasks and risk scenarios.

## Announcement: OpenSpec offers a lighter spec-driven workflow

📹 [48:14](https://youtube.com/watch?v=PfGP_fnKvy8&t=2894)

[OpenSpec](https://github.com/Fission-AI/OpenSpec) describes itself as a lighter, more iterative alternative to Spec Kit. Pamela had not tried it yet and usually works from plans rather than maintaining a formal specification, so she shared it as an option to investigate rather than a recommendation based on experience.

## Announcement: Text watermarking can alter meaning if token choices are not truly equivalent

📹 [53:22](https://youtube.com/watch?v=PfGP_fnKvy8&t=3202)

Pamela questioned an example in [Anthropic's explanation of Claude text watermarking](https://www.anthropic.com/news/claude-text-watermark) that treated "overcast" and "gray" as interchangeable. Those words can carry materially different meaning, so she argued that watermarking substitutions should only use genuinely synonymous and similarly probable tokens. She expected further research to improve on the current approach.

## Announcement: The Open Source AI Gap Map highlights underserved parts of the stack

📹 [54:37](https://youtube.com/watch?v=PfGP_fnKvy8&t=3277)

The [Open Source AI Gap Map](https://www.currentai.org/blogs/introducing-the-gap-map-v0-1) provides an interactive view of where open-source AI packages are strong and where more work is needed. Pamela suggested exploring it to identify opportunities for new tooling.

## Announcement: Pamela published a guide to safer PostgreSQL MCP servers

📹 [55:02](https://youtube.com/watch?v=PfGP_fnKvy8&t=3302)

Pamela published a [companion article about building safer MCP servers for PostgreSQL](https://blog.pamelafox.org/2026/08/building-safe-mcp-servers-for-your.html), based on her recent talk about the tradeoffs among free-form SQL, read-only access, and narrowly typed tools.
