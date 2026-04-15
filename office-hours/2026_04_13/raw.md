# April 13, 2026 Python + AI Office Hours resources

## Recording

https://studio.youtube.com/video/EjHmFtoR8d4/edit

## Copied text from slides

🏢 Microsoft / GitHub
• Responses API migration agent live  aka.ms/azure-openai-to-responses
• Copilot CLI remote control from mobile  github.blog/changelog/2026-04-13-remote-control-cli-sessions-on-web-and-mobile-in-public-preview/• Copilot CLI multi-model reflection reviewer github.blog/ai-and-ml/github-copilot/github-copilot-cli-combines-model-families-for-a-second-opinion
• VS Code: Agent customizations youtu.be/os2eqa69gko
• Agent-first development video series w/ VS Code + Copilot code.visualstudio.com/learn/foundations/introduction-to-agent-first-development

🌐 Industry
• DSPy + RLMs talk: reasoning models  youtube.com/watch?v=AsgDgYwj8wA
• Dropbox search relevance w/ DSPy  youtube.com/watch?v=gGGCJWbqHqc
• MCP conformance suite for servers  github.com/modelcontextprotocol/conformance
• ParseBench: doc OCR benchmark  www.llamaindex.ai/blog/parsebench

📅 Upcoming Events• Host your agents on Foundry (Online): Apr 27-30   https://aka.ms/AgentsOnFoundry/series
• Azure Cosmos DB Conf (Online): April 28 developer.azurecosmosdb.com/conf/• AgentCon (Silicon Valley): May 4   agentcon.city/silicon-valley
• PyCon US (Long Beach): May 13-19 us.pycon.org/2026
• Microsoft Build (SF): June 2-3 aka.ms/MS_Build_26_DAC26

👩‍💻 What I've Been Up To
• Migrated RAG demo to Responses API, GPT-5.4  github.com/Azure-Samples/azure-search-openai-demo
• Built /review-pr-comments skill  github.com/pamelafox/review-pr-comments
• Built /recap-my-week agent skill  github.com/pamelafox/recap-my-week
• Built /comedy-roast agent skill  github.com/pamelafox/comedy-roast-skill
• Used MCP elicitations in FastMCP  gofastmcp.com/servers/elicitation

## Open tabs

https://github.com/Azure-Samples/azure-search-openai-demo/pull/3038
https://streamyard.com/teams/yfgXFbwTJEBTHs5jbsSYAiTk/broadcasts
https://github.com/Azure-Samples/azure-openai-to-responses
https://github.com/Azure-Samples/azure-search-openai-demo/releases
https://github.blog/changelog/2026-04-13-remote-control-cli-sessions-on-web-and-mobile-in-public-preview/
https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-combines-model-families-for-a-second-opinion/
https://code.visualstudio.com/learn/foundations/introduction-to-agent-first-development
https://www.youtube.com/watch?v=os2eqa69gko
https://code.visualstudio.com/learn/foundations/introduction-to-agent-first-development
https://github.com/pamelafox/recap-my-week/blob/main/.agents/skills/recap-my-week/SKILL.md
https://github.com/microsoft/work-iq
https://www.llamaindex.ai/blog/parsebench?utm_medium=socials&utm_source=xjl&utm_campaign=2026-apr-
https://github.com/stanfordnlp/dspy
https://pamelafox.org/talks/
https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/#8-3d-unicorn
https://www.bing.com/search?qs=AS&pq=autoresearch+andr&sk=CSYN1&sc=7-17&pglt=513&q=autoresearch+andrej+karpathy&cvid=b03644c046da44c78f15423434921b40&gs_lcrp=EgRlZGdlKgcIABAAGPkHMgcIABAAGPkHMgYIARAAGEAyBggCEEUYOTIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMggIBxDpBxj8VdIBCDI5OTNqMGo3qAIAsAIA&FORM=ANNAB1&PC=U531
https://github.com/karpathy/autoresearch
https://www.anthropic.com/glasswing
https://github.com/pamelafox
https://app.ai.engineer/e/ai-engineer-worlds-fair-2026
https://developer.microsoft.com/en-us/reactor/?search=openclaw&page=1
https://developer.microsoft.com/en-us/reactor/series/S-1653/
https://www.nvidia.com/en-us/ai/nemoclaw/
https://www.npmjs.com/package/openclaw
https://github.com/modelcontextprotocol/conformance
https://github.com/pamelafox/review-pr-comments
https://vancouver.websummit.com/
https://techcrunch.com/2026/04/13/microsoft-is-working-on-yet-another-openclaw-like-agent/
https://github.com/pamelafox
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryhosted-agentframework,,ai-account-nivdj7gkpbmk2,ai-project-pf-foundryhosted-agentframework/build/agents/internal-hr-benefits-agent/build?version=5
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents#publish-hosted-agents-to-channels
https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-logs-status/

