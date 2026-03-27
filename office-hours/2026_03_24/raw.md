# March 24th, 2026 Python + AI Office Hours resources

## Recording

https://www.youtube.com/watch?v=Uufh7cPUnmQ

## Copied text from slides

News:
New agent-framework release candidate for Python
Blog post: Deploy agent to cloud with azd:From code to cloud: Deploy an AI agent to Microsoft Foundry in minutes with azd - Azure SDK Blog

What I'm working on:
Porting Chat Completions API to Responses API
Foundry Agents service: run, evaluate, red teaming
Foundry IQ + Foundry agents

Upcoming events:
Microsoft AI Tour (Global): https://aitour.microsoft.com/flow/microsoft/aitour/landing/page/home
MVP summit (Redmond, WA): https://summit.microsoft.com/
MCP summit (NYC): https://events.linuxfoundation.org/mcp-dev-summit-north-america/
Azure Cosmos DB Conf (Online): https://developer.azurecosmosdb.com/conf/ 
PyCon 2026 (LA, CA): https://us.pycon.org/2026/
Posette (Online): https://posetteconf.com/2026/ 


## Open tabs

https://posetteconf.com/2026/talks/an-mcp-for-your-postgres-db/
https://github.com/Azure/azure-dev/issues/4067#issuecomment-3917772214
https://streamyard.com/teams/yfgXFbwTJEBTHs5jbsSYAiTk/broadcasts
https://github.com/pamelafox/python-foundryagent-demos/blob/main/scripts/quality_eval.py
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryagent-demos-azd,,foundry-tyaf4mbilk6jo,foundry-project-tyaf4mbilk6jo/discover/tools?registry=%2Fsubscriptions%2Fd105e4a9-bf86-4040-b97c-564af427727f%2Fresourcegroups%2Fpublic-registry-eastus%2Fproviders%2Fmicrosoft.apicenter%2Fservices%2Fconnectors-registry-prod-bl
https://ai.azure.com/allresources?tid=d91aa5af-8c1e-442c-b77c-0b92988b387b
https://pypi.org/project/agent-framework/#history
https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/
https://gist.github.com/pamelafox/e4f0817f79460c49425caf2c9706a847
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents#create-a-hosted-agent
https://github.com/Azure-Samples/azure-openai-to-responses
https://github.com/Azure-Samples/ai-model-start
https://github.com/Azure-Samples/openai-chat-backend-fastapi/pull/95/changes#diff-ffceb2a90b7e00399a465d8e90d36bec5d978025ff8784fef9c9fee4b972b7c5
https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses?view=foundry-classic&tabs=python-secure
https://luma.com/htkxoidx
https://code.visualstudio.com/docs/copilot/customization/agent-skills
https://github.com/microsoft/azure-skills
https://github.com/microsoft/waza
https://www.bing.com/search?pglt=513&q=sensei+github+shayne&cvid=3b31f30693f445d5b432be750ce3e3c4&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIICAEQ6QcY_FXSAQgzMjc4ajBqMagCALACAA&FORM=ANNAB1&PC=U531
https://github.com/spboyer/sensei
https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/
https://pypi.org/project/agent-framework/
https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents/custom/system-utility-agent
https://github.com/microsoft/agent-framework/tree/main
https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/group-chat?pivots=programming-language-python
https://github.com/orgs/microsoft-foundry/discussions/166
https://github.com/orgs/microsoft-foundry/discussions/331
https://hamel.dev/notes/llm/evals/memes/index.html#background
https://hamel.dev/blog/posts/evals-faq/
https://labondemand.com/Event/SignIn/12c943dd-ae58-44d4-b05c-98ed1e27ffa7/?room=3c1fc2ae-e4b0-443c-a4b8-bfef6f6e5eac


# Pasted chat


