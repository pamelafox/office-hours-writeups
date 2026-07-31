# July 29 Office Hours Resources

This OH was a special OH for the Microsoft IQ Deep Dive series, focusing on Work IQ for session 2.

## Recording

https://www.youtube.com/watch?v=69IFV1zZEdA

## Discord chat paste

Pamela FoxRole icon, Microsoft — Yesterday at 11:02 AM
https://aka.ms/iqdeepdive/resources
GitHub
Microsoft IQ Deep Dive with Python (livestream series): Resources ...
Join us for our 3-part live stream series on using Microsoft IQ to ground your agents and AI apps! Register for the series Livestreams Tune in for the live streams from July 28th - July 30th, or wa...
Microsoft IQ Deep Dive with Python (livestream series): Resources ...
Ayca BasRole icon, Microsoft — Yesterday at 11:03 AM
Hey all 👋
Andrew Storms — Yesterday at 11:03 AM
Are there any pre-built autopilot agent templates for different use cases? If so, where can we find them?
Pamela FoxRole icon, Microsoft — Yesterday at 11:04 AM
https://github.com/microsoft/iqdeepdive/tree/main/src/agent-workiq-autopilot
GitHub
iqdeepdive/src/agent-workiq-autopilot at main · microsoft/iqdeepdive
Contribute to microsoft/iqdeepdive development by creating an account on GitHub.
Contribute to microsoft/iqdeepdive development by creating an account on GitHub.
Bernhard Merkle — Yesterday at 11:04 AM
👍
DaTruAndi — Yesterday at 11:05 AM
Good afternoon
Ayca BasRole icon, Microsoft — Yesterday at 11:05 AM
Readme should be sufficient enough, ping me on LinkedIn if you have any issues or file an issue in the repo
Pamela FoxRole icon, Microsoft — Yesterday at 11:06 AM
https://www.linkedin.com/in/aycabas/
https://www.linkedin.com/in/paolopialorsi/
Ayca BasRole icon, Microsoft — Yesterday at 11:06 AM
Also, this is the main documentation I followed through when building Autopilot in case you need a reference: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/agent-365
Publish an autopilot in Microsoft Agent 365 - Microsoft Foundry
Learn how to publish a Foundry Hosted agent as an autopilot in Microsoft Agent 365, submit it for approval, and validate it in Teams.
Publish an autopilot in Microsoft Agent 365 - Microsoft Foundry
Bernhard Merkle — Yesterday at 11:06 AM
do you have best practices for these IQ deployments e.g. how to structure it or maintain it in a larger environment ?
pablocotan — Yesterday at 11:07 AM
How shall we evaluate the data retrieved by Work-IQ? 
I guess that we would get different results depending on the type and cleanliness of the data that is stored and accessed by Work-IQ.
Damian — Yesterday at 11:08 AM
Can we get an AI Agent to use Work IQ for different tenants? I'm thinking about creating a single AI Agent that uses this tool for some of our partners so it can work in their tenant
Pamela FoxRole icon, Microsoft — Yesterday at 11:09 AM
https://www.microsoft.com/en-us/microsoft-agent-365
Microsoft Agent 365: The Control Plane for Agents
Observe, govern, and secure AI agents confidently with Agent 365. Extend Microsoft 365 and Microsoft Security controls to manage agentic AI at scale.
Ayca BasRole icon, Microsoft — Yesterday at 11:10 AM
Depending on the scenario, you can limit the allowed list of tools in Work IQ to manage the responses. For example, not every scenario would need "Ask", you can also manage retrieved responses using "Fetch". And I always run evals over agents + Work IQ together to understand the accuracy.
pablocotan — Yesterday at 11:12 AM
but I would like to separate the evaluation of the retrieval from the evaluation of the agent.

