# Source: LeetCode Problems (Company Tags)

LeetCode tags problems by company and tracks how recently they've been asked. The problem list page is public but frequency/recency data requires a premium subscription.

---

## Step 1: Public Problem List

WebFetch the company-tagged problem list:
```
https://leetcode.com/problemset/?company=<company-slug>
```

Derive `<company-slug>` from the company name: lowercase, spaces → hyphens, special chars dropped. Examples: `google`, `meta`, `amazon`, `jane-street`, `two-sigma`.

This page returns a JS-rendered list — if the HTML is empty (SPA shell), use the GraphQL API instead.

---

## Step 2: GraphQL — Problem List (public, no auth)

```bash
curl 'https://leetcode.com/graphql/' \
  -H 'Content-Type: application/json' \
  --data '{
    "operationName": "problemsetQuestionList",
    "variables": {
      "categorySlug": "all",
      "limit": 50,
      "skip": 0,
      "filters": {
        "companySlug": "<COMPANY_SLUG>"
      }
    },
    "query": "query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) { problemsetQuestionList: questionList(categorySlug: $categorySlug limit: $limit skip: $skip filters: $filters) { total: totalNum questions: data { acRate difficulty frontendQuestionId: questionFrontendId paidOnly: isPaidOnly title titleSlug topicTags { name slug } } } }"
  }'
```

This returns all problems tagged for the company. The list is sorted by frequency (most asked first) but recency data (`companyTagStats`) requires premium.

---

## Step 3: Authenticated Access — Frequency and Recency

**Never ask the user to paste a session cookie into chat.** Check for a locally-stored cookie file first:

```
~/.config/interview-research/cookies/leetcode.txt
```

Same file used by the LeetCode Forums source (`leetcode-forums.md`) — contains `csrftoken=<value>; LEETCODE_SESSION=<value>` on one line. If it exists and is non-empty, Read it directly and extract `csrftoken` for the `X-CSRFToken` header.

If the file is missing or empty, tell the user this requires a premium LeetCode account, and:

```
Please update it yourself:

1. Log into leetcode.com (premium account required)
2. Open DevTools → Application → Cookies → leetcode.com
3. Copy: csrftoken  and  LEETCODE_SESSION
4. Write "csrftoken=<value>; LEETCODE_SESSION=<value>" to
   ~/.config/interview-research/cookies/leetcode.txt (chmod 600)
5. Tell me once it's updated.
```

Then stop and wait. Once provided, fetch company tag stats including time periods:
```bash
curl 'https://leetcode.com/graphql/' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: csrftoken=<CSRFTOKEN>; LEETCODE_SESSION=<SESSION>' \
  -H 'X-CSRFToken: <CSRFTOKEN>' \
  --data '{
    "operationName": "getCompanyTag",
    "variables": { "slug": "<COMPANY_SLUG>" },
    "query": "query getCompanyTag($slug: String!) { companyTag(slug: $slug) { name questions { status difficulty title titleSlug frequencyTimePeriod } imgUrl } }"
  }'
```

`frequencyTimePeriod` values: `1` = last 6 months, `2` = last year, `3` = all time. Filter for `frequencyTimePeriod: 1` to approximate "recently asked."

---

## Step 4: Parse Results

From the GraphQL response, extract each question:
- `title` — problem name
- `difficulty` — Easy/Medium/Hard
- `titleSlug` — used to build the URL
- `topicTags[].name` — patterns (e.g. Array, Dynamic Programming, Graph)
- `frequencyTimePeriod` — 1 means asked in last 6 months (closest proxy to "last 3 months")

Source URL format:
```
https://leetcode.com/problems/<titleSlug>/
```

---

## Step 5: WebSearch Fallback

If the company slug is not recognized by LeetCode's company tag system:
```
WebSearch: leetcode company tag "<company>" problems list
WebSearch: leetcode "<company>" interview questions 2026
```

Also search for the correct LeetCode company slug:
```
WebSearch: leetcode.com/problemset company=<variations of company name>
```
