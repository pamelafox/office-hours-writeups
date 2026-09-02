# September 1, 2026 Office Hours Q&A

## Announcement: FastMCP v4 released

📹 [00:14](https://www.youtube.com/watch?v=vYuocS1keFs&t=14)

[FastMCP 4](https://gofastmcp.com/getting-started/whats-new) is now stable. It supports the newer sessionless MCP protocol while negotiating compatibility with clients that still use the older session-based protocol. Existing FastMCP users should follow the upgrade guide, run their tests, and test against both kinds of clients. [Can I Use MCP](https://caniuse.dev/embed/host-compare) can help identify which protocol features different hosts currently support.

## How can an MCP server be protected from an unsafe or compromised agent?

📹 [02:07](https://www.youtube.com/watch?v=vYuocS1keFs&t=127)

MCP security documentation often emphasizes authentication and authorization, but protecting a server from the agent itself requires a broader threat model. The exact controls depend on the anticipated attack, such as prompt injection, unsafe tool use, or unauthorized network access. The [MCP security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) are a starting point, but application and infrastructure controls are also necessary.

## Discussion: OpenAI Hugging Face incident

📹 [03:53](https://www.youtube.com/watch?v=vYuocS1keFs&t=233)

### Security lessons

📹 [03:53](https://www.youtube.com/watch?v=vYuocS1keFs&t=233)

The [OpenAI report](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) and subsequent analyses highlighted several security failures: the agents were not adequately isolated from the network, relevant monitoring was not enabled, and instructions were relied upon where enforced controls were needed.

Use defense in depth: enforce sandbox and network restrictions in infrastructure, monitor network activity, retain audit trails, run health checks, and consider guardian models and canaries. [XBOW's agent-safety guidance](https://xbow.com/blog/autonomous-agent-safety-guardrails) illustrates the distinction between soft prompt-based scoping and hard controls. Pamela also shared the [Dwarkesh Patel account](https://www.dwarkesh.com/p/openai-huggingface) and [Gary Marcus's critique of that account for overly anthropomorphizing the agents](https://garymarcus.substack.com/p/5-lessons-from-the-openai-hugging).

### Agent communication style

📹 [09:43](https://www.youtube.com/watch?v=vYuocS1keFs&t=583)

John brought up the agents' shortened communication style, noting that they dropped grammatical words while remaining understandable. Pamela found this linguistically interesting and suggested that the agents might be communicating more efficiently. Their ability to shorten language selectively could indicate a meaningful grasp of linguistic structure, or it could reflect patterns in training data such as terse online conversations. It's unclear if there's a definitive cause.

## Are large language models mainly developed by Anthropic?

📹 [16:24](https://www.youtube.com/watch?v=vYuocS1keFs&t=984)

No. Many organizations develop both closed and open-weight models, including Anthropic, OpenAI, xAI, Moonshot AI, Zhipu AI, and Meta. Rankings change by benchmark and by user preference, so a leaderboard should not be treated as a universal answer. [Artificial Analysis](https://artificialanalysis.ai/#intelligence) provides a current comparison across model providers and metrics.

## Demo: ChatGPT support for WebMCP

📹 [22:09](https://www.youtube.com/watch?v=vYuocS1keFs&t=1329)

WebMCP lets a website expose structured tools directly from its page. During the demo, the ChatGPT desktop app recognized a test site's tools without being explicitly told to use WebMCP, requested permission, listed the tools, and successfully called one to add a pizza topping.

According to the [ChatGPT site-tools documentation](https://learn.chatgpt.com/docs/webmcp), this support is available in the desktop app rather than the web version. Pamela sees the ChatGPT support for WebMCP as a great way to bring it to the masses, but also thinks that most websites should be offering standard MCP servers instead or in addition. For developers interested in MCP, the [WebMCP Challenge](https://openai.com/webmcp-challenge/) is a great excuse to experiment with it.

## Discussion: VS Code agent hook for completion

📹 [31:25](https://www.youtube.com/watch?v=vYuocS1keFs&t=1885)

[Agent hooks](https://code.visualstudio.com/docs/agent-customization/hooks) run configured actions when specific events occur during GitHub Copilot agent sessions in VS Code and the Copilot app. Pamela configured a `Stop` hook that plays a completion sound whenever an agent stops. If the computer has been idle for more than 60 seconds, the hook also uses macOS `say` to speak the conversation title, letting her know which task completed while she is away from the computer. Her [agent-completion hook](https://gist.github.com/pamelafox/c9cb3e000fdf127741b121d7c5abbf02) contains the configuration.

Another option is to have a local model summarize the agent's final message before speaking it. Hooks can also enforce deterministic follow-up work such as linting; check out [Nicholas C. Zakas's agent-hooks article](https://humanwhocodes.com/blog/2026/05/vscode-agent-hooks/) as a more advanced example.

## Discussion: DSpy meetup and improvements

📹 [36:24](https://www.youtube.com/watch?v=vYuocS1keFs&t=2184)

[DSPy](https://dspy.ai/) treats prompts as compiled artifacts. Developers specify input/output signatures, and an optimizer searches for an effective implementation rather than requiring hand-maintained prompts. Pamela described a meetup demonstration of DSPy.Flex that optimized an entire Python module, not only its prompts. When rewarded for reducing model calls, it generated code that used regular expressions for routine checks and called an LLM only when necessary, improving the demonstrated accuracy while using fewer LLM calls.

## Discussion LM15, an alternative to LiteLLM

📹 [38:29](https://www.youtube.com/watch?v=vYuocS1keFs&t=2309)

[LM15](https://github.com/lm15-dev) is an effort to build smaller, lower-level model-agnostic libraries in Python, Rust, Go, and TypeScript. At the time of the session it supported responses and chat-completions APIs, and its maintainers had tested at least Azure key-based access. Pamela considered it worth watching as an alternative to LiteLLM, though her Azure testing was not yet complete.

## Should framework-agnostic APIs for a voice agent be exposed through MCP?

📹 [39:38](https://www.youtube.com/watch?v=vYuocS1keFs&t=2378)

Usually, yes. If several agent frameworks need portable access to the same API endpoints, an MCP server provides a common protocol and constrains how tool parameters are presented. Most major agent frameworks already support MCP.

Protocol compatibility does not guarantee identical behavior. Start with a clear tool schema, then evaluate the expected models and frameworks to see whether they choose the right tool and supply the right parameters. Pamela's [MCP tool-schema evaluation](https://blog.pamelafox.org/2026/03/do-stricter-mcp-tool-schemas-increase.html#frameworks) found more variation across models and reasoning-effort settings than across agent frameworks, although framework differences still existed.

### Were those MCP evaluations built with `azure-ai-evaluation`?

📹 [43:43](https://www.youtube.com/watch?v=vYuocS1keFs&t=2623)

No. A coding agent generated a custom evaluation harness, despite initially being asked to use Pydantic AI Evals. For tool calls with known expected arguments, the evaluators could use exact comparisons rather than an LLM judge. An LLM judge may still help with free-text parameters.

Pamela recommended recording as much run data as possible, including reasoning settings and tool calls, then using a coding agent to compare runs and investigate anomalies. Human scrutiny remains important: one apparent framework failure was actually caused by a local-date versus UTC difference, which only became clear after rerunning at different times.

## How is the GitHub Copilot SDK different from Microsoft Agent Framework?

📹 [47:38](https://www.youtube.com/watch?v=vYuocS1keFs&t=2858)

The [GitHub Copilot SDK for Python](https://github.com/github/copilot-sdk/tree/main/python) provides programmatic access to the agent harness underlying Copilot CLI and the Copilot app. Microsoft Agent Framework is a higher-level framework for building agents and workflows. They overlap, but Agent Framework can also host a Copilot SDK agent as one component in a larger workflow.

Different harnesses may add different system prompts and manage tool calls differently. In Pamela's comparison, the most visible Copilot SDK difference was a date/time value in its underlying context, which affected a date-sensitive evaluation; she noted that behavior may since have changed.

### Does the Copilot SDK support subagents and parallel, sequential, or looping workflows?

📹 [49:54](https://www.youtube.com/watch?v=vYuocS1keFs&t=2994)

Pamela had not tested these capabilities enough to confirm them. She expected that features available through the Copilot CLI or app would generally be accessible through the SDK, but did not find an explicit subagent example during the session. For explicit workflow orchestration, integrating a Copilot SDK agent into Microsoft Agent Framework is another option.

## Announcement: Python 3.15 pending release

📹 [50:51](https://www.youtube.com/watch?v=vYuocS1keFs&t=3051)

Python 3.15.0rc2, the final release candidate preview for Python 3.15, was released on September 1. Pamela noted that Python 3.9 had reached end of life and Python 3.10 was approaching it, making it a good time to review supported Python versions.
