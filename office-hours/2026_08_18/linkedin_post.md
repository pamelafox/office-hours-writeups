🌐 I finally tried WebMCP live, and the experiment raised as many useful questions as it answered.

Topics we covered:

🧰 The model: A website registers structured tools with names, descriptions, and input schemas. Agents can then use those tools instead of scraping the page or guessing how to manipulate its DOM.

https://webmcp.dev/

🍕 The first test: We enabled Chrome's experimental WebMCP support, opened a pizza-maker demo, inspected its available tools in DevTools, and invoked them directly.

https://googlechromelabs.github.io/webmcp-tools/demos/pizza-maker/

🔌 The agent setup: We installed the Chrome DevTools MCP server in GitHub Copilot so the coding agent could control a live Chrome instance and discover the page's WebMCP tools.

https://github.com/ChromeDevTools/chrome-devtools-mcp

🤖 The surprising behavior: Copilot initially changed the pizza through ordinary DOM access. It called the registered WebMCP tool only after we explicitly told it to use that tool rather than the DOM.

✨ The other assistant: We also tried Chrome's Gemini-powered assistant, but tool discovery and invocation were inconsistent. WebMCP support is not yet something I would assume an agent will use automatically.

🪟 The Edge test: We successfully invoked a WebMCP tool from Edge DevTools. The origin-trial flow and whether the support came from Edge or shared Chromium functionality were still unclear.

https://learn.microsoft.com/en-us/microsoft-edge/web-platform/release-notes/151

🔒 The security boundary: Chrome DevTools MCP starts with a dedicated browser profile by default. Connecting an agent to a signed-in profile or remote-debugging session would expose much more power and needs careful isolation.

My takeaway: WebMCP is a promising contract between websites and agents. The website can declare the operations it supports, but agent clients still need a reliable way to prefer those declared tools over unrestricted browser automation.

I would love to see an agent mode that can use only the WebMCP tools exposed by a page, without also receiving full DOM access. That would make the boundary much easier for website owners and users to reason about.

Join us live every week: http://aka.ms/pythonai/oh

See the recording and questions here:
https://github.com/orgs/microsoft-foundry/discussions/280

#WebMCP #MCP #AIAgents #GitHubCopilot #WebDevelopment
