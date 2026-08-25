# Discord chat fallback

YouTube live chat replay was not available for this recording. Times below are Discord wall-clock times, not video timestamps.

Ahmed — 11:14 AM
I have 3 years of experience as a cloud platform engineer and am currently transitioning toward building AI automations, specifically chatbots and RAG agents (using Google Antigravity). While I can read and understand Python code decently well, I am not a developer from scratch, and I'm deeply skeptical of the raw code that AI agents generate. Given my infrastructure background, what are the best steps, frameworks, or architectural practices I should adopt to bridge this gap and build production-grade, highly reliable AI applications? Would love to hear your insights on balancing safe code execution with AI agent autonomy. Thanks!

Justin Trantham [FlowDevs.io] [FLOW] — 11:18 AM
Start with something fun and small

Pamela Fox [Microsoft] — 11:23 AM
https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-public-preview-markdown-for-agents-in-azure-app-service/4537023

pablocotan — 11:23 AM
also we have https://webmcp.dev/
Will that get more used?

Justin Trantham [FlowDevs.io] [FLOW] — 11:25 AM
I hope so - I create what I think would be helpful https://github.com/CakeRepository/JuanPage which works similar i think (just renders websites real time) user talks to chat and builds frontend at runtime. Then the agent builds the UI are runtime.

Are you using it?

Pamela Fox [Microsoft] — 11:26 AM
https://github.com/webmachinelearning/webmcp

Justin Trantham [FlowDevs.io] [FLOW] — 11:26 AM
No its all chat the agent looks at the codebase
Its schema driven
lol
Tell the agent to make you a pizza?
Github copilot with the pizza url?

Pamela Fox [Microsoft] — 11:32 AM
https://googlechromelabs.github.io/webmcp-tools/demos/pizza-maker/?share=JTdCJTIyc2l6ZSUyMiUzQSUyMkV4dHJhJTIwTGFyZ2UlMjIlMkMlMjJzdHlsZSUyMiUzQSUyMkNsYXNzaWMlMjIlMkMlMjJsYXllcnMlMjIlM0ElN0IlMjJzYXVjZSUyMiUzQWZhbHNlJTJDJTIyY2hlZXNlJTIyJTNBZmFsc2UlN0QlMkMlMjJ0b3BwaW5ncyUyMiUzQSU1QiU3QiUyMmVtb2ppJTIyJTNBJTIyJUYwJTlGJThDJUI2JUVGJUI4JThGJTIyJTJDJTIyc2l6ZSUyMiUzQSUyMk1lZGl1bSUyMiUyQyUyMmNvdW50JTIyJTNBNSU3RCU1RCU3RA%3D%3D

John [MVP] — 11:37 AM
I think you found it already but you needed to ask it to use the tool
the ai assistant thingy you clicked on before clicking on gemnii

Justin Trantham [FlowDevs.io] [FLOW] — 11:39 AM
It would be nice to never have to build a UI and just have the agent build it at watch time

Pamela Fox [Microsoft] — 11:40 AM
https://gofastmcp.com/apps/generative

pablocotan — 11:41 AM
What I understood as very useful is specially if the website has a lot of information to be scraped (and navigated), and you have a tool to find products, then it would be faster, save tokens, and simplify the agent work

Justin Trantham [FlowDevs.io] [FLOW] — 11:41 AM
have you looked at NLWeb?

John [MVP] — 11:41 AM
ohhh i found that removing the attached webpage works
in the message box below there is an x button
to attach the reference when asking

Pamela Fox [Microsoft] — 11:43 AM
https://github.com/ChromeDevTools/chrome-devtools-mcp

Justin Trantham [FlowDevs.io] [FLOW] — 11:47 AM
all my prompts end with "by any means necessary"
(just kidding)

Pamela Fox [Microsoft] — 11:48 AM
https://github.com/pamelafox/pydanticai-playwright-agent

Justin Trantham [FlowDevs.io] [FLOW] — 11:48 AM
Grok 4.6 has been pretty good

pablocotan — 11:48 AM
https://learn.microsoft.com/en-us/microsoft-edge/web-platform/release-notes/151 for testing webmcp.. in theory

Justin Trantham [FlowDevs.io] [FLOW] — 11:49 AM
I've been using it through Cursor

Pamela Fox [Microsoft] — 11:50 AM
https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf

Justin Trantham [FlowDevs.io] [FLOW] — 11:51 AM
Rating on the ability to create a bio weapon is actually nuts

Pamela Fox [Microsoft] — 11:55 AM
https://github.com/Fission-AI/OpenSpec

Justin Trantham [FlowDevs.io] [FLOW] — 11:55 AM
The idea of WorkOS seems interesting. I've been letting agents run longer overnight

pablocotan — 11:57 AM
there are several very good articles in MEDIUM comparing different frameworks for spec driven development. Based on the project state, complexity, team size, level of testing, etc.

Justin Trantham [FlowDevs.io] [FLOW] — 11:59 AM
Lol i love that I've been its fun to hear people are thinking of similar stories. The project we are working on allows for agents to control computers remotely (https://flowrmm.com/) and it actually works. The question becomes, what should we allow it to do

its an MCP Remote Management

pablocotan — 12:00 PM
Is it time?

Justin Trantham [FlowDevs.io] [FLOW] — 12:00 PM
🙂