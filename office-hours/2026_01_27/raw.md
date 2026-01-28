# January 27 2026 Office Hours Resources

## Recording

https://www.youtube.com/watch?v=3nlMoKu2g3Q

## Slide content:

News:
MCP Apps support in VS Code: https://code.visualstudio.com/blogs/2026/01/26/mcp-apps-support
VS Code Insiders: 200K context, 100 tool calls per session, Anthropic message API, Agent HQ (https://x.com/pierceboggan/status/2015910443395776647), Claude SDK integration, #askQuestion tool, switch agent tool, reads allowed outside workspace, isolated terminal sandbox
Andrej Karpathy: Coding is now 80% agentic?!
WorkIQ: https://github.com/microsoft/work-iq-mcp

What I'm working on this week:
GitHub Copilot CLI and SDK experiments: https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_01_26_copilot/writeup.md
azure-search-openai-demo: ACL support for cloud ingestion is released:https://github.com/Azure-Samples/azure-search-openai-demo/releases/tag/2026-01-27

Upcoming events:
Python + Agents series! https://aka.ms/PythonAgents/series 
Microsoft AI Tour: https://aitour.microsoft.com/flow/microsoft/aitour/landing/page/home
Py AI in SF: https://pyai.events/ 
MCP summit: https://events.linuxfoundation.org/mcp-dev-summit-north-america/program/cfp/
PyCon 2026: https://us.pycon.org/2026/


## Links from open tabs:

https://github.com/Azure-Samples/azure-search-openai-demo/releases/tag/2026-01-27
https://code.visualstudio.com/blogs/2026/01/26/mcp-apps-support
https://github.com/digitarald/mcp-apps-playground
https://modelcontextprotocol.github.io/ext-apps/api/
https://github.com/modelcontextprotocol/ext-apps/
https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_01_26_copilot/writeup.md
https://github.com/github/copilot-sdk
https://developer.microsoft.com/en-us/reactor/events/26647/?wt.mc_id=meetup_26647_email_reactor
https://github.com/Azure/AI-Dev-Days-Hackathon/tree/main
https://developer.microsoft.com/en-us/reactor/series/s-1638/
https://developer.microsoft.com/en-us/reactor/series/S-1631/?wt.mc_id=slidescontent_S-1631_webinar_reactor
https://github.com/github/spec-kit
https://github.com/Azure-Samples/azure-search-openai-demo/releases/tag/2026-01-27
https://capps-backend-mpzpi6o7z735i.politebay-4c3df20d.westus3.azurecontainerapps.io/
https://m365.cloud.microsoft/chat/conversation/09a48c8c-1675-4a61-80f9-e7ff822478eb?FORM=undexpand&fromcode=edgesidebar&redirectid=3b6b256b-330e-410b-b274-f68ba4ef7f77&auth=2&fromCode=CsrToSSR
https://github.com/orgs/microsoft-foundry/discussions/280
https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_01_26_copilot/writeup.md
https://github.com/pamelafox/presentation-writeups/blob/main/presentations/ignite-agentic-kb/outputs/writeup.md
https://portal.azure.com/#@caglobaldemos2602.onmicrosoft.com/resource/subscriptions/8077d4f9-d1b7-4c80-b6c2-cf9a2ec2d604/resourceGroups/rg-ant-agent-shop/providers/Microsoft.CognitiveServices/accounts/anthonyshaw-azuredocs-agents-res/projects/anthonyshaw-azuredocs-agents/overview
https://ai.azure.com/nextgen/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA%2Crg-pf-agentic-foundry-tutorial%2C%2Cpf-agentic-foundry-tuto-resource%2Cpf-agentic-foundry-tutorial/build/knowledge/search/c/pfagenticfoundrytutor0f87yf
https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-create-pipeline
https://github.com/microsoft/work-iq-mcp

## Discord chat paste

Pamela FoxRole icon, Microsoft — 11:07 AM
https://code.visualstudio.com/blogs/2026/01/26/mcp-apps-support
Giving Agents a Visual Voice: MCP Apps Support in VS Code
VS Code now supports MCP Apps, enabling AI agents to display interactive UIs for richer developer workflows.
Giving Agents a Visual Voice: MCP Apps Support in VS Code
signalstrike — 11:07 AM
Will we be able to deploy MCP apps  to Copilot/Teams? 
Thanks for asking your colleagues, @Pamela Fox . What should I be looking for, for the answer? Circle back here?
Pamela FoxRole icon, Microsoft — 11:13 AM
https://www.youtube.com/watch?v=gDSIxIGYk-o&pp=ygUla2VudCBkb2RkcyBmdXR1cmUgb2YgdXNlciBpbnRlcmFjdGlvbtgGCw%3D%3D
YouTube
Microsoft Developer
The Future of User Interaction with Kent C. Dodds
Image
signalstrike — 11:14 AM
I have relatives that use wechat for everything. Almost no websites. All chat based to do everything from ordering food to paying for stuff.
They use the old bot tech, i think, yea.
Pamela FoxRole icon, Microsoft — 11:15 AM
https://x.com/pierceboggan/status/2015910443395776647
Pierce Boggan (@pierceboggan)
New in @code Insiders: dedicated agent management UX with "Chat: Open Agent Sessions Window".

The UX for managing your agents is here in @code :)
Image

