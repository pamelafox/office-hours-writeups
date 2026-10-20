# October 20, 2026 Office Hours Q&A

## Announcement: Web IQ is available without a waitlist

📹 [0:37](https://youtube.com/watch?v=z6MeOTBrrNk&t=37)

[Microsoft Web IQ](https://webiq.microsoft.ai/), announced at Build, no longer requires a sign-up form. Any Azure customer can now get started, although the bigger launch announcement is expected at Ignite. Pricing has also dropped from about $12 to $7 per thousand calls.

Setup currently spans two portals: create a Microsoft Web IQ resource in the Azure portal, then sign into the Web IQ portal with the same Azure account to finish onboarding. The portal includes a playground for web, video, news, image, places, auto, and multi-answer search. News search was not available in the demo account. Pamela believed Browse also required special access, but the documentation does not list Browse as restricted, and the quickstart calls it directly.

Search results include a title, URL, content passage, last-updated time, crawl time, and adult-content flag. Web IQ does not generate summaries. Instead, it chunks pages and by default returns the passages that best answer the query, rather than complete page content. The [Web IQ engineering blog post](https://commandline.microsoft.com/grounding-system-agentic-web-engineering-retrieval/) explains the design: a Bing-based search index optimized for low-latency agent retrieval, where passages avoid sending entire, overly long documents to agents. Full-page `text`, `html`, or `markdown` content requires full document access; request it by opening a [Web IQ Support](https://aka.ms/microsoft-webiq-support) request and choosing the **Full-page content** category. Showing click-through links to users is a best practice and may also be required by the terms of use.

Web IQ is a straightforward HTTP API, and its quickstarts use plain HTTP requests. Official [Python and TypeScript SDKs](https://learn.microsoft.com/web-iq/integrations/sdk) are also available as `webiq` on PyPI and `@microsoft/webiq` on npm. Web IQ also has an MCP server. With the MCP server configured in GitHub Copilot, the prompt may need to explicitly say "use Web IQ," since Copilot also has its own default web search. In the demo, the MCP server returned results very quickly. Web IQ is a good option for grounding agents in real-time web results.

### What limitations does Web IQ have, including throttling from scraping protections and CAPTCHAs?

📹 [5:53](https://youtube.com/watch?v=z6MeOTBrrNk&t=353)

Each Web IQ resource starts with a default limit of 15 queries per second, which the demo portal also displayed as 900 queries per minute. The limit applies across all API keys and Entra ID clients for the resource. To request a higher limit, contact [Web IQ Support](https://aka.ms/microsoft-webiq-support) with your expected traffic and use case. Requests over the limit return HTTP 429 with a `retryAfter` value, and daily quota caps reset at 00:00 UTC.

Web Search and the other search APIs return already-indexed data, so scraping protections and CAPTCHAs do not affect those requests. The [Browse API](https://learn.microsoft.com/web-iq/reference/browse) can live-crawl a page with `liveCrawl` set to `fallback` (crawl only if the page is not indexed) or `force` (request a fresh crawl). The documentation does not say how live crawls handle CAPTCHAs or anti-bot protections. It does describe the possible outcomes: a forced crawl that returns stale content includes `liveCrawlSucceeded: false`, blocked or filtered URLs return HTTP 403, and too many concurrent live crawls return HTTP 430.

### What advantages does Web IQ have over Jina.ai?

📹 [9:21](https://youtube.com/watch?v=z6MeOTBrrNk&t=561)

Jina.ai's Reader API converts a URL into LLM-friendly text, so it is closer to Web IQ's [Browse API](https://learn.microsoft.com/web-iq/reference/browse) than its search APIs. Browse returns a page's full content as text, HTML, or Markdown, with options for live crawling and rendering dynamic pages. The Web IQ Browse API may require special access at this time, however. Replacing Jina.ai with Web IQ depends on Browse being available to your account, so try a Browse call with your own key first.

## Demo: Microsoft Decision-1 in Foundry

📹 [13:05](https://youtube.com/watch?v=z6MeOTBrrNk&t=785)

Microsoft Decision-1 is easy to deploy in Foundry, and the deployment includes a playground. Requests provide a state and a decisions JSON object containing questions.

The demo showed three question types:

* **Yes/no:** Returned a 99.7% probability that the statement was true.
* **Choice:** Selected an option, returned confidence for that choice, and included a confidence breakdown across options.
* **Score:** Rated priority on a scale from 0 to 2, returning a weighted score of 1.53 with only about 30% confidence. Low confidence is reasonable for prioritization, which is difficult even for humans.

Sam noted in chat that the scoring criteria were not specific enough. More detailed criteria and examples can improve confidence, but they can also overfit the prompt to the test examples. When making prompts more specific, evaluate them across a wide range of inputs, including novel inputs.

## Discussion: Using decision models for evals

📹 [16:25](https://youtube.com/watch?v=z6MeOTBrrNk&t=985)

Hamel Husain's new post on [how to use decision models for evals](https://hamel.dev/blog/posts/decision-model-evals/) compares several decision models, tunes their decision thresholds, and explains how to interpret their scores. Hamel announced that he joined OpenAI, which Pamela expects may improve OpenAI's evaluation tools.

In the post's comparison, OpenAI Decisions performed very well but cost about four times as much as alternatives. Jev did not meet the post's requirements in that experiment. The post did not include Microsoft Decision-1. Even without adopting its specific results, it is a useful guide to evaluating decision models before switching to them.

### Which decision model would work well for health and medication data?

📹 [18:14](https://youtube.com/watch?v=z6MeOTBrrNk&t=1094)

There is no clear recommendation because performance likely depends on each model's training data. Evaluate the models from Hamel's comparison and add Microsoft Decision-1. OpenAI Decisions is based on GPT-6 Luna, while [Microsoft-Decision-1](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/) is post-trained from Qwen3.5-9B. General benchmarks for those base models may provide clues about their health and medication knowledge.

Fine-tuning is another option. Decision models are much smaller than LLMs, which can make fine-tuning practical for specific scenarios. [Laya](https://github.com/NandhaKishorM/laya), a non-autoregressive decision engine that a colleague was fine-tuning, can be fine-tuned on a laptop in less than 24 hours, depending on the laptop's capabilities.

## Announcement: Jev adds image input and box localization

📹 [20:13](https://youtube.com/watch?v=z6MeOTBrrNk&t=1213)

Jev now supports [images](https://docs.typesafe.ai/images) and a new [Box question type](https://docs.typesafe.ai/primitives/box). TypeSafe labels these features "dreamer-ready" rather than production-ready, and requests must opt in with the `TypeSafe-Danger-Zone-Images: true` header.

Requests can include multiple named images, and questions can reference those assets by name. Box questions locate a described object in an image and return its bounding box. TypeSafe added Box because many developers were already trying to use decision models for object detection. One possible use is checking a front-door camera image to answer questions such as whether a cat is waiting to come inside.

The decision-model space is evolving quickly. More custom models are likely to come out, because an LLM can be larger than necessary for some tasks.

## Announcement: Microsoft AI pre-trains a new base model

📹 [23:14](https://youtube.com/watch?v=z6MeOTBrrNk&t=1394)

The Microsoft AI team published [Frontier Pre-training at Microsoft AI](https://microsoft.ai/news/frontier-pre-training-at-microsoft-ai/), which describes how it trains MAI models. The team completed pre-training a new base model that will serve as the foundation for future MAI models, so more MAI models are likely in the pipeline.

The post is highly technical and is most useful for readers interested in LLM training. Its data strategy includes collecting more web content while prioritizing novel data and reducing duplicates. The team also expanded its vision-language corpus with image-text pairs for captioning, spatial reasoning, medical understanding, and sheet-music reading.

Microsoft AI is led by Mustafa Suleyman, who began his career at DeepMind. For background on DeepMind, Pamela recommended [The Infinity Machine](https://www.amazon.com/dp/0593831845), a book about Demis Hassabis that also discusses Suleyman.

## What is Microsoft Copilot Managed Runtime?

📹 [26:01](https://youtube.com/watch?v=z6MeOTBrrNk&t=1561)

[Microsoft Copilot Managed Runtime](https://learn.microsoft.com/microsoft-365/managed-apps/?view=o365-worldwide) is a preview service for creating, publishing, and managing apps from Microsoft 365 Copilot experiences, including Copilot Code. It is distinct from the Copilot agent harness, though Copilot Code and similar products may use that harness behind the scenes.

The documentation is marked as pre-release, requires enrollment in the Frontier program, and focuses on internal line-of-business apps. It includes admin-center management, Microsoft Entra-secured connectors, Agent 365 integration, Power Platform publishing, and bringing your own GitHub repository. Justin reported that Lovable uses it to publish apps into Power Apps. Nick noted that it looks similar to canvas apps.

This could fill a gap in the Microsoft ecosystem: other AI platforms make it easy to vibe-code an app and share it. The documentation did not explain how to use the runtime directly from GitHub Copilot, such as through an agent plugin. Pamela planned to ask colleagues whether there is a more developer-friendly GitHub Copilot story.

## Announcement: Workshops on agent containers and model swapping

📹 [31:29](https://youtube.com/watch?v=z6MeOTBrrNk&t=1889)

The [Stack It Yourself workshop](https://github.com/bbenz/stack-it-yourself-workshop/) for AGNTCon + MCPCon builds a containerized agent that runs locally with Docker Compose. It makes the architecture more robust with OpenTelemetry and an Ollama container, and it includes Kubernetes resources.

The [Model Swap Workshop recording](https://www.youtube.com/watch?v=UGjk3Uk0MxM) from AI Engineer is now available. Its models are from June and are now outdated, but the [workshop repository](https://github.com/pamelafox/model-swap-workshop) is designed for swapping in newer models and comparing them.

## Discussion: Synthetic handwriting data from Opus 5.5

📹 [33:10](https://youtube.com/watch?v=z6MeOTBrrNk&t=1990)

While testing an OCR ingestion pipeline for Ignite, Pamela asked Opus 5.5 for good sample data. It invented its own synthetic handwriting-generation approach. This showed how capable current models are at creating synthetic data when realistic test inputs are hard to find.

## Demo: HydraFusion in GitHub Copilot

📹 [34:16](https://youtube.com/watch?v=z6MeOTBrrNk&t=2056)

HydraFusion is now available in VS Code. Enable `chat.copilot.hydraFusion.enabled` in VS Code's settings, then choose **HydraFusion** or **HydraFusion Max** from the chat model picker.

Nick Brady joined to demo HydraFusion in the GitHub Copilot app. His screen share was visible during the session, but the recording did not capture his audio. In the Discord chat, Nick said HydraFusion is now his daily driver and a big productivity boost for tasks such as research with GPT-6 Luna.

An attendee reported that HydraFusion consumed usage faster than using Sonnet directly and wanted a way to prevent it from using Opus. You can't choose which models HydraFusion uses, nor designate expensive or cheap models. According to the [HydraFusion documentation](https://docs.github.com/en/early-access/copilot/hydrafusion), it uses only models available in your plan and allowed by your organization's or enterprise's model policies, and its model mix changes as GitHub evaluates new models. Because HydraFusion bills each model it uses at that model's standard rate, tasks that use multiple models can consume more AI credits than a single-model request.

### Can HydraFusion use local models or an NPU?

📹 [43:02](https://youtube.com/watch?v=z6MeOTBrrNk&t=2582)

DaTruAndi noted that HydraFusion used cloud models when they last checked. The Windows Experience blog post, [Building Windows for hybrid intelligence](https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/), says HydraFusion will tap into on-device models on Windows to make tokens go further. That hybrid intelligence capability is coming to the GitHub Copilot app, GitHub Copilot CLI, and VS Code in an experimental preview later in October.

The session did not confirm when or how HydraFusion would select local models. Justin shared the [Aion Instruct Preview sample](https://github.com/microsoft/Aion-Instruct-Preview-Sample/), which demonstrates on-device language model inference on Windows Copilot+ PCs. DaTruAndi said they are building their own inference engine because ONNX Runtime was too limited and resource-intensive for their needs.

## Demo: Creating a canvas in VS Code

📹 [49:52](https://youtube.com/watch?v=z6MeOTBrrNk&t=2992)

[VS Code 1.142 adds canvas support](https://code.visualstudio.com/updates/v1_142#_canvases-preview), and VS Code and the GitHub Copilot app now use the same harness. That convergence makes canvases more useful for developers who switch between the Copilot app and VS Code because they still want to edit code directly. Nick also showed a canvas in the Copilot app earlier in the session.

Canvases let agents create small, interactive web pages for working with data and the agent in a more visual way than chat. In VS Code, enable the **Chat: Canvas Enabled** setting, then invoke the built-in skill with `/create-canvas`.

The demo created a canvas to visualize Azure AI Search index statistics. Canvas extensions are JavaScript files using the `.extension.mjs` extension. They define a `createCanvas` function and actions that can interact with the main agent. A follow-up prompt added a button that sends index details back into chat.

Canvases are most useful when interactions in the canvas send information or actions back to the agent. They can also serve as quick visualizations; because visualizations are now cheap to create, it is worth trying them often. A canvas is not a replacement for a full local web app when you need one.

### Should you use canvases or MCP apps?

📹 [56:12](https://youtube.com/watch?v=z6MeOTBrrNk&t=3372)

Canvases currently work only in GitHub Copilot surfaces, including VS Code and the GitHub Copilot app. Nick noted that canvases also started working in Copilot CLI, where they open in another window. They are a good choice for GitHub Copilot-only teams or personal workflows.

For portability across coding agents, use an MCP app instead. An MCP server can return an app, and an agent plugin can bundle skills with a local stdio MCP server that serves the app.

## What does Pamela use for making slides?

📹 [1:01:06](https://youtube.com/watch?v=z6MeOTBrrNk&t=3666)

Pamela uses Reveal.js whenever she can choose the slide tool. Her [AI-powered presentation workflow slides](https://pamelafox.github.io/ai-powered-presentation-workflow/) describe her current approach, and her older [HTML slides for programming](https://pamelafox.github.io/html-slides-for-programming/) presentation covers a previous workflow. Her [presentation skills repository](https://github.com/pamelafox/presentation-skills) contains agent skills for processing presentations.

Nick uses [Slidev](https://sli.dev/).
