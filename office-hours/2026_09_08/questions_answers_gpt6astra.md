# September 8, 2026 Office Hours Q&A

## Discussion: GPT-6 Astra availability, capabilities, and early impressions

📹 [00:38](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=38)

GPT-6 Astra is now available in [GitHub Copilot](https://github.blog/changelog/2026-09-04-gpt-6-astra-is-generally-available-in-github-copilot/) and [Microsoft Foundry](https://azure.microsoft.com/en-us/blog/gpt-6-astra-frontier-intelligence-for-work-now-generally-available-in-microsoft-foundry/). Pamela successfully deployed it through the Foundry Portal during office hours.

[OpenAI's launch post](https://openai.com/index/gpt-6-astra/) highlights programming, math, tool use, and computer use as promising areas. Pamela's own testing of Astra was limited: Astra generated this week's news roundup, but she has not yet tried it on especially difficult tasks and has not seen a major improvement for her usual work. Justin shared a more substantial result: a project that previously took about ten seconds to connect to a computer now took no more than one second. Reports from Pamela's colleagues also suggest that newer models can handle planning without requiring an explicit planning mode.

### Mid-turn steering and how it differs from queued messages

📹 [07:18](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=438)

[Mid-turn steering in the OpenAI API](https://developers.openai.com/api/docs/guides/steering) lets you send new direction while a response is still running. This differs from queuing a message for later. Copilot's existing steering, as described in the session, delivers the message after a tool call rather than interrupting a long reasoning step or tool call.

The API capability uses a bidirectional WebSocket connection. Pamela expected it could improve responsiveness in VS Code and the Copilot app, but did not know whether either client had already integrated it. She planned to ask the teams; API support should not be taken as confirmation of client support.

### Choosing when to use an expensive model

📹 [09:20](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=560)

There is no need to switch every task to Astra simply because it is new. Copilot labels it as very high cost, and models such as GPT 5.6 Sol already handle many of Pamela's tasks well. One possible approach is to use Astra for a difficult initial plan, then hand implementation to GPT 5.6 Sol or a smaller model such as Luna or Terra.

## Discussion: What recent agent incidents teach us about sandboxing

📹 [10:17](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=617)

[Simon Willison's write-up about agents communicating through public wikis](https://simonwillison.net/2026/Sep/4/rogue-agent-wikis/) follows up on the agent incidents discussed the previous week. The main takeaway: sandbox restrictions need to hold up against unexpected behavior, not just ordinary API conventions.

Two examples stood out:

* Allowing all HTTP GET requests is not equivalent to allowing only reads. A server can implement state-changing operations through GET, even though that is not the usual convention.
* Domain-based network restrictions can fail if an agent can manipulate local hostname resolution, as reported with edits to `/etc/hosts` in the wiki incident.

For more on sandboxing and monitoring recommendations, see [Dwarkesh Patel's interview with Ajeya Cotra](https://www.youtube.com/watch?v=X50zezLFWWI&t=2493s).

## What resources can help with evaluating AI workflows?

📹 [13:50](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=830)

A workflow is a chain of calls, some to LLMs and some to other code. The right evaluation depends on what the workflow is supposed to produce. Start with the expected outputs and concrete success and failure cases rather than choosing a framework first.

* **Structured outputs:** For classification, extraction, or other predictable data, write checks that compare the actual output with the expected result for a given input.
* **Natural-language outputs:** Consider an LLM-as-judge approach with a task-specific rubric and representative examples. Defining what makes an answer successful or unsuccessful takes more work than checking a structured value.
* **Built-in evaluators:** Generic criteria such as intent resolution or task adherence may be useful starting points. Tool-call-specific evaluators are less relevant when the workflow is not an agent choosing and calling tools.

Three useful resources:

* [Foundry rubric evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rubric-evaluators) can help develop custom scoring criteria, including using traces in Azure Monitor as input to the process.
* [Microsoft ASSERT](https://commandline.microsoft.com/assert-written-intent-executable-evals/) offers an open-source approach to bootstrapping evaluations, including suggested personas, scenarios, synthetic data, and rubrics.
* [The evals-skills project](https://github.com/ai-evals-course/evals-skills) can guide a coding agent through evaluation practices when building a custom evaluation setup.

Using a particular framework is less important than following sound evaluation practices. Pamela often writes her own evaluations. The hardest part is usually obtaining useful data and identifying real failure modes: if traces already exist, inspect them for errors; if not, synthetic examples can provide a starting point.

## Demo: Iterating on a garden fence design with MAI-Image-2.5

📹 [20:00](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=1200)

An [image-generation and editing skill](https://github.com/pamelafox/presentation-skills/tree/main/.agents/skills/generate-images-mai/scripts) helped Pamela communicate a garden fence design to a contractor. The skill calls MAI-Image-2.5 in Foundry through a Python script and supports both text-only prompts and an input image.

GPT-5.6 Sol acted as the coordinating LLM in Copilot: it translated Pamela's feedback into image prompts and chose whether to use the original garden photo or one of the intermediate generated images. This made it possible to iterate with the contractor instead of trying to describe every visual detail in words.

One limitation appeared after repeated edits: the background in an intermediate image had acquired a triangulated texture. Pamela suspected that repeatedly feeding generated images back into the model had accumulated artifacts. The result was still useful for communicating the design, but it illustrated a risk of long image-editing chains.

### Can the image be turned into a CAD drawing for construction?

📹 [23:33](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=1413)

A coding-capable model such as Astra might help turn the design into a 2D CAD drawing. Justin suggested [OpenSCAD](https://openscad.org/), mentioning that people had used it with other models.

The generated design was not a reliable source of measurements. The agent struggled to depict a fence at the requested three-foot height, and Pamela did not trust the dimensions in the supplies list it produced. Including a tape measure or another known scale reference in the image could help communicate size. The visual mockup should not be treated as a dimensionally accurate construction drawing.

## Is GPT-6 Astra in Foundry only available through an agents endpoint?

📹 [25:38](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=1538)

No. Astra's model page lists both **Chat Completions** and **Responses**. Responses is the newer OpenAI API and the recommended choice when possible; Pamela migrated her own samples to it. **Messages** refers to the Anthropic Messages API used by Claude models, not an endpoint for Astra.

The confusion came from Foundry's model-comparison page, which showed "Messages" and "Agents" but did not clearly list Chat Completions or Responses. Its descriptions of code input support were also inconsistent.

Pamela suspected that "Agents" indicated compatibility with Foundry prompt agents rather than a requirement to invoke the model through an agent service, but could not confirm the label's meaning. She planned to raise it with the team. The individual model page provided clearer evidence of Astra's supported inference APIs than the comparison checklist.

## Discussion: HydraFusion chooses model orchestration for coding tasks

📹 [30:04](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=1804)

[Project HydraFusion](https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/) is an experimental research preview available in Copilot CLI at the time of the session. To try it, update the CLI, enable experimental features, and select HydraFusion from the model choices. Pamela saw a demo but has not used it herself.

Although it appears as a model selection, HydraFusion chooses an orchestration strategy. Based on the task, it can use a single model, a cascade with a draft and judge followed by an optional repair, or a draft-and-critique approach followed by revision.

Unlike Auto model selection, HydraFusion chooses how models work together, not just which model to call. The intended benefit is better defaults for people who have not already customized their planning, subagents, and model choices. Someone with a heavily customized workflow might see less improvement.

### Will HydraFusion come to GitHub Copilot Chat too?

📹 [32:28](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=1948)

Pamela's understanding from conversations with the team was that they wanted to bring HydraFusion to other Copilot experiences. However, she checked the announcement and did not find a public promise there. She gave no confirmed release date or guarantee of availability in Copilot Chat.

## Announcement: Preparing for Python 3.15

📹 [34:08](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=2048)

Python 3.15 is approaching its October release, so now is a good time to move older projects closer to the current releases. Dependencies are not always ready immediately, though. Pamela usually stays about one version behind when that is necessary to keep the packages she needs working.

## Discussion: Skills over MCP and inconsistent agent-plugin support

📹 [34:36](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=2076)

The [skills-over-MCP proposal](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2640) has been accepted to move forward. It will let an MCP server expose skills as resources, so users could receive guidance associated with a server without separately installing those skills. An accepted proposal is different from a complete implementation: specification work and client adoption still needed to follow.

There are two approaches: agent plugins bundle skills and MCP servers into an installable package, while skills over MCP lets a server expose its own skills directly. If your MCP server has clear skills that belong to it, prefer exposing them through MCP once client support is available, rather than requiring users to install a separate plugin. Agent plugins still make sense for bundling multiple servers and skills or offering different combinations of them.

## Discussion: Linguistic drift and the need to edit AI-generated prose

📹 [41:28](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=2488)

[Pydantic's investigation of linguistic drift](https://pydantic.dev/articles/linguistic-drift-at-the-frontier) traced the increasing use of words such as "seam" in AI-assisted software writing. The article proposes a feedback loop: a model overuses a term, people publish the output, and that text becomes training material that can reinforce the pattern in later models. The investigation pointed to Opus 4.6 as a possible origin for the particular pattern discussed; this was an account of the investigation, not independent verification of how model training caused it.

The authors also created [VocabGuard](https://github.com/mpfaffenberger/vocabguard), which attempts to detect and rewrite this kind of language and can be used with Pydantic AI or separately. Pamela found the exploration interesting but was not convinced that automated vocabulary rewriting was necessarily the right solution.

Review AI-generated prose as carefully as code. Pamela was increasingly happy with model-generated code but frustrated by READMEs, documentation, and blog posts published without an editing pass. Instructions to use simple English or a particular writing style may help, but authors still need to check whether the output is clear and sounds like something they want readers to spend time on.

## Demo: Asynchronous collaboration with GitHub Copilot in Teams

📹 [45:49](https://www.youtube.com/watch?v=uErJ9SlVXbQ&t=2749)

A Teams channel connected to a GitHub repository lets collaborators discuss work and delegate tasks to GitHub Copilot in the same place. Pamela and a colleague used this setup to collaborate asynchronously on a small demo repository instead of finding time for a live pair-programming call.

Several practical details emerged from using it:

* **Mention `@GitHub` for each request.** Ordinary conversation with a colleague does not automatically become an instruction to the agent.
* **Explicitly request a pull request.** In this demo, the agent sometimes made changes without opening a PR, so requests needed to include "make a PR."
* **Check network restrictions when downloads fail.** The default firewall blocked domains needed to download a Hugging Face embedding model. Allowlisting domains was an option; for this particular personal repository, which has no secrets, Pamela ultimately disabled the firewall. That was a choice for this demo setup, not general advice to remove network protection.
* **Start a new thread after changing the firewall settings.** In their testing, the existing thread did not pick up the changed access, while a new one could complete the work and create the PR.

She has made several requests to the engineering team: per-channel instructions and clearer model configuration.

This format is a good fit for small collaborative repositories where the team would already be discussing work in chat. For larger or public repositories, keep substantial conversations in repository issues and discussions. The workflow is also available in Slack, where Pamela found the experience somewhat smoother.
