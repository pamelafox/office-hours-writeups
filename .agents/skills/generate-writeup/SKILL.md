---
name: generate-writeup
description: "Generate a structured Q&A write-up from a weekly Python + AI Office Hours recording. Use when asked to create an office-hours write-up, extract questions and answers, or process a recording for a specific date."
argument-hint: "Office-hours date (YYYY-MM-DD) and, if needed, the YouTube URL"
---

# Generate Office Hours Write-up

Create an easy-to-read, searchable Q&A write-up for a weekly Python + AI Office Hours recording.

## Inputs

- The office-hours date, normally supplied as `YYYY-MM-DD`
- The YouTube URL, either supplied by the user or available in that date's existing files

If the date is not explicit, infer it only when the target date is unambiguous from the current context or existing office-hours directory. Otherwise, ask for it.

## Procedure

1. Use the `youtube-transcript` skill to fetch the recording transcript with timestamps. Save the unmodified result as `office-hours/YYYY_MM_DD/transcript.md`.
2. Use the `youtube-live-chat` skill to fetch the live chat. Save it as `office-hours/YYYY_MM_DD/live_chat.md`. If YouTube has no chat replay, check `raw.md` for pasted Discord chat and use that as supplemental context.
3. Read the transcript and chat, identify the main questions and answers, and distinguish follow-up questions from new topics.
4. Write `office-hours/YYYY_MM_DD/questions_answers.md` using the format below.
5. Check that every heading has the correct timestamp link and that factual claims and shared links are grounded in the transcript or chat.

## Output Rules

- Begin with a descriptive title such as `# July 21, 2026 Office Hours Q&A`.
- Use `##` headings for main questions and `###` headings for follow-up questions.
- Put a linked video timestamp immediately below every question or follow-up heading.
- Summarize answers clearly rather than reproducing the transcript verbatim.
- Add inline links to natural words or phrases in the answer text.
- Add a `Links shared:` list only for links that do not have an obvious inline anchor.
- Do not include upcoming events as a write-up section.
- Put announcements that do not answer a user question in a final `## Announcements` section.
- Preserve meaningful caveats, uncertainty, and distinctions from the spoken answer.

## Format

```markdown
# Month D, YYYY Office Hours Q&A

## Question 1?

📹 [12:34](https://youtube.com/watch?v=VIDEO_ID&t=754)

Answer to question 1 with a natural [inline link](https://example.com).

Links shared:

* [Link without a natural inline anchor](https://example.com)

### Follow-up question 1a?

📹 [15:20](https://youtube.com/watch?v=VIDEO_ID&t=920)

Answer to the follow-up question.

## Question 2?

📹 [18:45](https://youtube.com/watch?v=VIDEO_ID&t=1125)

Answer to question 2.
```