X•Yesterday at 2:11 PM
signalstrike — 11:16 AM
I have, i've been getting errors, unfortunately. Had to switch back to the CLI
coulthrustRole icon, Microsoft — 11:16 AM
Copioot sdk and copilot cli are kind of cool
signalstrike — 11:17 AM
speaking of SDKs, I do have a question about a couple of them.
SpecKit helps a lot to get the more "craft" developers adopting AI Assistants.
Pamela FoxRole icon, Microsoft — 11:18 AM
https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_01_26_copilot/writeup.md
GitHub
office-hours-writeups/office-hours/2026_01_26_copilot/writeup.md at...
Contribute to pamelafox/office-hours-writeups development by creating an account on GitHub.
office-hours-writeups/office-hours/2026_01_26_copilot/writeup.md at...
coulthrustRole icon, Microsoft — 11:19 AM
I got the custom agents to work with the copilot sdk
The remote copilot vs local is a little confusing
ZeroFlame — 11:19 AM
I've started a project where my goal is 99% entirely agentic written code. Finding a very specific point where the agents are starting to run into limitations with context and starting to introduce larger issues. Might have to change up approach to reduce complexity of each section.
Nick Drew

 — 11:20 AM
Pamela, I got an email about a upcoming hackathon hosted by Microsoft. Is this something you're involved with: https://developer.microsoft.com/en-us/reactor/events/26647/?wt.mc_id=meetup_26647_email_reactor.
Microsoft Reactor
AI Dev Days Hackathon: Build the Future with AI Apps, Agents, and S...
Learn new skills, meet new peers, and find career mentorship. Virtual events are running around the clock so join us anytime, anywhere!
Microsoft Reactor
signalstrike — 11:21 AM
Is this a good place to ask about the msft foundry sdk or agent-framework sdk?
signalstrike — 11:22 AM
Are you using something like SDD to guide the coding agent?
coulthrustRole icon, Microsoft — 11:22 AM
It makes ephemeral agents , if you connect it to a repo it will use the agents in the repo .github agents directory
Something like that 🙂
Fresh Cheese — 11:23 AM
Your voice cut out for me
signalstrike — 11:23 AM
I can hear her fine.
ZeroFlame — 11:23 AM
For this specific instance I provided limited instruction set, more with the idea of someone using Github Spark for example to create a tool to satisfy a specific need.
Fresh Cheese — 11:24 AM
Thanks. It was a me problem.
ZeroFlame — 11:24 AM
Audio and video had cut out for me at the same time as well but it recovered on its own.
signalstrike — 11:25 AM
Maybe we can hook it up to n8n as a perception layer and use other tools with read access to do writes.
Pamela FoxRole icon, Microsoft — 11:26 AM
https://developer.microsoft.com/en-us/reactor/series/s-1638/
Microsoft Reactor
Agents League | Microsoft Reactor
Attend Reactor Event Series for on-going opportunities to learn, connect, and build. Expand your skillset.
Agents League | Microsoft Reactor
coulthrustRole icon, Microsoft — 11:27 AM
Amazong
Pamela FoxRole icon, Microsoft — 11:27 AM
https://github.com/Azure/AI-Dev-Days-Hackathon
GitHub
GitHub - Azure/AI-Dev-Days-Hackathon
Contribute to Azure/AI-Dev-Days-Hackathon development by creating an account on GitHub.
https://developer.microsoft.com/en-us/reactor/series/S-1631/
Microsoft Reactor
Python + Agents: Building AI agents and workflows with Agent Framew...
Attend Reactor Event Series for on-going opportunities to learn, connect, and build. Expand your skillset.
Python + Agents: Building AI agents and workflows with Agent Framew...
Chrisslayy

 — 11:29 AM
