# Discord office hours write-ups: Instructions for coding agents

The goal of this repo is to turn the recordings of weekly Discord office hours into a text format that is easy to read and search. Each week, we will have a new markdown file in this repo that contains the write-up for that week's office hours.

## Generating the write-up

When generating the write-up, follow these steps:

* Use the youtube-transcript skill to fetch the transcript of the YouTube video for that week's office hours. Make sure to include timestamps.
* Identify the main questions and answers
* Generate a markdown file at "office-hours/YYYY_MM_DD/questions_answers.md" with each question as a header (##) and the corresponding answer below it. If there are follow-up questions, use sub-headers (###) for those. Do not include the "upcoming events" as a section in the write-up.
* Include a timestamp link below each heading, linking to that point in the YouTube video.

For example:

## Question 1?

📹 [12:34](https://youtube.com/watch?v=VIDEO_ID&t=754)

Answer to question 1.

Links shared:

* [Link 1](https://example.com)

### Follow-up question 1a?

📹 [15:20](https://youtube.com/watch?v=VIDEO_ID&t=920)

Answer to follow-up question 1a.

## Question 2?

📹 [18:45](https://youtube.com/watch?v=VIDEO_ID&t=1125)

Answer to question 2.

## Posting to the Discussions thread

When asked by the user, you can post each Q&A as a comment to the GitHub Discussion thread using the discussion-commenter skill:

```bash
uv run .github/skills/discussion-commenter/post_qas.py \
  "office-hours/YYYY_MM_DD/questions_answers.md" \
  "https://github.com/orgs/microsoft-foundry/discussions/280" \
  "YYYY/MM/DD"
```

Each `##` section becomes a separate comment, prefixed with the date and question title (e.g., "**2026/01/06: How do you set up Entra OBO?**").

## Generating the YouTube description

When asked to generate a YouTube description, create a `youtube_description.md` with:

1. A brief intro line
2. A link to the discussion thread
3. Timestamps for each question (YouTube auto-links timestamps that appear at the start of a line in `MM:SS` or `H:MM:SS` format)

For example:

```text
Weekly Python + AI office hours - January 6, 2026

This is just a recording from the Discord office hours, for those who couldn't attend live.
Join the live weekly OH here: http://aka.ms/aipython/oh

See a write-up of each weekly office hours here:
https://github.com/orgs/microsoft-foundry/discussions/280

Timestamps:
0:00 Intro
5:48 How do you set up Entra OBO flow for Python MCP servers?
20:24 Which MCP inspector should I use for testing servers with Entra authentication?
28:04 How do you track LLM usage tokens and costs?
30:32 How do you keep yourself updated with all the new changes related to AI?
36:30 How do you build a Microsoft Copilot agent in Python?
46:39 How do I learn about AI from scratch as a backend developer?
49:50 What's new with the RAG demo after SharePoint was added?
53:53 Will companies create internal MCP servers?
```

Note: YouTube automatically makes timestamps clickable when they appear at the start of a line. Do not include the `📹` emoji or markdown links in the YouTube description.

## Generating a LinkedIn post

When asked to generate a LinkedIn post, create a summary with:

1. An intro line with emoji
2. A "Topics we covered" section with emoji bullets and Unicode bold headers (LinkedIn doesn't support markdown bold)
3. A news section if there were announcements
4. A link to the discussion thread (not the YouTube recording directly)
5. Relevant hashtags

Use Unicode bold characters (𝗮𝗯𝗰𝗱𝗲𝗳𝗴...) instead of markdown **bold** since LinkedIn doesn't render markdown.

For example:

```text
🐍 This week's Python + AI Office Hours was packed with great questions!

𝗧𝗼𝗽𝗶𝗰𝘀 𝘄𝗲 𝗰𝗼𝘃𝗲𝗿𝗲𝗱:

🎧 𝗣𝗼𝗱𝗰𝗮𝘀𝘁 𝗿𝗲𝗰𝗼𝗺𝗺𝗲𝗻𝗱𝗮𝘁𝗶𝗼𝗻𝘀 for learning AI - description here

📚 𝗧𝗵𝗲 𝘁𝘂𝘁𝗼𝗿𝗶𝗮𝗹 𝘁𝗿𝗮𝗽 - How to move from watching to building

Join us live every week: http://aka.ms/aipython/oh

See the recording and questions here:
https://github.com/orgs/microsoft-foundry/discussions/280

#Python #AI #GenerativeAI
```