And I think that evaluating the responses we could detect a bad data source in it (assuming that Work-IQ always retrieves quite well no matter the data type , location, size, etc.) 
Ayca BasRole icon, Microsoft — Yesterday at 11:13 AM
I am running custom evals over agents with Work IQ MCP tools to understand the quality of the answers coming from the tool.
@Pamela Fox maybe you can share a bit how you evaluate the performance of MCP tools in Foundry Agents in general, which will be the same way for Work IQ for now, until we have something better.
Bernhard Merkle — Yesterday at 11:15 AM
pablo mentioned debugging facilities in declarative agents, how does that work ? do i have to instrument code or we debug via the OTEL data or LLM traces ? and how does it work for non-declarative agents ?
pablocotan — Yesterday at 11:16 AM
The impression I have with Work-IQ (and the same with the Google alternative), is that we get probable answers, but in many cases we need the correct answers. Unless we could evaluate it, we cannot be sure about the result.
And besides that, I imagine we can degrade its performance based on the data used in the user environment. 
Pamela FoxRole icon, Microsoft — Yesterday at 11:16 AM
https://github.com/Azure-Samples/foundry-hosted-agentframework-demos/blob/main/scripts/quality_eval.py
GitHub
foundry-hosted-agentframework-demos/scripts/quality_eval.py at main...
A demo project that deploys Agent Framework agent to Foundry Hosted Agents - Azure-Samples/foundry-hosted-agentframework-demos
A demo project that deploys Agent Framework agent to Foundry Hosted Agents - Azure-Samples/foundry-hosted-agentframework-demos
Ayca BasRole icon, Microsoft — Yesterday at 11:19 AM
Also I ran evals to the same agent multiple times by changing the allowed tool list. You'd be suprised by the change in accuracy when you give the agent "no more than necessary tools".
Pamela FoxRole icon, Microsoft — Yesterday at 11:20 AM
https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/debugging-agents-copilot-studio
Bernhard Merkle — Yesterday at 11:20 AM
cool 🙂
Andrew Storms — Yesterday at 11:23 AM
How do Copilot Studio agents relate to Foundry agents? My impression is you choose one or the other (depending on if you want low code vs full code) and they don't really interact
Damian — Yesterday at 11:24 AM
I was thinking about deploying the agent to Teams as an app so my partners can install the agent app
Andrew Storms — Yesterday at 11:25 AM
Thank you!
Bernhard Merkle — Yesterday at 11:27 AM
for publish agents are there any security checks or frameworks to check the agent against risky action ? in order to avoid security issues
Damian — Yesterday at 11:29 AM
Correct I meant an agent that can be installed on different tenants but the agent can only see the information from the tenant the agent is installed on
DaTruAndi — Yesterday at 11:30 AM
is there life demos/video/screen sharing today?
RyanPrice1001 — Yesterday at 11:30 AM
Thanks A, P and P again! 🚀 🚀 🚀
Bernhard Merkle — Yesterday at 11:31 AM
ok, guardrails are at runtime, and question is if there is something also for buildtime, like a static analyzer
pablocotan — Yesterday at 11:31 AM
More on quality of responses:
If different team members trigger Work-IQ, their underlying M365 environments (emails, Teams chats, version histories) vary.  What patterns and configurations do you recommend to scope tools and lock down source data versions so the team gets standardized, reliable results?

