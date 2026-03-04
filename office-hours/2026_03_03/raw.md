# March 3rd, 2026 Python + Agents Session 4 Office Hours Resources

## Recording:

https://www.youtube.com/watch?v=UDZ8oACh_1g
The recording cut out near the end due to internet issues. It may be possible to figure out the remaining questions asked based off the chat transcript.

## Slide content:

No slides for the office hours itself, this session was a follow-up office hours after this livestream:
https://developer.microsoft.com/en-us/reactor/events/26691/

## Links from open tabs:
https://streamyard.com/teams/yfgXFbwTJEBTHs5jbsSYAiTk/broadcasts
https://github.com/orgs/microsoft-foundry/discussions/331
https://github.com/Azure-Samples/python-agentframework-demos
http://localhost:28000/management/ai-agent
https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_01_26_copilot/writeup.md
https://github.com/Azure-Samples/azure-search-openai-demo/compare/main...pamelafox:azure-search-openai-demo:sdkexperiments
https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/
https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-campaigns/
http://127.0.0.1:8095/?entity_id=workflow_in_memory_workflowbuilder-3cd7f0be-f844-44c0-8940-639eb3e28a73_42dc02fdce6847cc885dd7ce5bca8dff
https://learn.microsoft.com/en-us/agent-framework/workflows/
https://developer.microsoft.com/en-us/reactor/series/S-1628/
https://learn.microsoft.com/en-us/credentials/browse/?terms=azure%20ai
https://github.com/orgs/microsoft-foundry/discussions/166
https://learn.microsoft.com/en-us/azure/foundry-local/get-started
https://github.com/microsoft/Foundry-Local

## Discord chat paste

Silvestre-PO — 11:33 AM
nop
Pamela FoxRole icon, Buildathon-Mod — 11:33 AM
BRB!
Pamela Fox
 is now a speaker. — 11:33 AM
Jorge Zúñiga — 11:34 AM
👌
Nnamdi — 11:34 AM
yes i can hear
bane — 11:34 AM
yes
dapakwat — 11:34 AM
👍
Nnamdi — 11:34 AM
how do you stop an agent from outputting an old value in its context rather than re-running a function tool or an api call?
saelcc03

 — 11:34 AM
It was an interesting session:)
Where do you post these discord sessions btw?
dapakwat — 11:35 AM
Awesome sesh
Nnamdi — 11:36 AM
it as an exchage rate agent
the agent didn't respet the prompt. it called once and then wanted to use stale values
theonlywur — 11:38 AM
How do you prevent malicious prompts from proliferating your workflows?
Pamela FoxRole icon, Buildathon-Mod — 11:39 AM
https://aka.ms/pythonagents/resources
GitHub
Python + Agents livestream series: Resources · microsoft-foundry ...
Join us for our 6-part live stream series on using Python with the Microsoft Agent Framework to build AI agents and agentic workflows! Register for the series Livestreams Tune in for the live strea...
Join us for our 6-part live stream series on using Python with the Microsoft Agent Framework to build AI agents and agentic workflows! Register for the series Livestreams Tune in for the live strea...
dapakwat — 11:39 AM
you are just too awesome...😆
GPSRole icon, Microsoft — 11:40 AM
THISONEFINAL.pptx
zαδoc — 11:42 AM
Hi Pamela. Please what would be your recommended approach of integrating the GitHub Copilot CLI and SDK in a DevOps workflow?
GPSRole icon, Microsoft — 11:42 AM
@zαδoc what do you mean by devops workflow? What are you trying to build/accomplish?
Pamela FoxRole icon, Buildathon-Mod — 11:45 AM
https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/
The GitHub Blog
Don Syme
Automate repository tasks with GitHub Agentic Workflows
Build automations using coding agents in GitHub Actions to handle triage, documentation, code quality, and more.
Automate repository tasks with GitHub Agentic Workflows
zαδoc — 11:45 AM
Analyzing CVEs in dependencies and making corrective actions on the PR
Steve Harris — 11:45 AM
Have you tried building MAF applications using Claude Code or Codex?
theonlywur — 11:46 AM
Is it just me or is the audio cut out?
dapakwat — 11:47 AM
sounds fine for me
GPSRole icon, Microsoft — 11:47 AM
sound is fine
bane — 11:48 AM
How likely is there to be scenario where the conditional workflow keeps requesting a "REVISION", causing an infinite loop, and Is there a way/need to prevent that?
Steve Harris — 11:49 AM
Thanks.
GPSRole icon, Microsoft — 11:50 AM
yeah I thought we changed it to 20?
lol
what happens if you set it to 8 now?
nice lol
Nnamdi — 11:53 AM
or if the llm get's into an attractor state and so maybe you need to summarise and restart.
Rose P

 — 11:54 AM
does the executor context include iteration count? Could you just skip the reviewer and return Approved or kick off some other flow?
CarnegieJ

 — 11:55 AM
Audio cut out on my end as well, I rejoined to resolve it.
RaBa — 11:56 AM
is it possible to see this session after its done? what is the link?
Tea-Leaf — 11:57 AM
When I uv run examples/workflow_switch_case.py --devui I get an unhanlded exception, which I don't get when I run without --devui. Is it something in my environment?

Error in workflow execution: 'NoneType' object has no attribute 'category'
Error setting up trace capture: 'dict' object has no attribute 'type'
Error executing entity workflow_in_memory_workflowbuilder-848b0991-f1a4-442d-8558-4950df568037_823f72e3d6954601bdb24183a635d9a4: generator didn't stop after throw()
RaBa — 11:58 AM
👍
Tea-Leaf — 11:58 AM
🙂 tks
Yes, in a couple of other switching/conditional examples the workflow didn't complete under devui, but worked fine with command line.
GPSRole icon, Microsoft — 12:01 PM
nice catch 🙂
saelcc03

 — 12:02 PM
