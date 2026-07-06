---
name: research
description: Research company-specific interview problems from Glassdoor, LeetCode Forums, Hello Interview, LeetCode problem sets, and Blind. Every finding must have a source URL. Defaults to last 3 months.
---

# Company Interview Research

Research what coding problems a company asked recently across 5 sources. **Every claim must have a source URL attached — no URL, no inclusion.**

## Arguments

Parse `$ARGUMENTS` for:
- **`<company>`** (positional, required) — company name to research
- **`--source <name>`** — run only one source: `glassdoor`, `leetcode-forums`, `hello-interview`, `leetcode-problems`, `blind`
- **`--months <n>`** — lookback window in months (default: 3)

---

## Source Reference Files

Before fetching, read the relevant source file(s) in `sources/`:
- `sources/glassdoor.md`
- `sources/leetcode-forums.md`
- `sources/hello-interview.md`
- `sources/leetcode-problems.md`
- `sources/blind.md`

Each file contains: the search URL pattern, curl command for auth tokens (if required), the exact API query or fetch strategy, and how to parse the response.

---

## Credentials

Some sources (Glassdoor, LeetCode, Blind, Hello Interview) work better or only with an authenticated session. **Never ask the user to paste a session cookie, auth token, or curl command into chat** — it's a live credential and gets permanently exposed the moment it lands in a message.

Instead, each source reads its cookie from a fixed local file:

| Source | File |
|---|---|
| Glassdoor | `~/.config/interview-research/cookies/glassdoor.txt` |
| LeetCode (Forums + Problems) | `~/.config/interview-research/cookies/leetcode.txt` |
| Hello Interview | `~/.config/interview-research/cookies/hellointerview.txt` |
| Blind | `~/.config/interview-research/cookies/blind.txt` |

Each file holds just the Cookie header value (everything after `Cookie:` in a captured browser request) on one line. If a file exists and is non-empty, Read it directly and use its contents — don't echo it back to the user. If it's missing or empty, tell the user how to populate it themselves (see each source's `Step 0`/auth section in `sources/*.md`) and wait — don't proceed with a stale or missing cookie, and don't accept the value through chat as a substitute.

These are session cookies, not long-lived API keys — Cloudflare clearance tokens expire in hours, LeetCode sessions in ~2 weeks. When a previously-working source starts hitting login walls again, tell the user which file to refresh.

---

## Phase 1: Setup

1. Parse company name from args. Derive a URL-safe slug: lowercase, spaces → hyphens (e.g. "Meta" → "meta", "Jane Street" → "jane-street").
2. Calculate the cutoff date: today minus `--months` (default 3). Use this to filter all results.
3. If `--source` is provided, skip to Phase 2 for that source only. Otherwise run all 5 in sequence.

---

## Phase 2: Fetch Each Source

For each source, follow the instructions in the corresponding `sources/*.md` file exactly.

**Execution order** (go in this order to try public access before requiring auth):
1. LeetCode Problems (partially public)
2. LeetCode Forums (partially public)
3. Hello Interview (partially public)
4. Blind (partially public)
5. Glassdoor (auth token required)

**For sources requiring auth tokens:**
If the user has not yet provided a token, output the instructions from the source file (what to open in browser, what to copy, what curl to run), then pause and ask the user to paste the token or curl output back. Do not skip — mention that results for that source will be added once the token is provided.

**WebSearch fallback:** If WebFetch of a direct API returns an error or a login wall, fall back to:
```
WebSearch: site:<domain> "<company>" interview questions coding 2026
```
Then WebFetch the top 3–5 result URLs to extract problems.

---

## Phase 3: Aggregate and Deduplicate

After fetching all sources:
1. Collect all problems with their source URLs and reported dates.
2. Group by problem title (case-insensitive). If the same problem appears across multiple sources, merge into one entry and list all source URLs.
3. Drop any problem with no source URL.
4. Sort by most recently reported first.
5. Flag entries older than the cutoff with ⚠.

---

## Phase 4: Output

```
=================================================================
RESEARCH: <Company> · Last <N> Months  (cutoff: <date>)
=================================================================

SOURCE: LeetCode Problems
──────────────────────────────────────────────────────────────
• Two Sum [Easy]
  Pattern: hash-map
  Source: https://leetcode.com/problems/two-sum/ (company tag)
  Frequency: high (last 3 months)

• Median of Two Sorted Arrays [Hard]
  Pattern: binary-search
  Source: https://leetcode.com/problems/median-of-two-sorted-arrays/ (company tag)

SOURCE: LeetCode Forums
──────────────────────────────────────────────────────────────
• "SWE Intern <Company> — May 2026 — Phone Screen"
  Problems mentioned: Two Sum, Valid Parentheses
  Source: https://leetcode.com/discuss/interview-experience/...
  Reported: 2026-05-15

SOURCE: Glassdoor
──────────────────────────────────────────────────────────────
• Coding: reverse a linked list, given a list of intervals merge overlapping ones
  Source: https://www.glassdoor.com/Interview/...
  Reported: 2026-04-20

SOURCE: Hello Interview
──────────────────────────────────────────────────────────────
• (content found or "No public content found for <company>")

SOURCE: Blind
──────────────────────────────────────────────────────────────
• Thread: "<Company> SDE interview loop 2026"
  Problems mentioned: LRU Cache, System Design: URL Shortener
  Source: https://www.teamblind.com/post/...
  Reported: 2026-06-01

=================================================================
CONSOLIDATED PROBLEM LIST  (<N> unique problems, last <N> months)
=================================================================
Problem                         Pattern           Sources
──────────────────────────────────────────────────────────────
Two Sum                         hash-map          LC Problems, LC Forums
Valid Parentheses               stack             LC Forums
LRU Cache                       design            Blind
...
=================================================================
Top patterns this company tests: <pattern-1>, <pattern-2>, <pattern-3>
=================================================================
```

---

## Rules

- **No source URL = problem is excluded.** Never include a finding you cannot cite.
- If a source returns no results, write: `No results found for <company> in the last <N> months.`
- If a source requires auth and the user has not provided a token, write: `[Awaiting token — see instructions above]`
- Dates must be explicit (YYYY-MM-DD). If only month/year is available, note it as approximate.
- Do not hallucinate problem names. Only include problems explicitly mentioned in the fetched content.
- For Blind and Glassdoor, quote the original text and extract problem names from it — do not paraphrase into a generic LeetCode title unless the match is unambiguous.