i want off this website now please
Pamela FoxRole icon, Microsoft — 11:29 AM
https://humanwhocodes.com/blog/2025/06/persona-based-approach-ai-assisted-programming/
signalstrike — 11:30 AM
Ok, I'll ask next time. I have a conflict and will watch the recording. RE: SDD, I like speckit by github.
Pamela FoxRole icon, Microsoft — 11:31 AM
https://speckit.org/
Spec Kit - AI-Powered Specification-Driven Development Toolkit
Spec Kit helps developers build high-quality software faster with AI-powered Spec-Driven Development. Transform specifications into executable code with Spec Kit's innovative toolkit.
https://github.com/Azure-Samples/azure-search-openai-demo/releases/tag/2026-01-27
GitHub
Release ACL support for cloud ingestion pipeline · Azure-Samples/a...
This release adds Access Control List (ACL) support for the cloud ingestion pipeline, enabling document-level security filtering in Azure AI Search. Documents stored in Azure Data Lake Storage Gen2...
This release adds Access Control List (ACL) support for the cloud ingestion pipeline, enabling document-level security filtering in Azure AI Search. Documents stored in Azure Data Lake Storage Gen2...
coulthrustRole icon, Microsoft — 11:33 AM
Sweet isnt the acl built into ai search now ?
Could you support acls from other idp like okta or whatever aws and gcp are using
Customers have other idp's  so consuming data from salesforce other system with other idp and maintain acls is the question genesis
coulthrustRole icon, Microsoft — 11:42 AM
Random question there are memory tools you can add to github copilot have you tried that ? Any reason i would want to use an additinal memory provider
Also Dem left for Anthropic 🙁
JohnRole icon, MVP — 11:43 AM
Did you try gpt-5?
coulthrustRole icon, Microsoft — 11:44 AM
Well github copilot for the memory question
Skills ? Have you tried this from Anthropic and why would I use this
Yeah several memory mcp servers
Pamela FoxRole icon, Microsoft — 11:49 AM
https://github.com/pamelafox/presentation-writeups
GitHub
GitHub - pamelafox/presentation-writeups: Skills and tools to turn ...
Skills and tools to turn my presentations into writeups - pamelafox/presentation-writeups
Skills and tools to turn my presentations into writeups - pamelafox/presentation-writeups
coulthrustRole icon, Microsoft — 11:51 AM
Question. I have customers asking when should I use foundry iq retrieval agents with sources like elastic etc vs use a elastic mcp tool as an example..so wrapping a knowledge source in foundry iq vs  using a knowledge source outside of  foundry iq
You are answering my question thanks
Customers are asking how to track semantic / knowledge drift when all of the knowledge is behind foundry iq its an interesting upcoming subject
mark6871

 — 11:57 AM
four non-related names lol
coulthrustRole icon, Microsoft — 11:57 AM
2 names and 4 acronyms
Cognitive search
RyanPrice1001 — 11:58 AM
Same name for different things scares namers into action.
coulthrustRole icon, Microsoft — 11:59 AM
Just use a guid
pierred7274

 — 12:02 PM
Thanks for sharing the presentation repo
RyanPrice1001 — 12:02 PM
Thanks Pamela!
libis22 — 12:02 PM
Thank you!!!!
RyanPrice1001 — 12:02 PM
There is an agent for that.
coulthrustRole icon, Microsoft — 12:02 PM
Amazing call