Are you taking part in agents league judge?
GPSRole icon, Microsoft — 12:03 PM
GitHub outage is happening, including copilot
MarcusS — 12:04 PM
What is the link to your Javascript series?
Pamela FoxRole icon, Buildathon-Mod — 12:05 PM
https://developer.microsoft.com/en-us/reactor/series/S-1628/
Microsoft Reactor
The JavaScript AI Build-a-thon | Microsoft Reactor
Attend Reactor Event Series for on-going opportunities to learn, connect, and build. Expand your skillset.
Image
indu — 12:05 PM
I cannot hear you
saelcc03

 — 12:05 PM
is there a certification about agents from microsoft? like for azure there's azure fundamentals certification?
CarnegieJ

 — 12:06 PM
Rejoin the meeting
GPSRole icon, Microsoft — 12:06 PM
ai-900
and i think ai-101?
Tea-Leaf — 12:06 PM
Try refresh the web page (F5)
Pamela FoxRole icon, Buildathon-Mod — 12:08 PM
https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/
Microsoft Certified: Azure AI Engineer Associate - Certifications
Design and implement an Azure AI solution using Azure AI services, Azure AI Search, and Azure Open AI.
Microsoft Certified: Azure AI Engineer Associate - Certifications
CarnegieJ

 — 12:06 PM
AI-102 is a good one
GPSRole icon, Microsoft — 12:07 PM
oh yeah I think it is 102 not 101
thanks @CarnegieJ
just announced lol
Jorge Zúñiga — 12:07 PM
Which LLMs or SLMs do you recommend for running workflows locally?
GPSRole icon, Microsoft — 12:07 PM
we just lost you @Pamela Fox
Larry.Herzlich — 12:07 PM
yes
GPSRole icon, Microsoft — 12:07 PM
you froze
RyanPrice1001 — 12:08 PM
And, you are back!
CarnegieJ

 — 12:08 PM
Looks like there may bee DDOS happening
dapakwat — 12:08 PM
back
Jorge Zúñiga — 12:08 PM
AI -102
GPSRole icon, Microsoft — 12:08 PM
associate should be 102
fundamentals should be 900
Pamela FoxRole icon, Buildathon-Mod — 12:09 PM
https://learn.microsoft.com/en-us/credentials/applied-skills/create-an-ai-agent/
Microsoft Applied Skills: Create an AI agent - Applied Skills
Validate your technical skills and open doors to new possibilities of advancement with Microsoft Applied Skills.
Microsoft Applied Skills: Create an AI agent - Applied Skills
https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/
Microsoft Certified: Azure AI Fundamentals - Certifications
Demonstrate fundamental AI concepts related to the development of software and services of Microsoft Azure to create AI solutions.
Microsoft Certified: Azure AI Fundamentals - Certifications
jackz

 — 12:10 PM
Is there a place （URL) that I can find all your courses series to go through?
victor muthomi — 12:10 PM
What is the status in development of Foundry local for linux environment s
Jorge Zúñiga — 12:10 PM
@Pamela Fox AI-102
Pamela FoxRole icon, Buildathon-Mod — 12:10 PM
https://aka.ms/pythonai/resources
GitHub
Python + AI livestream series: Resources · microsoft-foundry · Di...
Join us for our 9-part live stream series on using Python with Generative AI models! 🐍 🤖 Register for the series Livestreams The livestreams are over, but you can catch up with recordings here: Top...
Python + AI livestream series: Resources · microsoft-foundry · Di...
GPSRole icon, Microsoft — 12:10 PM
ntd!
Pamela FoxRole icon, Buildathon-Mod — 12:10 PM
https://aka.ms/pythonmcp/resources
GitHub
Python + MCP livestream series: Resources · microsoft-foundry · D...
Join us for our 3-part live stream series on using Python to build FastMCP series on Azure! Livestreams Tune in for the live streams from Dec. 16th - 18th, or watch them after: Topic Register Slide...
Python + MCP livestream series: Resources · microsoft-foundry · D...
https://aka.ms/pythonagents/resources
GitHub
Python + Agents livestream series: Resources · microsoft-foundry ...
Join us for our 6-part live stream series on using Python with the Microsoft Agent Framework to build AI agents and agentic workflows! Register for the series Livestreams Tune in for the live strea...
Join us for our 6-part live stream series on using Python with the Microsoft Agent Framework to build AI agents and agentic workflows! Register for the series Livestreams Tune in for the live strea...
https://pamelafox.org/talks/
jackz

 — 12:11 PM
Thanks! May I communicate with you by email?
CarnegieJ

 — 12:11 PM
The Agent League hackathon has some really cool submissions that use the MSL MCP for helping with learning resource curations.
jackz

 — 12:14 PM
Thanks we have a lecture (free) of AI fundamentals for high school students which includes hands on exercises, like to talk to see if we can use some of the skills presented
Thanks, you have an email?
victor muthomi — 12:15 PM
okay .... I'll wait for your feedback.
what is your email?
saelcc03

 — 12:15 PM
I will gve a session about agents in my university too! I'd love to use your slides:)
jackz

 — 12:16 PM
Thanks! Pamelaffox@gmail.com
Pamela FoxRole icon, Buildathon-Mod — 12:16 PM
https://pamelafox.github.io/my-py-talks/
jackz

 — 12:16 PM
Sorry
saelcc03

 — 12:16 PM
will there be a surprise at the end of agents series?
certification from microsoft:)