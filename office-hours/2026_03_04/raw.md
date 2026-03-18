# March 4th, 2026 Python + Agents Session 5 Office Hours Resources

## Recording:

https://www.youtube.com/watch?v=txskCy6Vmzc

## Slide content:

No slides for the office hours itself, this session was a follow-up office hours after this livestream:
https://developer.microsoft.com/en-us/reactor/events/26692/

## Links from open tabs:

https://github.com/Azure-Samples/Agentic-AI-Investment-Analysis-Sample/blob/main/api-app/app/what_if_chat/what_if_workflow.py
https://github.com/Azure-Samples/Agentic-AI-Investment-Analysis-Sample
https://github.com/orgs/microsoft-foundry/discussions/324
https://learn.microsoft.com/en-us/agent-framework/workflows/
https://github.com/Azure-Samples/python-agentframework-demos/actions
https://github.com/orgs/microsoft-foundry/discussions/165
https://github.com/Azure-Samples/Agentic-AI-Investment-Analysis-Sample
https://github.com/orgs/microsoft-foundry/discussions/331
https://github.com/Azure-Samples/python-agentframework-demos/blob/main/presentations/english/session-3/README.md
https://github.com/microsoft/agent-framework/tree/main/python/packages/lab
https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/magentic?pivots=programming-language-python
https://github.com/microsoft/agent-framework/tree/main/python/packages
https://github.com/AgentEvalHQ/AgentEval
https://hamel.dev/
https://hamel.dev/blog/posts/evals-faq/
https://aaif.io/
https://docs.langchain.com/oss/python/deepagents/overview
https://github.com/Azure-Samples/azure-search-openai-demo/tree/main/.github/workflows
https://gist.github.com/pamelafox/e2c01f0a331b14a309a59063db59855e
https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-azure-open-ai-models-bring-fast-expressive-and-real%E2%80%91time-ai-experiences-in-m/4496184
https://github.com/elbruno/ElBruno.Realtime
https://github.com/Azure-Samples/eShopLite/tree/main/scenarios/03-RealtimeAudio

## Discord chat paste

Pamela Fox
 is now a speaker. — 11:33 AM
Akash — 11:35 AM
How to increase performance of Multi agent system ?
Time
Latecy
Gpt 4 nano
Zai-Daddy

 — 11:37 AM
How to incorporate a2a protocols into model to model orchestrations to integrate other agents/providers into the foundry orchestration
dapakwat — 11:37 AM
can you reshare the repo for the finance orchestration example we looked at the end of the session?
pablocotan — 11:37 AM
Limitations in workflows evaluation using Microsoft Foundry if we deploy our agent as hosted agent?
Manuel — 11:38 AM
audio is not working
Bernhard Merkle — 11:38 AM
any recommendation for evaluation framework ? (deepeval, ragas, others ?)
GPSRole icon, Microsoft — 11:39 AM
I had a question come in:

He has tools inside an agent that extract data. He built a middleware layer that intercepts the tool results and saves them to the workflow's shared_state so no LLM can alter the exact values. Then another middleware substitutes those exact values back into the final output using a template/placeholder pattern.

The problem is that middlewares don't have native access to the WorkflowContext or shared_state in the framework. He's manually injecting the reference from the executor. He asked if there's a more native way. 
Pamela FoxRole icon, Buildathon-Mod — 11:39 AM
https://learn.microsoft.com/en-us/agent-framework/integrations/a2a
A2A Integration
Learn how to expose Microsoft Agent Framework agents using the Agent-to-Agent (A2A) protocol for inter-agent communication.
A2A Integration
Tea-Leaf — 11:39 AM
Refresh your web page. Audio is on.
Zai-Daddy

 — 11:39 AM
Ok yeah awsome thank you
Satya Sai Nandigam#1709

 — 11:39 AM
