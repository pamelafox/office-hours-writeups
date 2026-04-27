# April 20, 2026 Python + AI Office Hours resources

## Recording

https://www.youtube.com/watch?v=l3vM3e7BK6U

## Copied text from slides

🏢 Microsoft / GitHub
• GitHub Copilot pricing plans: github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals•  VS Code 1.116: Copilot now built-in  code.visualstudio.com/updates/v1_116
• Claude Opus 4.7 GA in GitHub Copilot  code.visualstudio.com/updates/v1_116
• Copilot CLI: thinking effort config  code.visualstudio.com/updates/v1_116
• Agent Host Protocol: subagents & teams  code.visualstudio.com/updates/v1_116


👩‍💻 What I've Been Up To
• Foundry Hosted Agent Framework demo   github.com/pamelafox/foundry-hosted-agentframework-demo
• Foundry Agent Anthropic demo   github.com/pamelafox/python-foundryagent-anthropic-demo
• PyCon 2026 MCP tutorial progress   github.com/pamelafox/pycon2026-mcp-tutorial
• MCP for Postgres DB demo  github.com/pamelafox/mcp-for-postgres-db-demo
• RAG demo: active PRs & maintenance   github.com/Azure-Samples/azure-search-openai-demo

📅 Upcoming Events• Host your agents on Foundry (Online): Apr 27-30   https://aka.ms/AgentsOnFoundry/series
• Azure Cosmos DB Conf (Online): April 28 developer.azurecosmosdb.com/conf/• AgentCon (Silicon Valley): May 4   agentcon.city/silicon-valley
• PyCon US (Long Beach): May 13-19 us.pycon.org/2026
• Microsoft Build (SF): June 2-3 aka.ms/MS_Build_26_DAC26


## Open tabs

https://github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals/
https://github.com/pricing
https://github.com/Azure-Samples/azure-openai-entity-extraction/blob/main/extract_word_docx.py
https://www.bing.com/search?pglt=513&q=markitdown&cvid=db848a09dced42f79725011e3425ba2a&gs_lcrp=EgRlZGdlKgYIABBFGDsyBggAEEUYOzIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEAyCAgJEOkHGPxV0gEIMjA4N2owajeoAgCwAgA&FORM=ANNAB1&PC=U531&ntref=1
https://github.com/microsoft/markitdown/blob/main/packages/markitdown-ocr/README.md
https://portal.azure.com/#home
https://capps-backend-pkfkow3nk2uc6.proudsmoke-91e3c40a.westus3.azurecontainerapps.io/
https://capps-backend-pkfkow3nk2uc6.proudsmoke-91e3c40a.westus3.azurecontainerapps.io/
https://github.com/Azure-Samples/azure-search-openai-demo/tree/main/app/backend/prepdocslib
https://github.com/pamelafox/python-foundryagent-demos/blob/main/infra/main.bicep
https://learn.microsoft.com/en-us/azure/search/search-how-to-integrated-vectorization?tabs=prepare-data-storage%2Cprepare-model-aoai#prepare-your-embedding-model
https://github.com/Azure-Samples/azure-content-understanding-mcp-server
https://github.com/microsoft/Vancouver-Web-Summit-2026-GitHub-Copilot-SDK-Hackathon
https://www.bing.com/search?pglt=513&q=agents+league+winners+microsoft&cvid=acfb64b8fae54be0a735e20dd85d6169&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIICAQQ6QcY_FXSAQgzMDY4ajBqN6gCALACAA&FORM=ANNAB1&PC=U531
https://techcommunity.microsoft.com/blog/azuredevcommunityblog/agents-league-meet-the-winners/4507503
https://github.com/pamelafox/mcp-for-postgres-db-demo
https://pamelafox.github.io/mcp-for-postgres-db-demo/
https://github.com/pamelafox/pycon2026-mcp-tutorial
https://us.pycon.org/2026/schedule/sponsor-presentations/#May15
https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-ai-agent-builder-associate-certification/4494125
https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-azure-ai-apps-and-agents-developer-associate/4494126

# Pasted chat


