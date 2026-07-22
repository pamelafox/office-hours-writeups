# Python + AI Office Hours: Instructions for coding agents

This repo supports two parts of the weekly Python + AI Office Hours workflow:

1. **Before office hours:** Prepare the weekly news roundup used during the session.
2. **After office hours:** Turn the recording into an easy-to-read, searchable Q&A write-up and related publishing content.

## Before office hours: Generate the weekly news roundup

Use the `generate-weekly-news-roundup` skill when asked to prepare the weekly Python + AI Office Hours news roundup webpage or browser preview. Follow `.agents/skills/generate-weekly-news-roundup/SKILL.md` as the source of truth for gathering and categorizing news from Gmail, WorkIQ/Outlook, Twitter/X, GitHub, and the web.

The skill produces a self-contained HTML webpage with Microsoft/GitHub, Industry, and "What I've Been Up To" columns for a full-screen browser presentation.

Run every required source search, restrict results to the date range specified by the skill, verify links and attribution, and include upcoming events in the "What I've Been Up To" column.

## After office hours: Generate and publish the write-up

Each week has a directory under `office-hours/YYYY_MM_DD/` containing the recording-derived artifacts for that session.

* Use the `generate-writeup` skill to create a structured Q&A write-up from the office hours recording.
* Use the `generate-youtube-description` skill to create a YouTube description and timestamp chapters from the Q&A write-up.
* Use the `generate-linkedin-post` skill to create a LinkedIn recap from the Q&A write-up.
* Use the `post-comments` skill to publish each Q&A to the GitHub Discussion and create `comments.md`.
