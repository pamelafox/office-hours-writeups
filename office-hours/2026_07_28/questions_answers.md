# July 28, 2026 Office Hours Q&A

These office hours followed session 1 of the [Microsoft IQ Deep Dive](https://aka.ms/iqdeepdive/resources) series, which covered Foundry IQ.

## Can we talk about data privacy, like anonymization and keeping PII out of the LLM?

📹 [0:50](https://youtube.com/watch?v=eIQvKPOxsfc&t=50)

For controlling who can see what, Azure AI Search has built-in [document-level access control](https://learn.microsoft.com/azure/search/search-document-level-access-overview). When you set up the index you designate which fields hold the Entra OID and the Entra group IDs, store those values on each document chunk, and then pass the user's token when you search. Only chunks that pertain to that user come back. That approach is most useful when you are indexing documents from an arbitrary source and need full control over visibility.

The other option is a remote knowledge source. Work IQ requires the user's token, so it will only ever return information that user can already see, and the access control comes for free.

For keeping PII away from the model entirely, one option is to avoid an LLM at certain stages. Configuring the knowledge base in minimal mode means no LLM is involved in query planning, and a plain search call involves even fewer services. But if you are building an agent that answers questions or takes actions, you have to ask whether the question can still be answered without the PII. If it can, [PII detection and redaction](https://learn.microsoft.com/azure/ai-services/language-service/personally-identifiable-information/how-to/redact-text-pii) in Azure AI Language (now part of Foundry tools) can strip sensitive values before the text reaches the model. There is also now a PII category available in Foundry guardrails.

Running a local model through Foundry Local is another route, as suggested in chat: the agent runs on your own machine, and it can still reach out to a Foundry IQ knowledge base in minimal mode so fewer services see the data. Lee Stott added that Azure Local supports disconnected and sovereign scenarios with Foundry Local plus cloud hybrid deployments.

It is also worth knowing the [Azure OpenAI data privacy policy](https://learn.microsoft.com/azure/foundry/responsible-ai/openai/data-privacy): prompts are not available to other customers, not available to OpenAI or other model providers, and not used to train models without your permission. That is one of the stronger privacy policies in the industry and not everyone realizes it exists.

Links shared:

* [Security filter pattern in Azure AI Search](https://learn.microsoft.com/azure/search/search-security-trimming-for-azure-search)

## What guards exist against indirect prompt injection?

📹 [5:42](https://youtube.com/watch?v=eIQvKPOxsfc&t=342)

[Foundry guardrails](https://learn.microsoft.com/azure/foundry/guardrails/guided-set-up) apply at the model level. Default guardrails are applied to Foundry models, but you can create custom guardrails and choose which risks to detect. Jailbreak detection is always on; indirect prompt injection is the one you need to add explicitly, because that is the attack that arrives inside your data or a tool response rather than from the user. Content harms support custom block lists, and there are also protected material checks, a PII category, and, for hosted agents, network egress rules. Some of the newer categories run LLM-as-judge evaluations, which will add latency, so think carefully before running those inline.

Beyond guardrails, the practical rule is that your agent can only do as much as you give it access to. If you do not want it sending email, do not give it a tool that sends email. If it needs to, require human approval, or route the action through another LLM check that asks whether this particular email should be sent.

Guardrails are the first place to look because they attach to the model: set up the guardrail, assign it to the model, use that model in your agent, and every model call gets checked.

Links shared:

* [Detect prompt attacks with Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-jailbreak)

### Can I apply the guardrails to LLMs that are not hosted on Foundry?

📹 [17:54](https://youtube.com/watch?v=eIQvKPOxsfc&t=1074)

Not the native Foundry guardrails — those are designed for Foundry models and Foundry Agent Service workloads only, and Foundry models always come with them applied. For any other model endpoint, use [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-jailbreak) and policy-based controls, which offer Prompt Shields and custom detection and can be applied to virtually any model by placing them in your application or agent orchestration layer.

For mixed estates spanning OpenAI, Anthropic, and local models, treat guardrails as a runtime architecture pattern rather than a model feature, so the same safety controls apply regardless of where the model is hosted.

## Are knowledge sources and the services that touch the data located in our tenant, or can we control the country/region?

📹 [8:39](https://youtube.com/watch?v=eIQvKPOxsfc&t=519)

Region residency depends on the feature. Connected models live in whatever region you deploy them to, and most other components are region-restricted, but each Azure AI Search feature has its own behavior, so check that feature's documentation. The [region support documentation](https://learn.microsoft.com/azure/search/search-region-support) shows which features are available where. Remote knowledge sources depend on the individual source — Web IQ, for example, is a global service and may have to stay global architecturally.

For strict residency requirements, validate three things separately: the region of the knowledge sources (SharePoint, Blob, OneLake), the region of the Azure AI Search service backing the knowledge base, and the documented residency commitments for Foundry IQ indexing, retrieval, reasoning, and enrichment.

## Should I add my relational database or my raw files as the data source for a document chat experience?

📹 [10:27](https://youtube.com/watch?v=eIQvKPOxsfc&t=627)

Context from the developer asking the question: They are building an HR document management app already uses Azure Content Understanding to detect document type and extract key fields into a relational database outside Azure. They're wondering whether to index both the raw files and the extracted data.

It depends on the questions users ask, and you could add both. One approach is two tools: one that queries the extracted structured data and one that queries the original documents. Or make them two knowledge sources in a single knowledge base. The extracted data is attractive because it is already clean.

Another approach is to fold the extracted data into the search index as metadata fields on each chunk, so a result returns both the text chunk and its metadata — page number, section heading, date. This is sometimes called content stuffing or content expansion, and it gives the LLM more to work with.

Whichever direction you pick, start experimenting and set up evaluations with something like 50 representative questions. Do not validate a solution against three sample questions, because it will work great for exactly those three and you will have no idea what happens beyond them.

## Does Foundry IQ handle ASPX-based SharePoint content well?

📹 [12:52](https://youtube.com/watch?v=eIQvKPOxsfc&t=772)

There are multiple SharePoint options. The [indexed SharePoint knowledge source](https://learn.microsoft.com/azure/search/agentic-knowledge-source-how-to-sharepoint-indexed?pivots=python) has Azure AI Search index your SharePoint content, which makes a copy. The advantage of a copy is control: you can customize ingestion, and you can still enforce the document-level permissions described earlier.

There is also a [remote SharePoint option](https://learn.microsoft.com/azure/search/search-how-to-index-sharepoint-online#index-aspx-site-pages), but it is essentially the Copilot indexer. Its documentation does mention indexing modern ASPX site pages, but if Copilot was already failing to retrieve reliably from those pages, this path will hit the same retrieval quality issues, because ingestion and retrieval are both handled by Copilot rather than Azure AI Search. It is also still in preview, and it is unclear how much long-term staying power it has now that Work IQ exists.

The two forward-looking recommendations are Work IQ or indexing it yourself with Azure AI Search. You would need to build a custom skill for ingesting the ASPX files at this point, however. Stay tuned for improvements in the future.

## Are RAG data permissions checked at query time, or cached? If someone is removed from an Entra group, is there a delay?

📹 [16:34](https://youtube.com/watch?v=eIQvKPOxsfc&t=994)

Security trimming is cached, per a confirmation from the Foundry IQ team during the session. So if someone is removed from a group, there is some caching delay before that takes effect for RAG queries. The exact cache duration was still being confirmed.

## If we add Work IQ as a knowledge source, what does that cost on top of Work IQ itself?

📹 [20:52](https://youtube.com/watch?v=eIQvKPOxsfc&t=1252)

To understand the pricing, let's break the pipeline into stages. Query planning uses an LLM, so that cost lands in your LLM budget, not your search budget. The call out to the remote source itself does not appear to carry a separate Foundry IQ charge. The cost that comes out of your search budget is agentic reasoning — the result merging and reranking stage — because that model lives in the search service.

So for a remote knowledge source, search is handled by the remote source, query planning is an LLM cost, and result merging is the Azure AI Search cost. The [pricing page](https://azure.microsoft.com/pricing/details/search/) confirms that separate charges are incurred for remote knowledge sources like SharePoint and web, with agentic retrieval billed on reranking tokens. Semantic ranker charges apply only to indexes.

There is also now a [serverless tier for Azure AI Search](https://learn.microsoft.com/azure/search/search-sku-tier), announced at Build. It is in preview, so it is not practical to rely on yet, but once it ships properly it should substantially reduce search service pricing.

## Do you have experience with Dataverse and using FetchXML or OData queries to connect to models?

📹 [24:39](https://youtube.com/watch?v=eIQvKPOxsfc&t=1479)

No, Pamela was not personally familiar with Microsoft Dataverse.

[Dataverse](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro) is the database layer for Power Platform, and it does have a [Dataverse MCP server](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-mcp), which means you can connect it to an agent. It also shows up in the Foundry tool catalog, so you can add Dataverse to a Foundry toolbox. Authentication requires bringing your own client ID.

For Power Platform and Dataverse-specific questions, the [Microsoft 365 & Power Platform Community](https://pnp.github.io/) is a better venue.

## What role do knowledge graphs and ontologies play in retrieving knowledge or reasoning in Foundry IQ?

📹 [26:48](https://youtube.com/watch?v=eIQvKPOxsfc&t=1608)

Foundry IQ currently has no particular knowledge graph integration. The team has been looking at and working with [GraphRAG](https://microsoft.github.io/graphrag/query/global_search/) for a long time, because a graph answers questions that chunk-based search cannot — "what are the top five themes in this data?" is impossible to answer from retrieved chunks. GraphRAG builds semantic clusters and searches across them. The hard part is productionizing it: GraphRAG is token-hungry, slow, and expensive, and making it performant enough to ship is still an open problem.

If you want to approximate it yourself, you can precompute the graph and store it as multiple indexes in one knowledge base rather than computing on demand:

* A zoomed-in index where every entry is a document chunk.
* An index of document summaries.
* An index of themes found across all documents.
* Entity indexes — people mentioned, objects, relationships.

Then a knowledge base spanning those sources can answer both detailed and zoomed-out questions while staying performant. As always, the right data layout depends on the questions you actually get.

Note that Fabric IQ has a feature called graph, but that is about connecting relational data rather than working with unstructured content.

## How do I filter documents indexed in AI Search based on user roles?

📹 [31:46](https://youtube.com/watch?v=eIQvKPOxsfc&t=1906)

Context from chat: the approach in question was adding a custom `roles` field to the index and narrowing retrieval per user during search, using [custom Entra roles](https://learn.microsoft.com/entra/identity/role-based-access-control/custom-create?tabs=admin-center).

That approach is right. Azure AI Search does have [built-in support for filtering based on Entra IDs and groups](https://learn.microsoft.com/azure/search/search-document-level-access-overview), but not for [Entra roles](https://learn.microsoft.com/entra/identity/role-based-access-control/permissions-reference), so you can  implement it yourself with a filter. Add a roles field to each document, construct the filter yourself, and combine it with any other filters you need.

## Can the built-in tool that Foundry agents use to connect to an AI Search index return custom fields from that index?

📹 [44:09](https://youtube.com/watch?v=eIQvKPOxsfc&t=2649)

A knowledge base should be able to return all the fields. When you create a knowledge source you specify the source data fields — things like blob path, snippet, parent ID — as well as which fields are actually searched. The source data fields are what get returned, and there is an option to request additional fields for the reference source data.

The catch, demonstrated live, is the MCP server. When you use the Foundry IQ MCP server you cannot customize retrieval parameters and you cannot access the full references. It returns inline reference markers like `ref_id 1` but not the separate reference objects with your custom fields. Foundry Toolbox with a knowledge base has the same drawback, since it uses the MCP server underneath.

Using the custom tool path instead gives you the references. During a live demo on the call, the custom tool path also returned `source_data: null`, which was unexpected. That was likely a serialization issue, as you can see non-null `source_data` in the notebook references outputs.

## Is there a decision tree for when to stay inside M365 and Copilot Studio versus going to Foundry?

📹 [38:44](https://youtube.com/watch?v=eIQvKPOxsfc&t=2324)

An honest caveat first: Pamela has only tried Copilot Studio once, about three years ago, so this is not a fair head-to-head comparison. Her personal decision rule is to go where she can write the most code and have the most control, which means Foundry, particularly Foundry hosted agents.

There is a whole spectrum of control:

* Copilot Studio — least control, though SDKs exist so it is not purely no-code.
* Foundry prompt agents — more control.
* Foundry hosted agents — more control again, with easy deployment, observability, monitoring, evaluations, and the optimizer built in.
* Container Apps, including the new Container Apps sandboxes — deploy the agent yourself.
* Kubernetes — maximum control, maximum intensity.

Integrations used to be a strong argument for Copilot Studio, but Foundry now has connections to Fabric IQ, Work IQ, and Foundry IQ, a growing tool catalog (Dataverse included), toolboxes, and custom tools via OpenAPI, MCP, or A2A.

The practical advice is to list the features you need, the flexibility and control you need, and how you like to develop, and see which fits.

Lee Stott's advice: lead with Copilot Studio when low-code makers or business teams are building, the organization already uses Power Platform, the agent mainly lives in Teams or M365 Copilot, and governance and rapid delivery matter more than deep customization. Lead with Foundry when professional developers own the solution, the team already uses GitHub, VS Code, Azure DevOps, or agent frameworks, and you need advanced RAG, custom models, observability, evaluations, or multi-agent orchestration. Use both when the experience lives in Teams/M365 but the intelligence layer needs advanced AI engineering.

## If information lives in Work IQ, are the retrieval methods different from retrieving through Foundry IQ?

📹 [43:05](https://youtube.com/watch?v=eIQvKPOxsfc&t=2585)

Yes. Work IQ is a remote data source, so comparing indexed SharePoint against remote Work IQ is comparing two genuinely different retrieval pipelines.

The recommendation is to compare them for your data. If Work IQ is good enough, use it — with a remote data source you do not have to worry about keeping a copy fresh or reimplementing data access control. Only when it is not good enough, or is missing something you need, should you move to indexing the data yourself.

## Where is the right boundary between Foundry IQ for grounded knowledge and your own application for tenant isolation, permissions, and action approvals?

📹 [53:47](https://youtube.com/watch?v=eIQvKPOxsfc&t=3227)

Context from chat: the developer is building an Azure-first RMM platform adding an operator chat that answers from runbooks and can help take action on endpoints, deployed into customer Azure environments.

Once an agent both retrieves knowledge and takes actions, you are in lethal trifecta territory: access to private data, the ability to communicate externally, and exposure to untrusted content such as web search results. Even without the third element, access to data plus the ability to send an email is already risky.

The usual recommendation is a human approval step — and the honest part is that this is something you build. Where the approval happens is your application's job. One pattern seen in production on top of Foundry IQ is a customer service setup with an inbox of items to process, ranked by priority, flagging the ones that really need human review. Building that means building an interface, or adding more LLM checks along the way that decide whether there is enough confidence to take the next step.

One design habit worth adopting: whenever an agent can take an action, also give it the ability to *not* take the action. Let it opt out and say it does not have enough confidence right now.

Links shared:

* [Securing AI: data access control for RAG](https://speakerdeck.com/pamelafox/securing-ai-data-access-control-for-rag)

## Announcement: MCP 2.0 ships today

📹 [30:25](https://youtube.com/watch?v=eIQvKPOxsfc&t=1825)

Today is the release of MCP 2.0, and the GitHub MCP server already has updates for the new spec version. There are MCP graduation release parties happening around the world today. Upcoming MCP coverage includes [MCP Live](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/join-us-for-our-mcp-live-—-a-free-livestream-covering-all-things-mcp/4537980) on September 8, in-person events in San Francisco and Bengaluru, and a VS Code livestream in mid-August focused on MCP 2.0.

## Demo: publishing a Foundry hosted agent to Teams

📹 [35:06](https://youtube.com/watch?v=eIQvKPOxsfc&t=2106)

A live walkthrough of publishing a Foundry hosted agent from Foundry Toolbox into Teams. Publishing creates an Azure Bot Service resource, and the agent then appears under "Manage your apps" in Teams, with a sign-in link on first use.

The main gotcha is tenancy: the agent only works inside the tenant you published it to, because the login is tenant-specific. If you work across multiple tenants — as is common at Microsoft, where production tenants are reserved for production — publish the hosted agent to your test tenant and use Teams from that same test tenant. Lee Stott noted in chat that your Teams admin will need to deploy the agent for a live tenant.