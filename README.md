# Python + AI Office Hours

This repo supports two parts of the weekly Python + AI Office Hours workflow using GitHub Copilot and [agent skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills): preparing the news roundup before office hours, then generating and publishing the recording-based write-up afterward. Agent-facing instructions are in [AGENTS.md](AGENTS.md).

[📺 See a video recording of this repo in action](https://youtube.com/live/l_sdnLWNwUc)

## User workflow

### Before office hours

1. Add a folder under `office-hours/` for the week's session, named with the date in `YYYY_MM_DD` format.
2. Run the [`/generate-weekly-news-roundup`](.agents/skills/generate-weekly-news-roundup/SKILL.md) skill to generate the weekly news roundup webpage.
3. Review the roundup for accuracy, attribution, working links, and upcoming events before presenting it.

### After office hours

1. Add `raw.md` to the week's folder with the YouTube recording URL and any supplemental resources, such as pasted Discord chat logs or weekly slide content.
2. Run the [`/generate-writeup`](.agents/skills/generate-writeup/SKILL.md) skill, then review `questions_answers.md` for accuracy and formatting.
3. Run the [`/post-comments`](.agents/skills/post-comments/SKILL.md) skill to publish each Q&A to the GitHub Discussion and create `comments.md`.
4. Run the [`/generate-youtube-description`](.agents/skills/generate-youtube-description/SKILL.md) skill to create `youtube_description.md` with chapter timestamps.
5. Run the [`/generate-linkedin-post`](.agents/skills/generate-linkedin-post/SKILL.md) skill to create `linkedin_post.md`.

Each completed week should have a structure like this:

```text
office-hours/
  YYYY_MM_DD/
    office-hours-news.html       # Pre-event browser roundup
    raw.md                       # Recording URL and supplemental resources
    transcript.md                # Timestamped recording transcript
    live_chat.md                 # YouTube live chat, when available
    questions_answers.md         # Q&A write-up with timestamps
    comments.md                  # GitHub Discussion comment links
    youtube_description.md       # YouTube description and chapters
    linkedin_post.md             # LinkedIn recap
```

## Resources

- [Weekly office hours recordings & Q&A](https://aka.ms/pythonai/oh/links)
- [Weekly live office hours](https://aka.ms/pythonai/oh)
