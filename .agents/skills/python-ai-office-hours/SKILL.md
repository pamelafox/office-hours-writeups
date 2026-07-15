---
name: python-ai-office-hours
description: >
  Generate a weekly PPTX slide deck for Python+AI Office Hours.
  Searches Gmail emails, WorkIQ chats, tweets, and GitHub activity from the past 7 days,
  categorizes news into Microsoft/GitHub vs Industry vs My Work, and produces
  a single-slide widescreen presentation with color-coded columns.
  Can also generate a full-screen HTML webpage version for browser preview.
allowed-tools:
  - shell
---

# Python + AI Office Hours — Weekly Slide Generator

You are helping **Pamela Fox** prepare her weekly **Python + AI Office Hours**.
Your job is to gather the past week's news, categorize it, and generate a
single-slide PPTX summarizing everything.

## Step 1 — Gather news from the past 7 days

Run **all four** data sources in parallel:

### 1a. Gmail (recent emails)
- Use the Gmail MCP server to find recent emails from the past 7 days.
- Run **all of the following searches** and read each matching thread in full
  (not just the snippet — use `gmail-get_thread` or equivalent to retrieve the
  complete body before extracting items):

  | Search query | Why |
  |---|---|
  | `from:noreply@email.openai.com after:YYYY/MM/DD` | OpenAI product updates (Codex, ChatGPT, API changes) |
  | `from:"Pragmatic Engineer" after:YYYY/MM/DD` | The Pulse + deep-dives on AI/dev trends |
  | `from:"Global AI Community" after:YYYY/MM/DD` | Global AI Weekly newsletter |
  | `from:hq@globalai.community after:YYYY/MM/DD` | Global AI Weekly (alternate sender address) |
  | `from:newsletter@humanwhocodes.com after:YYYY/MM/DD` | Human Who Codes AI developer newsletter |
  | `(AI OR Python OR OpenAI OR "Azure OpenAI" OR LLM OR GPT OR Copilot OR MCP OR Foundry) after:YYYY/MM/DD` | Catch-all for other relevant newsletters |

- For **every** matching email: fetch the full thread body, not just the subject/snippet.
  Extract all announcements, releases, migration notices, and noteworthy items.
- **Global AI Weekly special handling:** This newsletter is HTML-only (the
  plaintext body just says "your email can't display HTML"). After fetching the
  thread with `gmail-get_thread`, look for the **webview URL** in the plaintext
  body (format: `https://link.globalai.community/emails/webview/NNNNNN/NNNNNNNN`).
  Then use `web_fetch` on that URL to get the rendered newsletter content with
  all headlines, summaries, and links. You may need to paginate `web_fetch` with
  `start_index` to get the full issue.
- Search for announcements, migration notices, new releases, blog posts, and
  other noteworthy emails relevant to Python/AI work.

### 1b. WorkIQ (emails & chats)
- Search for items mentioning: Python, AI, OpenAI, Azure OpenAI, LLM, GPT,
  Copilot, developer tools, MCP, agent framework, Foundry, Responses API.
- **Source routing:** VS Code Insiders and Linux Foundation newsletters are in
  Pamela's Outlook account. Query them through WorkIQ, not Gmail.
- Explicitly query WorkIQ/email context for:
  - `subject:"VS Code Insiders Update"` (Outlook)
  - `from:"The Linux Foundation"` (Outlook)
  - `"News you might have missed"`
  - `from:pytorchevents@linuxfoundation.org` (Outlook)
  - `from:noreply@email.openai.com` (OpenAI product updates in Outlook)
  - `from:github-copilot-insiders@microsoft.com` (GitHub Copilot insiders updates in Outlook)
  - `to:developertools-mvp-nda@mstechdiscussions.com` (Developer Tools MVP NDA emails in Outlook)
- Look for announcements, migration notices, new releases, blog posts, and
  notable discussions.

### 1c. Twitter / X

#### Distinguishing Pamela's tweets from her home timeline

