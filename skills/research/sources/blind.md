# Source: Blind (TeamBlind)

teamblind.com is a professional forum where engineers share anonymous interview experiences. Most posts are publicly readable without authentication, but Blind frequently gates full post bodies behind a login wall — direct fetches often return only the page shell.

---

## Step 0: Authenticated Access (optional, unlocks gated posts)

**Never ask the user to paste a session cookie into chat.** Check for a locally-stored cookie file first:

```
~/.config/interview-research/cookies/blind.txt
```

This file should contain the Cookie header value on one line (the full cookie string from a logged-in browser request to teamblind.com, including `bl_session_v2`). If it exists and is non-empty, Read it directly and pass it as the `-b`/Cookie header when fetching `teamblind.com/post/<slug>` and search URLs — don't echo the contents back to the user.

If the file is missing or empty, proceed to Step 1 unauthenticated (expect gated content), and optionally tell the user:

```
Blind gates most post content behind login. To unlock it, update your own cookie file:

1. Log into teamblind.com in your browser
2. Open DevTools → Network tab, reload, click any request to teamblind.com
3. Copy the Cookie header value
4. Write it to ~/.config/interview-research/cookies/blind.txt (chmod 600)
5. Tell me once it's updated.
```

---

## Step 1: WebSearch (primary approach)

Blind's search is behind a login wall but Google indexes its content well. Use WebSearch first:

```
WebSearch: site:teamblind.com "<company>" interview questions 2026
WebSearch: site:teamblind.com "<company>" coding interview SWE 2026
WebSearch: site:teamblind.com "<company>" phone screen onsite loop
```

Run all three searches. Collect the URLs from results.

---

## Step 2: WebFetch Individual Posts

WebFetch each URL returned from the searches. Blind posts typically load on direct URL access without requiring login.

```
https://www.teamblind.com/post/<slug>
```

From each post, extract:
- Problem names or descriptions mentioned in the post body
- The interview round (phone screen / onsite / take-home)
- Post date (shown in the post header — YYYY-MM-DD or "X days ago" → convert)
- Any links to LeetCode problems referenced

---

## Step 3: Blind Search Page

Try WebFetch on Blind's search directly:
```
https://www.teamblind.com/search?q=<company>+interview+questions
https://www.teamblind.com/search?q=<company>+coding+interview
```

If the page renders post listings (not a login wall), extract titles and URLs for further fetching in Step 2.

---

## Step 4: Parse Results

From each post extract:
- Explicit problem names (e.g. "they asked LRU Cache and Median of Two Sorted Arrays")
- Implicit descriptions (e.g. "design a rate limiter" → flag as System Design, not a LeetCode problem)
- Post date — filter to cutoff date

**Date handling:**
- "X days ago" → subtract from today's date
- "Jun 2026" → use as YYYY-MM (approximate, treat as in-range if within last 3 months)
- Posts with no date visible → include with a note: `(date unknown)`

Source URL: exact post URL from teamblind.com. Never use the search engine result URL as the source — always link the actual post.

---

## Step 5: Parse Problem Mentions

Blind posts use informal language. Apply these heuristics:
- Direct LeetCode name: match against known problem titles ("Two Sum", "LRU Cache", "Merge Intervals", etc.)
- Problem number: "#146", "LC 200" → look up title from the number
- Description: "they asked me to find the k-th largest element" → record as the description, not as a matched LeetCode title, unless the match is unambiguous

For ambiguous descriptions: quote the original text from the post and mark it as `[unverified problem match]`.

---

## Fallback: No Public Content

If Blind returns login walls for all attempts:
- Note: `[Blind: content behind login for this company — no public posts indexed]`
- Still include the search URL as a reference for the user to check manually:
  `https://www.teamblind.com/search?q=<company>+interview`
