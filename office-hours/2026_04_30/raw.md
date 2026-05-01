# April 30, 2026 "Host your agents on Foundry" Day 3 (Quality + Safety Evals)

## Recording:

https://www.youtube.com/watch?v=B3-otzOjgJI

## Slide content:

No slides for the office hours itself, this session was a follow-up office hours after this livestream:
https://developer.microsoft.com/en-us/reactor/events/26934/

## Browser tabs

https://github.com/Azure-Samples/foundry-hosted-agentframework-demos/tree/main/scripts
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryhosted-agentframework,,ai-account-nivdj7gkpbmk2,ai-project-pf-foundryhosted-agentframework/build/evaluations/eval_c80af04e7b674a619c4fc1adc26d082d/run/evalrun_17d649af781c4db588f6602b2ba4b59b
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryhosted-agentframework,,ai-account-nivdj7gkpbmk2,ai-project-pf-foundryhosted-agentframework/build/evaluations/eval_32eac7f083aa45c4867afcd056247dc5/run/evalrun_08584240528973144622417454618CU06
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryhosted-agentframework,,ai-account-nivdj7gkpbmk2,ai-project-pf-foundryhosted-agentframework/build/evaluations/eval_8bc8d9ee249c4c56b946aa0c5953876b/run/evalrun_08584240493545287729515263520CU13
http://0.0.0.0:8089/?tab=charts
https://portal.azure.com/#@caglobaldemos2605.onmicrosoft.com/resource/subscriptions/8077d4f9-d1b7-4c80-b6c2-cf9a2ec2d604/resourceGroups/rg-pf-foundryhosted-agentframework/providers/Microsoft.Insights/components/appi-nivdj7gkpbmk2/agents
https://portal.azure.com/#@caglobaldemos2605.onmicrosoft.com/resource/subscriptions/8077d4f9-d1b7-4c80-b6c2-cf9a2ec2d604/resourceGroups/rg-pf-foundryhosted-agentframework/providers/Microsoft.Insights/components/appi-nivdj7gkpbmk2/alertsV2
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryhosted-agentframework,,ai-account-nivdj7gkpbmk2,ai-project-pf-foundryhosted-agentframework/build/guardrails/list
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryhosted-agentframework,,ai-account-nivdj7gkpbmk2,ai-project-pf-foundryhosted-agentframework/build/models/deployments/gpt-5.2/playground
https://ai.azure.com/nextgen/r/gHfU-dG3TIC2ws-aLsLWBA,rg-pf-foundryhosted-agentframework,,ai-account-nivdj7gkpbmk2,ai-project-pf-foundryhosted-agentframework/build/agents/hosted-agentframework-agent/build
https://outlook.cloud.microsoft/mail/inbox/id/AAQkAGNiMDE5MmZmLTExMzUtNGRhMC1hYTliLTk5YWVhNGYyMjM0ZAAQAFaq6MxFU5RMkr47WcHCkq0%3D
https://github.com/orgs/microsoft-foundry/discussions/380#discussioncomment-16770568
https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluation-github-action
https://hamel.dev/notes/llm/evals/memes/index.html#background
https://www.microsoft.com/en-us/research/project/hax-toolkit/?msockid=2e216b54b5bf6ebb115c7dfcb4716f4e
https://www.microsoft.com/en-us/haxtoolkit/library/example,guideline/
https://www.microsoft.com/en-us/haxtoolkit/uploads/2025/01/Visual-uncertainty-expressions-low-generation-probabilities-768x464.png
https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-retrieve?pivots=python#call-the-mcp-endpoint
https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/.github/workflows/evaluate.yaml
https://build.microsoft.com/en-US/sessions?search=nitya&sortBy=relevance
https://github.com/Azure-Samples/ai-quality-safety-demos/blob/main/samples/chat_error_contentfilter.py
https://github.com/microsoft/azure-skills/tree/main/skills/microsoft-foundry/foundry-agent
https://github.com/hamelsmu/evals-skills/blob/main/skills/eval-audit/SKILL.md#2-evaluator-design
https://arxiv.org/pdf/2604.08224

## Discord chat