The `getUsersTimeline` API returns the **home timeline** (tweets from everyone
Pamela follows), NOT just her own tweets. **Do NOT assume every tweet returned
is written by Pamela.** To get only Pamela's own tweets, you MUST either:

1. **Preferred:** Use a Twitter search query scoped to her account:
   `from:pamelafox` with `start_time` / `end_time` filtering. This guarantees
   only her authored tweets are returned.
2. **Alternative:** If using `getUsersTimeline`, request `author_id` in
   `tweet.fields` and filter results to keep only tweets where
   `author_id == "10483202"`. Discard all others — they are from accounts
   she follows.

**CRITICAL for the "What I've Been Up To" column:** Only attribute activities,
blog posts, conference attendance, talks, and demos to Pamela if the tweet is
**authored by her** (verified via `author_id` or `from:pamelafox` search).
Tweets from other people on her timeline are news sources for the Microsoft/GitHub
or Industry columns — never for the "My Work" column.

#### Pagination — home timeline fills up fast

The `getUsersTimeline` API returns the home timeline (hundreds of tweets/day
from all followed accounts), so a single `max_results: 100` call with a 7-day
window will typically only cover the most recent day or two.

**If using `getUsersTimeline`, you MUST paginate** using the `next_token`
returned in each response, or make day-by-day calls with narrowing
`end_time` values, until you've covered the full 7-day window.

**Preferred approach:** Use a `from:pamelafox` Twitter search instead — this
returns only Pamela's own tweets and is far less likely to need pagination.

#### Fetching steps

- Fetch Pamela's own recent tweets (username: **pamelafox**, user ID: **10483202**)
  for the past 7 days. Use `from:pamelafox` search with `start_time` filtering,
  or `getUsersTimeline` with `author_id` filtering (see above).
  **Paginate day-by-day or via next_token to cover all 7 days.**
- Fetch her liked tweets (up to 100) for links, articles, and notable takes.
  **Important:** The liked-tweets API does NOT support `start_time` filtering —
  it returns recent likes regardless of when the tweet was posted. After fetching,
  you MUST check each liked tweet's `created_at` and discard any posted before
  the 7-day window. Use `getPostsByIds` with `tweet.fields: ["created_at"]` to
  verify dates in bulk.
- For any tweets found via search, also apply `start_time` to the search query
  and verify `created_at` on returned results.
- Extract links, article titles, author names, and key topics.

### 1d. GitHub
- Check `gh api /users/pamelafox/events` for recent PRs, commits, and releases.
- If that fails, search recent activity via `gh api /search/issues?q=author:pamelafox+created:>YYYY-MM-DD`.

### 1e. GitHub Changelog
- Fetch the GitHub Changelog RSS feed at `https://github.blog/changelog/feed/`.
  This is the source of truth for GitHub product releases; do not search Gmail
  for GitHub release announcements.
- Parse every feed item published during the past 7 days. Keep the title,
  publication date, categories, canonical `<link>`, and relevant details from
  `content:encoded`.
- Prioritize releases relevant to Python/AI developers, including Copilot,
  agentic development, CodeQL AI security, MCP, APIs, Actions, and developer
  tooling. Drop unrelated account-management and UI-only updates.
- Link bullets to the canonical changelog post, not the RSS feed URL.

### 1f. GitHub Blog
- Fetch the main GitHub Blog RSS feed at `https://github.blog/feed/`.
  This feed contains engineering deep dives, architecture posts, tutorials, and
  product stories that are not necessarily included in the Changelog feed.
- Parse every feed item published during the past 7 days. Keep the title,
  publication date, author, categories, canonical `<link>`, description, and
  relevant details from `content:encoded`.
- Prioritize posts about Copilot, agentic workflows, AI/ML, LLMs, developer
  tools, Python, APIs, architecture, and security. Drop company news and
  operational reports unless directly relevant to developers.
- Link bullets to the canonical blog post, not the RSS feed URL.

