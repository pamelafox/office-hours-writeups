# February 24, 2026 Python + Agents Session 1 Office Hours Resources

## Recording

https://www.youtube.com/watch?v=6HzauGnbRwA

## Slide content

No slides for the office hours itself, this session was a follow-up office hours after this livestream:
https://developer.microsoft.com/en-us/reactor/events/26688/

## Links from open tabs

https://github.com/orgs/microsoft-foundry/discussions/331
https://streamyard.com/teams/yfgXFbwTJEBTHs5jbsSYAiTk/videos/4rw9mnw6mxkd
https://github.com/Azure-Samples/python-agentframework-demos
https://didactic-space-acorn-9jgx9q494f7jr4.github.dev/
https://github.com/marketplace?type=models
https://simonwillison.net/2025/Sep/18/agents/
https://pypi.org/project/agent-framework/#history
http://127.0.0.1:8080/?entity_id=agent_in_memory_weekend-planner_b64655a78b4242bcae61a4ceb29fa7b1
https://onedrive.live.com/:p:/g/personal/B79CD1DB3ADA14C5/IQCvu3CcPAihQJR2lTLHhL2mAesfMurcz5Z57agwBYSDtLE?resid=B79CD1DB3ADA14C5!s9c70bbaf083c40a194769532c784bda6&ithint=file%2Cpptx&e=TE2ks7&migratedtospo=true&redeem=aHR0cHM6Ly8xZHJ2Lm1zL3AvYy9iNzljZDFkYjNhZGExNGM1L0lRQ3Z1M0NjUEFpaFFKUjJsVExIaEwybUFlc2ZNdXJjejVaNTdhZ3dCWVNEdExFP2U9VEUya3M3
https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?view=foundry-classic&tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#global-standard-model-availability
https://github.com/Azure-Samples/python-ai-agent-frameworks-demos/blob/main/examples/agentframework_tool.py
https://ollama.com/search?c=tools
https://www.bing.com/search?pglt=513&q=docker+inside+container+docker+internal+localhost&cvid=d961740b19e64a9691e3ba5ceffed244&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIICAEQ6QcY_FXSAQg2Nzc3ajBqMagCALACAA&FORM=ANNAB1&PC=U531
http://127.0.0.1:8080/?entity_id=agent_in_memory_supervisor_2824306ed37a471ebf9037b25d3af51b
https://developers.openai.com/api/docs/guides/function-calling#parallel-function-calling
https://github.com/microsoft/agent-framework/tree/main/python/samples/02-agents/providers/github_copilot
https://github.com/microsoft/agent-framework/blob/main/python/samples/02-agents/providers/github_copilot/github_copilot_basic.py
https://github.com/microsoft/agent-framework/tree/main/python/packages/github_copilot
https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli
https://github.com/login/device/success
https://docs.github.com/en/github-models/use-github-models/prototyping-with-ai-models#rate-limits
https://github.com/marketplace/models/azure-openai/gpt-4-1-mini
https://github.com/Azure-Samples/python-openai-demos/blob/main/chat.py

## Discord chat paste

TeakDragon — 11:36 AM
vote for what ever middleware is
JCurtis — 11:36 AM
I can hear you
Patrick

 — 11:36 AM
I was wondering about the function about middleware. I am still a little fuzy on when to use that.
sbonds — 11:36 AM
720 did suck. Glad it will be fixed.
GPSRole icon, Microsoft — 11:37 AM
yes
was 720 for ide
sbonds — 11:37 AM
It was 720 for the whole screen including the speaker video. Was bad.
saelcc03

 — 11:37 AM
what is 720?:0
Silvestre — 11:37 AM
Quality on session live on YT
el guansito — 11:37 AM
Hey Pam why the tools have hardcoded returns?
sbonds — 11:38 AM
Hey, I'm glad it will be better tomorrow.
TeakDragon — 11:39 AM
I think the other screen stopped showing
sbonds — 11:40 AM
As a blatant plug for a service I like but I get no payment for... the boot.dev "Build an AI Agent" course aligns nicely with the content from this course.

