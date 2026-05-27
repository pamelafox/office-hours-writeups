# May 26th Weekly Python + AI Office Hours

## Recording

https://www.youtube.com/watch?v=mZ-WgdquFIE

## Slide content


🏢 Microsoft / GitHub
• Azure OpenAI Assistants API retiring Aug 26  learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/assistants
• Migrate Assistants → Foundry Agent Service  learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/assistants
• MAI models: image, voice, transcribe in Foundry  microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/
• Responses API: new standard for Azure OpenAI  learn.microsoft.com/en-us/azure/ai-services/openai/how-to/responses
• GitHub MCP server: reply to inline PR comments  github.com/github/github-mcp-server/pull/1856
• GitHub Copilot model menu refined for consistency github.blog/changelog/2026-05-20-updates-to-available-models-in-copilot-on-web/
• agent-framework: Monty as CodeAct provider  github.com/microsoft/agent-framework/pull/5915

🌐 Industry
• Google Antigravity 2.0: IDE → agent orchestration  techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/
• OpenAI Codex: now on mobile + Chrome extension  developers.openai.com/codex/app/chrome-extension
• Anthropic Project Glasswing: Claude finds bugs  anthropic.com/research/glasswing-initial-update
• MCP 2026-07-28 RC: now stateless, no session id  github.com/modelcontextprotocol/modelcontextprotocol
• WorkOS auth.md: open agent registration protocol  workos.com/blog/agent-registration-with-auth-md

👩‍💻 What I've Been Up To
• Blog: PyCon US 2026 reflections  blog.pamelafox.org/2026/05/pycon-2026-reflections.html
• Talk: AI-powered presentation workflow  pamelafox.github.io/ai-powered-presentation-workflow/
• Tutorial slides: MCP server at PyCon 2026  pamelafox.github.io/pycon2026-mcp-tutorial/
• Video: Claude Sonnet + agent-framework demo  youtube.com/watch?v=LYwV8IQVRIo
• Skill: GitHub MCP PR review comments  github.com/pamelafox/review-pr-comments• Gmail MCP servergithub.com/mattgotteiner/gmail-local-mcp

📅 Upcoming events
• Microsoft Build SF: Jun 2–3, 2026 build.microsoft.com
• Posette (Virtual): Jun 16–18, 2026  posetteconf.com/2026/
• Agents League (Virtual): June 4-14)
info.microsoft.com/Agents-League-Hackathon-Registration.html


## Open tabs

https://gist.github.com/saxenanurag/a63f4c801709e4100880eed75e21e4c5
https://streamyard.com/324j8uf53v
https://github.com/orgs/microsoft-foundry/discussions/280
https://github.com/microsoft/agent-framework/releases/tag/python-1.6.0
https://pypi.org/project/agent-framework/#history
https://github.com/pamelafox/review-pr-comments/blob/main/.agents/skills/review-pr-comments/SKILL.md
https://learn.microsoft.com/en-us/azure/foundry-classic/openai/concepts/assistants
https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate?tabs=python#migrate-classic-agents-to-new-agents
https://github.com/pamelafox/pycon2026-mcp-tutorial/issues/3
https://github.com/pamelafox/pycon2026-mcp-tutorial/pull/4
https://docs.github.com/en/copilot?articles-filter=sub-agent
https://code.claude.com/docs/en/github-actions
https://www.bing.com/search?q=github+copilot+CLI+hooks&cvid=ffc1bc56a22f424589e76ab4cd30048a&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEAyCAgJEOkHGPxV0gEIMzA0MWowajeoAgCwAgA&FORM=EDGUC2&PC=U531&source=chrome.ob
https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks
https://x.com/dsp_/status/2057780712187580924
https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
https://workos.com/blog/agent-registration-with-auth-md
https://github.com/mattgotteiner/gmail-local-mcp
https://github.com/microsoft/Build26-LAB532/blob/main/notebooks/part3-fabric-iq-to-kb.ipynb
https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/app/backend/Dockerfile
https://gofastmcp.com/integrations/openapi
https://docs.github.com/en/copilot/reference/ai-models/model-hosting
https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
https://www.nsa.gov/Portals/75/documents/Cybersecurity/CSI_MCP_SECURITY.pdf?ver=bmgiSbNQLP6Z_GiWtRt6bg%3d%3d
https://www.caisconf.org/
https://www.openhands.dev/
https://github.com/NVIDIA/OpenShell
https://www.bing.com/search?q=docker+sandbox+create&cvid=19bf2f3590184eb9a7423ad960445d1f&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyCAgDEOkHGPxV0gEINDEyNGowajeoAgCwAgA&FORM=EDGUC2&PC=U531&source=chrome.ob
https://docs.docker.com/ai/sandboxes/
https://docker.github.io/docker-agent/configuration/models/

