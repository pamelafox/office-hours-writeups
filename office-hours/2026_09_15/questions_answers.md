# September 15, 2026 Office Hours Q&A

## Announcement: MCP Live recordings and learning resources

📹 [00:50](https://youtube.com/watch?v=gC5q1lQz4wg&t=50)

The recordings, slides, and related references from MCP Live are collected in a [session recap](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/explore-the-latest-in-mcp-all-recordings-from-mcp-live/4556775). The talks go deep into MCP and are best suited to developers who already know the basics. Newcomers can start with the [Python + MCP series](https://aka.ms/pythonmcp/rewatch) or the cross-language [MCP for Beginners curriculum](https://github.com/microsoft/mcp-for-beginners).

## Can office hours be held at a time that works better for India?

📹 [03:22](https://youtube.com/watch?v=gC5q1lQz4wg&t=202)

No single time works across all global time zones, and Pacific Time has little overlap with Indian Standard Time. Every session is recorded and published with a transcript through the [office-hours resources](https://aka.ms/pythonai/oh/links). Other hosts also run Discord office hours at different times, which may offer a better fit.

## Demo: Using the Azure DevOps MCP server to review proposals

📹 [09:41](https://youtube.com/watch?v=gC5q1lQz4wg&t=581)

The Azure DevOps MCP server was installed directly from GitHub Copilot's customization interface. Pamela used it to cluster roughly 30 conference proposals by topic, making it easier to review related submissions together.

## What resources and practices help with learning the GitHub Copilot app?

📹 [12:35](https://youtube.com/watch?v=gC5q1lQz4wg&t=755)

Start with the [GitHub Copilot App for Beginners playlist](https://www.youtube.com/playlist?list=PLNBWjViYXaIY), which progresses from introductory workflows to automations, parallel agents, canvases, and continuing sessions in VS Code. Follow product changes through the [Copilot app changelog](https://github.com/github/app/blob/main/changelog.md) and the broader [GitHub changelog](https://github.blog/changelog/).

For hands-on learning, experiment with automations, delegate work to subagents, run agents in parallel, and customize the app around recurring tasks. Canvases can add an interactive interface to those workflows.

## How should an application migrate from temperature controls to reasoning models?

📹 [16:26](https://youtube.com/watch?v=gC5q1lQz4wg&t=986)

Reasoning effort and temperature are not equivalent. Temperature changes token-sampling probabilities, while reasoning effort changes how much reasoning the model performs. Some OpenAI models discussed in the session permit temperature only when reasoning effort is set to `none`, while newer models may require removing the parameter entirely. Anthropic exposes different thinking controls, including adaptive thinking and token budgets. Model-specific documentation therefore has to be checked during each migration.

When a model does not expose temperature or log probabilities, shape the behavior through prompt engineering. Build evaluations that measure the desired output, compare reasoning-effort levels, and optimize the prompt against that score. Tools such as [DSPy](https://dspy.ai/) or [GEPA's optimize-anything](https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/) can help when the behavior can be measured. For hallucination reduction specifically, do not assume that reasoning effort is a direct replacement for temperature; evaluate the new model's default behavior on the application's actual cases.

## What AI skills should a .NET developer build for career growth?

📹 [25:11](https://youtube.com/watch?v=gC5q1lQz4wg&t=1511)

Learn the foundations of AI engineering: using language models, embedding models, and other generative AI models to build complete applications. The [Python + AI series](https://aka.ms/pythonai/rewatch) covers those fundamentals even though it uses Python. Reinforce the concepts by building end-to-end AI projects and by observing how coding agents approach real implementation tasks.

## Demo: Building interactive GitHub Copilot canvases

📹 [26:15](https://youtube.com/watch?v=gC5q1lQz4wg&t=1575)

A canvas can be a quick single-page prototype or a richer interface that exchanges information with the Copilot agent. The first example was a browser audio recorder made in a few minutes. The second was a dashboard for reviewing job listings: an automation ranked listings and stored them in SQLite, while changing a status in the canvas sent a message to Copilot so it could update the database.

Canvases are specific to the GitHub Copilot app rather than a portable standard. For an MCP server, an MCP App provides a related pattern: user interactions in the app can return context to the server and agent. More canvas examples are available through [Awesome GitHub Copilot extensions](https://awesome-copilot.github.com/extensions/).

### Can a canvas design an agent architecture and deploy it to Microsoft Foundry?

📹 [31:33](https://youtube.com/watch?v=gC5q1lQz4wg&t=1893)

The Microsoft Foundry Copilot plugin includes a canvas that collects configuration for a Foundry hosted agent, including the project, model, tools, skills, and guardrails. Once configured, it sends the choices to the agent, which scaffolds the project and its deployment files such as Bicep and `azure.yaml`.

The demonstrated canvas is primarily a hosted-agent creation and deployment flow. It did not appear to design a multi-agent architecture, so it should not be treated as a general visual architecture tool.

## What can extract PDF content into structured data or JSON?

📹 [39:52](https://youtube.com/watch?v=gC5q1lQz4wg&t=2392)

For a managed service, Azure Content Understanding combines OCR from Azure Document Intelligence with language-model processing. It can handle handwriting and complex layouts, represent expressive tables as HTML, describe charts, emit Chart.js-style JSON that can recreate a chart, extract metadata, and produce semantically meaningful chunks.

For local or open-source processing, select tools based on document difficulty, output requirements, licensing, and cost. Isaac Flath's article on [VLM OCR for hard documents](https://isaacflath.com/writing/vlm-ocr-for-hard-documents) provides additional guidance.

### How is Azure Content Understanding charged?

📹 [41:42](https://youtube.com/watch?v=gC5q1lQz4wg&t=2502)

Document extraction is metered by page and processing level. During the session, the pricing page showed $0.01 per 1,000 pages for minimal processing and $5 per 1,000 pages for standard processing. Minimal mode is for digital documents that do not need OCR or layout processing; basic adds OCR, while standard adds layout analysis such as table recognition and figure extraction. Check the current [Azure Content Understanding pricing](https://azure.microsoft.com/en-us/pricing/details/content-understanding/) and [metering explanation](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/pricing-explainer#document-content-extraction-meters) before estimating production costs.

### Should Azure Content Understanding be used to classify documents into known categories?

📹 [44:43](https://youtube.com/watch?v=gC5q1lQz4wg&t=2683)

It can can be used for a pipeline that classifies documents, but it may be excessive if classification is the only requirement. A small local model can be more economical for mapping documents to a few predefined categories. With labeled examples and a measurable score, DSPy can optimize the structured-output prompt and balance output quality against token usage or model calls.

### Which open-source PDF library should a proprietary application consider?

📹 [47:04](https://youtube.com/watch?v=gC5q1lQz4wg&t=2824)

Check licensing before choosing a parser. Pamela had used PyMuPDF but noted that it uses AGPL-3.0 with separate commercial licensing for proprietary applications. She planned to investigate [pypdfium2](https://github.com/pypdfium2-team/pypdfium2), a more permissively licensed wrapper around PDFium, while noting that it may be slower. A small local vision-language model such as [Gemma](https://ollama.com/library/gemma4) is another option for harder extraction tasks.

## How can local Gemma models be run?

📹 [51:49](https://youtube.com/watch?v=gC5q1lQz4wg&t=3109)

[Ollama](https://ollama.com/) provides Gemma models, including MLX variants optimized for macOS. [Foundry Local](https://www.foundrylocal.ai/models?cpu&gpu&npu&family=gemma) also offers Gemma and is particularly worth investigating on Windows, where its models can be optimized for the available hardware.

## How can someone start learning to build AI models?

📹 [52:32](https://youtube.com/watch?v=gC5q1lQz4wg&t=3152)

Work through Sebastian Raschka's [Build a Large Language Model (From Scratch)](https://sebastianraschka.com/llms-from-scratch/). Its Python notebooks walk through implementing a language model and provide a practical foundation in the matrix operations behind transformers. Raschka also publishes technical breakdowns of new model architectures and has material on building reasoning models.
