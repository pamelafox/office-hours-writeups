# February 25, 2026 Python + Agents Session 2 Office Hours Resources

## Recording:

https://www.youtube.com/watch?v=X0m0GxJRT0Y

## Slide content:

No slides for the office hours itself, this session was a follow-up office hours after this livestream:
https://developer.microsoft.com/en-us/reactor/events/26689/

## Links from open tabs:

https://streamyard.com/teams/yfgXFbwTJEBTHs5jbsSYAiTk/videos/p7cp3bs3nd7n/edit
https://github.com/Azure-Samples/python-agentframework-demos
https://congenial-waddle-rp5xgr5xv3577r.github.dev/
https://github.com/orgs/microsoft-foundry/discussions/331
https://github.com/Azure-Samples/python-agentframework-demos?tab=readme-ov-file#using-azure-ai-foundry-models
https://github.com/pamelafox/presentation-writeups/blob/main/presentations/python-agents-session1/outputs/writeup.md
https://learn.microsoft.com/en-us/agent-framework/get-started/hosting?pivots=programming-language-python
https://github.com/simonjj/playwright-mcp-on-aca
https://docs.mem0.ai/open-source/features/graph-memory
https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview?view=foundry-classic&pivots=programming-language-python
https://github.com/Azure-Samples/ai-model-start?tab=readme-ov-file#the-ai-model-starter-kit
https://github.com/langchain-ai/langchain/blob/94a58825d352e15b2f5a132859b08827f7b208fb/libs/langchain_v1/langchain/agents/middleware/context_editing.py
https://microsoft.sharepoint.com/teams/GitHubCopilotatMicrosoft/Shared%20Documents/Copilot%20in%20VS%20Code/Screenshot%202026-02-23%20at%2011.21.47%E2%80%AFAM.png
https://docs.weaviate.io/weaviate/tutorials/multi-vector-embeddings
https://techcommunity.microsoft.com/blog/appsonazureblog/what%E2%80%99s-new-for-python-on-app-service-for-linux-pyproject-toml-uv-and-more/4468903
https://github.com/microsoft/agent-framework/pull/4210
https://tonybaloney.github.io/posts/performance-benchmarking-llm-models.html
https://github.com/toon-format/toon

## Discord chat paste

sbonds — 11:39 AM
Q for Pam: How can we configure the GitHub workspace to call paid, authenticated Azure LLMs to avoid the issues with free GitHub LLM usage? ("How can we give Microsoft more money" seems like an odd question for me to ask, but there it is...)

Pamela FoxRole icon, Microsoft — 11:42 AM
https://github.com/orgs/microsoft-foundry/discussions/331
Bernhard Merkle — 11:42 AM
we go full speed 🙂
sbonds — 11:43 AM
A: RTFM https://github.com/Azure-Samples/python-agentframework-demos?tab=readme-ov-file#using-azure-ai-foundry-models
GitHub
GitHub - Azure-Samples/python-agentframework-demos
Contribute to Azure-Samples/python-agentframework-demos development by creating an account on GitHub.
Contribute to Azure-Samples/python-agentframework-demos development by creating an account on GitHub.
sbonds — 11:44 AM
Must use keyless or code changes needed.

Rose P

 — 11:45 AM
Will this series cover hosting agents in Azure, such as options, best practices?
sbonds — 11:46 AM
There was a question about how to have multi-tier memory choices to store lots of stuff if more details are needed but keeping the local storage managable. Is it helpful to toss the details when summarizing or is it useful to keep them as part of a re-summary with the full original context?
Patrick

 — 11:47 AM
What would you suggest how to learn all of this? I think I will try to build a standard agent first and then build on that. Or if you have any other suggestions, please let me know... 😢
Pamela FoxRole icon, Microsoft — 11:47 AM
https://learn.microsoft.com/en-us/agent-framework/get-started/hosting?pivots=programming-language-python
Step 6: Host Your Agent
Deploy your agent so users and other agents can interact with it.
Step 6: Host Your Agent
sbonds — 11:47 AM
I recommend this paid service for learning more: https://www.boot.dev/courses/build-ai-agent-python

It's NOT cheap but the lessons are well thought out and hands-on.
Boot.dev
Build an AI Agent in Python [Full Course] | Boot.dev
Write a toy agentic code editor in Python, similar to Claude Code or Cursor's Agent Mode. Understand how agents work from scratch by using the Google Gemini API to create an LLM-powered code agent. You'll use function calling and feedback loops to build an agent that can find and fix bugs in a real project!
Build an AI Agent in Python [Full Course] | Boot.dev
Bernhard Merkle — 11:48 AM
VSCode often forgets about that i have a .venv in my project, so does is swap out that knowledge out of its memory from time to time ? i then starts process which fail to run of course because libs etc are missing. (they are in the .venv)
Patrick

 — 11:48 AM
