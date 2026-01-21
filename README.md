# Discord Office Hours write-ups

This repo turns recordings of weekly Discord office hours into structured Q&A write-ups, using VS Code GitHub Copilot and [custom skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills). The user-facing instructions are below, and he agent-facing instructions are in [AGENTS.md](AGENTS.md).

## User workflow

1. Add a new folder under `office-hours/` for each week's office hours, named with the date in `YYYY_MM_DD` format. Add `raw.md` with raw resources: typically that's the YouTube recording links, Discord pasted chat logs, and weekly slide content.

2. Ask GitHub Copilot to generate the structured Q&A write-up:

    ```text
    Generate a markdown write-up of the weekly Python + AI office hours held on DATE.
    ```

3. Review the generated `questions_answers.md` for accuracy and formatting.

4. Ask GitHub Copilot to post each Q&A as a comment to the GitHub Discussion thread using the `discussion-commenter` skill:

    ```text
    Post each Q&A from the write-up as a comment to the GitHub Discussion thread,
    and create a markdown list of the comment URLs in `comment_url.md`.
    Comment URLs should be relative, not absolute.
    ```

    That will use the GitHub CLI, authenticated as you, to post each question and answer as a separate comment in the discussion thread.

5. Ask GitHub Copilot to generate a YouTube-friendly description:

    ```text
    Generate a YouTube description for the weekly Python + AI office hours held on DATE, based off the Q&A write-up.
    ```

    That will generate `youtube_description.md` with timestamps and links, and you can copy-paste that into the YouTube video description.

6. Ask GitHub Copilot to generate a LinkedIn post:

    ```text
    Write a LinkedIn post summarizing this week's topics.
    ```

    LinkedIn doesn't support markdown, so the post will use Unicode bold characters for emphasis. Copy-paste the output directly into LinkedIn.

You should end up with a structure like this:

```text
office-hours/
  YYYY_MM_DD/
    raw.md                 # Raw resources: YouTube links, chat logs, slides
    questions_answers.md   # Q&A write-up with timestamps
    youtube_description.md # Description for YouTube video
```

## Resources

- [Weekly office hours recordings & Q&A](https://github.com/orgs/microsoft-foundry/discussions/280)
- [Weekly live office hours](http://aka.ms/aipython/oh)