### 1g. Pamela's talks page
- Fetch `https://pamelafox.org/talks` to verify talk titles, dates, and URLs.
  Use this as the source of truth for any conference talks attributed to Pamela
  in the "What I've Been Up To" column — do NOT rely on tweet text alone, as
  the home timeline may contain other speakers' talks from the same conference.

### 1h. Upcoming Events
- Fetch Pamela's GitHub profile page at `https://github.com/pamelafox` and look
  for upcoming events listed there (conference talks, livestreams, meetups, etc.).
- Treat events listed on `github.com/pamelafox` as a required source of truth:
  include all relevant future professional events found there unless clearly canceled
  or outside the intended audience.
- Also check WorkIQ and Twitter results for any event announcements.
- Include these in an "📅 Upcoming Events" subsection inside the "What I've Been
  Up To" column (not as a standalone section). Render events as a table with
  columns: Date | Event | Location.

## Step 2 — Categorize items

Sort every newsworthy item into exactly one of three buckets:

| Column | Color | What goes here |
|--------|-------|----------------|
| 🏢 Microsoft / GitHub | Purple `#6F2DA8` | News from Microsoft, Azure, GitHub, Copilot, VS Code, MS Research |
| 🌐 Industry | Green `#1A7F37` | Open-source tools, conferences, research papers, talks from non-MS sources |
| 👩‍💻 What I've Been Up To | Blue `#0D6EFD` | Pamela's own blog posts, PRs, livestreams, conference talks, samples |