Pamela FoxRole icon, Microsoft — 3/24/26, 11:08 AM
https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/
Azure SDK Blog
PuiChee (PC) Chan
From code to cloud: Deploy an AI agent to Microsoft Foundry in minu...
This post walks through the full end-to-end workflow: deploying an AI agent to Microsoft Foundry, invoking it remotely, running it locally for development, and monitoring it in real time—all from Visual Studio (VS) Code.
From code to cloud: Deploy an AI agent to Microsoft Foundry in minu...
Jona M — 3/24/26, 11:10 AM
🫶  sounds good how can deployour agents into foundry.
Pamela FoxRole icon, Microsoft — 3/24/26, 11:11 AM
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents
Hosted agents in Foundry Agent Service (preview) - Microsoft Foundry
Deploy and manage containerized agents on Foundry Agent Service (preview) with managed hosting, scaling, and observability.
Hosted agents in Foundry Agent Service (preview) - Microsoft Foundry
https://github.com/Azure-Samples/azure-openai-to-responses
GitHub
GitHub - Azure-Samples/azure-openai-to-responses: Migrate your Pyth...
Migrate your Python apps from the AzureOpenAI client with Chat Completions API to the OpenAI client with Responses API. - Azure-Samples/azure-openai-to-responses
Migrate your Python apps from the AzureOpenAI client with Chat Completions API to the OpenAI client with Responses API. - Azure-Samples/azure-openai-to-responses
Jona M — 3/24/26, 11:13 AM
are you sharing your screen @Pamela Fox ,
RyanPrice1001 — 3/24/26, 11:13 AM
Lost the screen share here.
Jona M — 3/24/26, 11:14 AM
😄
Jay [CLAW],  — 3/24/26, 11:14 AM
Hehe
RyanPrice1001 — 3/24/26, 11:14 AM
( I was sure it would bounce back )
😂
Jona M — 3/24/26, 11:14 AM
now seeing it
Pamela FoxRole icon, Microsoft — 3/24/26, 11:15 AM
https://github.com/Azure-Samples/ai-model-start
GitHub
GitHub - Azure-Samples/ai-model-start: The fastest way to get start...
The fastest way to get started with any AI model — DeepSeek, Grok, Llama, Phi, GPT, and more — using stable OpenAI SDKs and the GA OpenAI/v1 Responses API. Secure, production-grade, and enterprise-...
The fastest way to get started with any AI model — DeepSeek, Grok, Llama, Phi, GPT, and more — using stable OpenAI SDKs and the GA OpenAI/v1 Responses API. Secure, production-grade, and enterprise-...
John v — 3/24/26, 11:16 AM
can you briefly explain the difference between chat completion vs response api
Nnamdi — 3/24/26, 11:18 AM
does it store on the openai server?
libis22 — 3/24/26, 11:21 AM
would you be able to briefly explain why skills MD files can be a replacement for MCP approach. not sure if this is fake news 😆 

