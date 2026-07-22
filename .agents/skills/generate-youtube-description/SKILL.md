---
name: generate-youtube-description
description: "Generate a YouTube description for a weekly Python + AI Office Hours recording from its Q&A write-up. Use when asked for video copy, chapter timestamps, or youtube_description.md for a specific office-hours date."
argument-hint: "Office-hours date (YYYY-MM-DD)"
---

# Generate YouTube Description

Create `office-hours/YYYY_MM_DD/youtube_description.md` from that date's `questions_answers.md`.

## Procedure

1. Read `office-hours/YYYY_MM_DD/questions_answers.md`.
2. Extract the title date, every question or announcement title, and its video timestamp.
3. Preserve chronological recording order, including announcements or demos that have timestamps.
4. Write the description using the template below.
5. Verify that every timestamp matches the Q&A write-up and appears at the beginning of its line so YouTube will auto-link it.

## Output Rules

- Start with a brief intro line naming the weekly office hours and date.
- Include the standard live office-hours URL and write-up URL shown below.
- Add a `Timestamps:` section with `0:00 Intro` first, followed by each timestamped topic.
- Use plain `M:SS` or `H:MM:SS` timestamps, not Markdown links.
- Do not include the `📹` emoji.
- Keep chapter titles concise while preserving the meaning of each question.

## Template

```text
Weekly Python + AI office hours - January 6, 2026

This is just a recording from the Discord office hours, for those who couldn't attend live.
Join the live weekly OH here: http://aka.ms/pythonai/oh

See a write-up of each weekly office hours here:
https://aka.ms/pythonai/oh/links

Timestamps:
0:00 Intro
5:48 How do you set up Entra OBO flow for Python MCP servers?
20:24 Which MCP inspector should I use for testing servers with Entra authentication?
```