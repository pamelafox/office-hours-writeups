# March 5th, 2026 Python + Agents Session 5 Office Hours Resources

## Recording

https://www.youtube.com/watch?v=FMi-SHU_55g
Unfortunately the recording only covered the first 10 minutes, so most Q&A will not be recoverable.
See if you can ascertain Q&A from the chat.


## Slide content:

No slides for the office hours itself, this session was a follow-up office hours after this livestream:
https://developer.microsoft.com/en-us/reactor/events/26693/


## Links from open tabs:

https://github.com/Azure-Samples/agent-openai-python-banking-assistant
https://github.com/Azure-Samples/agent-openai-python-banking-assistant/tree/main/app/backend/app/agents/foundry_v2
https://streamyard.com/teams/yfgXFbwTJEBTHs5jbsSYAiTk/videos
https://github.com/orgs/microsoft-foundry/discussions/331
https://github.com/Azure-Samples/python-agentframework-demos
https://fictional-space-robot-wgq4796rj29p5q.github.dev/
https://ca-web-c7qeb2joygass.wittysmoke-26b339d3.francecentral.azurecontainerapps.io/
https://github.com/langchain-ai/agent-inbox
https://docs.dbos.dev/python/examples/agent-inbox
http://127.0.0.1:8090/?entity_id=workflow_in_memory_workflowbuilder-5268ea84-ba29-4c51-b1eb-5716362c8ae4_e3af18e9b49d42b7bc4da83343c88592
https://github.com/settings/personal-access-tokens/new
https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff?pivots=programming-language-python
https://developer.microsoft.com/en-us/reactor/events/26693/
https://learn.microsoft.com/en-us/agent-framework/agents/skills?pivots=programming-language-python#security-best-practices
https://github.com/pamelafox/presentation-writeups/commit/42da36cb6dc5f68c1ee38b03b59131e741e44d21#diff-a54ff182c7e8acf56acfd6e4b9c3ff41e2c41a31c9b211b2deb9df75d9a478f9
https://openrouter.ai/models?order=top-weekly
https://code.visualstudio.com/blogs/2025/10/22/bring-your-own-key
https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
https://github.com/copilot/c/4771c7f7-5888-4e29-becd-ca35f108f031
https://pypi.org/project/opentelemetry-instrumentation-openai/
https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/app/backend/requirements.in
https://github.com/microsoft/agent-framework/blob/main/python/samples/02-agents/providers/azure_ai/azure_ai_basic.py
https://github.com/orgs/microsoft-foundry/discussions/331

## Discord chat paste