https://www.boot.dev/lessons/44e182d7-c2c6-4c7e-9313-1b078e301344

This is an EXPENSIVE service but the content is good.
Boot.dev
Build an AI Agent in Python: Build an AI Agent | Boot.dev
Ready to finally become a backend developer? Don't make it a grind. The smartest way to learn to code is to ensure you're never bored.
Build an AI Agent in Python: Build an AI Agent | Boot.dev
Patrick

 — 11:40 AM
so when you have N8N nodes, you have also things like "context" and "options" and stuff. Is that the same?
LotharMaax

 — 11:40 AM
Had a lot of trouble starting up the codespace.  (1) Was "main" the correct branch to use?  (2) I got an error on my very first uv run attempt: "'Unavailable model: gpt-5-mini'".  I think this was addressed in the chat, but it scrolled off before I could see the solution.
sbonds — 11:41 AM
The trick of rewinding video and then watching forward on 2x saved me a BUNCH of times in Pam's high speed info dump.
The above gpt-5-mini missing was solved by setting the environment variable GITHUB_MODEL to "gpt-4o" in one of several ways.

Awesome thanks Pam!
GPSRole icon, Microsoft — 11:43 AM
I love boot.dev
LotharMaax

 — 11:43 AM
In the terminal window before "uv run"?
@Salmanthird — 11:43 AM
Thanks sbonds 
 Helpful
perfectstorm — 11:43 AM
working with devui & can see the tool calls well

is it possible to the the full information sent to the llm? or is there a better way to view this?
sbonds — 11:43 AM
The problem with what context means is that it is...

context-dependent
Patrick

 — 11:44 AM
yeah, it's confusing sometimes...
sbonds — 11:44 AM
I solved it by using "export GITHUB_MODEL=gpt-4o" before running "uv run examples/agent_basic.py"
Patrick

 — 11:44 AM
great! another context...
pierred7274

 — 11:44 AM
Good point about distinguishing context and tools from the model’s perspective
Tea-Leaf — 11:44 AM
@Pamela Fox Curious to know whether these examples were coded manually, vibe coded, or a mix?
LotharMaax

 — 11:45 AM
I was just trying that exact same thing 😉
Patrick

 — 11:45 AM
It worked for me...
Pamela FoxRole icon, Microsoft — 11:45 AM
https://github.com/marketplace?type=models
GitHub
GitHub Models
Create AI-powered applications with GitHub
Create AI-powered applications with GitHub
Craig — 11:45 AM
You need to request GPT 5 from Microsoft to enable it on your new foundry
GPSRole icon, Microsoft — 11:45 AM
gpt-5-mini worked for me
and worked for someone else that I asked
@Salmanthird — 11:45 AM
I think middle ware will surely help for blue teamers . Since you can input several trade point and timing for the functions to prevent miss use @Pamela Fox
GPSRole icon, Microsoft — 11:45 AM
wondering if it was jsut an issue in the moment?
can someone else try now?
sbonds — 11:46 AM
Shoot... I looked away and don't know where the Discord rewind button is. 🙂

do you recommend starting with a deployed model with foundry for learning? I wanna do a multi agent with mcp integrations
Patrick

 — 11:47 AM
I do get an error sometimes
It's not stable
Tea-Leaf — 11:48 AM
I can see gpt-5-mini in my list of models, but still cannot use it in the examples. I had to set the model choice to gpt-4o

openai.BadRequestError: Error code: 400 - {'error': {'code': 'unavailable_model', 'message': 'Unavailable model: gpt-5-mini', 'details': 'Unavailable model: gpt-5-mini'}} 
perfectstorm — 11:48 AM
excellent, thank you
itsmeleece — 11:49 AM
At first gpt-5-mini worked, then I got an error, now it's taking a while...
asx — 11:50 AM
can we use local ollama models with the agent-framework?
Patrick

 — 11:50 AM
