# Source: LeetCode Forums (Discuss)

LeetCode's Discuss section contains interview experience posts tagged by company. The public feed is readable without auth; authenticated access via GraphQL gives richer filtering.

---

## Step 1: Public WebFetch (no auth)

Try this URL first — LeetCode discuss is publicly readable:
```
https://leetcode.com/discuss/interview-experience/?search=<company-slug>&orderBy=Newest
```

WebFetch the URL. Look for interview experience post titles and dates in the HTML. Extract problem names mentioned in post summaries visible on the listing page.

Also try:
```
https://leetcode.com/discuss/compensation/?search=<company>&orderBy=Newest
```

---

## Step 2: GraphQL API (deeper access, partially public)

This endpoint works without auth for most queries:

```bash
curl 'https://leetcode.com/graphql/' \
  -H 'Content-Type: application/json' \
  -H 'Referer: https://leetcode.com/discuss/interview-experience/' \
  --data '{
    "operationName": "categoryTopicList",
    "variables": {
      "pageNo": 1,
      "numPerPage": 20,
      "orderBy": "newest",
      "query": "<COMPANY>",
      "categories": ["interview-question", "interview-experience"]
    },
    "query": "query categoryTopicList($categories: [String!]!, $pageNo: Int!, $numPerPage: Int!, $orderBy: String!, $query: String!) { categoryTopicList(categories: $categories, pageNo: $pageNo, numPerPage: $numPerPage, orderBy: $orderBy, query: $query) { edges { node { id title slug post { creationDate voteCount } lastActivity } } } }"
  }'
```

Run this curl as-is — it does not require authentication. If it returns 403, proceed to Step 3.

---

## Step 3: Authenticated Access (if needed)

**Never ask the user to paste a session cookie into chat.** Check for a locally-stored cookie file first:

```
~/.config/interview-research/cookies/leetcode.txt
```

This file should contain the Cookie header value on one line, e.g. `csrftoken=<value>; LEETCODE_SESSION=<value>`. If it exists and is non-empty, Read it directly and extract `csrftoken` from within it for the `X-CSRFToken` header — don't echo the contents back to the user.

If the file is missing or empty, tell the user:

```
I need a LeetCode session cookie, but I won't take it in chat.
Please update it yourself:

1. Log into leetcode.com in your browser
2. Open DevTools → Application tab → Cookies → leetcode.com
3. Copy the value of: csrftoken  and  LEETCODE_SESSION
4. Write "csrftoken=<value>; LEETCODE_SESSION=<value>" to
   ~/.config/interview-research/cookies/leetcode.txt (chmod 600)
5. Tell me once it's updated.
```

Then stop and wait. Once provided, run:
```bash
curl 'https://leetcode.com/graphql/' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: csrftoken=<CSRFTOKEN>; LEETCODE_SESSION=<SESSION>' \
  -H 'X-CSRFToken: <CSRFTOKEN>' \
  --data '{
    "operationName": "categoryTopicList",
    "variables": {
      "pageNo": 1,
      "numPerPage": 20,
      "orderBy": "newest",
      "query": "<COMPANY>",
      "categories": ["interview-question", "interview-experience"]
    },
    "query": "query categoryTopicList($categories: [String!]!, $pageNo: Int!, $numPerPage: Int!, $orderBy: String!, $query: String!) { categoryTopicList(categories: $categories, pageNo: $pageNo, numPerPage: $numPerPage, orderBy: $orderBy, query: $query) { edges { node { id title slug post { creationDate voteCount } lastActivity } } } }"
  }'
```

---

## Step 4: Fetch Individual Posts

For each post returned, WebFetch the full post to extract problem names:
```
https://leetcode.com/discuss/interview-experience/<slug>/
```

Parse the post body for:
- LeetCode problem names (usually quoted or linked)
- Links to `leetcode.com/problems/` (strongest signal — exact problem URL)
- Date of the interview (often in the post body or title)

---

## Step 5: Parse Results

From each post extract:
- `creationDate` (Unix timestamp) → convert to YYYY-MM-DD → filter by cutoff
- `title` → interview context (company, role, date)
- Problems mentioned → list each with the post URL as source

Source URL format:
```
https://leetcode.com/discuss/interview-experience/<slug>/
```

---

## Fallback: WebSearch

```
WebSearch: site:leetcode.com/discuss "<company>" interview experience 2026
```

WebFetch the top 5 results. Only include problems that have a direct leetcode.com/discuss URL as source.