# Pasted chat

Pamela FoxRole icon, Microsoft — 11:11 AM
https://github.com/Azure-Samples/azure-openai-to-responses
GitHub
GitHub - Azure-Samples/azure-openai-to-responses: Migrate your Pyth...
Migrate your Python apps from the AzureOpenAI client with Chat Completions API to the OpenAI client with Responses API. - Azure-Samples/azure-openai-to-responses
https://github.blog/changelog/2026-04-13-remote-control-cli-sessions-on-web-and-mobile-in-public-preview/
The GitHub Blog
Allison
Remote control CLI sessions on web and mobile in public preview - G...
The Copilot CLI is no longer a purely local experience. Today we’re launching copilot --remote: With remote capabilities, you can now monitor and steer a running CLI session directly from…
Remote control CLI sessions on web and mobile in public preview - G...
Nnamdi — 11:13 AM
codex has it via chatgpt app.

also claude code has remote that llows you connect to claude code on your home machine via claude mobile app
Ash Agarwal [King],  — 11:14 AM
Hi
Pamela FoxRole icon, Microsoft — 11:15 AM
https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-combines-model-families-for-a-second-opinion/
The GitHub Blog
Nick McKenna
GitHub Copilot CLI combines model families for a second opinion
Discover how Rubber Duck provides a different perspective to GitHub Copilot CLI.
GitHub Copilot CLI combines model families for a second opinion
M.Farias — 11:15 AM
I missed a few "offices" and I’m back now...
could you please explain a bit more about WORK IQ MCP? I know you’re using it daily....
Nnamdi — 11:15 AM
codex is limited to cloud and you need to attach github repos. i might use it when i'm out at events to run tests and debug
BlackPandaChan — 11:16 AM
I've made the mistake of helping our copilot studio team and mannnnn am I tired of making topics and adaptive cards
Pamela FoxRole icon, Microsoft — 11:19 AM
https://github.com/pamelafox/recap-my-week
GitHub
GitHub - pamelafox/recap-my-week: An agent skill to recap a work week
An agent skill to recap a work week. Contribute to pamelafox/recap-my-week development by creating an account on GitHub.
GitHub - pamelafox/recap-my-week: An agent skill to recap a work week
https://github.com/microsoft/work-iq
GitHub
GitHub - microsoft/work-iq: MCP Server and CLI for accessing Work IQ
MCP Server and CLI for accessing Work IQ. Contribute to microsoft/work-iq development by creating an account on GitHub.
GitHub - microsoft/work-iq: MCP Server and CLI for accessing Work IQ
https://www.youtube.com/watch?v=os2eqa69gko
YouTube
James Montemagno
Mastering AI with VS Code's New Agent Customizations
Image
https://code.visualstudio.com/learn/foundations/introduction-to-agent-first-development
Introduction to agent-first development
Learn how harness, model, context, tools, and prompt work together for effective agent-first development in VS Code.
Introduction to agent-first development
https://www.llamaindex.ai/blog/parsebench
ParseBench: The First Document Parsing Benchmark for AI Agents
Introducing ParseBench 2,000+ human-verified pages and 167K test rules to evaluate document OCR across tables, charts, formatting, and more for AI agents. Open source.
ParseBench: The First Document Parsing Benchmark for AI Agents
Pamela FoxRole icon, Microsoft — 11:27 AM
https://github.com/stanfordnlp/dspy
GitHub
GitHub - stanfordnlp/dspy: DSPy: The framework for programming—no...
DSPy: The framework for programming—not prompting—language models - stanfordnlp/dspy
DSPy: The framework for programming—not prompting—language models - stanfordnlp/dspy
pierred7274 [OLMA],  — 11:27 AM
Thanks Pamela for the shares — VSCode is becoming more formidable with its plugins, so explaining workflow  adjustments to AI helps
Silvestre-PO — 11:27 AM
Excellent episode "Is context engineering the new RAG?" 😎 
https://www.youtube.com/watch?v=wGpJdn8frYE
YouTube
Microsoft Azure
Is context engineering the new RAG?
Image
Pamela FoxRole icon, Microsoft — 11:28 AM
https://www.youtube.com/@cmpnd_ai
YouTube
cmpnd
Building with and supporting compound AI system research and software.
Image
M.Farias — 11:28 AM
looks like another either docling or opendataloader that was released .. 😮‍💨
pablocotan — 11:28 AM
I read about people starting to use autoresearch for automatic improvement of RAG parameters tunning. Do you think that it would make sense?
Pamela FoxRole icon, Microsoft — 11:29 AM
https://www.youtube.com/watch?v=BU59cYcz4WU
YouTube
Microsoft Developer
Foundry IQ: Querying the Multi-Source AI Knowledge Bases
Image
https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/
GEPA
GEPA: optimize_anything: A Universal API for Optimizing any Text Pa...
GEPA's new API setting state-of-the-art results on optimizing any text parameter: code, prompts, agent architectures, and more. If you can measure it, you can optimize it.
GEPA: optimize_anything: A Universal API for Optimizing any Text Pa...
https://github.com/karpathy/autoresearch
GitHub
GitHub - karpathy/autoresearch: AI agents running research on singl...
AI agents running research on single-GPU nanochat training automatically - karpathy/autoresearch
AI agents running research on single-GPU nanochat training automatically - karpathy/autoresearch
M.Farias — 11:34 AM
are you excited about Mythos the new anthropic model ? 👀
Pamela FoxRole icon, Microsoft — 11:36 AM
https://www.anthropic.com/glasswing
Project Glasswing: Securing critical software for the AI era
A new initiative to secure the world’s most critical software and give defenders a durable advantage in the coming AI-driven era of cybersecurity.
Anthropic logo
pablocotan — 11:37 AM
a difficult question: I heard lately that very few people are actually using copilot in the MS365 context. What I heard is that the answers are not good or too much filtered. Do you think that this is true? Would it be something that could change without sacrifying safety?
pierred7274 [OLMA],  — 11:39 AM
Do you think the deployment of OpenClaw is a reflection that it is safe to use? I am still confused on privacy concerns but still seeing wider support for it. Are my concerns understandable or unfounded?
Nnamdi — 11:40 AM
Are you in Edge or Copilot. Mine doesn't llok like that?
pierred7274 [OLMA],  — 11:40 AM
Good that MSoft is rolling out a way to use claw with privacy
Kcloud — 11:43 AM
With MS offering the widest reach in network and platform, I believe MS will be in the centre of all automation.
Pamela FoxRole icon, Microsoft — 11:44 AM
"Deploy an secure OpenClaw (Yes, really!)"
 
