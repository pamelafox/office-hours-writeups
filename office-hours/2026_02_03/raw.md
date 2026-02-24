# Feb 3 2026 Office Hours Resources

## Recording
https://youtu.be/V-mUPDW6Tgg

## Slide content:

News:
OpenClaw: https://openclaw.im/  (don't install it! security issues abound)
Skills for GitHub Copilot and other agentic coders:
https://skills.sh/
https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md
Postgres learning path: https://learn.microsoft.com/en-us/training/paths/build-ai-apps-azure-database-postgresql/ 


What I'm working on this week:
Migrating from Chat Completions to Responses API
Py AI talk: Evaluating 12 MCP tool schemas with 4 different agents (Pydantic-AI, Langchain, MAF, Copilot SDK)
azure-search-openai-demo: Porting from Prompty to Jinja2


Upcoming events:
Python + Agents series! https://aka.ms/PythonAgents/series 
Microsoft AI Tour: https://aitour.microsoft.com/flow/microsoft/aitour/landing/page/home
Py AI in SF: https://pyai.events/ 
MCP summit: https://events.linuxfoundation.org/mcp-dev-summit-north-america/program/cfp/
PyCon 2026: https://us.pycon.org/2026/


## Links from open tabs:

https://openclaw.im/
https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md
https://github.com/pamelafox
https://openclaw.im/
https://www.moltbook.com/
https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys
https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code
https://openai.com/codex/get-started/
https://blog.kilo.ai/p/cline-just-acqui-hired
https://skills.sh/
https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md
https://github.github.com/awesome-copilot/skills/
https://github.com/pamelafox/office-hours-writeups
https://code.visualstudio.com/docs/copilot/customization/agent-skills
https://github.com/Azure-Samples/azure-search-openai-demo/tree/main/.github/prompts
http://127.0.0.1:50505/
https://github.com/Azure-Samples/openai-chat-app-quickstart/pull/359
https://github.com/Azure-Samples/openai-chat-app-quickstart/pull/358
https://github.com/github/github-mcp-server
https://learn.microsoft.com/en-us/training/paths/build-ai-apps-azure-database-postgresql/
https://developer.microsoft.com/en-us/reactor/series/S-1631/?wt.mc_id=slidescontent_S-1631_webinar_reactor
https://pyai.events/speakers
https://events.linuxfoundation.org/mcp-dev-summit-north-america/program/cfp/
https://us.pycon.org/2026/
https://github.com/pamelafox/personal-linkedin-agent

## Discord chat paste


https://github.com/orgs/microsoft-foundry/discussions/280
GitHub
Python + AI Weekly Office Hours: Recordings & Resources · microsof...
Each week, we hold weekly office hours about all things Python + AI in the Foundry Discord. Join the Discord here: http://aka.ms/pythonai/oh This thread will list the recordings of each office hour...
Python + AI Weekly Office Hours: Recordings & Resources · microsof...
Justin Trantham [FlowDevs.io]

 — 11:06 AM
Open steal your secret keys
BlackPandaChan — 11:06 AM
IMO stay away for now, but it is a neat social experiment, art, not sure what to call it, lol. The moltbook supabase backend is not secure.
Dinesh

 — 11:06 AM
Macbook minis are running out of it
Human. — 11:07 AM
will it run fine on nvidia jetson orin?
Justin Trantham [FlowDevs.io]

 — 11:07 AM
I saw a video from Moltbook all the secrets are aviable through their API. Its completely open
Humans are also posting on Moltbook sooo.. lol
BlackPandaChan — 11:08 AM
Yeah justin it's wild, I just had to call it out because people quickly go from installing clawdbot or nanoclawd to using moltbook
Pamela FoxRole icon, Microsoft — 11:08 AM
https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys
wiz.io
Hacking Moltbook: AI Social Network Reveals 1.5M API Keys | Wiz Blog
Learn how a misconfigured Supabase database at Moltbook exposed 1.5M API keys, private messages, and user emails, enabling full AI agent takeover.
Hacking Moltbook: AI Social Network Reveals 1.5M API Keys | Wiz Blog
BlackPandaChan — 11:08 AM
This is the exact article I just finished reading, lol
yass 🦆 — 11:08 AM
am i the only one that i have the voice cutting !
Pamela FoxRole icon, Microsoft — 11:09 AM
https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code
The creator of Clawd: "I ship code I don't read"
Listen now (114 mins) | How Peter Steinberger, creator of OpenClaw (formerly: Clawd), builds and ships like a full team by centering his development workflow around AI agents.
The creator of Clawd: "I ship code I don't read"
Justin Trantham [FlowDevs.io]

 — 11:09 AM