Work-IQ (as well as Google's version) seem to be good to try find some information faster, but not to use like we might use a team's Hybrid-RAG/GraphRAG , in which we have control about the data, and we evaluate continuously the retrieval quality. 
Bernhard Merkle — Yesterday at 11:32 AM
not sure if it make sense 😉
Pamela FoxRole icon, Microsoft — Yesterday at 11:32 AM
https://www.youtube.com/watch?v=xI3wMCC0oBY
YouTube
Microsoft Reactor
Microsoft IQ Deep Dive with Python: Work IQ
Image
DaTruAndi — Yesterday at 11:32 AM
Ok. Thanks for clarifying
The initial comment about getting all IQs working within one tenant is still giving me pause. If it’s so challenging for all yall - what about us? Are there investments to easily “workiq avengers assemble”? 
Pamela FoxRole icon, Microsoft — Yesterday at 11:39 AM
https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/appsource/publish
Publish App on Teams Store - Teams
Publish your app to Microsoft Teams Store or AppSource. What to expect after you submit, tips for rapid approval and publishing apps linked to a SaaS offer.
Publish App on Teams Store - Teams
Damian — Yesterday at 11:39 AM
Thanks a lot!
John v — Yesterday at 11:41 AM
we have a requirement  to build a custom agent, where our data resides in sharepoint, outlook and confluence. Honestly workiq is bit confusing and initially thinking to do through microsoft graph api. is there any sample demos related to it?
Bernhard Merkle — Yesterday at 11:42 AM
yes i setup my own outlook tennant via the m365 developer license. this works great
Pamela FoxRole icon, Microsoft — Yesterday at 11:43 AM
Copilot Credits enabling: https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
Managing AI experiences enabled by usage-based billing
Copilot Credits power usage-based billing across eligible AI experiences. Discover how to allocate, monitor, and optimize spending using the Cost management dashboard in the Microsoft 365 admin center.
Managing AI experiences enabled by usage-based billing
Ayca BasRole icon, Microsoft — Yesterday at 11:44 AM
I also have seed in the autopilot demo for emails 🙂 It's fun to test it out once you setup the licenses and permissions stuff.
pablocotan — Yesterday at 11:46 AM
Copilot Studio has traditionally enforced payload caps on tool responses. How are Work-IQ MCP results handled under the hood—and are there key payload or truncation differences between running Work-IQ in Copilot Studio versus an Azure AI Foundry agent?
Pamela FoxRole icon, Microsoft — Yesterday at 11:50 AM
https://learn.microsoft.com/en-us/agent-framework/agents/harness
Agent Harnesses
Learn what an agent harness is and how to use the batteries-included HarnessAgent (C#) and create_harness_agent (Python) to build capable, autonomous agents.
Agent Harnesses
Kory — Yesterday at 11:51 AM
in the demo, Ayca had "WorkMate" and said that seperate users could also use it and it would work in the context of that user.  She mentioned that "WorkMate" would need a MS Licence such as E5.  So my question is when "WorkMate" is used in each users context, does it need multiple Licenses
John v — Yesterday at 11:52 AM
thank you paolo, follow up question if document or data access is restricted to different users. initially i assume based on the user entra id the agent will respond to the question. how does access look like for workiq if it's already returning to summarized response?
Ayca BasRole icon, Microsoft — Yesterday at 11:52 AM
If you create a single instance which is used across multiple people, then you'll need a single E5 license
yes
pablocotan — Yesterday at 11:52 AM
More related to Work-IQ usage from Copilot-Studio agents vs Foundry Agents:

Since Copilot Studio relies on its own managed orchestrator and query decomposition and filtering, should we expect differences in reasoning quality, tool-calling sequences, or execution speed when querying Work-IQ  ?
Ayca BasRole icon, Microsoft — Yesterday at 11:54 AM
One single Workmate instance can report to me but Paolo and Pamela can also access to it as well. so you'd use the same instance across. But there might be scenarios where you'd need multiple instances then every instance requires an E5 license.
Bernhard Merkle — Yesterday at 11:56 AM
off-topic: how was the MCP 2.0 party 😇  🎉  😂
John v — Yesterday at 11:56 AM
i mean does workiq also access the data just the user can able to access only? i misunderstood and assumed workiq can access all the data related to tenant instead of just a user.
Pamela FoxRole icon, Microsoft — Yesterday at 11:57 AM
MCP cake!!
Image
https://www.linkedin.com/posts/pamela-s-fox_mcp-share-7488110838822866944-f_Qn/
LinkedIn
#mcp | Pamela Fox
Big week for the MCP ecosystem! The new MCP 2026-07-28 specification just dropped, bringing a stateless protocol core, a formal extensions framework, and major updates to authorization, routing, scalability, and long-running tasks.

If you're wondering what these changes mean in practice, join us for MCP Live! on September 9, a 5-hour livestrea...
#mcp | Pamela Fox
Bernhard Merkle — Yesterday at 11:58 AM
its the http of the future 🙂
pablocotan — Yesterday at 11:59 AM
thank you very much for the answers and the thinking together...
Ayca BasRole icon, Microsoft — Yesterday at 11:59 AM
Thank you all 🙂
Bernhard Merkle — Yesterday at 11:59 AM
great session and presentation 🙏
Pamela FoxRole icon, Microsoft — Yesterday at 11:59 AM
https://aka.ms/iqdeepdive/resources
GitHub
Microsoft IQ Deep Dive with Python (livestream series): Resources ...
Join us for our 3-part live stream series on using Microsoft IQ to ground your agents and AI apps! Register for the series Livestreams Tune in for the live streams from July 28th - July 30th, or wa...
Join us for our 3-part live stream series on using Microsoft IQ to ground your agents and AI apps! Register for the series Livestreams Tune in for the live streams from July 28th - July 30th, or wa...
Damian — Yesterday at 11:59 AM
Thank you
Paolo Pialorsi
 ended Microsoft IQ Deep Dive with Python: Work IQ — Yesterday at 12:00 PM
Pamela FoxRole icon, Microsoft — Yesterday at 12:03 PM
@Damian  Lee also shared this blog post about publishing to Teams: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/building-and-deploying-microsoft-hosted-agents-to-microsoft-teams/4540376