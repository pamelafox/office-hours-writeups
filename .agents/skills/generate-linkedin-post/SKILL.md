---
name: generate-linkedin-post
description: "Generate a LinkedIn post summarizing a weekly Python + AI Office Hours session. Use when asked for social copy, a LinkedIn recap, or linkedin_post.md based on an office-hours Q&A write-up."
argument-hint: "Office-hours date (YYYY-MM-DD), or use the current session context"
---

# Generate LinkedIn Post

Create `office-hours/YYYY_MM_DD/linkedin_post.md` from that date's `questions_answers.md`.

## Procedure

1. Read the target date's Q&A write-up and identify the strongest audience-relevant topics.
2. Summarize each selected topic in one concise emoji-led line.
3. Add a news section when the write-up contains announcements.
4. End with the standard live-event and discussion links, followed by relevant hashtags.
5. Check that claims and links are supported by the Q&A write-up.

## Output Rules

- Open with a short, engaging intro line that includes an emoji.
- Add a `Topics we covered:` section.
- Format each topic as an emoji, a plain-text topic header, a colon, and a concise description.
- Add a `News:` section only when there are announcements worth highlighting.
- Link readers to the discussion/write-up thread, not directly to the YouTube recording.
- Use `https://github.com/orgs/microsoft-foundry/discussions/280` or the repository's standard short link `https://aka.ms/pythonai/oh/links` for the recording and questions.
- Include `Join us live every week: http://aka.ms/pythonai/oh`.
- End with relevant hashtags such as `#Python #AI #GenerativeAI`, adding specific tags only when supported by the topics.
- Do not use Unicode bold characters because they are inaccessible. Use plain text and spacing for structure.
- Keep the post concise enough for LinkedIn and avoid duplicating the full write-up.

## Example

```text
🐍 This week's Python + AI Office Hours was packed with great questions!

Topics we covered:

🎧 Podcast recommendations: A few useful shows for keeping up with Python and AI

📚 The tutorial trap: How to move from watching to building

Join us live every week: http://aka.ms/pythonai/oh

See the recording and questions here:
https://github.com/orgs/microsoft-foundry/discussions/280

#Python #AI #GenerativeAI
```