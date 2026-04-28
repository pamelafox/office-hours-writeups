# April 27, 2026 "Host your agents on Foundry" Day 1

## Recording:

https://www.youtube.com/watch?v=o4-1LI3-uqw

## Slide content:

No slides for the office hours itself, this session was a follow-up office hours after this livestream:
https://developer.microsoft.com/en-us/reactor/events/26932/

# Browser open tabs

https://github.com/orgs/microsoft-foundry/discussions/380
https://github.com/Azure-Samples/foundry-hosted-agentframework-demos
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryhosted-agentframework,,ai-account-nivdj7gkpbmk2,ai-project-pf-foundryhosted-agentframework/build/agents/hosted-agentframework-agent/build
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryhosted-agentframework,,ai-account-nivdj7gkpbmk2,ai-project-pf-foundryhosted-agentframework/build/agents/hosted-agentframework-agent/traces
https://portal.azure.com/Error/UE_SessionExpired?shown=true#@caglobaldemos2605.onmicrosoft.com/resource/subscriptions/8077d4f9-d1b7-4c80-b6c2-cf9a2ec2d604/resourceGroups/rg-pf-foundryhosted-agentframework/providers/Microsoft.Insights/components/appi-nivdj7gkpbmk2/agents
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryhosted-agentframework,,ai-account-nivdj7gkpbmk2,ai-project-pf-foundryhosted-agentframework/build/agents/hosted-agentframework-workflow/build
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryhosted-agentframework,,ai-account-nivdj7gkpbmk2,ai-project-pf-foundryhosted-agentframework/build/guardrails/blocklists
https://github.com/microsoft/agent-framework/tree/main/python/samples
https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/
https://github.com/Azure-Samples/python-agentframework-demos/blob/main/presentations/english/session-2/README.md#dynamic-memory-with-mem0
https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage?pivots=python
https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/
https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-regions-limits-virtual-network
https://github.com/pamelafox
https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
https://pydantic.dev/docs/ai/harness/code-mode/#_top
https://x.com/notifications/mentions
https://github.com/microsoft/agent-framework
https://learn.microsoft.com/en-us/agent-framework/agents/observability?pivots=programming-language-python#spans-and-metrics
https://sql-benchmark.nicklothian.com/?utm_source=breadbox
https://devblogs.microsoft.com/foundry/from-local-to-production-the-complete-developer-journey-for-building-composing-and-deploying-ai-agents/#step-3:-make-agents-stateful-with-memory-in-foundry-agent-service-(public-preview)
https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent#deploy-using-the-rest-api
https://learn.microsoft.com/en-us/azure/api-management/api-management-gateways-overview
https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities
https://pydantic.dev/articles/pydantic-monty
https://github.com/saxenanurag/strava-mcp/blob/main/strava_mcp/services/analysis.py
https://github.com/pydantic/monty
https://gist.github.com/pamelafox/47c380e63687164fe1748c231f07998f
https://github.com/pamelafox
edge://newtab/

# Discord chat

