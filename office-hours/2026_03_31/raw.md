# March 31st, 2026 Python + AI Office Hours resources


## Recording

https://www.youtube.com/watch?v=02InkgJM8Do

## Copied text from slides

News:
New agent-framework release candidate for Python (rc6)
Copilot requires opt-out if you don't want it to train on your chats: https://github.blog/changelog/2026-03-25-updates-to-our-privacy-statement-and-terms-of-service-how-we-use-your-data/

What I'm working on:
FastMCP + Entra auth options
Porting Chat Completions API to Responses API
Foundry hosted agent series!

Upcoming events:
Microsoft AI Tour (Global): https://aitour.microsoft.com/flow/microsoft/aitour/landing/page/home
MCP summit (NYC): https://events.linuxfoundation.org/mcp-dev-summit-north-america/
Azure Cosmos DB Conf (Online): https://developer.azurecosmosdb.com/conf/ 
PyCon 2026 (LA, CA): https://us.pycon.org/2026/
Posette (Online): https://posetteconf.com/2026/ 
Code with Claude (SF, NY, Tokyo): https://claude.com/blog/code-with-claude-san-francisco-london-tokyo 
Build 2026 (SF): https://build.microsoft.com/ 

## Open tabs

https://app.ai.engineer/e/ai-engineer-worlds-fair-2026/speaker-registration
https://github.com/Azure-Samples/azure-search-openai-demo/pull/3021#pullrequestreview-4031945099
https://github.com/Azure-Samples/python-mcp-demos/pull/55
https://streamyard.com/teams/yfgXFbwTJEBTHs5jbsSYAiTk/broadcasts
https://github.com/pamelafox/azure-cosmosdb-identity-aware-mcp-server
https://github.blog/ai-and-ml/github-copilot/building-ai-powered-github-issue-triage-with-the-copilot-sdk/
https://pypi.org/project/agent-framework/#description
https://bredbox.app/saves
https://sql-benchmark.nicklothian.com/?utm_source=breadbox#best-for-self-hosting
https://www.canirun.ai/
https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/#1-coding-agent-skills
https://developer.microsoft.com/en-us/reactor/series/S-1655/?wt.mc_id=slidescontent_S-1655_webinar_reactor
https://github.com/spboyer/sensei
https://github.com/microsoft/waza
https://github.com/microsoft/GitHub-Copilot-for-Azure
https://github.com/microsoft/azure-skills
https://www.linkedin.com/feed/update/urn:li:activity:7444615065921646592/
https://arxiv.org/pdf/2603.21687
https://www.bing.com/search?q=azure%20ai%20vision%20API%20integration%20guide&qs=n&form=QBRE&sp=-1&ghc=2&lq=0&pq=azure%20ai%20vision%20api%20integration%20guide&sc=12-37&sk=&cvid=2CECDCDD31F246CB92637A15B7F2F08E
https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/migration-options
https://learn.microsoft.com/en-us/azure/search/cognitive-search-skill-vision-vectorize
https://learn.microsoft.com/en-us/azure/search/cognitive-search-skill-vision-vectorize
https://github.com/orgs/microsoft-foundry/discussions/280
https://github.com/modelcontextprotocol/experimental-ext-skills
https://hamel.dev/blog/posts/revenge/?ck_subscriber_id=3545905957&utm_source=convertkit&utm_medium=email&utm_campaign=New%20Blog%20Post:%20The%20Revenge%20of%20the%20Data%20Scientist%20-%2021166563
https://www.youtube.com/@Pydantic
https://arxiv.org/abs/2504.19874
https://github.com/Azure-Samples/nim-on-azure-serverless-gpus-demos?tab=readme-ov-file
https://learn.microsoft.com/en-us/azure/container-apps/serverless-gpu-nim?tabs=bash
https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/
https://techcommunity.microsoft.com/blog/appsonazureblog/bulletproof-agents-with-the-durable-task-extension-for-microsoft-agent-framework/4467122
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents#create-a-hosted-agent
https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/virtual-networks
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents#limits-pricing-and-availability-preview
https://x.com/pierceboggan
https://blog.pamelafox.org/2025/08/how-i-learn-about-generative-ai.html

# Pasted chat