Silvestre-PO — 11:11 AM
New sign-ups for GitHub Copilot Pro, Pro+, and Student plans are paused. 🙁
asx — 11:11 AM
Hey Pamela! Do you have a workflow for using agents for pulling data out of PDFs. Is markitdown a good library for this? Need to do NER on PDF docs. 
Pamela FoxRole icon, Microsoft — 11:13 AM
https://github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals/
The GitHub Blog
Allison
Changes to GitHub Copilot plans for individuals - GitHub Changelog
As shared in our recent blog post, we’re making the following changes to Copilot plans for individuals as part of our ongoing efforts to ensure service reliability and a sustainable…
Changes to GitHub Copilot plans for individuals - GitHub Changelog
Silvestre-PO — 11:14 AM
The same for qwen code plan lite 🤓
asx — 11:16 AM
I want to get the PDF to a point where I can pull out entities using an agent. I think converting it to markdown will make it easier.
Very cool!
M.Farias — 11:20 AM
Yeah my documents are crazy like this because we have a lot of blueprint as and electrical engineer...
sanz — 11:20 AM
Hi, have a question - using the text embedding small model, we keep getting - Error: Error code: 400 - {'error': {'message': 'Could not complete vectorization action. The vectorization endpoint returned status code '400' (BadRequest).\nStatus: 502 (Bad Gateway)\n\nContent:\n{"error":{"code":"","message":"Could not complete vectorization action. The vectorization endpoint returned status code '400' (BadRequest)."}}, if we adjust some setting in foundry, it work, but after few hours this comes back, have you seen anything like that ?
asx — 11:23 AM
I am trying to avoid PDFs as much as I can but sometimes I cannot. 🥲
M.Farias — 11:24 AM
I miss this AI assistant to write codes when Im using jupyter notebook 🥲 
Justin Trantham [FlowDevs.io] [FLOW],  — 11:24 AM
I print all my documents
M.Farias — 11:26 AM
both of them skiped all images that you have in your file... 
asx — 11:26 AM
Also, do you have a workflow for accessing PDFs in sharepoint? Do I have to use the GraphAPI? 
ShivammRole icon, MVP — 11:29 AM
Are tables , images and other info are preserved while OCR?
Can you share your repo as well for document intelligence if you have any?
JohnRole icon, MVP — 11:31 AM
Maybe it's under image_content not text_content
Maybe because it was repeated? Every letter is repeated twice
asx — 11:38 AM
This is really cool! Thank you so much! 🙏🏾
Document intelligence looks like works a lot better than just markitdown
Pamela FoxRole icon, Microsoft — 11:40 AM
https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/app/backend/prepdocslib/pdfparser.py
https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/app/backend/prepdocslib/mediadescriber.py
sanz — 11:41 AM
Have you tried Azure AI Foundry Atlassian MCP server with OAuth passthrough? authentication succeeds, tool calls fail , Is that an foundry issue? How can we debug this?
yes ai search
pablocotan — 11:42 AM
https://github.com/Azure-Samples/azure-content-understanding-mcp-server
sanz — 11:42 AM
so it works, but fail randomly
Pamela FoxRole icon, Microsoft — 11:44 AM
https://learn.microsoft.com/en-us/azure/search/search-how-to-integrated-vectorization?tabs=prepare-data-storage%2Cprepare-model-aoai#prepare-your-embedding-model
Integrated Vectorization Using REST APIs - Azure AI Search
Learn how to use the REST APIs to define an indexer pipeline that includes chunking and vectorization.
Integrated Vectorization Using REST APIs - Azure AI Search
sanz — 11:44 AM
if we adjust some param on the model ,, it starts working, but over few hours we get the same error
thanks
M.Farias — 11:46 AM
any comments for this Microsoft Hackathon ? Since im based in Vancouver, definetely I will submit my AI idea ...
https://github.com/microsoft/Vancouver-Web-Summit-2026-GitHub-Copilot-SDK-Hackathon
GitHub
GitHub - microsoft/Vancouver-Web-Summit-2026-GitHub-Copilot-SDK-Hac...
Contribute to microsoft/Vancouver-Web-Summit-2026-GitHub-Copilot-SDK-Hackathon development by creating an account on GitHub.
GitHub - microsoft/Vancouver-Web-Summit-2026-GitHub-Copilot-SDK-Hac...
asx — 11:47 AM
I am building an agent so GraphAPI will probably be the route to go.
sanz — 11:47 AM
playground, agent
yes
yes gpt-4o
also catalog is still /sse and not /mcp
does hosted work in private networking yet ?
Pamela FoxRole icon, Microsoft — 11:54 AM
https://techcommunity.microsoft.com/blog/azuredevcommunityblog/agents-league-meet-the-winners/4507503
TECHCOMMUNITY.MICROSOFT.COM
Agents League: Meet the Winners | Microsoft Community Hub
Agents League brought together developers from around the world to build AI agents using Microsoft's developer tools. With 100+ submissions across three...
Agents League: Meet the Winners | Microsoft Community Hub
https://github.com/pamelafox/mcp-for-postgres-db-demo
RyanPrice1001 — 11:55 AM
Thanks Pamela! 🚀
Pamela FoxRole icon, Microsoft — 11:55 AM
https://pamelafox.github.io/mcp-for-postgres-db-demo/
https://github.com/pamelafox/pycon2026-mcp-tutorial
asx — 11:56 AM
I will be at PyCon but I will miss your tutorial.
Silvestre-PO — 11:57 AM
https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-ai-agent-builder-associate-certification/4494125

New Microsoft Certified: AI Agent Builder Associate Certification
TECHCOMMUNITY.MICROSOFT.COM
New Microsoft Certified: AI Agent Builder Associate Certification |...
Building agents for real-world workflows takes more than prompts. Show you are ready to design and manage secure, enterprise‑ready agents in Microsoft...
New Microsoft Certified: AI Agent Builder Associate Certification |...
also New Microsoft Certified: Azure AI Apps and Agents Developer Associate
https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-azure-ai-apps-and-agents-developer-associate/4494126
TECHCOMMUNITY.MICROSOFT.COM
New Microsoft Certified: Azure AI Apps and Agents Developer Associa...
Ready to move from prototypes to production? Demonstrate your readiness to deliver scalable, real‑world AI apps and agents using Azure services and Microsoft...
New Microsoft Certified: Azure AI Apps and Agents Developer Associa...
goodbye AI-102
M.Farias — 11:59 AM
Microsoft E-learning is super boring
Silvestre-PO — 12:00 PM
https://aiskillsnavigator.microsoft.com/
This is new