GPSRole icon, Microsoft — 11:04 AM
a couple of people were asking if there are any evals you know of that will score on cost/token efficiency 
lpk — 11:05 AM
Are there any built-in evaluators which don't depend on LLM-as-a-judge approach?
pablocotan — 11:06 AM
For each quality evaluator, the context of the agent is more than the query (short and long term memory). How could we take it into account for the quality evaluations using Foundy Evaluations?
Pamela FoxRole icon, Microsoft — 11:08 AM
https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/custom-evaluators#code-based-evaluators
Custom Evaluators - Microsoft Foundry
Learn how to create custom evaluators for your AI applications using code-based or prompt-based approaches.
Custom Evaluators - Microsoft Foundry
https://hamel.dev/notes/llm/evals/memes/index.html#background
Hamel's Blog - Hamel Husain
Evals Memes – Hamel’s Blog - Hamel Husain
Notes on applied AI engineering, machine learning, and data science.
Evals Memes – Hamel’s Blog - Hamel Husain
Kalyan a.k — 11:12 AM
in a Multi agent environment should we have evals for each agent vs final response?
pablocotan — 11:15 AM
I read that an option could be to use an SLM to pre-process traces and feed each of them into a knowledge graph using the concepts of the built-in evaluators to extract entities and relationships. It was stated that this would help to reduce LLM costs instead of evaluating traces using an LLM from text.
lpk — 11:16 AM
Could you expand a bit on any approaches we could take for streaming & online eval together (async?)?
Kalyan a.k — 11:17 AM
what is recommended practice after the app is live. Should we schedule evals frequently?
Garvey — 11:19 AM
Does the cluster evaluation operate similarly to theme analysis for conversational agents?
Kalyan a.k — 11:20 AM
​​are there any benchmarks(cutoff score) we can refer to say an app is prod ready?
pablocotan — 11:22 AM
Could we also directly feed images and audios to the agent in Foundry safety evaluation?
Pamela FoxRole icon, Microsoft — 11:22 AM
https://www.microsoft.com/en-us/haxtoolkit/library/example,guideline/
Microsoft HAX Toolkit
Jung Huh
HAX Design Library - Microsoft HAX Toolkit
HAX Design Library Interactive collection of the 18 Guidelines for Human-AI Interaction, with design patterns for applying them and examples.
Yadel — 11:25 AM
my take with writing custom eval is I almost never get the Analyze results to show results, my eval may read 100% and yet Analyze result shows 0. It's very confusing 
pablocotan — 11:26 AM
Would the interaction between agents (or agent to sub-agent) need to be different evaluated?
Kalyan a.k — 11:27 AM
agreed 🙂
if an answer is highly relevant but has a low groundedness score, how should a developer adjust their retrieval strategy .ex: User asks a question and the llm responds with an answer (relavent to the question (may be used web search tool)) but the information may not be in the actual document
Yadel — 11:31 AM
exactly
see here
Image
Image
pablocotan — 11:35 AM
You mentioned not long ago that Azure AI search retrieval is better that Work IQ. I guess that will also depend on the data in Work IQ, and for this reason it hink that it might make sense to evaluate Work IQ retrieval. How could we do that and even detect how to improve it?
lpk — 11:36 AM
Can you please share the evaluators microsoft doc page we've been discussing about?
Kalyan a.k — 11:39 AM
can we briefly discuss evals with CI/CD integration?
Garvey — 11:40 AM
You need to search either way. Could you use foundry iq?
Ai search*
lpk — 11:40 AM
Azure AI Search with Sharepoint IQ is Foundry IQ right?
Pamela FoxRole icon, Microsoft — 11:41 AM
https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/custom-evaluators
Custom Evaluators - Microsoft Foundry
Learn how to create custom evaluators for your AI applications using code-based or prompt-based approaches.
Custom Evaluators - Microsoft Foundry
Garvey — 11:41 AM
Yes, foundry iq
Pamela FoxRole icon, Microsoft — 11:42 AM
https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-retrieve
Query Knowledge Base via APIs or MCP - Azure AI Search
Learn how to Query a knowledge base using the retrieve action or MCP endpoint in Azure AI Search using REST APIs, Azure SDKs, or any MCP-compatible client.
Query Knowledge Base via APIs or MCP - Azure AI Search
pablocotan — 11:43 AM
i had to use copilot to find the name "Work IQ" to be able to make my last question... There is not reason to learn it if it could change soon again 😆
RyanPrice1001 — 11:46 AM
Worksbetter_x.yz would be nice.
lpk — 11:46 AM
Many of the great foundry features are in preview - any roadmap for GA?