\Rxsnr — 11:35 AM
What are some real world use cases for the handoff with interaction pattern? There were some points regarding the human being potentially offline (was curious about potential real world scenarios surrounding this)
asx — 11:36 AM
When building agents, does it make sense to use an MCP or just use the underlying python methods? I am working on a project where I will build an MCP server and an agent.
Keva — 11:36 AM
The way to create a human in the loop workflow in a api is to use checkpoints right?
Tea-Leaf — 11:37 AM
Super series. It's hard to stay motivated to attend a multi-part series, but they way you structured it made it digestible and raised my knowledge level each day. Thank you!
srinivas — 11:39 AM
in a previous session you had mentioned that executors in a  sequential workflow sends both a message and an output to another executor. But how do we know or find this out? Can we figure this out somehow - in the devui or by some other means?
taylormc89 — 11:40 AM
Is she currently speaking?  I can't hear anything
dapakwat — 11:41 AM
restart discord
4m4rillo — 11:41 AM
Yes
itsmeleece — 11:41 AM
@taylormc89 I had to refresh to hear
Nnamdi — 11:41 AM
how do we protect our api keys and tokens from github agent?  Also what task was it doing when your github agent deleted an item?
taylormc89 — 11:42 AM
got it!  thanks flks
Pamela FoxRole icon, Buildathon-Mod — 11:45 AM
https://github.com/langchain-ai/agent-inbox
https://docs.dbos.dev/python/examples/agent-inbox
pablocotan — 11:45 AM
i understand that agent-skills are experimental in agent-framework, but I would like to know your opinion on their usage considering the examples you presented in the series. Here is compared with using workflows https://learn.microsoft.com/en-us/agent-framework/agents/skills?pivots=programming-language-python
Pamela FoxRole icon, Buildathon-Mod — 11:55 AM
"chat.tools.terminal.autoApprove": {
Tea-Leaf — 11:59 AM
While working through the series running in VSCode+DevContainer, I put my GITHUB_TOKEN (classic) in my .env file. What's a more secure way to store/provide it? 
pablocotan — 12:00 PM
please check the comparison with workflows  in the link I sent
GPSRole icon, Microsoft — 12:00 PM
@Tea-Leaf for local that is fine, in production you would want to use something like keyvault
Tea-Leaf — 12:01 PM
Understood. Would love to hear if I can do something more secure, even for local/dev.
GPSRole icon, Microsoft — 12:02 PM
@Tea-Leaf hmm what are you worried/want to avoid?
Tea-Leaf — 12:03 PM
Sharing the .env file or screensharing it in a presentation for example.
asx — 12:03 PM
update the date
GPSRole icon, Microsoft — 12:05 PM
so make sure it is not in your version control, our .gitignore takes care of that, for screen sharing what we do is avoid having the file open and use camoflogue extension in vs code.
pablocotan — 12:06 PM
i mean, the comparison
GPSRole icon, Microsoft — 12:07 PM
@Tea-Leaf if that is your worry I would make sure you use keyless auth and then not need to worry about api keys/tokens
there's also things like Infisical
https://github.com/Infisical/infisical
VK — 12:11 PM
I was able to run the agent_evaluation.py by temporarily updating the DEFAULT_MAX_COMPLETION_TOKENS_REASONING_MODELS = 20000 in the /workspace/.venv/lib/python3.12/site-packages/azure/ai/evaluation/_constants.py file
Tea-Leaf — 12:11 PM
😆
pablocotan — 12:13 PM
perhaps I am wrong, but ti seems to me that skills could be applicable for agents in the workflows, but not for replacing them (as in the article implied), because we want specialized agents that work well  in delimited tasks/knowledge/tools. Does this makes sense in agent-framework applications?
MarcusS — 12:13 PM
Can't one just have the .env file encrypted, then have the process that needs it decrypt it in memory?
asx — 12:18 PM
have you considered using openrouter with vscode + byok?
🤣
kimi 2.5 is really good for python dev
gcrumrine — 12:20 PM
My question is how are you defining the trust boundary between the agent and the MCP server? Are you treating the agent as a potentially compromised client and enforcing tool-level authorization on the MCP side, or assuming the agent itself is trusted? I feel like this all boils down to how do we ensure MCP tools are protected from attacks that cause the agent to call tools with unintended parameters. For example you have a malicious document that instructs the model to exfiltrate data through some tool call.
Pamela FoxRole icon, Buildathon-Mod — 12:21 PM
https://openrouter.ai/models?order=top-weekly
OpenRouter
Models | OpenRouter
Browse models on OpenRouter
Models | OpenRouter
Silvestre-PO — 12:21 PM
With VS Code Insiders is an easy integrated byok with GitHub copilot chat using OpenAI compatibility 
Pamela FoxRole icon, Buildathon-Mod — 12:21 PM
https://code.visualstudio.com/blogs/2025/10/22/bring-your-own-key
Expanding Model Choice in VS Code with Bring Your Own Key
Learn how the new Language Model Chat Provider API in VS Code is enabling more model choice and extensibility for chat experiences via the Bring Your Own Key experience.
Expanding Model Choice in VS Code with Bring Your Own Key
gcrumrine — 12:23 PM
But then is that exposed in some payload log that could be used unintentionally?
pablocotan — 12:24 PM
is there an example/article/video that you could share in which an agent framework application is interacting with other agents, both running in Foundry, and also accessing other tenant services. Not just the code, but also explaining the other required configurations in the tenant and in Foundry.
gcrumrine — 12:25 PM
Thanks!
yes
Thats what I was looking for really
PeterM — 12:27 PM
your presentation highlighted patterns of agents which I found very useful. Is there some effort to classify  agent patterns, similar to the Design Patterns for object oriented programming in the 90s by the GoF
gcrumrine — 12:30 PM
Thank you
RyanPrice1001 — 12:30 PM
Thanks Pamela! 🚀
Pamela FoxRole icon, Buildathon-Mod — 12:32 PM
https://github.com/microsoft/agent-framework/blob/main/python/samples/02-agents/providers/azure_ai/azure_ai_basic.py
GitHub
agent-framework/python/samples/02-agents/providers/azure_ai/azure_a...
A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. - microsoft/agent-framework
A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. - microsoft/agent-framework
gcrumrine — 12:34 PM
New term of the week! lol
itsmeleece — 12:35 PM
This has been great - thank you!!!
PeterM — 12:36 PM
Thanks Pamela
bane — 12:36 PM
Thank you for another wonderful series! 🥳 💙
gcrumrine — 12:36 PM
Thank you!
VK — 12:37 PM
Thanks Pamela, for making a very helpful series.
dapakwat — 12:37 PM
Thank you so much Pamela!!!
MarcusS — 12:37 PM
Thank you very much!!!
asx — 12:37 PM
Thank you!!
pablocotan — 12:37 PM
thank you
Arachnar — 12:37 PM
👍
el guansito — 12:37 PM
Thanks a lot Pam!