Justin Trantham [FlowDevs.io] [FLOW],  — 11:07 AM
:pepe_wave:
:clippy:
BlackPandaChan — 11:08 AM
👋
Pamela FoxRole icon, Microsoft — 11:10 AM
https://github.blog/changelog/2026-03-25-updates-to-our-privacy-statement-and-terms-of-service-how-we-use-your-data/
The GitHub Blog
Allison
Updates to our Privacy Statement and Terms of Service: How we use y...
Hey GitHub Community, We’ve made some important updates to our Privacy Statement and Terms of Service to keep you informed about how we handle your data. Notably, from April 24…
Updates to our Privacy Statement and Terms of Service: How we use y...
https://github.com/orgs/community/discussions/188488
GitHub
FAQ: Privacy Statement update on Copilot data use for model trainin...
Hello GitHub Community👋 We’re sharing an update to our Privacy Statement and Terms of Service about how we use personal data to develop, improve, and secure GitHub products and services, including ...
FAQ: Privacy Statement update on Copilot data use for model trainin...
John v — 11:10 AM
what is GA(Generally Available) version? can't we not install agent framework ?
gotham64 — 11:13 AM
Your screen sharing stopped
Pamela FoxRole icon, Microsoft — 11:14 AM
https://sql-benchmark.nicklothian.com/?utm_source=breadbox
LLM SQL Benchmark
A fast benchmark for Agentic Natural Language to SQL Generation.
LLM SQL Benchmark
https://www.canirun.ai/
CanIRun.ai
CanIRun.ai — Can your machine run AI models?
Detect your hardware and find out which AI models you can run locally. GPU, CPU, and RAM analysis in your browser.
CanIRun.ai — Can your machine run AI models?
https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything
GEPA
GEPA: optimize_anything: A Universal API for Optimizing any Text Pa...
GEPA's new API setting state-of-the-art results on optimizing any text parameter: code, prompts, agent architectures, and more. If you can measure it, you can optimize it.
GEPA: optimize_anything: A Universal API for Optimizing any Text Pa...
pablocotan — 11:17 AM
do you know if anyone in Microsoft has already tested TurboQuant for local models?
it could be useful for foundry local
Pamela FoxRole icon, Microsoft — 11:18 AM
https://aka.ms/AgentsOnFoundry/series
Microsoft Reactor
Host your agents on Foundry | Microsoft Reactor
Attend Reactor Event Series for on-going opportunities to learn, connect, and build. Expand your skillset.
Image
Justin Trantham [FlowDevs.io] [FLOW],  — 11:19 AM
Have you used the work iq mcp server?
🗼
We can only see browser
pablocotan — 11:23 AM
does Microsoft have anything to check agent-skills for security and effectiveness? I imagine something that would allow users to upload the agent-skill folder, and let it be tested (for foundry, or for copilot studio or other no/low-code tool)
John v — 11:23 AM
is "Host your agent series" not on consecutive days?
Pamela FoxRole icon, Microsoft — 11:25 AM
https://github.com/spboyer/sensei
GitHub
GitHub - spboyer/sensei: Skill for iteratively improving SKILL.md f...
Skill for iteratively improving SKILL.md frontmatter compliance using the Ralph loop pattern - spboyer/sensei
Skill for iteratively improving SKILL.md frontmatter compliance using the Ralph loop pattern - spboyer/sensei
https://github.com/microsoft/waza
GitHub
GitHub - microsoft/waza: CLI / Framework for Agent Skills - create,...
CLI / Framework for Agent Skills - create, test, measure and improve skill quality and effectiveness - microsoft/waza
CLI / Framework for Agent Skills - create, test, measure and improve skill quality and effectiveness - microsoft/waza
https://github.com/microsoft/azure-skills
GitHub
GitHub - microsoft/azure-skills: Official agent plugin providing sk...
Official agent plugin providing skills and MCP server configurations for Azure scenarios. - microsoft/azure-skills
Official agent plugin providing skills and MCP server configurations for Azure scenarios. - microsoft/azure-skills
RyanPrice1001 — 11:31 AM
I saw your LI post about "mirage" problem, have you seen any?
Pamela FoxRole icon, Microsoft — 11:32 AM
https://arxiv.org/abs/2603.21687
arXiv.org
MIRAGE: The Illusion of Visual Understanding
Multimodal AI systems have achieved remarkable performance across a broad range of real-world tasks, yet the mechanisms underlying visual-language reasoning remain surprisingly poorly understood. We report three findings that challenge prevailing assumptions about how these systems process and integrate visual information. First, Frontier models...
Image
RyanPrice1001 — 11:34 AM
Thanks!
John v — 11:34 AM
why people saying mcp is dead? is it because of skills?
Pamela FoxRole icon, Microsoft — 11:36 AM
https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/migration-options
Migrate from Azure Vision in Foundry Tools - Image Analysis - Found...
Guidance for migrating from Azure Vision - Image Analysis API to alternative solutions before its retirement in September 2028.
Migrate from Azure Vision in Foundry Tools - Image Analysis - Found...
Saksh [MSAZ], Role icon, Buildathon-Mod — 11:37 AM
Hi Pam,