@GPS I saw a video of you talking about that you were overwhelmed... I feel a little like that right now 🙂
Pkay — 11:48 AM
2 question (sorry if naive or basic)
1) Why to use agent fwk and not foundry SDK
2) And why to consider non foundry hosting options. 
Pamela FoxRole icon, Microsoft — 11:48 AM
https://github.com/simonjj/playwright-mcp-on-aca
Bernhard Merkle — 11:48 AM
is should say VSCode Github Copilot
GPSRole icon, Microsoft — 11:49 AM
@Patrick lol nothing a little extra studying can't cure 🙂

Manny — 11:49 AM
from your 2 presentations thus far, it appears designing your overall project (programs/agents) cannot be llm agnostic.  The way we design/build tools, manage memory are designed based on the llm.  Can you confirm?  Thanks!
sbonds — 11:49 AM
I'm thinking more when a summary happens, should the original be saved for a later summary?
Patrick

 — 11:50 AM
haha!! yeah I know. I am still relatively young... 🤣
Tea-Leaf — 11:51 AM
How/why would the original summary be used later?
Patrick

 — 11:52 AM
Food!!!
sbonds — 11:52 AM
My thought was that if the full original context was kept for some short-term use it would allow each summary to be higher quality instead of having losses building on losses leading to lower quality.
dapakwat — 11:52 AM
like llm council? aka andrej karpathy?
sbonds — 11:52 AM
E.g. the 100x-transcoded video problem. 🙂
GPSRole icon, Microsoft — 11:53 AM
i love boot.dev
algos course with python is awesome
sbonds — 11:53 AM
Just don't talk with me about red/black trees. Ow! My brain!
Bernhard Merkle — 11:53 AM
hey cool, did not know this
Tea-Leaf — 11:54 AM
I peeked at the summarization prompt and it seems like summarizing once may be good enough, keeping in mind you're trying to trim out extraneous info from being passed to the agent/LLM, which can reduce quality. 
sbonds — 11:55 AM
Yeah, we're trying to minimize the amount sent to the primary LLM. My thought was that we could get better info by sending more to the summarizing LLM.

Probably no way to know since it will depend on the specific situation. I'll just have to try it and see. 🙂

Rose P

 — 11:58 AM
I have a PoC running in a Foundry Agent and I have started running into its limitations
It makes some choices for you but doesn't seem to offer ways to change them if you are using the Portal. I have to dig deeper into the SDK to see what I can configure through that
Pamela FoxRole icon, Microsoft — 12:01 PM
https://github.com/Azure-Samples/ai-model-start
Manny — 12:03 PM
Thank You!
TeakDragon — 12:03 PM
Has anybody who use Foundry Agent run into breaking changes? Wondering if I would need to keep up with version after a half year or so
Pamela FoxRole icon, Microsoft — 12:04 PM
https://github.com/langchain-ai/langchain/blob/94a58825d352e15b2f5a132859b08827f7b208fb/libs/langchain_v1/langchain/agents/middleware/summarization.py
sbonds — 12:06 PM
Good example of lost context with the "Yes, please"
Pkay — 12:07 PM
yes, today with new foundry. the code interpreter is not working on eus2 since morning 🙂
dapakwat — 12:07 PM
Also had that experience.  Now I know why.
sbonds — 12:08 PM
"Should I delete all your files?"
"No, thank you."
"OK, should I make a summary of our conversation?"
"Yes, please"
compacting conversation
deleting all your files
Tea-Leaf — 12:08 PM
So, did CoPilot expect you to use the thumbs up button to reply to the summary question?
Hiram

 — 12:08 PM
that yes please is very funny in agent mode... "experiences from the field"
Pkay — 12:09 PM
hahaha flu 🙂

sbonds — 12:09 PM
I figured the thumbs were like the elevator "door close" button.
Bernhard Merkle — 12:10 PM
we have a railguard for e.g. prompts to have a minimal lenght for agents (not GH Copilot). You can ignore it, but it "motivates" people to be more explicit and deliver the context so the LLMs/Agent gets the right direction.
now Agent.IQ ?
Rose P

 — 12:11 PM
I also prefer the code path but I lost that argument lol
Patrick

 — 12:12 PM
So what are the issues with Foundry? I am try to use that
Bernhard Merkle — 12:12 PM
is IQ using graphRAG ? with knowledge graphs ?
Patrick

 — 12:13 PM
What do you recommend for building agents...? for learning i mean 
Rose P

 — 12:13 PM