I’m not aware of systemic evaluation and versioning systems, any suggestions on what to use for proper evaluation
Pamela FoxRole icon, Buildathon-Mod — 11:40 AM
https://github.com/Azure-Samples/Agentic-AI-Investment-Analysis-Sample
GitHub
GitHub - Azure-Samples/Agentic-AI-Investment-Analysis-Sample: Sampl...
Sample App using Agent Framework for analysis of investment opportunities. - Azure-Samples/Agentic-AI-Investment-Analysis-Sample
Sample App using Agent Framework for analysis of investment opportunities. - Azure-Samples/Agentic-AI-Investment-Analysis-Sample
https://github.com/orgs/microsoft-foundry/discussions/331
GitHub
Python + Agents livestream series: Resources · microsoft-foundry ...
Join us for our 6-part live stream series on using Python with the Microsoft Agent Framework to build AI agents and agentic workflows! Register for the series Livestreams Tune in for the live strea...
Python + Agents livestream series: Resources · microsoft-foundry ...
srinivas — 11:43 AM
how does tracing logging etc work with workflows?
or do we use same tools as with agents?
Pamela FoxRole icon, Buildathon-Mod — 11:44 AM
https://github.com/microsoft/agent-framework/tree/main/python/packages/lab
pablocotan — 11:46 AM
This is not Python, but was presented today in the MAF/SK weekly meeting, made by a MS MVP with the support from the MAF team. It would be great to have a similar solution integrated in Python.  https://github.com/AgentEvalHQ/AgentEval
GitHub
GitHub - AgentEvalHQ/AgentEval: AgentEval — .NET AI Agent Testing...
AgentEval — .NET AI Agent Testing &amp;amp; Evaluation Framework / Make agent testing feel like normal .NET testing. Fluent assertions for tool calls, streaming performance metrics (TTFT/latency), ...
AgentEval — .NET AI Agent Testing &amp; Evaluation Framework / Make agent testing feel like normal .NET testing. Fluent assertions for tool calls, streaming performance metrics (TTFT/latency), cost...
Pamela FoxRole icon, Buildathon-Mod — 11:46 AM
https://github.com/microsoft/agent-framework/discussions
Bernhard Merkle — 11:47 AM
will the Microsoft Agentframework (MAF) be submitted to the aaif.io so that we have a common API and common patterns for agentframeworks (e.g. MCP has been submitted to the aaif.io)
GPSRole icon, Microsoft — 11:48 AM
pins go to us again.
Tea-Leaf — 11:48 AM
Thanks for the follow-up. Appreciate it, Pam.
Pamela FoxRole icon, Buildathon-Mod — 11:52 AM
https://hamel.dev/
Hamel's Blog - Hamel Husain
Hamel Husain’s Blog – Hamel’s Blog - Hamel Husain
Notes on applied AI engineering, machine learning, and data science.
Hamel Husain’s Blog – Hamel’s Blog - Hamel Husain
https://hamel.dev/blog/posts/evals-faq/
Hamel's Blog - Hamel Husain
LLM Evals: Everything You Need to Know – Hamel’s Blog - Hamel H...
A comprehensive guide to LLM evals, drawn from questions asked in our popular course on AI Evals. Covers everything from basic to advanced topics.
LLM Evals: Everything You Need to Know – Hamel’s Blog - Hamel H...
GPSRole icon, Microsoft — 11:53 AM
hahaha
Bernhard Merkle — 11:53 AM
just want to avoid that we have e.g. 3 different terms for the same pattern etc...
Arachnar — 11:57 AM
Well MS doesn't need their own frontier models since they own ~30% of the OpenAI for profit entity
Craig — 11:58 AM
There are the PHI models
TeakDragon — 11:58 AM
Starting to sound like Event versioning
Bernhard Merkle — 11:59 AM
and for versioning you have also weights during training etc so there you need LMOps
Pamela FoxRole icon, Buildathon-Mod — 12:00 PM
https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/.github/workflows/evaluate.yaml
Bernhard Merkle — 12:02 PM
to debug a workflow we can also set breakpoints in VScode and get called back ?
GPSRole icon, Microsoft — 12:06 PM
great question
TeakDragon — 12:06 PM
Not sure how to phrase this but we have all the patterns but do we have the problems they solve architecturally
GPSRole icon, Microsoft — 12:07 PM
maual vibecoding
TeakDragon — 12:08 PM
yes
pablocotan — 12:11 PM
do you know of an example in which it is used the OpenAI Realtime API with MS Agent Framework
I am looking in a similar approach with Google Live API and the ADK
Pamela FoxRole icon, Buildathon-Mod — 12:13 PM
https://github.com/elbruno/ElBruno.Realtime Bruno Capuano
GitHub
GitHub - elbruno/ElBruno.Realtime: Pluggable real-time audio conver...
Pluggable real-time audio conversation framework for .NET. Local VAD, STT, TTS, and LLM - elbruno/ElBruno.Realtime
Pluggable real-time audio conversation framework for .NET. Local VAD, STT, TTS, and LLM - elbruno/ElBruno.Realtime
https://github.com/Azure-Samples/eShopLite/tree/main/scenarios/03-RealtimeAudio
GitHub
eShopLite/scenarios/03-RealtimeAudio at main · Azure-Samples/eShop...
eShopLite is a set of reference .NET applications implementing an eCommerce site with features like Semantic Search, MCP, Reasoning models and more. - Azure-Samples/eShopLite
Nnamdi — 12:15 PM
can we get the fullstack code for the ai finane agent ou showed in the course?
Pamela FoxRole icon, Buildathon-Mod — 12:15 PM
https://github.com/Azure-Samples/Agentic-AI-Investment-Analysis-Sample
GitHub
GitHub - Azure-Samples/Agentic-AI-Investment-Analysis-Sample: Sampl...
Sample App using Agent Framework for analysis of investment opportunities. - Azure-Samples/Agentic-AI-Investment-Analysis-Sample
Sample App using Agent Framework for analysis of investment opportunities. - Azure-Samples/Agentic-AI-Investment-Analysis-Sample
Nnamdi — 12:15 PM
is that also front-emd?
Bernhard Merkle — 12:16 PM
moving target....
RyanPrice1001 — 12:16 PM
Thanks Pamela!
Pamela FoxRole icon, Buildathon-Mod — 12:17 PM
1.0.0b260212