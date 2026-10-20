# Web IQ feedback from Python + AI Office Hours

Feedback from trying Microsoft Web IQ live during the October 20, 2026 Python + AI Office Hours ([recording](https://www.youtube.com/watch?v=z6MeOTBrrNk&t=37)), plus follow-up research in the Web IQ portal and Microsoft Learn documentation.

## Overall impressions

* Web IQ felt shockingly fast, both in the playground and through the MCP server in GitHub Copilot.
* Passage-based results are a great default for agent grounding.
* The price drop from about $12 to $7 per thousand calls is a strong selling point.
* Attendees were interested and immediately compared Web IQ with tools they already use, especially Jina.ai.

## Onboarding

* **The two-portal setup is confusing.** Users create a resource in the Azure portal, then switch to the Web IQ portal to sign in and connect it. A single guided flow, or at least clear handoff instructions between portals, would help.
* **The Web IQ portal still describes limited access.** The documentation landing page says Web IQ is "available in limited access to select enterprise customers" and tells users to "request access by completing the form above," even though the waitlist is gone.
* **The invitation-code FAQ is obsolete.** "Why can't I verify my invitation code?" should be removed or rewritten for self-service onboarding.
* **The visible access form is closed.** During the session, a form related to restricted capabilities was closed, leaving no obvious path forward.

## Feature access

* **Clearly list which features require approval.** News search was unavailable in the demo account, and I wasn't sure whether Browse required special access. The docs say available APIs depend on the account, but I could not find a single table showing what is available by default and what needs approval.
* **Provide one request path for every restricted feature.** Full-page content in Web Search and News Search has a clear Azure Support category, **Full-page content**. I could not find documentation explaining how to request News access. The MCP documentation only says that unavailable MCP tools require contacting a Microsoft representative, which self-service customers may not have. Consider Azure Support categories, or a working portal form, for each restricted capability.
* **Confirm whether Browse is available by default.** No documentation lists Browse as restricted, and the Microsoft Learn quickstart calls it directly, but I came away from the portal believing it needed special access. If Browse is restricted, say so in the quickstart along with the expected error; if not, make sure the portal doesn't suggest otherwise.
* **Show disabled capabilities in context.** When a playground feature or MCP tool is unavailable, explain why and link directly to the request process.

## Quotas and rate limits

* **Surface the quota-increase path in the portal.** The portal displayed limits of 15 queries per second and 900 queries per minute, but I could not find how to increase them there. Microsoft Learn says to contact Web IQ Support with expected traffic and use case; link that directly from the quota display.
* **Explain how limits relate.** The portal showed both 15 QPS and 900 QPM. The FAQ only describes the 15 QPS default. Also document the daily cap that produces `AuthUserDailyUsageExceeded`.
* **Set expectations for increases.** Document typical approval criteria, response times, and whether limits can differ by API.

## SDK discoverability

* **Feature the official SDKs in the quickstarts.** The Python and TypeScript SDKs exist as `webiq` on PyPI and `@microsoft/webiq` on npm, but both quickstarts use raw HTTP, and the playground generates plain HTTP code. I said in the session that no SDK existed because I could not find one.
* **Link package pages to source and docs.** Neither package lists a repository, homepage, or documentation URL. Add project URLs and publish a public repository or release notes so developers can trust and evaluate them.
* **Link the SDKs from the Web IQ portal documentation.** The SDKs are currently easy to miss under Microsoft Learn integrations.
* **Use the Python package name prominently.** Developers may search for `microsoft-webiq` or `azure-ai-webiq`; the actual package name is simply `webiq`.

## Response fields

* **Explain `instrumentationSuffix` where it appears.** I saw it in playground results and did not know what it was for. The instrumentation guide explains that it supports LLM citation and user-click logging, but the playground and API reference should link directly to that guide.
* **Clarify when instrumentation fields appear.** Explain whether these fields are expected in a default account, whether instrumentation is enabled by default, and how customers can enable or disable it.

## MCP and agent experience

* **Help agents choose Web IQ over built-in web search.** GitHub Copilot already has web search, so I had to explicitly say "use Web IQ" to make it call the MCP server. Guidance for agent instructions, tool descriptions, or skills that make Web IQ the preferred grounding source would help.
* **Document restricted MCP tools.** If a tool is hidden because the account lacks access, document the hidden tools and how to request them.

## Competitive positioning

An attendee asked how Web IQ compares with Jina.ai for an automated pipeline that gets fresh web data.

* Jina.ai Reader maps most closely to Web IQ Browse, but it wasn't clear whether Browse is available by default.
* Web IQ does not generate summaries; it returns relevant passages. A short comparison of search, passage retrieval, browse, and summarization would help developers choose the right API.
* Clarify how Browse live crawls handle CAPTCHAs and anti-bot protections. Search results come from indexed data, but Browse's `liveCrawl: "force"` and `"fallback"` modes fetch pages on demand. The docs describe the failure signals (`liveCrawlSucceeded: false` for stale content, 403 for blocked URLs, 430 for too many crawls) but not whether protected pages can be crawled or what developers should expect.

## Questions answered by documentation

These are no longer open questions, but making the answers easier to find would help:

* Quota increases: contact [Web IQ Support](https://aka.ms/microsoft-webiq-support) with expected traffic and use case.
* Full-page content: request the **Full-page content** category through Web IQ Support.
* `instrumentationSuffix`: see the [instrumentation guide](https://learn.microsoft.com/web-iq/guides/instrumentation).
* SDKs: see [Use the Microsoft Web IQ SDKs for Python and TypeScript](https://learn.microsoft.com/web-iq/integrations/sdk).
