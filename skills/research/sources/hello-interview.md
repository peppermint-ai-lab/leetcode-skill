# Source: Hello Interview

hellointerview.com provides structured interview prep content by company. Some content is gated behind a membership, but company overview pages and some problem lists are publicly accessible.

---

## Step 0: Authenticated Access (optional, unlocks gated reports)

**Never ask the user to paste a session cookie into chat.** Check for a locally-stored cookie file first:

```
~/.config/interview-research/cookies/hellointerview.txt
```

This file should contain the Cookie header value on one line (from a logged-in browser request to hellointerview.com, including `hi.session-token-2`). If it exists and is non-empty, Read it directly and pass it as the `-b`/Cookie header when fetching community/question pages — membership-gated pages often show only 3 of "10+" or "20+" reports to logged-out users, and more with a valid session. Don't echo the contents back to the user.

If the file is missing or empty, proceed to Step 1 unauthenticated, and optionally tell the user:

```
Some Hello Interview content is gated behind membership. To unlock it, update your own cookie file:

1. Log into hellointerview.com in your browser
2. Open DevTools → Network tab, reload, click any request to hellointerview.com
3. Copy the Cookie header value
4. Write it to ~/.config/interview-research/cookies/hellointerview.txt (chmod 600)
5. Tell me once it's updated.
```

---

## Step 1: Company Page

WebFetch the company-specific prep page:
```
https://www.hellointerview.com/learn/code/company/<company-slug>
```

Also try:
```
https://www.hellointerview.com/company/<company-slug>
```

If neither resolves, use WebSearch to find the correct URL:
```
WebSearch: site:hellointerview.com "<company>" interview prep problems
```

WebFetch the top result.

---

## Step 2: Community / Forum Posts

Hello Interview has a community section with interview reports:
```
https://www.hellointerview.com/community?company=<company-slug>
```

Also try:
```
WebSearch: site:hellointerview.com "<company>" interview experience 2026
```

WebFetch each result URL. Look for:
- Problem names in post titles or body
- Dates (filter to cutoff)
- Direct problem links (e.g. `hellointerview.com/learn/code/problem/...`)

---

## Step 3: Parse Results

From each page, extract:
- Problem names and their difficulty
- Pattern/topic tags if shown
- Date of report (YYYY-MM-DD or YYYY-MM)

Source URL: use the exact URL you fetched (e.g. `https://www.hellointerview.com/learn/code/company/<company-slug>`).

If a problem links to a LeetCode equivalent, record both the Hello Interview source URL and the LeetCode URL as supplementary.

---

## Step 4: Gated Content

If the page returns a paywall or login redirect:
- Note: `[Hello Interview: content gated behind membership]`
- Record the URL that was blocked as the source reference
- Do not fabricate problem names

---

## Fallback: WebSearch Only

If direct WebFetch fails entirely:
```
WebSearch: hellointerview.com "<company>" coding interview questions
WebSearch: hellointerview "<company>" interview problems list 2026
```

Use the search result snippet text as the source, but only if the URL resolves to hellointerview.com. Include the Google result URL or the page URL — not the search engine URL itself.