The previous version of Foundry is no longer being updated to support newer models such as GPT-5. The new Foundry still has a lot of services that are in preview 
Pkay — 12:13 PM
not using hosted agent ?
pixelsnbits — 12:13 PM
With MS Agent Framework, is there any middleware context caching that can cut down on token usage? (My grip on the AI Agent ecosystem vocab is still new, so forgive me if the question doesn't make sense ..) .. something different than summarization 
Rose P

 — 12:14 PM
Yeah, I pushed for langchain but the team wanted a hosted solution
This series is making me want to start that argument again though
I just think in code, not infrastructure deployments/configuration
JohnRole icon, MVP — 12:16 PM
Do you have any samples with app service and uv on azure?
pixelsnbits — 12:16 PM
Yes
Pamela FoxRole icon, Microsoft — 12:18 PM
https://github.com/langchain-ai/langchain/blob/94a58825d352e15b2f5a132859b08827f7b208fb/libs/langchain_v1/langchain/agents/middleware/context_editing.py
Bernhard Merkle — 12:18 PM
modelrouter  saves also token
asx — 12:18 PM
This might be out of scope but is it possible to use Skills ala github copilot?
pixelsnbits — 12:18 PM
Great, much appreciated for the outloud thinking, def realize there's no exact answer
JohnRole icon, MVP — 12:19 PM
https://techcommunity.microsoft.com/blog/appsonazureblog/what’s-new-for-python-on-app-service-for-linux-pyproject-toml-uv-and-more/4468903
TECHCOMMUNITY.MICROSOFT.COM
What’s New for Python on App Service for Linux: pyproject.toml, u...
Python apps on Azure App Service for Linux just got a lot easier to build and ship! We’ve modernized the build pipeline to support new deployment options...
What’s New for Python on App Service for Linux: pyproject.toml, u...
GPSRole icon, Microsoft — 12:19 PM
let me find it one sec
JohnRole icon, MVP — 12:19 PM
I found this but not able to make it work lol 
Bernhard Merkle — 12:19 PM
but modelrouting helps only for simple questions when you have a tool expensive LLM for that question IMO
GPSRole icon, Microsoft — 12:19 PM
@John what error do you get?
app or container?
https://github.com/madebygps/azd-simple-fastapi-container-appservice
GitHub
GitHub - madebygps/azd-simple-fastapi-container-appservice: Basic c...
Basic containarized FastAPI as an AZD template for Azure App Service - madebygps/azd-simple-fastapi-container-appservice
GitHub - madebygps/azd-simple-fastapi-container-appservice: Basic c...
JohnRole icon, MVP — 12:20 PM
app service, i'm getting the logs
pixelsnbits — 12:20 PM
https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-router?view=foundry-classic .. assume this is similar to GitHub Copilot agent when selecting 'Auto' for model selection

Model router for Microsoft Foundry concepts - Azure OpenAI
asx — 12:20 PM
sweet
Pamela FoxRole icon, Microsoft — 12:21 PM
https://github.com/microsoft/agent-framework/pull/4210
JohnRole icon, MVP — 12:21 PM
@GPS 2026-02-25T20:20:28.2458875Z Updated PYTHONPATH to '/opt/startup/app_logs:/tmp/8de74a9b92de4ee/antenv/lib/python3.12/site-packages'
2026-02-25T20:20:28.2805986Z /tmp/8de74a9b92de4ee/entrypoint.sh: line 7: uv: command not found
GPSRole icon, Microsoft — 12:21 PM
do you have link to repo?
JohnRole icon, MVP — 12:22 PM
it was working i'm trying to port it to uv
https://github.com/Azure-Samples/Cosmic-Food-RAG-app
Hiram

 — 12:23 PM
Can you share some comments about the TOON notation project? https://github.com/toon-format/toon
GitHub
GitHub - toon-format/toon: 🎒 Token-Oriented Object Notation (TOO...
🎒 Token-Oriented Object Notation (TOON) – Compact, human-readable, schema-aware JSON for LLM prompts. Spec, benchmarks, TypeScript SDK. - toon-format/toon
GitHub - toon-format/toon: 🎒 Token-Oriented Object Notation (TOO...
Pamela FoxRole icon, Microsoft — 12:23 PM
https://tonybaloney.github.io/posts/performance-benchmarking-llm-models.html
https://www.dbreunig.com/
Drew Breunig
Drew Breunig
Writing about AI, geo, culture, media, data, and the ways they interact.
Image
https://x.com/dbreunig/status/2021447592996167872
Drew Breunig (@dbreunig)
Nice to see data confirming what we suspected about TOON, and other novel formats: saving a handful of tokens in the data format is wasted if models aren't trained on the format.
Image

X•2/10/26, 8:53 PM
Manuel — 12:26 PM
are these office hours recorded for later access ?
Hiram

 — 12:26 PM
Ohh I see thats very insighfull its works a lot to my research... thank you so much for sharing!
Pamela FoxRole icon, Microsoft — 12:26 PM
https://github.com/orgs/microsoft-foundry/discussions/331
Manuel — 12:26 PM
🎉
Manny — 12:27 PM
Nice work.  Thanks much!
bane — 12:27 PM
Thank you!
Bernhard Merkle — 12:27 PM
great session 🙂
Manuel — 12:27 PM
do you Blog ?
itsmeleece — 12:27 PM
Thanks!
RyanPrice1001 — 12:27 PM
Thanks Pamela!
coolasc

 — 12:27 PM
great session and thank you once again
Rose P

 — 12:27 PM
Another great session!!
Patrick

 — 12:27 PM
Thanks @Pamela Fox !! awesome as always
pixelsnbits — 12:27 PM
Thanks Pamela, exciting stuff
juan lanzi — 12:28 PM
Thank you so much!
MarcusS — 12:28 PM
Very nice job.  Thank you
dapakwat — 12:28 PM
Yes absolutely.  Thank you for a great session.  One day late, but still awesome.  Be here tomorrow and the following sesh.