Was delighted when traces & observability went GA! 
Pamela FoxRole icon, Microsoft — 11:46 AM
https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluation-github-action
How to run an evaluation in GitHub Action - Microsoft Foundry
How to run evaluation in GitHub Action to streamline the evaluation process, allowing you to assess model performance and make informed decisions before deploying to production.
How to run an evaluation in GitHub Action - Microsoft Foundry
https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/.github/workflows/evaluate.yaml
GitHub
azure-search-openai-demo/.github/workflows/evaluate.yaml at main ·...
A sample app for the Retrieval-Augmented Generation pattern running in Azure, using Azure AI Search for retrieval and Azure OpenAI large language models to power ChatGPT-style and Q&amp;A expe...
azure-search-openai-demo/.github/workflows/evaluate.yaml at main ·...
Garvey — 11:49 AM
For Foundry IQ you get results based on how you configure the knowledge base and knowledge source indexes. Depends on the strength of the chat completion model, the output chosen, and the reasoning effort for sorting or compiling the info indexed in the knowledge sources.
pablocotan — 11:50 AM
It would be good it Microsoft could offer a pay-per-execution service to evaluate retrieval quality from Work IQ for an specific user/team/section. And if the evaluation could also make an analysis to recommend changes to the data inside it, or rules that could be changed in it to affect retrieval performance. Last year was enough to get data, this year we go more into expecting a more professional approach to create and evaluate agents.
Kalyan a.k — 11:51 AM
Any hackathons planned in the near future?
Pamela FoxRole icon, Microsoft — 11:52 AM
https://build.microsoft.com/en-US/sessions/LAB532?source=sessions
From data to context: Agent‑ready knowledge with Foundry IQ
What if your coding agent could reason over enterprise knowledge—across files, data, and work signals—without leaving your developer workflow? In this hands-on lab, you’ll build a reusable knowledge base in Foundry IQ using the Microsoft Foundry portal, expose it as an MCP server, and connect it to GitHub Copilot CLI—no custom RAG plumbi...
Image
Yadel — 11:53 AM
Just in case anyone runs into this situation the solution is below.
when using general models if the content generated is flagged as unsafe, you may not get a response or incomplete response or even a message saying the question cannot be answer for safety reasons.
The way around it is creating your a custom guardrail.
To land an example, I was recently generating content for a Law school about homicide and content got flagged 
Kalyan a.k — 11:54 AM
I got offline AI award in js buildathon
wanted to explore more on Foundry
lpk — 11:56 AM
So So grateful for this series - Learned a ton through the live & the office hours too!!

Thank you so much for answering our questions!! 🙌
Kalyan a.k — 11:56 AM
thank you Pamela!!. we can use LLM as a judge 
RyanPrice1001 — 11:56 AM
Series are way more helpful than document surfing -- even with an agent/LLM
Thanks Pamela!
Kalyan a.k — 11:58 AM
Thank you very much Pamela, very productive and useful sessions!!
pablocotan — 11:58 AM
Any possibility of having any time soon an agent in Foundry or a CLI, or a repository with skill/agents for copilot/copilot-cli, that could analys our agent, its knowledge, and could interact with the user to asses what the evaluations could be, and automatically "create" evaluations in Foundry Evaluations?
(kind of suggestion for the Foundry evaluation team)
Pamela FoxRole icon, Microsoft — 11:59 AM
https://github.com/microsoft/azure-skills/blob/main/skills/microsoft-foundry/foundry-agent/observe/observe.md
GitHub
azure-skills/skills/microsoft-foundry/foundry-agent/observe/observe...
Official agent plugin providing skills and MCP server configurations for Azure scenarios. - microsoft/azure-skills
azure-skills/skills/microsoft-foundry/foundry-agent/observe/observe...
https://build.microsoft.com/en-US/sessions/LAB540?source=sessions
Observe, optimize and protect your hosted agents in Microsoft Foundry
Modern agents fail in ways traditional monitoring can’t catch. In this hands-on lab, learn how Microsoft Foundry Observability helps you move from prototype → production with context-specific evaluation suites (auto-generated evaluators + test datasets) wired into developer workflows via skills/MCP tooling for hosted agents. Then scale quali...
Image
https://github.com/hamelsmu/evals-skills
GitHub
GitHub - hamelsmu/evals-skills: Skills for AI Evals to compliment t...
Skills for AI Evals to compliment the course: AI Evals For Engineers & PMs - hamelsmu/evals-skills
Skills for AI Evals to compliment the course: AI Evals For Engineers & PMs - hamelsmu/evals-skills
Silvestre-PO — 12:01 PM
This is paper is interesting... talking about  Protocols and Harness Engineering
https://arxiv.org/pdf/2604.08224
Garvey — 12:03 PM
Thank you!
lpk — 12:03 PM
Thank you so much!!
itsmeleece — 12:03 PM
Thanks!
Silvestre-PO — 12:03 PM
Thanks Pam!
pablocotan — 12:03 PM
thank you!!!!
Kalyan a.k — 12:04 PM
Thank you once again!