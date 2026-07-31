# July 30, 2026 Office Hours Q&A

## What is the difference between GQL and Cypher?

📹 [00:57](https://youtube.com/watch?v=q6MeccGbKNs&t=57)

GQL is the [ISO-standard graph query language](https://www.iso.org/standard/76120.html). Cypher predates it and is very similar, so people already using Cypher will recognize many of the same concepts. A useful overview of what the GQL standard adds is available in this [GQL versus Cypher comparison](https://nebula-graph.io/posts/gql-vs.-cypher-what-the-new-iso-standard-brings-to-the-table).

## Should we put all our data in OneLake and ingest it into Foundry knowledge bases from there?

📹 [02:03](https://youtube.com/watch?v=q6MeccGbKNs&t=123)

It depends on what else you need to do with the data. OneLake makes sense when you want to use other Fabric capabilities over the same data. If the only goal is retrieval or search, storing content in Azure Blob Storage or Azure Data Lake Storage and indexing it directly may be simpler and less expensive.

The decision should account for the data's format, update frequency, query patterns, and cost. A Fabric data agent may be enough when it can query the source remotely. If you need custom processing or more control over retrieval, [Azure AI Search can index OneLake files and shortcuts](https://learn.microsoft.com/azure/search/search-how-to-index-onelake-files). That creates another copy, though the indexer can detect additions, updates, and deletions.

### What about text columns containing paragraphs, such as website comments or product descriptions?

📹 [07:07](https://youtube.com/watch?v=q6MeccGbKNs&t=427)

For unstructured or paragraph-length text, consider whether the questions need semantic similarity rather than only structured queries. If so, an Azure AI Search index is likely the better fit because it can combine vector and keyword search. The exact choice still depends on the content and the questions users will ask; the speaker had not tested this specific storage pattern through a Fabric data agent.

## Can Fabric IQ answer questions about a Power BI report through its semantic model?

📹 [08:56](https://youtube.com/watch?v=q6MeccGbKNs&t=536)

A Fabric data agent can answer questions grounded in the data exposed by the semantic model. It generates and runs DAX queries against that model. It does not inspect the report's visual presentation, so it cannot necessarily answer questions about what appears in a particular chart or on a report page. A useful rule is that if the question can be answered by a DAX query over the model, the data agent can potentially answer it.

## Do I need administrator permissions to create a Fabric ontology?

📹 [11:57](https://youtube.com/watch?v=q6MeccGbKNs&t=717)

The tenant administrator must first enable the required [ontology preview tenant settings](https://learn.microsoft.com/fabric/iq/ontology/overview-tenant-settings). Once those settings are enabled, a workspace user can create an ontology much like other Fabric items; the creator does not necessarily need to be the tenant administrator. Provisioning a new Fabric capacity is a separate operation and may require additional tenant permissions.

## Which Fabric capacities support ontologies and data agents?

📹 [14:33](https://youtube.com/watch?v=q6MeccGbKNs&t=873)

Ontologies and data agents are available on paid Fabric capacities, starting with F2; they do not require F64. F2 can be sufficient for learning and experimentation, although repeated or intensive queries may hit capacity limits. Current rates are listed on the [Microsoft Fabric pricing page](https://azure.microsoft.com/en-us/pricing/details/microsoft-fabric/).

### Are Fabric IQ AI capabilities available in the Fabric free trial?

📹 [17:01](https://youtube.com/watch?v=q6MeccGbKNs&t=1021)

No. Data agents and other Fabric AI capabilities are not available in the free trial, so experimenting with them requires a paid capacity such as F2.

### How are Fabric Ontology costs calculated?

📹 [19:51](https://youtube.com/watch?v=q6MeccGbKNs&t=1191)

Ontology usage is billed through Fabric capacity units, with different meters for definition changes, AI operations, and graph cache storage. Definition usage is triggered by create, update, and delete operations rather than reads. Natural-language reasoning is token-based, and some storage or operation meters use time windows, so grouping related editing work may reduce repeated window charges. Capacity administrators can inspect usage through the Fabric Capacity Metrics app. Because these details can change during preview, consult the current [ontology billing and capacity usage documentation](https://learn.microsoft.com/fabric/iq/ontology/resources-capacity-usage).

## Where can I learn more about Fabric IQ and ontologies?

📹 [23:12](https://youtube.com/watch?v=q6MeccGbKNs&t=1392)

The [Fabric IQ learning path](https://learn.microsoft.com/training/paths/get-started-fabric-iq/) provides a broad introduction, while the [Create an Ontology with Fabric IQ module](https://learn.microsoft.com/training/modules/create-ontology-with-fabric-iq/) and [ontology overview](https://learn.microsoft.com/fabric/iq/ontology/overview) focus on ontology concepts and setup. The [Ontology Playground](https://aka.ms/ontology-playground) offers a hands-on way to explore graphs, relationships, and examples.

When following training or documentation, an LLM can also act as a tutor: ask it to compare unfamiliar Fabric concepts with systems you already know and to clarify each point of confusion. This is most useful when the model is grounded in current documentation and helps deepen your understanding rather than doing the learning for you.

Links shared:

* [Semantic Weekly episode 1: Fabric IQ](https://aka.ms/sematic-weekly/001)
* [Semantic Weekly episode 2: Ontology](https://aka.ms/semantic-weekly/002)

## Where does Graph fit among the Foundry Toolbox tools for Fabric?

📹 [29:30](https://youtube.com/watch?v=q6MeccGbKNs&t=1770)

Foundry does not currently expose Graph as a direct tool or dedicated MCP server. To query Fabric Graph from a Foundry agent, either add it as a data source for a Fabric data agent, or write a custom tool that can execute GQL queries. The [Foundry Toolbox notebook](https://github.com/microsoft-foundry/forgebook/blob/main/notebooks/mastering-foundry-toolbox.ipynb) shows how to add Fabric Data Agent to a Foundry Toolbox.

## Can LangChain, Pydantic AI, or another agent framework use Fabric IQ?

📹 [31:31](https://youtube.com/watch?v=q6MeccGbKNs&t=1891)

Yes. Fabric IQ capabilities are exposed through MCP servers, so another framework can connect to the server URL and supply a user token with access to the Fabric workspace. Local use is relatively straightforward; deployment is harder because the application must obtain and pass the appropriate user token.

For Foundry hosted agents, framework support for the Responses protocol also matters. The Foundry documentation explains the differences between the [Responses and invocation protocols](https://learn.microsoft.com/agent-framework/hosting/foundry-hosted-agent?pivots=programming-language-python). LangChain has a [Foundry Responses adapter and hosted LangGraph samples](https://github.com/langchain-ai/langchain-azure/tree/main/samples/hosting/langgraph-hosted-agents), making it the more direct route discussed in the session. Pydantic AI can connect to MCP, but without a Responses adapter it may need the simpler invocations protocol, which can lose Foundry integrations that assume Responses, potentially including some publishing features. The exact unavailable features were not confirmed during the session.

Links shared:

* [Pydantic AI MCP example](https://github.com/Azure-Samples/python-ai-agent-frameworks-demos/blob/main/examples/pydanticai_mcp_github.py)
* [LangChain MCP example](https://github.com/Azure-Samples/python-ai-agent-frameworks-demos/blob/main/examples/langchainv1_mcp_github.py)

## Is the Microsoft skills-for-fabric repository recommended for coding agents?

📹 [36:25](https://youtube.com/watch?v=q6MeccGbKNs&t=2185)

The [skills-for-fabric repository](https://github.com/microsoft/skills-for-fabric) appears current and can give coding agents focused Fabric instructions. Skills can occasionally become stale or over-trigger, so install only the relevant skills and remove them if they interfere. For GitHub Copilot in VS Code, the recommended starting point is the [Microsoft Fabric extension](https://marketplace.visualstudio.com/items?itemName=fabric.vscode-fabric), which prompts users to install its Fabric MCP server companion and can browse or open workspace resources.

### What if the coding agent does not run in VS Code?

📹 [42:21](https://youtube.com/watch?v=q6MeccGbKNs&t=2541)

The repository's skills can be installed for other compatible coding agents. For command-line workflows, [Fabio](https://github.com/iemejia/fabio) is also recommended as an agent-oriented CLI for Fabric operations and deployments.