yeah, I am thinking of that as well @asx
sbonds — 11:51 AM
I tried a re-check via "unset OPENAI_MODEL" and got a return of "Unavailable model: gpt-5-mini"
Patrick

 — 11:51 AM
I have ollama installed on my laptop but haven't put it in an agent yet
pierred7274

 — 11:51 AM
Need to review middleware for understanding but great that you raised the topic
Patrick

 — 11:52 AM
ahaha!!
Rose P

 — 11:52 AM
I missed the session. Does anyone have a link to the example repo?
GPSRole icon, Microsoft — 11:52 AM
we manually vibe coded it

I think of MLStudio and ollama as middleware but could be thinking of it wrong
RaBa — 11:53 AM
Where can we see recording for this session? I missed first part
Tea-Leaf — 11:53 AM
Very cool. Thanks, Pam.
JCurtis — 11:53 AM
She uses her experience to direct the LLM 🙂
Patrick

 — 11:53 AM
I am still struggling with that though, If I should use vibe coding or not.. The thing is I want to understand it.
saelcc03

 — 11:53 AM
https://github.com/Azure-Samples/python-agentframework-demos
GitHub
GitHub - Azure-Samples/python-agentframework-demos
Contribute to Azure-Samples/python-agentframework-demos development by creating an account on GitHub.
Contribute to Azure-Samples/python-agentframework-demos development by creating an account on GitHub.
pierred7274

 — 11:54 AM
Raba I think Pam has a YouTube where recordings go
sbonds — 11:55 AM
I finished an entire boot.dev "Making an AI agent course" for $0.07 in AI payments.
TeakDragon — 11:55 AM
I did a Claude one for less then $5
Craig — 11:55 AM
does the tracing in framework sdk also work with the openai tracing?
libis22 — 11:56 AM
https://www.youtube.com/watch?v=I4vCp9cpsiI
YouTube
Microsoft Reactor
Python + Agents: Building your first agent in Python
Image
coolasc

 — 11:56 AM
vibe but know is, I think, the rule, vibing isn't bad, as long as you know what the output does by looking at it, so you know to come in and fix when needed
Pamela FoxRole icon, Microsoft — 11:56 AM
client = OpenAIChatClient(
        base_url=os.environ.get("OLLAMA_ENDPOINT", "http://localhost:11434/v1"),
        api_key="none",
        model_id=os.environ.get("OLLAMA_MODEL", "llama3.1:latest"),
    )
Craig — 11:56 AM
For local models just make sure you pick a model that supports tooling. not all models support tooling
Tea-Leaf — 11:57 AM
Feedback on agent_mcp_remote.py

It failed to run with gpt-4o
Reverting to gpt-5-mini allowed it to get a bit further, but it stopped with a message that I need to create an azure storage account
Pamela FoxRole icon, Microsoft — 11:57 AM
https://ollama.com/search?c=tools
Tools models · Ollama
Tools models on Ollama.
Image
GPSRole icon, Microsoft — 11:57 AM
@Tea-Leaf can you copy the message here please
should not need a storage account, that might be the models response
Patrick

 — 11:58 AM
ollama is huge
Craig — 11:58 AM
gpt-oss and the glm models are real nice to use if you have the vram. Qwen models are good for lower vram
Tea-Leaf — 11:58 AM
Doh!
sbonds — 11:58 AM
This didn't work, but I tried manually adding gpt-5-mini to the Model Catalog via the AI Toolkit.
GPSRole icon, Microsoft — 11:59 AM
did you use an ai to do it? lol
itsmeleece — 11:59 AM
🤯
GPSRole icon, Microsoft — 12:02 PM
HAHAHAHA
gotta love manual vibecoding
saelcc03

 — 12:02 PM
are all of the models you are using free?
Patrick

 — 12:03 PM