Did you check out TurboQuant?
Pamela FoxRole icon, Microsoft — 11:38 AM
https://github.com/orgs/microsoft-foundry/discussions/280
GitHub
Python + AI Weekly Office Hours: Recordings & Resources · microsof...
Each week, we hold weekly office hours about all things Python + AI in the Foundry Discord. Join the Discord here: http://aka.ms/aipython/oh This thread will list the recordings of each office hour...
Each week, we hold weekly office hours about all things Python + AI in the Foundry Discord. Join the Discord here: http://aka.ms/aipython/oh This thread will list the recordings of each office hour...
https://github.com/orgs/microsoft-foundry/discussions/280#discussioncomment-16338085
GitHub
Python + AI Weekly Office Hours: Recordings & Resources · microsof...
Each week, we hold weekly office hours about all things Python + AI in the Foundry Discord. Join the Discord here: http://aka.ms/aipython/oh This thread will list the recordings of each office hour...
Each week, we hold weekly office hours about all things Python + AI in the Foundry Discord. Join the Discord here: http://aka.ms/aipython/oh This thread will list the recordings of each office hour...
https://github.com/modelcontextprotocol/experimental-ext-skills
https://www.youtube.com/@Pydantic
YouTube
Pydantic
The Pydantic Stack is a collection of developer tools to build your AI engineering apps. Pydantic AI (type-safe agent framework), Pydantic Logfire (AI observability with support for full-stack apps), Pydantic Evals (AI evaluation), Pydantic AI Gateway (AI model routing), and Pydantic Validation.
Image
 [MSAZ], 
Nnamdi — 11:42 AM
I heard memory prices went down on the news. It just means that the KV cache used during LLM inference - prefill is significantly reduced.  It only applies to model hosts. I assume most hosting platforms will adopt it 
Pamela FoxRole icon, Microsoft — 11:43 AM
https://hamel.dev/blog/posts/revenge/
Hamel's Blog - Hamel Husain
The Revenge of the Data Scientist – Hamel’s Blog - Hamel Husain
Is Data Science in decline?
The Revenge of the Data Scientist – Hamel’s Blog - Hamel Husain
https://github.com/Alberto-Codes/turboquant-vllm/tree/main
GitHub
GitHub - Alberto-Codes/turboquant-vllm: TurboQuant KV cache compres...
TurboQuant KV cache compression for consumer GPUs — 3.76x compression validated on Molmo2 + RTX 4090 - Alberto-Codes/turboquant-vllm
GitHub - Alberto-Codes/turboquant-vllm: TurboQuant KV cache compres...
https://ollama.com/blog/mlx
Ollama is now powered by MLX on Apple Silicon in preview · Ollama ...
Today, we're previewing the fastest way to run Ollama on Apple silicon, powered by MLX, Apple's machine learning framework.
Ollama is now powered by MLX on Apple Silicon in preview · Ollama ...
Saksh [MSAZ], Role icon, Buildathon-Mod — 11:46 AM
Ah, cause I am thinking that they will have a greater context, they will effectively be faster for smaller tasks, and more comprehensive and better response quality for larger ones.

We would probably have less token usage!
RyanPrice1001 — 11:47 AM
The beginning, for turboquant as a concept:
https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/

will reach iclr and aistat by May
TurboQuant: Redefining AI efficiency with extreme compression
Image
Dinesh [UnAI],  — 11:48 AM
when can we see agent framework durable agent in azure functions series ?
pablocotan — 11:48 AM
provides good results with lower VRAM usage -> better models in less RAM
RyanPrice1001 — 11:48 AM
Thanks Pamela!
Pamela FoxRole icon, Microsoft — 11:51 AM
https://techcommunity.microsoft.com/blog/appsonazureblog/bulletproof-agents-with-the-durable-task-extension-for-microsoft-agent-framework/4467122
TECHCOMMUNITY.MICROSOFT.COM
Bulletproof agents with the durable task extension for Microsoft Ag...
Today, we're thrilled to announce the public preview of the durable task extension for Microsoft Agent Framework. This extension transforms how you...
Bulletproof agents with the durable task extension for Microsoft Ag...
Nnamdi — 11:51 AM
from chatgpt thinking:

