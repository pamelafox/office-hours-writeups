---
name: generate-linkedin-news
description: "Generate a LinkedIn news post and matching headline image for the news discussed at a weekly Python + AI Office Hours session. Use when asked for a LinkedIn news roundup, linkedin_news_post.md, a news screenshot for LinkedIn, or office-hours-news-linkedin.png."
argument-hint: "Office-hours date (YYYY-MM-DD), or use the current session context"
---

# Generate LinkedIn News Post and Image

After office hours, create two artifacts in `office-hours/YYYY_MM_DD/`:

1. `linkedin_news_post.md`: the news links discussed that week, grouped by topic.
2. `office-hours-news-linkedin.png`: a headline-only image of the same groups, built from `office-hours-news-linkedin.html`.

## Inputs

- `office-hours-news.html` (or the slide content in `raw.md`): the roundup prepared before the session.
- The Discord chat in `raw.md` or `live_chat.md`: news links shared during the session, such as same-day launches.
- The YouTube recording URL from `raw.md`.

Leave out the "What I've Been Up To" items and upcoming events. They are Pamela's own work, not news.

## Procedure

### 1. Draft the post

Write `linkedin_news_post.md` using the format below.

- Group links into 5–7 logical topics, such as Frontier labs, Microsoft Foundry, GitHub Copilot, Python packages, AI safety, and AI engineering practices. Choose groups that fit the week's news.
- Put the biggest news first. Same-day model launches go at the top of their group.
- Add important news links shared in chat, including the official announcement from the lab that made the launch.
- Use full URLs. LinkedIn shortens them when posting.
- Use 🎥 for the recording line. 📹 can get corrupted in the file.

### 2. Wait for Pamela's edits

Pamela usually rewrites the intro and removes some links. Before building the image, re-read `linkedin_news_post.md` and use only the groups and links that remain.

### 3. Build the image page

Copy [template.html](./template.html) to `office-hours/YYYY_MM_DD/office-hours-news-linkedin.html` and fill it in:

- Replace `{{DATE_RANGE}}` with the roundup range, such as `Sept 15–22`. Keep the heading exactly `🐍 Python + AI Weekly News: <range>`, with no subheading, date badge, or footer.
- Add one `<article>` per group, in the same order as the post, and give each group a different color class.
- Include headlines only. Links cannot be clicked in an image.
- Combine closely related items into one headline. For example, "Foundry agents gain routines" and "Foundry hosted agents add egress controls" become "Foundry agents gain routines and egress controls."
- Update each group's `N items` count after combining items.
- Keep every headline and column header to one line. Shorten long headlines, for example "Copilot runtime ported to Rust, using Copilot" instead of "GitHub ported the Copilot runtime to Rust, using Copilot."
- Six groups fit the 3×2 grid best. With a different number of groups, change `grid-template-columns` so rows stay balanced.

### 4. Screenshot and verify

```bash
uv run .agents/skills/generate-linkedin-news/screenshot.py \
  office-hours/YYYY_MM_DD/office-hours-news-linkedin.html \
  office-hours/YYYY_MM_DD/office-hours-news-linkedin.png
```

The script renders a 1600px-wide viewport at 2x, waits for the Sora web font to load, and crops the image to the page content. It exits with an error and lists any heading or headline that wraps. Shorten those items and re-run it until it passes.

View the PNG to confirm that boxes in each row line up and the snake emoji renders as a black silhouette.

## Post Format

```text
<Short intro line about the week's news>
Here's the news we discussed in my weekly office hours-

🔬 Frontier labs:

"Headline"
https://example.com/full-url

☁️ Microsoft Foundry:

"Headline"
https://example.com/full-url

🎥 Watch this week's office hours where we discussed the news:
https://www.youtube.com/watch?v=VIDEO_ID

💬 See the write-ups and recordings all my weekly office hours:
https://aka.ms/pythonai/oh/links
```

End with the recording link and `https://aka.ms/pythonai/oh/links`. Do not use `http://aka.ms/pythonai/oh`.

## Style Decisions

The template encodes choices Pamela made after comparing many variants. Keep them unless she asks otherwise:

- Heading: Sora 600 from Google Fonts at 4rem. She found the system fonts she compared too blocky.
- Snake emoji rendered as a black silhouette.
- Light dotted background, white cards, and column headers filled with the group color.
- Font sizes are close to the largest that fit on one line at 1600px: heading 4rem, column headers 1.9rem, headlines 1.15rem.
