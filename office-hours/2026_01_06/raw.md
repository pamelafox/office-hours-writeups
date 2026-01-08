# January 6, 2026 Office Hours Resources

* [Recording](https://www.youtube.com/watch?v=LZLg_hQYk4I)

These were the primary topics and links shared:

* MCP + Python
   * [PR to python-mcp-demos to add Entra OBO](https://github.com/Azure-Samples/python-mcp-demos/pull/27)
   * [MCPJam Inspector](https://github.com/MCPJam/inspector)
   * [Python + MCP series recap](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/learn-how-to-build-mcp-servers-with-python-and-azure/4479402)
* Building M365 Agents for Microsoft Copilot in Python:
   * [Blog post: Bring your own agents to M365 Copilot](https://devblogs.microsoft.com/microsoft365dev/bring-your-own-agents-into-microsoft-365-copilot/)
   * [Learn Docs: Deploy agent to M365](https://learn.microsoft.com/en-us/microsoft-365/agents-sdk/deploy-azure-bot-service-manually)
   * [Agent-framework + M365](https://github.com/microsoft/agent-framework/tree/main/python/samples/demos/m365-agent)
* [Resources for learning generative AI](https://blog.pamelafox.org/2025/08/how-i-learn-about-generative-ai.html)
* [Pragmatic Engineer: Building MCP servers in the real world](https://newsletter.pragmaticengineer.com/p/mcp-deepdive)

## Weekly slide content

Recent happenings:
Holiday break!

What I'm working on this week:
Entra OBO with Python MCP servers:https://github.com/Azure-Samples/python-mcp-demos/pull/27
Planning next Reactor series: what should it be about?

Upcoming events:
Microsoft AI Tour: https://aitour.microsoft.com/flow/microsoft/aitour/landing/page/home#find-city
MCP summit: https://events.linuxfoundation.org/mcp-dev-summit-north-america/program/cfp/
PyCon 2026: https://us.pycon.org/2026/


## Chat paste

These are pasted logs from the Discord chat during the office hours:


Pamela Fox — Yesterday at 11:06 AM
https://github.com/Azure-Samples/python-mcp-demos/pull/27
GitHub
Adding a tool that requires specific Entra group for access by pame...
This WIP branch shows how to use the Graph API with OBO flow to find out the groups of the signed in user, and use that to decide whether to allow access to a particular group.
First it modifies th...
This WIP branch shows how to use the Graph API with OBO flow to find out the groups of the signed in user, and use that to decide whether to allow access to a particular group.
First it modifies th...
technoidsvserse

 — Yesterday at 11:07 AM
Hi Pam
John v — Yesterday at 11:07 AM
are you sharing screen?
unclepatrick — Yesterday at 11:10 AM
Still don’t see screen?
John — Yesterday at 11:10 AM
yes, can see
mark6871

 — Yesterday at 11:10 AM
yep
technoidsvserse

 — Yesterday at 11:11 AM
GitHub actions authentication was failing and finally I had to zip deploy , I didn’t open any issue though
Indium

 — Yesterday at 11:12 AM
I can't see the screen either just black
Habibi — Yesterday at 11:13 AM
Rejoin
Indium

 — Yesterday at 11:16 AM
Rejoined twice and I still can't see the screen
mark6871

 — Yesterday at 11:20 AM
did you close discord completely and then rejoin after you reopen discord? 
pierred7274

 — Yesterday at 11:22 AM
I can see the screen
Chris — Yesterday at 11:22 AM
Stream is good
libis22 — Yesterday at 11:22 AM
It didn't work for me on phone but on browser it works.
mark6871

 — Yesterday at 11:23 AM
handling memory over long chat conversation would be nice to know tricks on
arunvinoth — Yesterday at 11:24 AM
See you in NYC 😎
libis22 — Yesterday at 11:24 AM
Can you please show the MCP inspector usage once? It didn't work for me when I tried
mark6871

 — Yesterday at 11:26 AM
mpc jam inspector ftw
John — Yesterday at 11:26 AM
would you recommend using frameworks for tracking llms usage tokens/costs (like langsmith, opik) or just saving it on prem and building a dashboard over it?
if you prefer saving it where would you recommend? in the same database as the application (for example, postgresql) or another database
John v — Yesterday at 11:27 AM
how did you keep yourself updated with all the new changes related to AI? I'm sure microsoft alone make lot of changes. curious to see what sources you follow.
perfectstorm — Yesterday at 11:28 AM
we are using litellm
Pamela Fox — Yesterday at 11:31 AM
https://github.com/MCPJam/inspector
GitHub
GitHub - MCPJam/inspector: Build ChatGPT Apps and MCP servers locally.
Build ChatGPT Apps and MCP servers locally. Contribute to MCPJam/inspector development by creating an account on GitHub.
Build ChatGPT Apps and MCP servers locally. Contribute to MCPJam/inspector development by creating an account on GitHub.
libis22 — Yesterday at 11:31 AM
JAM it is! 🙂
John — Yesterday at 11:33 AM
if you use multiple providers you need a way to consolidate it
pierred7274

 — Yesterday at 11:33 AM
How is MCPJams differ from LMStudio as MCP? Does it just boil down to models available since LM has small language models?
Pamela Fox — Yesterday at 11:35 AM
https://blog.pamelafox.org/2025/08/how-i-learn-about-generative-ai.html
How I learn about generative AI
I do not consider myself an expert in generative AI, but I now know enough to build full-stack web applications on top of generative AI mode...
Image
unclepatrick — Yesterday at 11:35 AM
Not sure if this is on topic, but what can you point me to that shows the possibilities for building a complete Microsoft copilot agent in python, including our own custom API calls to different services?
Pamela Fox — Yesterday at 11:36 AM
https://elite-ai-assisted-coding.dev/
Elite AI Assisted Coding | Substack
The ONE place to go for everything you need to know about AI assisted coding and tools. Click to read Elite AI Assisted Coding, a Substack publication.
Elite AI Assisted Coding | Substack
shafikul — Yesterday at 11:37 AM
as backend developer non-cse background .. how can i learn from scratch about ai
Pamela Fox — Yesterday at 11:37 AM
https://www.dbreunig.com/2025/12/29/2025-in-review.html
Drew Breunig
2025 in Review: Jagged Intelligence Becomes a Fault Line
Looking back on 2025, the incredible pace of AI is stunning. But fast growth brings disconnects.
Image
unclepatrick — Yesterday at 11:41 AM
Like for users using Microsoft Copilot app
Yes like from there
Or even from that web UI
pierred7274

 — Yesterday at 11:42 AM
Thanks Pam for answering my question
unclepatrick — Yesterday at 11:43 AM
That might be good.
perfectstorm — Yesterday at 11:44 AM
we are using this one:
https://learn.microsoft.com/en-us/agent-framework/
Agent Framework documentation
Agent Framework documentation.
Agent Framework documentation
XxXChilangoXxX

 — Yesterday at 11:45 AM
✌️🏽✌️🏽
unclepatrick — Yesterday at 11:46 AM
Ok I can do more research on it.
Thanks!
Pamela Fox — Yesterday at 11:47 AM
https://github.com/microsoft/agent-framework/tree/main/python/samples/demos/m365-agent
GitHub
agent-framework/python/samples/demos/m365-agent at main · microsof...
A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. - microsoft/agent-framework
agent-framework/python/samples/demos/m365-agent at main · microsof...
https://learn.microsoft.com/en-us/microsoft-365/agents-sdk/deploy-azure-bot-service-manually
Deploy your agent to Azure manually
Learn how to deploy your agent to Azure, Teams, or M365
Deploy your agent to Azure manually
unclepatrick — Yesterday at 11:48 AM
SUPER HAPPY to hear your confusion as well! lol
Pamela Fox — Yesterday at 11:49 AM
https://devblogs.microsoft.com/microsoft365dev/bring-your-own-agents-into-microsoft-365-copilot/
Microsoft 365 Developer Blog
Daniel Carrasco
Bring your own agents into Microsoft 365 Copilot - Microsoft 365 De...
Custom Engine Agents now generally available—build and integrate your own AI into the flow of work Microsoft 365 Copilot is redefining how people interact with AI—embedding it directly into the flow of work as the intuitive, natural interface for agents: the ‘UI for AI’ As Copilot becomes the interface for AI in the workplace, we’re […]
Bring your own agents into Microsoft 365 Copilot - Microsoft 365 De...
unclepatrick — Yesterday at 11:50 AM
Wonderful. Thanks!!
perfectstorm — Yesterday at 11:51 AM
ttfn -- thx!
Pamela Fox — Yesterday at 11:52 AM
https://techcommunity.microsoft.com/blog/educatordeveloperblog/level-up-your-python--ai-skills-with-our-complete-series/4464546
TECHCOMMUNITY.MICROSOFT.COM
Level up your Python + AI skills with our complete series | Microso...
We've just wrapped up our live series on Python + AI, a comprehensive nine-part journey diving deep into how to use generative AI models from Python.
The...
Level up your Python + AI skills with our complete series | Microso...
pierred7274

 — Yesterday at 11:52 AM
The MCPJam explanation is terrific. Again thank you
Pamela Fox — Yesterday at 11:53 AM
https://techcommunity.microsoft.com/blog/azuredevcommunityblog/learn-how-to-build-mcp-servers-with-python-and-azure/4479402
TECHCOMMUNITY.MICROSOFT.COM
Learn how to build MCP servers with Python and Azure | Microsoft Co...
We just concluded Python + MCP, a three-part livestream series where we:

Built MCP servers in Python using FastMCP
Deployed them into production on Azure...
Learn how to build MCP servers with Python and Azure | Microsoft Co...
libis22 — Yesterday at 11:54 AM
Anything new on our RAG demo after the SharePoint data source add?
Pamela Fox — Yesterday at 11:57 AM
https://newsletter.pragmaticengineer.com/p/mcp-deepdive?utm_source=substack&publication_id=458709&post_id=181156882&utm_medium=email&utm_content=share&utm_campaign=email-share&triggerShare=true&isFreemail=true&r=47i8u&triedRedirect=true
Building MCP servers in the real world
How engineers and teams use MCP servers: from debugging to working with legacy systems, & giving non-devs more access. Details from 40+ devs – with some surprises
Building MCP servers in the real world
libis22 — Yesterday at 11:58 AM
As a company or even a department, do you think we will create MCP servers to for AI apps to connect to in the future?
Thank you!! as always, great content! 🙂