I saw some youtube vidoes on that. Also some good information on skills MD approach?
Pamela FoxRole icon, Microsoft — 3/24/26, 11:21 AM
https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses
Use the Azure OpenAI Responses API - Microsoft Foundry
Learn how to use the Azure OpenAI Responses API to create, retrieve, and delete stateful responses with Python or REST, including streaming and tools.
Use the Azure OpenAI Responses API - Microsoft Foundry
Nnamdi — 3/24/26, 11:22 AM
Hilarious!
Pamela FoxRole icon, Microsoft — 3/24/26, 11:22 AM
https://luma.com/htkxoidx
A Celebration of Life: Model Context Protocol (2024–2026) · Luma
On March 11, Model Context Protocol was pronounced dead on Twitter, after mass exposure to curl. It was one year old.
MCP is survived by CLI, thousands of…
A Celebration of Life: Model Context Protocol (2024–2026) · Luma
Nnamdi — 3/24/26, 11:22 AM
Alive and kicking
Pamela FoxRole icon, Microsoft — 3/24/26, 11:23 AM
https://code.visualstudio.com/docs/copilot/customization/agent-skills
Use Agent Skills in VS Code
Learn how to use Agent Skills in VS Code to teach GitHub Copilot specialized capabilities that work across VS Code, GitHub Copilot CLI, and GitHub Copilot coding agent.
Use Agent Skills in VS Code
Jona M — 3/24/26, 11:25 AM
I already created some agents with skills into our repositories, it was great
https://github.com/github/awesome-copilot
GitHub
GitHub - github/awesome-copilot: Community-contributed instructions...
Community-contributed instructions, agents, skills, and configurations to help you make the most of GitHub Copilot. - github/awesome-copilot
Community-contributed instructions, agents, skills, and configurations to help you make the most of GitHub Copilot. - github/awesome-copilot
there are alot skills
Pamela FoxRole icon, Microsoft — 3/24/26, 11:26 AM
https://github.com/pamelafox/office-hours-writeups/tree/main
GitHub
GitHub - pamelafox/office-hours-writeups
Contribute to pamelafox/office-hours-writeups development by creating an account on GitHub.
Contribute to pamelafox/office-hours-writeups development by creating an account on GitHub.
https://github.com/pamelafox/presentation-writeups/tree/main/.github/skills
GitHub
presentation-writeups/.github/skills at main · pamelafox/presentat...
Skills and tools to turn my presentations into writeups - pamelafox/presentation-writeups
Skills and tools to turn my presentations into writeups - pamelafox/presentation-writeups
Nnamdi — 3/24/26, 11:28 AM
I think skills with scripts is great. The agent can then just generate glue code to get inputs and outputsin the right shape
libis22 — 3/24/26, 11:29 AM
Thank you!
gcrumrine — 3/24/26, 11:29 AM
All great stuff
Pamela FoxRole icon, Microsoft — 3/24/26, 11:32 AM
https://github.com/microsoft/azure-skills
GitHub
GitHub - microsoft/azure-skills: Official agent plugin providing sk...
Official agent plugin providing skills and MCP server configurations for Azure scenarios. - microsoft/azure-skills
GitHub - microsoft/azure-skills: Official agent plugin providing sk...
https://github.com/microsoft/waza
GitHub
GitHub - microsoft/waza: CLI / Framework for Agent Skills - create,...
CLI / Framework for Agent Skills - create, test, measure and improve skill quality and effectiveness - microsoft/waza
CLI / Framework for Agent Skills - create, test, measure and improve skill quality and effectiveness - microsoft/waza
Zach Petersen — 3/24/26, 11:32 AM
Im not sure if its been brought up here yet but FYI - https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/
FutureSearch
Supply Chain Attack in litellm 1.82.8 on PyPI
litellm version 1.82.8 on PyPI contains a malicious .pth file that harvests SSH keys, cloud credentials, and secrets on every Python startup, then attempts lateral movement across Kubernetes clusters.
Supply Chain Attack in litellm 1.82.8 on PyPI
Pamela FoxRole icon, Microsoft — 3/24/26, 11:33 AM
https://github.com/spboyer/sensei
GitHub
GitHub - spboyer/sensei: Skill for iteratively improving SKILL.md f...
Skill for iteratively improving SKILL.md frontmatter compliance using the Ralph loop pattern - spboyer/sensei
GitHub - spboyer/sensei: Skill for iteratively improving SKILL.md f...
Nnamdi — 3/24/26, 11:34 AM
By pinning you mean pinning to a pypi version bnumber or a github commit hash?
JohnRole icon, MVP — 3/24/26, 11:35 AM
both were published today 
6~8 hours ago 
https://ramimac.me/trivy-teampcp/#timeline
Pamela FoxRole icon, Microsoft — 3/24/26, 11:42 AM
https://github.com/pamelafox/python-foundryagent-demos/
GitHub
GitHub - pamelafox/python-foundryagent-demos: Various demos of Foun...
Various demos of Foundry Agents using the Python SDK - pamelafox/python-foundryagent-demos
Various demos of Foundry Agents using the Python SDK - pamelafox/python-foundryagent-demos
Dinesh [UnAI],  — 3/24/26, 11:45 AM
is there a way to host agents in AKS and use the azure AI foundry orchestrations just for no code orchestrations alone 
? I was trying to do this but seems like only hosted agents are supported right and self hosted agents are not available in the no code orchestrator. any suggestion here.
John v — 3/24/26, 11:46 AM
i started playing around multi agent systems, can you have any recommendations for evals? like Evals 101 or something. i want to understand from basics like what is going on inside before running a package or something i don't fully understand for the sake of creation.
Dinesh [UnAI],  — 3/24/26, 11:48 AM
I meant the workflows option (sequnetial, group chat) that we have in new foundry.
problem with hosted agent is, its a managed service from microsoft and billed seperately as part of foundry project.
If I do that, then i have to take care scalling as well. but foundry workflows might scale things on their own - this is what I understand
I am okay with foundry workflows, but I want agents to be in AKS instead of microsoft managed. hosted agents is still in preview and doesn't have any financial agreement
got it, thanks you.
Pamela FoxRole icon, Microsoft — 3/24/26, 11:59 AM
https://hamel.dev/blog/posts/evals-faq/
Hamel's Blog - Hamel Husain
LLM Evals: Everything You Need to Know – Hamel’s Blog - Hamel H...
A comprehensive guide to LLM evals, drawn from questions asked in our popular course on AI Evals. Covers everything from basic to advanced topics.
LLM Evals: Everything You Need to Know – Hamel’s Blog - Hamel H...
 [UnAI], 
gcrumrine — 3/24/26, 11:59 AM
If you want agents in AKS, a practical workaround is to treat them as APIs and use something like n8n or Azure Logic Apps as the visual orchestrator. That gives you the no-code / low-code workflow layer, but you would own more of the scaling, retries, auth, and observability compared to Foundry-managed agents.
Pamela FoxRole icon, Microsoft — 3/24/26, 11:59 AM
https://github.com/orgs/microsoft-foundry/discussions/331
GitHub
Python + Agents livestream series: Resources · microsoft-foundry ...
Join us for our 6-part live stream series on using Python with the Microsoft Agent Framework to build AI agents and agentic workflows! Register for the series Livestreams Tune in for the live strea...
Join us for our 6-part live stream series on using Python with the Microsoft Agent Framework to build AI agents and agentic workflows! Register for the series Livestreams Tune in for the live strea...
https://github.com/pamelafox/python-foundryagent-demos/blob/main/scripts/quality_eval.py
GitHub
python-foundryagent-demos/scripts/quality_eval.py at main · pamela...
Various demos of Foundry Agents using the Python SDK - pamelafox/python-foundryagent-demos
Various demos of Foundry Agents using the Python SDK - pamelafox/python-foundryagent-demos
mark6871 — 3/24/26, 12:00 PM
yea those logic apps confuses me alot!