In plain English, TurboQuant means you can squeeze much more conversation history into the same graphics processing unit memory, so long prompts become cheaper and often faster to serve. Google says KV cache memory can drop by about 6 times or more, with up to 8 times faster attention computation on H100 in its tests, though real end-to-end gains will usually be smaller than that headline number. Accuracy looks close to unchanged around 3 to 4 bits in the reported benchmarks, so the main trade-off is much less painful than older aggressive quantization methods. For prefix caching, the practical win is big: the same cached prompt prefixes take far less memory, so you can keep more of them warm, for longer, across more users. The catch is that deployment support is still early, so actual benefits depend on your inference stack. ([Google Research][1])

[1]: https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/?utm_source=chatgpt.com "TurboQuant: Redefining AI efficiency with extreme compression"
TurboQuant: Redefining AI efficiency with extreme compression
Image
Dinesh [UnAI],  — 11:51 AM
I am really waiting for support for private networking in hosted agents in foundry. 
There is no ETA on this, any idea about when we can see this in foundry. ?
Ekko [KILO],  — 11:52 AM
Who is she ??
How do you see the future of AI?
Dinesh [UnAI],  — 11:54 AM
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents#limits-pricing-and-availability-preview
Image
Hosted agents in Foundry Agent Service (preview) - Microsoft Foundry
Deploy and manage containerized agents on Foundry Agent Service (preview) with managed hosting, scaling, and observability.
Hosted agents in Foundry Agent Service (preview) - Microsoft Foundry
Saksh [MSAZ], Role icon, Buildathon-Mod — 11:55 AM
Any tips to maximise the quality of GitHub Copilot Auto output (It just locks to the Codex model)? The GitHub Students subscription was cut off from selecting Opus and Sonnet models🙂. It gets confused or performs poorly, even though I provide a good context for agents.
victorm#1991 — 11:55 AM
How to start in AI world? AI Engineering: Building Applications with Foundation Models book is very valuable to understand basis, do you know what’s the audience and level? Thanks you
Pamela FoxRole icon, Microsoft — 11:58 AM
https://x.com/burkeholland
Burke Holland (@burkeholland) on X
Working on @code @microsoft. My views.

X
https://x.com/pierceboggan
Pierce Boggan (@pierceboggan) on X
pm lead @code

previous: @xamarinhq (acquired by microsoft)

X
https://blog.pamelafox.org/2025/08/how-i-learn-about-generative-ai.html
How I learn about generative AI
I do not consider myself an expert in generative AI, but I now know enough to build full-stack web applications on top of generative AI mode...
Image
Justin Trantham [FlowDevs.io] [FLOW],  — 11:59 AM
thanks!
a_hognos3 — 11:59 AM
I have a question regarding Agents. When deploying a container app using a New Foundry agent that has Azure AI Search as a tool, what roles and permissions should I give to the container app so I can create the AIProjectClient() ? Is DefaultAzureCredential() the only method available or is there another way?
gotham64 — 12:00 PM
Thanks Pamela
Pamela Fox
 ended Python + AI  (Office Hours) — 12:00 PM
Dinesh [UnAI],  — 12:00 PM
Thanks
Shadakshari S — 12:00 PM
Thank you!
Bruun [ARNA],  — 12:01 PM
Thanks Pamela. Great talk.
Pamela FoxRole icon, Microsoft — 9:47 PM
@a_hognos3 If you're using Foundry Agent Service, I have examples here that connect agents to Foundry IQ via the MCP endpoint, and the Bicep setups the necessary roles/connections. But you may be asking a different question.
https://github.com/pamelafox/python-foundryagent-demos/
GitHub
GitHub - pamelafox/python-foundryagent-demos: Various demos of Foun...
Various demos of Foundry Agents using the Python SDK - pamelafox/python-foundryagent-demos
@Saksh Pierce (from VS Code team) says "It should do better in Insiders, where our task detection model is now at 100% as of today. Based on those results, we'll roll to stable.
Today, Auto is based purely off available capacity and uptime, so the model mix can be quite static in how it's applied."