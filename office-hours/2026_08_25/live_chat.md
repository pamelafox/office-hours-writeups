BlackPandaChan — 11:08 AM
Any idea on how the billing works, is it based on who adds it to a channel, or who it's responding to, etc? 

What if the cost center bucket doesn't align with the channel user group (2 different cost centers?)
Is it in there and I just missed it?
I haven't read the docs yet, sorry I should have dug a bit before asking!
That's sensical!
I suppose the fact that it says it'll use your authentication likely means your credit bucket. This makes user-level budgets within cost centers even more important.
Abhishek Kumar [GMNI],  — 11:12 AM
A Start-up should opt for  Github Enterprise or not as its too  much costly  any solution or way out without sponsor ? 
JohnRole icon, MVP — 11:15 AM
maybe you didn't select yourself when you configured it?
yes
Krishna — 11:18 AM
so you created a slack account with same email same as github profile?
Pamela FoxRole icon, Microsoft — 11:19 AM
https://github.com/settings/installations
GitHub
Build software better, together
GitHub is where people build software. More than 150 million people use GitHub to discover, fork, and contribute to over 420 million projects.
Image
Image
Image
Krishna — 11:22 AM
i guess you logged into slack with same email as your github profile right?
Justin Trantham [FlowDevs.io] [FLOW],  — 11:23 AM
:flowdevsdancingrobot:
Krishna — 11:23 AM
ok makes sense
thank you!
JohnRole icon, MVP — 11:23 AM
I think we also now know how it's billed since it created a session on your github account
BlackPandaChan — 11:24 AM
Thank youuuuu!
Justin Trantham [FlowDevs.io] [FLOW],  — 11:25 AM
You have to add the app likely
You may need to do in in a thread
Image
You need a channel
Krishna — 11:31 AM
can i think this in MCP terms like Slack/Teams is client and github expose their services through server and github collects authentication of the user through oauth?
Jaybyrd [PYTX],  — 11:32 AM
Grateful for you putting this together! Kojo speaks so highly of you @Pamela Fox  I must run, but you have planted a seed.
JohnRole icon, MVP — 11:32 AM
maybe they sanitize links?
Justin Trantham [FlowDevs.io] [FLOW],  — 11:32 AM
People make channels/teams differently but per project is pretty normal
You have to make a team first.
JohnRole icon, MVP — 11:38 AM
it opened the pr as you? not copilot. how 
no it was copilot
yes, that's why I asked
Pamela FoxRole icon, Microsoft — 11:41 AM
https://docs.github.com/en/copilot/how-tos/copilot-integrations/integrate-cloud-agent-with-teams
GitHub Docs
Integrating Copilot cloud agent with Teams - GitHub Docs
You can use the GitHub integration in Teams to provide context and open pull requests all from within your Teams channels.
Image
Justin Trantham [FlowDevs.io] [FLOW],  — 11:45 AM
Grok Bot
Yeah, we got it included with Cursor.
pablocotan — 11:47 AM
Any comment on DeepSeek Harness? 
Do people talk about it in your environment?
Pamela FoxRole icon, Microsoft — 11:50 AM
https://github.com/openclaw/gogcli
GitHub
GitHub - openclaw/gogcli: Google Workspace in your terminal.
Google Workspace in your terminal. Contribute to openclaw/gogcli development by creating an account on GitHub.
GitHub - openclaw/gogcli: Google Workspace in your terminal.
lpk25 — 11:50 AM
Hey Pamela - hope you're doing well! - Can I get some documentation on hosted Agents being GA
Justin Trantham [FlowDevs.io] [FLOW],  — 11:50 AM
I think grok bot is good because it has access to a VM, MCP, Browser(in that VM), and automations
Pamela FoxRole icon, Microsoft — 11:51 AM
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/long-running-agent-resilience
Resilience for long-running Microsoft Foundry hosted agents (previe...
Understand how Microsoft Foundry hosted agents preserve long-running work, recover after process interruptions, and replay streamed results.
Resilience for long-running Microsoft Foundry hosted agents (previe...
lpk25 — 11:52 AM
Couldn't find it on blog
Got it Thank you!!!
Justin Trantham [FlowDevs.io] [FLOW],  — 11:53 AM
https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents
Hosted agents in Foundry Agent Service - Microsoft Foundry
Deploy and manage containerized agents on Foundry Agent Service with managed hosting, scaling, and observability.
Hosted agents in Foundry Agent Service - Microsoft Foundry
I guess yeah thats "concepts"
Pamela FoxRole icon, Microsoft — 11:54 AM
https://techcommunity.microsoft.com/blog/azuredevcommunityblog/browser-automation-with-pydantic-ai--playwright/4547971
TECHCOMMUNITY.MICROSOFT.COM
Browser automation with Pydantic-AI + Playwright | Microsoft Commun...
When we build agents, we often want to give them the ability to browse the web: open webpages, navigate from one page to the other, and read the content of a...
Browser automation with Pydantic-AI + Playwright | Microsoft Commun...
lpk25 — 11:55 AM
Where can we learn more about playwright?
How much does this cost?
pablocotan — 11:59 AM
For whom might be interested, I share the link to this article that seems to be important in the world of secure agents
https://blogs.nvidia.com/blog/open-secure-ai-alliance-contributions/ 
There are several tools provided from the members that worth to check.
Pamela FoxRole icon, Microsoft — 12:01 PM
https://github.com/pamelafox/personal-linkedin-agent
GitHub
GitHub - pamelafox/personal-linkedin-agent: An agent to manage my p...
An agent to manage my personal LinkedIn account, using playwright for browser automation. - pamelafox/personal-linkedin-agent
An agent to manage my personal LinkedIn account, using playwright for browser automation. - pamelafox/personal-linkedin-agent
https://aitour.microsoft.com/flow/microsoft/aitour27/globallanding/page/globalhome
Microsoft AI Tour | Accelerate your AI Transformation
See AI innovation in action. Explore customer stories, expert insights, hands-on experiences, and practical guidance to drive business transformation with AI.
Image
Justin Trantham [FlowDevs.io] [FLOW],  — 12:03 PM
:ty:
lpk25 — 12:03 PM
Thank you!!!!
BlackPandaChan — 12:04 PM
thank you!!!
lpk25 — 12:04 PM
Byee
JohnRole icon, MVP — 12:04 PM
thank you, bye!
Pamela Fox
 ended Python + AI  (Office Hours) — 12:04 PM
Pamela FoxRole icon, Microsoft — 12:14 PM
@lpk25 I found the announcement GA post is here: https://azure.microsoft.com/en-us/blog/gpt-5-6-now-available-in-microsoft-foundry/
But its bundled into other announcements, a bit hard to find-

Today, that vision moves from roadmap to reality with three sets of updates now generally available in Microsoft Foundry:

OpenAI’s latest frontier model series: GPT-5.6 Sol, GPT-5.6 Terra, and GPT-5.6—each tuned to a different workload, available in Standard Global and Standard Data Zones.
Asia-Pacific Data Zone, giving APAC customers a regional option to run frontier OpenAI models while keeping data processing within the region.
Production agents in Foundry Agent Service, with hosted agents, toolboxes, and publishing to Microsoft 365 Copilot and Microsoft Teams.
