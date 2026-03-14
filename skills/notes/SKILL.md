---
name: notes
description: Record learning notes with tags and spaced repetition reminders. Use to capture concepts, patterns, and insights during practice.
---

# Learning Notes

Record and review learning notes with spaced repetition.

## Arguments

Parse `$ARGUMENTS` for:
- **add [text]**: Add a new note
- **review**: Show notes due for review
- **list [tag]**: List notes, optionally filtered by tag
- **search [query]**: Search notes

## Commands

### Add Note

`/notes add [text]` or just `/notes [text]`

1. Parse the note content
2. Ask for tags (or extract from content): `Tags? (e.g., sliding-window, edge-cases)`
3. Save to `.interview/notes/{date}_{slug}.md`:

```markdown
# [Title or first line]

**Created**: {date}
**Tags**: {tags}
**Next Review**: {tomorrow}

---

{content}

---

## Review History
| Date | Recall | Next |
|------|--------|------|
```

4. Confirm: "Note saved. Tagged: {tags}. Review tomorrow."

### Review

`/notes review`

1. Read all notes from `.interview/notes/`
2. Find notes where `Next Review <= today`
3. For each due note:
   - Show the note content
   - Ask: "How well do you remember this? (1=forgot, 2=hard, 3=good, 4=easy)"
   - Update next review based on spaced repetition:
     - 1 (forgot): tomorrow
     - 2 (hard): +2 days
     - 3 (good): +4 days (or 2x previous interval)
     - 4 (easy): +7 days (or 2.5x previous interval)
   - Add row to Review History table

4. Summary: "Reviewed X notes. Next review due: {date}"

### List

`/notes list [tag]`

1. Read all notes
2. Filter by tag if provided
3. Display:

```
## Your Notes

| Date | Title | Tags | Next Review |
|------|-------|------|-------------|
| 2024-01-15 | Two pointer pattern | sliding-window | Tomorrow |
| 2024-01-14 | Edge case: empty array | edge-cases | In 3 days |
```

### Search

`/notes search [query]`

1. Grep through `.interview/notes/` for query
2. Show matching notes with context

## Auto-Link to Sessions

When saving a note during an active interview session (`.interview/.session.json` exists):
- Auto-add tag for current pattern
- Add link: `**From Session**: {problem_name}`

## Review Reminder

At start of `/interview` or `/study-plan`, check for due reviews:
- If notes due: "You have X notes due for review. Run `/notes review` after this session."

## Guidelines

- Keep notes concise - key insight only
- One concept per note for better recall
- Tags help find related notes later