## Pasted chat


https://github.com/microsoft/agent-framework/releases/tag/python-1.6.0
GitHub
Release python-1.6.0 · microsoft/agent-framework
[1.6.0] - 2026-05-21
Added

agent-framework-core: Shell tool with support for local and Docker execution (#5664)
agent-framework-monty: New Monty-backed CodeAct provider package (#5915)
agent-frame...
pablocotan — 11:12 AM
perfect!
VK — 11:12 AM
Yes
Pamela FoxRole icon, Microsoft — 11:14 AM
https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate?tabs=python#migrate-classic-agents-to-new-agents
Migrate to the new Foundry Agent Service - Microsoft Foundry
Learn how to migrate from the Assistants API and classic agents to the new Foundry Agent Service, including threads to conversations, runs to responses, and updated SDK patterns.
Migrate to the new Foundry Agent Service - Microsoft Foundry
adam — 11:14 AM
How's Github Copilot desktop app so far? 

I wonder whether the industry has mostly settled on the desktop UI - all desktop apps seem to be quite similar at the moment: Copilot Agents, Codex desktop, Claude desktop, Cursor agent window, Jetbrains Air, Antigravity, etc
pablocotan — 11:18 AM
can you create sub-agents with the github copilot desktop app?
and the very not-ready-yet-to-use  atigravity-CLI
adam — 11:20 AM
What do you mean by GH Copilot Coding Agent? The web based one?
pablocotan — 11:21 AM
And OpenCode, with the freedom to use any of those models
Nnamdi — 11:21 AM
there is also this ie claude code in the browser
Image
pablocotan — 11:22 AM
yes, both versions for OpenCode
JohnRole icon, MVP — 11:23 AM
Claude has coding agents too
pablocotan — 11:23 AM
And we can combine them using the CLIs in headless mode
JohnRole icon, MVP — 11:23 AM
you can @claude on github and it will work on it in the cloud 
it's claude github app 
https://code.claude.com/docs/en/github-actions
pablocotan — 11:24 AM
another argument to use the CLI versions is the possibility to kind of modify the harnesses using open-source plugins
adam — 11:24 AM
Opencode - interesting. So it might be similar-ish to Jetbrains Air, which also allows 3rd party agents/subscriptions as well as their own Junie agent
pablocotan — 11:26 AM
GSD, SUperpowers, teams of agents, etc.Using the hooks of the CLI coding-assistants
can you get access to the hooks of the github copilot desktop app?
Pamela FoxRole icon, Microsoft — 11:30 AM
https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
Model Context Protocol Blog
The 2026-07-28 MCP Specification Release Candidate
The release candidate for the next Model Context Protocol (MCP) specification is now available: a stateless protocol core, the Extensions framework, Tasks, MCP Apps, authorization hardening, and a formal deprecation policy.
The 2026-07-28 MCP Specification Release Candidate
https://workos.com/blog/agent-registration-with-auth-md
Agent Registration with Auth.md — WorkOS
Introducing auth.md — an open protocol that lets agents register for your service.
Agent Registration with Auth.md — WorkOS
https://github.com/mattgotteiner/gmail-local-mcp
GitHub
GitHub - mattgotteiner/gmail-local-mcp: Local stdio MCP server for ...
Local stdio MCP server for Gmail. Contribute to mattgotteiner/gmail-local-mcp development by creating an account on GitHub.
Local stdio MCP server for Gmail. Contribute to mattgotteiner/gmail-local-mcp development by creating an account on GitHub.
JohnRole icon, MVP — 11:33 AM
are you working on any new samples?
will you incroporate mcp somehow here?
pablocotan — 11:37 AM
do all the "official" models used through github copilot (any version) are being protected against prompt injection? Is there documentation about that? If they are, are they protected as when we configure out own agents in Foundry? 
JohnRole icon, MVP — 11:37 AM
maybe completly separate services connecting with each other
Pamela FoxRole icon, Microsoft — 11:41 AM
https://docs.github.com/en/copilot/reference/ai-models/model-hosting
GitHub Docs
Hosting of models for GitHub Copilot - GitHub Docs
Learn how different AI models are hosted for GitHub Copilot.
Image
pablocotan — 11:41 AM
I have started to worry about the requests we make with CLI or desktop assistants that get information from anywhere (emails, social networks, web search...)
Silvestre-PO — 11:43 AM
By the way, Security concerns in MCP design, implementation, and 
practices by NSA

https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/
Nnamdi — 11:44 AM
How likely is it that the US governemnt will limit access to chinese open source models because of the distillation going on?
Pamela FoxRole icon, Microsoft — 11:44 AM
https://www.caisconf.org/
ACM Conference on AI and Agentic Systems — ACM CAIS 2026
ACM CAIS 2026 — the ACM Conference on AI and Agentic Systems. Rigorous, reproducible research on compound AI architectures, optimization, and deployment. May 26–29, 2026 in San Jose.
ACM Conference on AI and Agentic Systems — ACM CAIS 2026
pablocotan — 11:45 AM
I am starting to think that OpenShell (or similar) makes more and more sense, to use it for each of our agents dedicated to specific tasks. It seems to me that we can control better and with more transparency that just using cloud very high-level options
Pamela FoxRole icon, Microsoft — 11:45 AM
https://www.openhands.dev/
OpenHands
OpenHands | The Open Platform for Cloud Coding Agents
Meet OpenHands, the open-source, model-agnostic platform for cloud coding agents. Automate real engineering work securely and transparently. Build faster with full control.
OpenHands | The Open Platform for Cloud Coding Agents
pablocotan — 11:46 AM
not that one
from NVIDIA
Pamela FoxRole icon, Microsoft — 11:46 AM
https://github.com/NVIDIA/OpenShell
GitHub
GitHub - NVIDIA/OpenShell: OpenShell is the safe, private runtime f...
OpenShell is the safe, private runtime for autonomous AI agents. - NVIDIA/OpenShell
GitHub - NVIDIA/OpenShell: OpenShell is the safe, private runtime f...
pablocotan — 11:46 AM
it uses kernel-level controls. Works with any agent
https://docs.nvidia.com/openshell/sandboxes/policies
Customize Sandbox Policies | NVIDIA OpenShell
Apply, iterate, and debug sandbox network policies with hot-reload on running OpenShell sandboxes.
Ahmed — 11:50 AM
I am new here, what exactly happens in these calls?
Nnamdi — 11:50 AM
the whole raison d'etre of agents is access to your folders, email, web serach, news api's, social media incl github. If you block these off then it takes away a lot of the attraction
Pamela FoxRole icon, Microsoft — 11:52 AM
https://docs.docker.com/ai/sandboxes/
Docker Documentation
Docker Sandboxes
Run AI coding agents in isolated environments
Docker Sandboxes
Z [LABS],  — 11:54 AM
How about https://docker.github.io/docker-agent/
Docker Agent Docs
Docker Agent — Run AI agents from YAML, like containers
Run AI agents like containers. Define them in YAML, share them through any OCI registry, and run them anywhere.
Good point
"Yes — a Docker Agent can be used with Microsoft Foundry, but it depends on how you deploy and configure it. Foundry’s Hosted Agents are designed to run containerized AI agents that can call Foundry models and tools, and Docker Agent is a framework for building and running such agents"