when you use ollama local on your laptop, do you use http://localhost/ ?
asx — 12:03 PM
can we pipe the copilot models in here? I do have a copilot subscription.
saelcc03

 — 12:03 PM
isn't it unsafe you show the keys? :0
sbonds — 12:04 PM
Tenant IDs are generally not a problem to be public.
Patrick

 — 12:04 PM
yeah oke, cool
Tea-Leaf — 12:04 PM
with the Ollama port
Patrick

 — 12:04 PM
oh 11434 nice
sbonds — 12:05 PM
It hurts my brain that Azure DevOps and Azure are different creds.
(It's still better than AWS)
Patrick

 — 12:06 PM
so how does the supervisor option work with multiple agents? That went a little fast for me 😄
haha, yes food stuff....
saelcc03

 — 12:08 PM
are yyou participating in agents league?
Patrick

 — 12:09 PM
that is so cool!
could that be because of the LLM?
Alden Weaver

 — 12:12 PM
That's interesting
Patrick

 — 12:12 PM
is that standard for gpt-5-mini?

https://developers.openai.com/api/docs/guides/function-calling#parallel-function-calling
Function calling | OpenAI API
Learn how function calling enables large language models to connect to external data and systems.
Function calling | OpenAI API
Patrick

 — 12:14 PM
Thank you @Pamela Fox !
Pamela FoxRole icon, Microsoft — 12:15 PM
https://github.com/microsoft/agent-framework/tree/main/python/samples/02-agents/providers/github_copilot
GitHub
agent-framework/python/samples/02-agents/providers/github_copilot a...
A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. - microsoft/agent-framework
A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. - microsoft/agent-framework
Patrick

 — 12:16 PM
It's for   good cause!!
Do you always use Codespaces or only for demo's and testing?
saelcc03

 — 12:21 PM
you changed the branch maybe?
Patrick

 — 12:21 PM
ram a little harder on the keyboard 🤣
asx — 12:21 PM
its all good. Thank you for trying. I will check out the example.
Pamela FoxRole icon, Microsoft — 12:21 PM
https://github.com/microsoft/agent-framework/tree/main/python/samples/02-agents/providers/github_copilot
GitHub
agent-framework/python/samples/02-agents/providers/github_copilot a...
A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. - microsoft/agent-framework
A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. - microsoft/agent-framework
Patrick

 — 12:22 PM
For sience!!
asx — 12:23 PM
lol
pablocotan — 12:24 PM
will the next series be about https://github.com/microsoft/agent-framework/tree/main/python/packages  , or you will have time to cover part of this?
GitHub
agent-framework/python/packages at main · microsoft/agent-framework
A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. - microsoft/agent-framework
agent-framework/python/packages at main · microsoft/agent-framework
asx — 12:24 PM
it does the pretty thing when you run it the first time
Patrick

 — 12:24 PM
oh no!!! not that screen again!
asx — 12:24 PM
copilot --banner
Craig — 12:24 PM
it only does it on the first time, change the copilot json config to allow it to run all the time 🙂
Patrick

 — 12:26 PM
What would be the use case of using copilot in a container?
asx — 12:27 PM
you can run it in yolo mode without worrying about it.
Patrick

 — 12:27 PM
haha YOLO mode... Do you need to configure that?
MarcusS — 12:28 PM
What is the Copilot curl command again?
Pamela FoxRole icon, Microsoft — 12:28 PM
https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli
GitHub Docs
Installing GitHub Copilot CLI - GitHub Docs
Learn how to install Copilot CLI so that you can use Copilot directly from the command line.
Image
Patrick

 — 12:29 PM
ohhhh that is actually a command!!?
🤣
I thought it was a joke LOL
Alden Weaver

 — 12:30 PM
Docker sandboxes
MarcusS — 12:30 PM
Thank you very much.  Great session.
bane — 12:30 PM
Thank you!
itsmeleece — 12:30 PM
See you tomorrow!!
asx — 12:31 PM
Thanks so much Pamela!