If you’re like me, you’ve heard all about OpenClaw, but you’ve also heard the warnings not to run it anywhere near your laptop or real credentials. The good news is that you can run OpenClaw in a sandboxed environment that keeps your machine and accounts out of harm’s way.
In this hands-on workshop, we’ll deploy OpenClaw to a secure Azure container platform, define clear isolation boundaries, sandbox tool access, and add guardrails to prevent runaway loops. We’ll also instrument the agent with observability so you can see exactly what it’s attempting and verify that your constraints are actually working.
We provide the Azure accounts and you bring the laptop. By the end, you’ll know how to deploy and validate a secure OpenClaw sandbox, and how to apply the same safety patterns in your own environment later.
Silvestre-PO — 11:46 AM
Tomorrow Bruno and Pablo series OpenClawNet - Scaffolding + Gateway + Local Chat

https://developer.microsoft.com/es-es/reactor/events/26919/
Microsoft Reactor
OpenClawNet - Scaffolding + Gateway + Local Chat | Microsoft Reactor
Aprenda nuevas aptitudes, conozca nuevos compañeros y busque orientación profesional. Los eventos virtuales tienen lugar todo el día, así que únase a nosotros en cualquier momento y desde cualquier lugar.
Image
Tambien en español serie 
pierred7274 [OLMA],  — 11:48 AM
Thanks Pamela for the sandbox/claw explanation— helps me put a perspective to it
pablocotan — 11:48 AM
I think Bruno is challenging the Python advocates to build MS-OpenClawPy
Pamela FoxRole icon, Microsoft — 11:48 AM
https://developer.microsoft.com/en-us/reactor/?search=openclaw&page=1
Microsoft Reactor
Home | Microsoft Reactor
Ready to get started with AI and the latest technologies? Microsoft Reactor provides events, training, and community resources to help developers, entrepreneurs and startups build on AI technology and more. Join us!
Image
Silvestre-PO — 11:49 AM
NemoClaw is the "enterprise wrapper"
Pamela FoxRole icon, Microsoft — 11:50 AM
https://www.nvidia.com/en-us/ai/nemoclaw/
NVIDIA AI
NVIDIA NemoClaw: Deploy Safer AI Agents in a Single Command
Policy-based privacy & local open model deployment
NVIDIA NemoClaw: Deploy Safer AI Agents in a Single Command
https://github.com/modelcontextprotocol/conformance
GitHub
GitHub - modelcontextprotocol/conformance: Conformance Tests for MCP
Conformance Tests for MCP. Contribute to modelcontextprotocol/conformance development by creating an account on GitHub.
GitHub - modelcontextprotocol/conformance: Conformance Tests for MCP
https://github.com/pamelafox/review-pr-comments
GitHub
GitHub - pamelafox/review-pr-comments: Review comments on active PR...
Review comments on active PR and decide how to triage them - pamelafox/review-pr-comments
M.Farias — 11:53 AM
are you coming here in Vancouver for the web summit ?  🥳
Silvestre-PO — 11:54 AM
Next... https://techcrunch.com/2026/04/13/microsoft-is-working-on-yet-another-openclaw-like-agent/
TechCrunch
Julie Bort
Microsoft is working on yet another OpenClaw-like agent | TechCrunch
The new features would be geared toward enterprise customers, with better security controls than the famously risky open source OpenClaw agent.
Microsoft is working on yet another OpenClaw-like agent | TechCrunch
pablocotan — 11:55 AM
perhaps we will soon hear about the CopiClaw
unclepatrick — 11:56 AM
I have a foundry agent up and running. How do I publish it as an M365 Copilot agent?
Kcloud — 11:57 AM
Thanks for your time mam
RyanPrice1001 — 11:57 AM
Thanks Pamels! 🚀
unclepatrick — 11:57 AM
Hosted agent
BlackPandaChan — 11:57 AM
just wanted to share open-jarvis in case people were looking for nemo/openclaw alternatives: https://github.com/open-jarvis/OpenJarvis
GitHub
GitHub - open-jarvis/OpenJarvis: Personal AI, On Personal Devices
Personal AI, On Personal Devices. Contribute to open-jarvis/OpenJarvis development by creating an account on GitHub.
GitHub - open-jarvis/OpenJarvis: Personal AI, On Personal Devices
pierred7274 [OLMA],  — 11:57 AM
Pamela rocks again —thank you
BlackPandaChan — 11:57 AM
the initial release post: https://scalingintelligence.stanford.edu/blogs/openjarvis/
Scaling Intelligence Lab at Stanford University
OpenJarvis: Personal AI, On Personal Devices
Image
John v — 11:57 AM
i know your foundry deployement session coming up, is there good resources to dig deeper on AI Agents deployment?
BlackPandaChan — 11:59 AM
Thanks again Pamela, all of these sessions you've hosted have been incredible! You make it look far too easy!
unclepatrick — 11:59 AM
Yeah, I thought I saw a publish button there also the other day
Pamela FoxRole icon, Microsoft — 12:01 PM
Hosted agents overview:
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents

Deploy a hosted agent (tutorial):
https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent?tabs=bash
Hosted agents in Foundry Agent Service (preview) - Microsoft Foundry
Deploy and manage containerized agents on Foundry Agent Service (preview) with managed hosting, scaling, and observability.
Hosted agents in Foundry Agent Service (preview) - Microsoft Foundry
Deploy a hosted agent - Microsoft Foundry
Deploy your containerized agent code to Foundry Agent Service using the Azure Developer CLI or Python SDK.
Deploy a hosted agent - Microsoft Foundry
https://github.com/puicchan/seattle-hotel-agent
GitHub
GitHub - puicchan/seattle-hotel-agent
Contribute to puicchan/seattle-hotel-agent development by creating an account on GitHub.
Contribute to puicchan/seattle-hotel-agent development by creating an account on GitHub.
https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-logs-status/
Azure SDK Blog
PuiChee (PC) Chan
Azure Developer CLI (azd): Debug hosted AI agents from your terminal
When a hosted AI agent crashes, azd now shows you the status and streams live logs—right from the CLI. The azure.ai.agents extension adds two commands: azd ai agent show displays your agent's container status, health, and error details, while azd ai agent monitor streams container logs in real time.
Azure Developer CLI (azd): Debug hosted AI agents from your terminal