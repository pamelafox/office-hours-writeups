---
name: post-comments
description: "Post each Q&A section from a weekly Python + AI Office Hours write-up to the Microsoft Foundry GitHub Discussion and create comments.md with anchor-only comment links. Use when asked to publish or post office-hours Q&A comments."
argument-hint: "Office-hours date (YYYY-MM-DD)"
---

# Post Office Hours Comments

Post each `##` section from `office-hours/YYYY_MM_DD/questions_answers.md` as a separate comment to the Microsoft Foundry GitHub Discussion, then record the resulting comment links.

## Prerequisites

- GitHub CLI (`gh`) is installed and authenticated.
- The authenticated user can comment on the discussion.
- The Q&A write-up is complete and ready to publish.

## Procedure

1. Convert the input date to both directory format (`YYYY_MM_DD`) and comment-prefix format (`YYYY/MM/DD`).
2. Run a dry run and review the parsed section count and content:

   ```bash
   uv run .agents/skills/discussion-commenter/post_qas.py \
     "office-hours/YYYY_MM_DD/questions_answers.md" \
     "https://github.com/orgs/microsoft-foundry/discussions/280" \
     "YYYY/MM/DD" \
     --dry-run
   ```

3. If the dry run is correct, run the same command without `--dry-run`.
4. Capture each posted comment URL from the command output.
5. Create `office-hours/YYYY_MM_DD/comments.md` as a Markdown list using each section title and the URL's fragment only.
6. Verify that the number and order of links match the posted `##` sections.

## Comment Format

Each `##` section becomes a separate discussion comment prefixed with the date and title:

```markdown
**2026/01/06: How do you set up Entra OBO?**

Answer content...
```

Follow-up `###` sections remain inside their parent comment.

## comments.md Format

Comment URLs must be anchor-only, not relative paths or absolute URLs:

```markdown
# Comments posted to discussion

* [How do you set up Entra OBO?](#discussioncomment-12345678)
* [Which MCP inspector should I use?](#discussioncomment-12345679)
```

Do not repost comments if publishing partially succeeds. Record the successful URLs and resolve the remaining sections individually.