**Guidelines:**
- Aim for 5–8 items per column (max ~11 in Industry if it's a busy week).
- Each item should be one concise bullet (≤ 60 chars ideally) plus a URL.
- **Every bullet MUST have a link.** Use `web_search` to find an authoritative
  URL (blog post, repo, docs page, announcement) for each item. Do not leave
  any bullet without a link unless no relevant URL exists after searching.
- In the PPT, links must be real clickable hyperlinks (not plain text only).
  Use the slide generator so each URL run has a hyperlink target set.
- Drop items that aren't relevant to a Python/AI developer audience.
- Drop purely personal/social content — keep it professional and technical.

## Step 3 — Generate the PPTX

Use the template script at `.agents/skills/python-ai-office-hours/generate_slides_template.py`
as a starting point. Copy it to a working file (e.g., `generate_slides.py`) and:

1. **Set the date** — replace the placeholder date with the current Monday's date
   (format: `Month Day, Year`, e.g., `April 7, 2026`).
2. **Fill in content** — replace the example bullets in each column with the
   categorized items from Step 2. Use the `bullet(tf, "text", "optional-url")` helper.
3. **Adjust column counts** — if one column has significantly more items, you can
   tweak font sizes slightly (±1pt) or add/remove spacer lines, but keep the
   overall layout consistent.

### Running the script

```bash
# Ensure python-pptx is installed
pip install python-pptx

# Generate the presentation
python generate_slides.py
```

The output file will be named `office-hours-YYYY-MM-DD.pptx`.

## Slide format rules (do not change)

- **Single slide** — everything fits on one widescreen (16:9) slide
- **Light mode** — white background (`#FFFFFF`)
- **Three columns** — left (MS/GitHub), middle (Industry), right (My Work)
- **Color-coded section headers** — purple, green, blue respectively
- **Font sizes**: title 22pt, section headers 16pt, bullets 13pt, links 10pt
- **Title format**: `🐍 Python + AI Office Hours — Weekly News Roundup — {date}`

## Step 3b — Generate an HTML webpage (alternative/additional output)

Instead of (or in addition to) the PPTX, generate a full-screen HTML webpage.
Each week's output goes in a date-named folder: `YYYY-MM-DD/office-hours-news.html`
(e.g., `2026-06-23/office-hours-news.html`). This is the **preferred output format**
when the user asks for a "webpage" or wants to preview in a browser.

### HTML structure

Use a self-contained single HTML file with:
- **Three-column responsive grid** (CSS Grid, `grid-template-columns: repeat(3, 1fr)`)
- **Column cards** with headers: 🏢 Microsoft / GitHub (purple `#6F2DA8`),
  🌐 Industry (green `#1A7F37`), 👩‍💻 What I've Been Up To (blue `#0D6EFD`)
- **Each item** is a card with the news text + a clickable hyperlink underneath
- **Upcoming Events** — a table (Date | Event | Location) inside the My Work column,
  separated by a border-top divider
- **Title**: `🐍 Python + AI Office Hours` with subtitle `Weekly News Roundup — {date}`
- **Footer** with the date range covered

### Theme requirements

Use the **Clawpilot theme** (invoke the `web-artifacts-builder` skill for the
exact CSS variables). Key requirements:
- Include the theme detection `<script>` that reads `?clawpilotTheme=` param or
  `prefers-color-scheme`
- All CSS variables must use `var(--cp-*)` tokens
- Font: `"Segoe UI", Aptos, Calibri, -apple-system, BlinkMacSystemFont, sans-serif`
- Cards: `border-radius: 16px`, subtle shadow, hover animation

### Previewing the webpage

After saving the HTML file, serve it and open it in a browser canvas:

```bash
# Start a DETACHED http server (must use mode="async", detach=true)
cd /Users/pamelafox && python3 -m http.server 8765
# Use: mode="async", detach=true, shellId="http-server"
```

Then open the browser canvas:
```
open_canvas(
  title="Office Hours News",
  type="browser",
  url="http://localhost:8765/python-ai-office-hours/YYYY-MM-DD/office-hours-news.html"
)
```

**IMPORTANT**: The HTTP server MUST be started with `detach: true` in async mode,
otherwise it will die when the bash session ends and the browser canvas will show
a blank page. Always verify the server is responding with a quick `curl` before
opening the canvas.

## Important notes

- The WorkIQ API can be flaky — if the first query fails, retry with a slightly
  different phrasing.
- Twitter liked tweets can produce large output — save to a temp file and parse.
- If GitHub events API fails, fall back to searching issues/PRs.
- **Gmail emails**: always fetch the full thread body — snippets alone will miss
  most of the content. If `gmail-get_thread` returns an error, try fetching the
  public web version of the newsletter (e.g. `globalai.community/weekly/NNN/`,
  or search `site:newsletter.pragmaticengineer.com` for the issue title).
- Always verify the generated PPTX exists and report the file path to the user.
- For the HTML webpage, always verify the server is running before opening the
  browser canvas. Use `curl -s http://localhost:8765/... | wc -l` to confirm.

## Step 4 — Output summary tables

After generating the slide/webpage, output two markdown tables in your response:

### Data Sources Summary

| Source | Status | Notes |
|--------|--------|-------|
| Gmail — Global AI Weekly | ✅ Success | Fetched via webview URL |
| Gmail — OpenAI updates | ✅ Success | 2 threads found |
| Gmail — Pragmatic Engineer | ⚠️ No results | No matching emails this week |
| WorkIQ | ✅ Success | 12 items extracted |
| Twitter — own tweets | ✅ Success | `from:pamelafox`, 8 tweets |
| Twitter — liked tweets | ✅ Success | 47 likes, 6 in date range |
| GitHub events | ✅ Success | 3 repos with activity |
| GitHub Changelog RSS | ✅ Success | 10 posts, 4 relevant |
| GitHub Blog RSS | ✅ Success | 5 posts, 2 relevant |
| pamelafox.org/talks | ✅ Success | Verified talk titles |
| github.com/pamelafox | ❌ Error | Rate limited / blocked |

List every source queried. Use ✅ for success, ⚠️ for no results, ❌ for errors.
Include a brief note (e.g., error message, number of items found, reason for no results).

### Sections Summary

| Section | Items |
|---------|-------|
| 🏢 Microsoft / GitHub | 8 |
| 🌐 Industry | 9 |
| 👩‍💻 What I've Been Up To | 3 |
| 📅 Upcoming Events | 2 |

This helps Pamela quickly verify coverage and spot any data-source failures.