sounds fine here @yass 🦆
BlackPandaChan — 11:09 AM
Moltbook DID make me think about building something similar within a discord community, as a fun social experiement, or a local reddit like lemming (where friends' agents can post) could be fun (and more secure)
Pamela FoxRole icon, Microsoft — 11:10 AM
https://www.letta.com/
Letta
The platform for stateful agents. Build AI agents with long-term memory, advanced reasoning, and custom tools using the Letta API and Agent Development Environment (ADE).
Letta
BlackPandaChan — 11:10 AM
ooo this is perfect thank you Pamela!
Pamela FoxRole icon, Microsoft — 11:10 AM
https://bsky.app/profile/cameron.stream
https://bsky.app/profile/did:plc:mxzuau6m53jtdsbqe6f4laov
Justin Trantham [FlowDevs.io]

 — 11:12 AM
Tried Codex app yet? I can't on my windrs computer.
Pamela FoxRole icon, Microsoft — 11:13 AM
https://blog.kilo.ai/p/cline-just-acqui-hired
Update: Cline clarified they are operational and there was no trans...
Kilo is doubling down on staying open
Update: Cline clarified they are operational and there was no trans...
Justin Trantham [FlowDevs.io]

 — 11:14 AM
it should be free right now, and 2x if you pay
It is but this is brand new as of yesterday*
BlackPandaChan — 11:18 AM
Everytime I've tried to use codex (pre 5.2 to be fair) I've regretted  not just doing it in claude code, lol. I've had decent luck with features, though.
Justin Trantham [FlowDevs.io]

 — 11:18 AM
yes
BlackPandaChan — 11:18 AM
The codex "app" is new!
gcrumrine — 11:19 AM
I think I still prefer the CLI.
Justin Trantham [FlowDevs.io]

 — 11:20 AM
The automations & prompt queueing seem interesting. I've seen other platforms include the prompt queueing recently (seems like it could also be a credit waster)
Pamela FoxRole icon, Microsoft — 11:20 AM
https://skills.sh/
Skills
The Agent Skills Directory
Discover and install skills for AI agents.
The Agent Skills Directory
https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md
GitHub
awesome-copilot/docs/README.skills.md at main · github/awesome-cop...
Community-contributed instructions, prompts, and configurations to help you make the most of GitHub Copilot. - github/awesome-copilot
Community-contributed instructions, prompts, and configurations to help you make the most of GitHub Copilot. - github/awesome-copilot
https://github.github.com/awesome-copilot/skills/
Skills - Awesome GitHub Copilot
Self-contained agent skills with instructions and bundled resources
Justin Trantham [FlowDevs.io]

 — 11:21 AM
Can you briefly explain what skills are? They are a bit confusing to me
Steve Hatt — 11:22 AM
How do I control the availability of skills i.e. can I block the use of ones my team found problematic?
pierred7274

 — 11:22 AM
👍
Justin Trantham [FlowDevs.io]

 — 11:25 AM
this. is. amazing.
gcrumrine — 11:26 AM
I think the biggest downside of the skills/task specific instructions workflow is that there seems to be context loss pretty frequently when you are chaining them together.
Right? So when a skill is invoked it should have all the information, but in my experience when you have a skill that can also invoke another skill sometimes it feels like a new session is somehow opened.
HeyMsShipley

 — 11:30 AM
do we have to use insiders to do this?
gcrumrine — 11:30 AM
This one looks pretty cool though
good idea.
Pamela FoxRole icon, Microsoft — 11:32 AM
https://code.visualstudio.com/docs/copilot/customization/agent-skills
Use Agent Skills in VS Code
Learn how to use Agent Skills in VS Code to teach GitHub Copilot specialized capabilities that work across VS Code, GitHub Copilot CLI, and GitHub Copilot coding agent.
Use Agent Skills in VS Code
gcrumrine — 11:35 AM
Dang, I wish everyone had that mentality. Code review is always a mental block for me because theres always a "better" way of doing things from someone else's point of view.
Pamela FoxRole icon, Microsoft — 11:35 AM
https://github.com/Azure-Samples/azure-search-openai-demo/tree/main/.github/prompts
GitHub
azure-search-openai-demo/.github/prompts at main · Azure-Samples/a...
A sample app for the Retrieval-Augmented Generation pattern running in Azure, using Azure AI Search for retrieval and Azure OpenAI large language models to power ChatGPT-style and Q&amp;amp;A expe...
azure-search-openai-demo/.github/prompts at main · Azure-Samples/a...
Justin Trantham [FlowDevs.io]

 — 11:36 AM
:thankyou:
"social engineering" lol
Pamela FoxRole icon, Microsoft — 11:44 AM
https://github.com/Azure-Samples/openai-chat-app-quickstart/pull/359
GitHub
Migrate to OpenAI Responses API by pamelafox · Pull Request #359 ...
Summary

migrate Azure OpenAI client and streaming to Responses API
update frontend stream parsing to Responses events
update tests/snapshots and remove deprecated API version config
bump openai SD...
Summary

migrate Azure OpenAI client and streaming to Responses API
update frontend stream parsing to Responses events
update tests/snapshots and remove deprecated API version config
bump openai SD...
Justin Trantham [FlowDevs.io]

 — 11:45 AM
MCP on codex is a pain...
It does, but you have to enable it
gcrumrine — 11:46 AM
in the cli I always have to run using the "--dangerously-bypass-approvals-and-sandbox" flag to get it to work properly with the MCP's I am wanting to use.
Justin Trantham [FlowDevs.io]

 — 11:47 AM
Dont quote me on that for the app - thats a CLI setting
gcrumrine — 11:50 AM
Lol create the agent to control the multiple agents. Offload mental load.
Good info there.
Sure, just a joke really.
Pamela FoxRole icon, Microsoft — 11:52 AM
https://learn.microsoft.com/en-us/training/paths/build-ai-apps-azure-database-postgresql/
Build AI Apps with Azure Database for PostgreSQL AI-3019 - Training
Build AI Apps with Azure Database for PostgreSQL. (AI-3019)
Image
Silvestre — 11:54 AM
Question random, what is you opinion about openclaw and moltbook ?
gcrumrine — 11:56 AM
Thanks for your time. This was my first time attending and it was nice, good information and food for thought! Have a good week everyone.
RyanPrice1001 — 11:57 AM
Thanks Pamela!
Pamela FoxRole icon, Microsoft — 11:57 AM
https://developer.microsoft.com/en-us/reactor/series/S-1631/?wt.mc_id=slidescontent_S-1631_webinar_reactor
Microsoft Reactor
Python + Agents: Building AI agents and workflows with Agent Framew...
Attend Reactor Event Series for on-going opportunities to learn, connect, and build. Expand your skillset.
Image
Justin Trantham [FlowDevs.io]

 — 11:57 AM
no love in minnesota 🙁
RyanPrice1001 — 11:59 AM
All the flyover states ...home grown python?
Human. — 11:59 AM
Chicago?
pierred7274

 — 11:59 AM
These are great. Will keep an eye open if Chicago is listed
John v — 11:59 AM
i saw your linkedin agent project using playwright, i have a question is it safe to ask agent to do job search in linkedin without getting blocked by linkedin as i assume they stopped offering jobs api for public.
Pamela FoxRole icon, Microsoft — 12:00 PM
https://github.com/pamelafox/personal-linkedin-agent