pablocotan — 11:10 AM
How does safety play a role in using websearch tool regarding prompt injection?
asx — 11:10 AM
Is there something similar to code mode in agent-framework? Or can I use Pydantic Monty?
pablocotan — 11:11 AM
What would be an efficient way to automatically analyze traces & logs?
Kalyan a.k — 11:12 AM
Does Hosted Agent support per agent identity and also is there any VNet support?
pablocotan — 11:12 AM
If we wrap a workflow as an agent, and it contains other agents(using tools), would the tracing still capture all internal information?
Weedy — 11:12 AM
Thanks. Got the answer.
ChandrashekarMuthumula — 11:13 AM
Yes how to pick better model that can query the db
jomor1114 — 11:17 AM
Not sure if this is the right time to ask this but I was trying to use the ADO mcp connection in foundry for creating new tickets in ado with an agent but it seems this functionality is not available atm. Do you know when or if this will be available?
Pamela FoxRole icon, Microsoft — 11:17 AM
https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
Prompt Shields in Azure AI Content Safety - Azure AI services
Learn about User Prompt injection attacks and document attacks and how to prevent them with the Prompt Shields feature.
Prompt Shields in Azure AI Content Safety - Azure AI services
asx — 11:19 AM
I have used Monty with FastMCP as a tool. I am thinking I could use it as a tool since it is a function.
Nnamdi — 11:19 AM
I've seen a couple of posts where people talk about having each agent of a multiagent system in its own sandbox. What are the pros and cons of this?
Kalyan a.k — 11:21 AM
what is the pricing criteria for Hosted agents?
sanz — 11:23 AM
Can we publish agents (prompt) when we have public n/w disabled ? I was able to publish it in past but I am not able to do so now. Also which endpoint we should use to connect to agent  from an external app? Is this correct - https://<foundry_prj>.services.ai.azure.com/api/projects/<prj_name>/applications/<AGENT_NAME>/protocols/openai ?
Kalyan a.k — 11:23 AM
Thank you @Pamela Fox !!
Pamela FoxRole icon, Microsoft — 11:24 AM
https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/virtual-networks?tabs=portal
Set up private networking for Foundry Agent Service - Microsoft Fou...
Set up private networking for Foundry Agent Service using Bicep or Terraform. Deploy a virtual network with private endpoints, DNS zones, and deny-by-default network rules.
Set up private networking for Foundry Agent Service - Microsoft Fou...
https://learn.microsoft.com/en-us/agent-framework/agents/observability?pivots=programming-language-python#spans-and-metrics
Observability
Learn how to use observability with Agent Framework
Observability
https://sql-benchmark.nicklothian.com/?utm_source=breadbox
LLM SQL Benchmark
A fast benchmark for Agentic Natural Language to SQL Generation.
LLM SQL Benchmark
Justin Trantham [FlowDevs.io] [FLOW],  — 11:28 AM
GPT-5.5 gunna be great at that i bet too
ChandrashekarMuthumula — 11:29 AM
Thank you 👍
pablocotan — 11:29 AM
In another discord event, it was presented how to connect Foundry Agents with Copilot Studio Agents. To acchieve that, it was necessary to assign certain RBAC changes to the hosted-agent. Is there any place with "typical" RBAC roles we might need for hosted-agents?
Nnamdi — 11:31 AM
is it much harder to set up? you might end up with each agent in a docker container if you want to scale it across a company or across lots of users. So maybe just for production scaling situations. 
Pamela FoxRole icon, Microsoft — 11:33 AM
https://devblogs.microsoft.com/foundry/from-local-to-production-the-complete-developer-journey-for-building-composing-and-deploying-ai-agents/
Microsoft Foundry Blog
Takuto Higuchi
From Local to Production: The Complete Developer Journey for Buildi...
When we launched Microsoft Agent Framework last October, we made a promise: building production-grade AI agents should feel as natural and structured as building any other software. Today, we’re delivering on that promise — with the v1.0 release of Microsoft Agent Framework and the general availability of Foundry Toolkit for Visual Studio Co...
From Local to Production: The Complete Developer Journey for Buildi...
💡 Pricing: Hosted agents billing begins April 22, 2026 during preview. You pay only for active execution: compute is $0.0994 per vCPU-hour and memory is $0.0118 per GiB-hour. Model inference and persistent memory are billed separately. See the Foundry Agent Service pricing page.
https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent#invoke-the-agent-1
Deploy a hosted agent - Microsoft Foundry
Deploy your containerized agent code to Foundry Agent Service using the Python SDK or REST API.
Deploy a hosted agent - Microsoft Foundry
Kalyan a.k — 11:38 AM
can we have agent endpoints proxied with a api gateway and have policies applied at the gateway level?
like ratelimiting, auth policies
..etc
yes
pablocotan — 11:43 AM
https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities
Kalyan a.k — 11:43 AM
I have seen this for Azure functions not sure abt agnets
Pamela FoxRole icon, Microsoft — 11:47 AM
https://pydantic.dev/articles/pydantic-monty
Pydantic Monty: A Minimal Python Sandbox for AI Agents | Pydantic
Meet Monty — a secure, minimal Python interpreter written in Rust for running AI-generated code. Learn where it sits between tool calling and full computer use, and why CodeMode matters for AI agents.
Pydantic Monty: A Minimal Python Sandbox for AI Agents | Pydantic
asx — 11:47 AM
Here is monty in my strava-mcp: https://github.com/saxenanurag/strava-mcp/blob/main/server.py#L142
GitHub
strava-mcp/server.py at main · saxenanurag/strava-mcp
MCP server for Strava API - Connect AI agents to your athletic data. Retrieve athlete stats, activities, lap splits, and GPS/heart rate streams. Built with Python and FastMCP. - saxenanurag/strava-mcp
strava-mcp/server.py at main · saxenanurag/strava-mcp
a local function is what I mean and then it just becomes a tool for an agent
find the max or min
riskfwd — 11:50 AM
Spent literally the last 50 mins troubleshooting RTC connection error 🤦‍♂️ this wasnt recorded was it? i was really looking forward to it!
sweet thanks!
asx — 11:52 AM
line 79 is exactly what I meant. Thank you.
Sweet!
Pamela FoxRole icon, Microsoft — 11:58 AM
https://gist.github.com/pamelafox/47c380e63687164fe1748c231f07998f
Gist
Agent Framework plus Monty tool
Agent Framework plus Monty tool. GitHub Gist: instantly share code, notes, and snippets.
Agent Framework plus Monty tool. GitHub Gist: instantly share code, notes, and snippets.
asx — 11:58 AM
Thank you!
RyanPrice1001 — 11:59 AM
Thanks Pamela!🚀🚀🚀
riskfwd — 11:59 AM
pam do you like getting nerd mail or as a public person does that give you the parasocial heebie jeebies? figured id ask before i send this one (not foundry) project over once its finished, since based on your git it seems like you dont just like flashcards cause they make good demos lol
Kalyan a.k — 11:59 AM
Thank you very much @Pamela Fox
pablocotan — 11:59 AM
unfortunatelly for Pamela, we go more and more into an agent-management world and away from the agent-coding world
riskfwd — 12:00 PM
yeah absolutely zero pressure to respond lol , wasnt a question but a share. thought youd find it interesting just cause how many times youve done similar impl 
Jorge Zúñiga — 12:00 PM
🙌 Thank you!
riskfwd — 12:00 PM
please come to the CIO Symposium next month at MIT! hit me up for a ticket
Pamela FoxRole icon, Microsoft — 12:01 PM
https://github.com/orgs/microsoft-foundry/discussions/380
GitHub
Host your agents on Foundry (livestream series): Resources · micro...
Join us for our 3-part live stream series on deploying your agents and workflows to Microsoft Foundry! Register for the series Livestreams Tune in for the live streams from April 27th - April 30th,...
asx — 12:01 PM
Thank you! 
pablocotan — 12:01 PM
thank you!
itsmeleece — 12:01 PM
Thanks!
Raja P — 12:01 PM
thanks
Kalyan a.k — 12:02 PM
Thank you!!
riskfwd — 12:02 PM
cya thanks
Pamela Fox
 ended Host your agents on Foundry: Microsoft Agent Framework — 12:02 PM
ErikN — 12:02 PM
I missed this whole thing! The announcement says this session is tomorrow. Is it being repeated tomorrow?
riskfwd — 12:02 PM
there is a 3 day series going on, and both the earlier stream and this after thing were recorded 🙂
riskfwd — 12:04 PM
hopefully i dont get nuked for copy pasting a MS link with this brand new account

https://aka.ms/AgentsOnFoundry/series
Microsoft Reactor
Host your agents on Foundry | Microsoft Reactor
Attend Reactor Event Series for on-going opportunities to learn, connect, and build. Expand your skillset.
Image
earlier stream here https://www.youtube.com/live/8N7q0Ucr3rw

correction: not 3 consecutive days. also you should look around for something happening on thursday... 
YouTube
Microsoft Reactor
Microsoft Reactor
Image
ErikN — 12:07 PM
"also you should look around for something happening on thursday..." intriguingly stated - you have my curiosity! Thanks for the links!