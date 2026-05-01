# April 30, 2026 - "Host your agents on Foundry" Day 3 (Quality + Safety Evals) Office Hours

This was a follow-up office hours after the "Host your agents on Foundry" Day 3 livestream about quality and safety evaluations.

## Are there evals that score on cost and token efficiency?

📹 [00:53](https://youtube.com/watch?v=B3-otzOjgJI&t=53)

There are no built-in evaluators for cost/token efficiency, but you can write a [custom code-based evaluator](https://learn.microsoft.com/azure/foundry/concepts/evaluation-evaluators/custom-evaluators#code-based-evaluators) for it. Token usage usually comes back in the API response (especially with the Responses API), so as long as that data is available, you can write a Python function that pulls it out and evaluates it. If token usage isn't in the API response, it should also be in OpenTelemetry traces, which is another way to access that data.

Pamela also always measures latency in her evaluations, which is straightforward since it's just elapsed time.

Note that Foundry evaluations do return operational metrics (latency and tokens) for each evaluation run, but those measure the evaluation itself, not the agent run being evaluated.

## Are there built-in evaluators that don't depend on LLM-as-a-judge?

📹 [04:32](https://youtube.com/watch?v=B3-otzOjgJI&t=272)

Yes — there are textual similarity evaluators (BLEU, ROUGE, etc.) from the NLP research space that don't use LLMs. However, Pamela doesn't recommend most of them for agents producing free-flowing text responses, as they tend not to be useful in that context.

The more practical approach is [custom code-based evaluators](https://learn.microsoft.com/azure/foundry/concepts/evaluation-evaluators/custom-evaluators#code-based-evaluators). For example, Pamela has a regex-based evaluator for her RAG app that checks whether citations in the answer match the ground truth — and it's one of her most useful evaluators. Code-based evaluators are also great for measuring things like token usage and latency without needing an LLM.

## How can agent context (like memory) be included in quality evaluations?

📹 [07:23](https://youtube.com/watch?v=B3-otzOjgJI&t=443)

When we send the hosted agent's response for judging, the `output_items` field in the responses contains not just the final output but all tool calls along the way. So if memory is implemented as a tool call, it will be included in `output_items` and visible to the evaluators. Many evaluators that appear to be end-to-end (like intent resolution) actually look at everything in the output items, including intermediate tool calls.

If memory isn't showing up in the output items, you'd need to find a way to inject it into the API response, since the evaluator can only access data that's either in the uploaded dataset or in the API response. With Foundry hosted agents using the Responses API adapter, there are constraints on what can be added to the response.

## In a multi-agent environment, should we have evals for each agent or just the final response?

📹 [10:22](https://youtube.com/watch?v=B3-otzOjgJI&t=622)

Both — start with end-to-end evaluations to get an overall picture, then break it down per agent to pinpoint where failures originate. How you evaluate depends on your multi-agent architecture:

- **Agents-as-tools architecture**: Each sub-agent is a tool, so you can use the built-in tool evaluators to check whether each agent was called correctly and what its response looked like.
- **More flexible architectures**: You'll likely need a [custom evaluator](https://learn.microsoft.com/azure/foundry/concepts/evaluation-evaluators/custom-evaluators#code-based-evaluators) — for example, a "handoff evaluator" that checks whether the triage agent correctly passed to the refund agent in the right scenarios.

Pamela noted that in her experience with handoff orchestration in Agent Framework, the handoffs were sometimes unpredictable, so a handoff evaluator could be very worthwhile. She'll also check with the product team about potential built-in multi-agent evaluators in the future.

### Would the interaction between agents (agent to sub-agent) need to be evaluated differently?

📹 [27:30](https://youtube.com/watch?v=B3-otzOjgJI&t=1650)

Yes, it depends on your architecture. For supervisor/agents-as-tools patterns, agents are just tools and can be evaluated that way. For more flexible architectures, a custom evaluator that looks at agent-to-agent interaction is the way to go — for example, evaluating whether handoffs happened at the right time with the right criteria.

## What does the "Analyze Results" cluster analysis do? Is it like theme analysis?

📹 [12:49](https://youtube.com/watch?v=B3-otzOjgJI&t=769)

The "Analyze Results" button on evaluation runs performs a cluster analysis that groups different kinds of failures together, helping you understand patterns in what went wrong. For example, on a run with 178 samples, it found clusters like "hallucinated response" (73 samples), "required rule unavailable", and "abrupt refusal" — each with suggestions for improvement.

This is different from general theme analysis because it specifically focuses on failures and how to fix them, rather than looking at all responses for general themes. It filters on failed samples and provides actionable suggestions.

## How can you approach streaming and online evaluation together?

📹 [16:13](https://youtube.com/watch?v=B3-otzOjgJI&t=973)

Generally, we don't recommend blocking live user-facing flows for evaluation calls. However, you could try a few approaches:

1. **Self-evaluation in the stream**: Ask the LLM to include its confidence level at the start or end of its streamed response. You can regex that out and render it in the UI. If confidence is low, trigger a second evaluation pass.

2. **Progress updates**: If doing online eval, stream updates to the user showing where you are in the process — "searching", "generating candidate response", "evaluating candidate response" — so they know something is happening rather than just watching a loading indicator.

3. **Confidence visualization**: The [Microsoft HAX Toolkit](https://www.microsoft.com/en-us/haxtoolkit/library/example,guideline/) has examples of highlighting low-confidence tokens in UI, showing users which parts of a response the model is less sure about.

Links shared:

* [Microsoft HAX Toolkit - Design Library](https://www.microsoft.com/en-us/haxtoolkit/library/example,guideline/)
* [Microsoft HAX Toolkit - Research Project](https://www.microsoft.com/en-us/research/project/hax-toolkit/)

## What is the recommended practice for running evals after the app is live?

📹 [20:50](https://youtube.com/watch?v=B3-otzOjgJI&t=1250)

Use a mix of scheduled evaluations at different frequencies:

- **Hourly**: A smoke test with ~5 queries to catch anything that's gone horribly wrong
- **Daily**: A medium test with ~50 queries for more thorough coverage
- **Weekly**: A larger test for comprehensive evaluation

The Foundry documentation defaults to daily for scheduled evals. You can set up multiple schedules with different names. Running 5 questions once an hour costs almost nothing.

### Are there benchmarks or cutoff scores to say an app is prod ready?

📹 [22:30](https://youtube.com/watch?v=B3-otzOjgJI&t=1350)

There's no universal cutoff. Even 100% on an evaluation doesn't mean the app is perfect, since these are LLM-based apps with LLM judges. Internal teams at Microsoft often run evaluations on at least 800–1,000 questions before the first deploy, but they use different thresholds for pass rates.

The practical approach many teams take: do your best effort with evaluations, then put the app out with appropriate UI messaging ("this is AI-generated, please give feedback"), and use continuous evaluation and user feedback to continue improving.

## Can images and audio be used in Foundry safety evaluations?

📹 [24:15](https://youtube.com/watch?v=B3-otzOjgJI&t=1455)

Not yet. Multimodal safety evaluation would require image and audio models with their guardrails turned off so they can analyze potentially unsafe content. The evaluation team is considering adding multimodal safety evaluations in the future.

## How does Azure AI Search compare to Work IQ, and how can you evaluate Work IQ retrieval?

📹 [33:40](https://youtube.com/watch?v=B3-otzOjgJI&t=2020)

Work IQ is an agent that wraps different retrieval mechanisms (SharePoint, emails, chats). To compare it with Azure AI Search, you'd run the same queries through both and compare results. However, it's important to understand what you're comparing:

- **Remote SharePoint** knowledge source in Azure AI Search/Foundry IQ uses a similar retrieval mechanism to Work IQ (API maintained by the M365 team)
- **Indexed SharePoint** knowledge source runs ingestion and creates chunks in your search index, giving you Azure AI Search's hybrid search and semantic ranking

So comparing Work IQ vs. Azure AI Search with indexed SharePoint would be the more meaningful comparison, since remote SharePoint and Work IQ use similar underlying retrieval.

### What is Foundry IQ exactly?

📹 [36:37](https://youtube.com/watch?v=B3-otzOjgJI&t=2197)

Foundry IQ is Azure AI Search using the new agentic knowledge base feature, typically accessed via the [MCP endpoint](https://learn.microsoft.com/azure/search/agentic-retrieval-how-to-retrieve?pivots=python#call-the-mcp-endpoint). The agentic knowledge base can wrap multiple sources including search indexes, indexed SharePoint, remote SharePoint, Bing, OneLake, and blob storage.

## How do you integrate evals with CI/CD?

📹 [41:27](https://youtube.com/watch?v=B3-otzOjgJI&t=2487)

Foundry has a built-in [GitHub Action for running evaluations](https://learn.microsoft.com/azure/foundry/how-to/evaluation-github-action) in CI/CD. You specify your sample data file and evaluators in the YAML config. Important: don't run evaluations on every commit. Instead, use a trigger like a `/evaluate` comment on PRs (with permissions checks so only authorized users can trigger it).

Pamela showed her existing [custom CI/CD eval workflow](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/.github/workflows/evaluate.yaml) for the RAG demo app, which uses a comment-based trigger restricted to repo owners, contributors, collaborators, and members. Another idea: use an LLM to look at a PR and decide whether evaluation should run automatically.

She needs to verify that the GitHub Action works with Foundry hosted agents specifically (it may have been built for prompt agents originally).

## Are there roadmaps for Foundry preview features going GA?

📹 [45:10](https://youtube.com/watch?v=B3-otzOjgJI&t=2710)

Pamela doesn't know specific timelines. Build (about a month away) is a common time for GA announcements, but she can't confirm anything. For hosted agents specifically, she'd want a longer baking period since it's a complex feature. She'll keep an eye out and share any news.

## Is there an agent or tool that can help create evaluations automatically in Foundry?

📹 [54:39](https://youtube.com/watch?v=B3-otzOjgJI&t=3279)

There are a few things moving in this direction:

- **Foundry Agent Skills**: The [`microsoft-foundry` skill](https://github.com/microsoft/azure-skills/tree/main/skills/microsoft-foundry/foundry-agent) in the azure-skills repo has an [observe section](https://github.com/microsoft/azure-skills/blob/main/skills/microsoft-foundry/foundry-agent/observe/observe.md) with skills for building evaluations. There's also an eval datasets skill. These are somewhat specific to the Foundry Toolkit extension.
- **Nitya's Build Lab**: The ["Observe, optimize and protect your hosted agents"](https://build.microsoft.com/en-US/sessions/LAB540?source=sessions) lab at Build will cover using skills and agents to build better evaluations.
- **Hamel Husain's eval skills**: Generic [eval skills](https://github.com/hamelsmu/evals-skills) including an ["eval audit"](https://github.com/hamelsmu/evals-skills/blob/main/skills/eval-audit/SKILL.md#2-evaluator-design) that checks best practices (e.g., ensuring evaluators are binary pass/fail rather than 1-5 scales). Even without using the skill directly, the criteria are useful as best practices.

## Announcements

📹 [51:23](https://youtube.com/watch?v=B3-otzOjgJI&t=3083)

- **Build labs**: Pamela is working on a [Foundry IQ lab at Build](https://build.microsoft.com/en-US/sessions/LAB532?source=sessions) that will try to use Foundry IQ, Work IQ, and Fabric IQ together. The lab is called "From data to context: Agent-ready knowledge with Foundry IQ".
- **Content safety filter handling**: If your agent encounters a content safety filter error, make sure to [handle it in your code](https://github.com/Azure-Samples/ai-quality-safety-demos/blob/main/samples/chat_error_contentfilter.py). The error comes back as an error code `content_filter` in the JSON response, and different SDKs surface it differently.
- **Eval skills and papers**: A paper on ["Protocols and Harness Engineering"](https://arxiv.org/pdf/2604.08224) was shared by a community member.
- **Future events**: No virtual hackathons are currently planned, but Build will have an in-person hackathon. The team is focusing on live stream series going forward.
