# April 20, 2026 Office Hours Q&A

## What's a good workflow for pulling entities out of PDFs? Is MarkItDown a good library?

📹 [4:02](https://youtube.com/watch?v=l3vM3e7BK6U&t=242)

Pamela demonstrated several approaches for extracting data from PDFs, starting with MarkItDown — a Microsoft open-source library that converts documents (DOCX, PDF, etc.) to Markdown. She showed an entity extraction example where a Word document was converted to Markdown and then sent to an LLM to extract fields like title, author, and headings.

She then compared MarkItDown vs. PyMuPDF (specifically `pymupdf4llm`) on a complex PDF with mixed layouts and images. PyMuPDF appeared to produce slightly better results with less repetitive text, though results will vary depending on document complexity.

For documents with images, Pamela demonstrated MarkItDown's OCR plugin, which uses an LLM to describe images found in documents.

The best results came from Azure Document Intelligence, which she demonstrated through her [RAG application](https://github.com/Azure-Samples/azure-search-openai-demo). Document Intelligence extracted far more figures and structural information from the PDF. Combined with an LLM for image descriptions (using a prompt like "describe the image with no more than five sentences"), this approach produced the richest output — including both text content and detailed figure descriptions that go beyond simple OCR text extraction.

She also mentioned Azure Content Understanding as a newer alternative hosted service worth exploring, and noted that Pablo shared an [Azure Content Understanding MCP server](https://github.com/Azure-Samples/azure-content-understanding-mcp-server) (built in .NET) for quick experimentation.

Links shared:

* [MarkItDown OCR plugin](https://github.com/microsoft/markitdown/blob/main/packages/markitdown-ocr/README.md)
* [azure-openai-entity-extraction sample](https://github.com/Azure-Samples/azure-openai-entity-extraction/blob/main/extract_word_docx.py)
* [RAG demo PDF parser (Document Intelligence)](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/app/backend/prepdocslib/pdfparser.py)
* [RAG demo media describer](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/app/backend/prepdocslib/mediadescriber.py)
* [Azure Content Understanding MCP server](https://github.com/Azure-Samples/azure-content-understanding-mcp-server)

### How do you access PDFs stored in SharePoint?

📹 [35:39](https://youtube.com/watch?v=l3vM3e7BK6U&t=2139)

If you just want to ask questions about a document, you could use Work IQ (which can query SharePoint content). But if you need the full document — for example, to run your own extraction pipeline — you'll need to use the Microsoft Graph API. In the future, Work IQ may add more Graph API functionality, but currently it's limited for full document retrieval.

## Bug report: Sporadic 400 errors from the Azure AI Search vectorization endpoint

📹 [30:43](https://youtube.com/watch?v=l3vM3e7BK6U&t=1843)

A community member reported intermittent 400 (Bad Request) errors when using text-embedding-small with Azure AI Search's integrated vectorization. Pamela first suggested checking RBAC permissions — specifically, the search service's managed identity needs the **Cognitive Services OpenAI User** role assigned to it. She showed this setup in her Bicep templates.

However, since the error was intermittent (working sometimes, failing other times), Pamela suspected it might be a rate limit error that isn't surfacing clearly. She messaged the Azure AI Search PM directly and asked the community member to share their search service ID, subscription, and timestamp of the error so the team could check the logs.

Links shared:

* [Integrated Vectorization - Prepare your embedding model](https://learn.microsoft.com/en-us/azure/search/search-how-to-integrated-vectorization?tabs=prepare-data-storage%2Cprepare-model-aoai#prepare-your-embedding-model)
* [Foundry agent demos Bicep template (RBAC example)](https://github.com/pamelafox/python-foundryagent-demos/blob/main/infra/main.bicep)

## Bug report: Authentication succeeds but tool calls fail with the Foundry Atlassian MCP server

📹 [36:35](https://youtube.com/watch?v=l3vM3e7BK6U&t=2195)

A community member reported that OAuth authentication succeeds for the Atlassian MCP server added from the Foundry catalog to a prompt agent, but tool calls fail. Pamela acknowledged there are known issues with remote MCP servers on Foundry, showing a similar internal server error she encountered.

For debugging, she recommended:

- Capturing the **request ID** from the error response and sharing it so the Foundry team can check logs.
- Considering **Foundry hosted agents** instead of prompt agents, which are easier to debug because the agentic loop runs in a Docker container where you can view container logs.

The new version of Foundry hosted agents is expected to ship this week or the following week.

## Any tips for the Vancouver Web Summit hackathon?

📹 [42:25](https://youtube.com/watch?v=l3vM3e7BK6U&t=2545)

A community member based in Vancouver mentioned they planned to submit to the Microsoft Vancouver Web Summit GitHub Copilot SDK Hackathon. Pamela suggested looking at the recently announced Agents League hackathon winners for inspiration on what judges look for.

Links shared:

* [Vancouver Web Summit 2026 GitHub Copilot SDK Hackathon](https://github.com/microsoft/Vancouver-Web-Summit-2026-GitHub-Copilot-SDK-Hackathon)
* [Agents League: Meet the Winners](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/agents-league-meet-the-winners/4507503)

## Announcements

📹 [0:42](https://youtube.com/watch?v=l3vM3e7BK6U&t=42)

**GitHub Copilot pricing changes:** New signups for GitHub Copilot Pro, Pro+, and Student plans are paused due to high demand. Free tier (with rate limits) is still available, and Business/Enterprise plans are unaffected. Additionally, Opus models have been removed from Pro — only Pro+ gets Opus 4.7.

* [Changes to GitHub Copilot plans for individuals](https://github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals/)

**VS Code 1.116 updates:** Copilot is now built-in to VS Code, Claude Opus 4.7 is GA in Copilot, thinking effort is configurable in Copilot CLI, and the Agent Host Protocol now supports subagents and teams.

* [VS Code 1.116 Release Notes](https://code.visualstudio.com/updates/v1_116)

**Foundry hosted agents livestream series:** Starting April 27-30, covering Agent Framework agents on Foundry, LangChain/LangGraph agents on Foundry, and evaluation/safety.

* [Host your agents on Foundry series](https://aka.ms/AgentsOnFoundry/series)

**New Microsoft certifications:** Two new AI certifications were shared — AI Agent Builder Associate (Copilot Studio focused) and Azure AI Apps and Agents Developer Associate (Python/Azure AI focused, with an 80% discount for the first 300 people before May 7th).

* [AI Agent Builder Associate Certification](https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-ai-agent-builder-associate-certification/4494125)
* [Azure AI Apps and Agents Developer Associate](https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-azure-ai-apps-and-agents-developer-associate/4494126)
* [AI Skills Navigator](https://aiskillsnavigator.microsoft.com/)

**PyCon US 2026:** Pamela will be giving an MCP tutorial on Wednesday, a tutorial at the Edu Summit on Thursday, and a sponsored session on Thursday or Friday. Microsoft booth will be open Thursday evening through Saturday.

* [PyCon 2026 MCP tutorial repo](https://github.com/pamelafox/pycon2026-mcp-tutorial)

**Upcoming events:**

* Azure Cosmos DB Conf (Online): April 28
* AgentCon (Silicon Valley): May 4
* PyCon US (Long Beach): May 13-19
* Microsoft Build (SF): June 2-3
