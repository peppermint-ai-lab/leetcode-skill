# Source: Glassdoor

Glassdoor interview reports require authentication for full access. Follow the steps below in order.

---

## Step 1: Find the Company Page

Use WebSearch to find the Glassdoor company interview URL:
```
WebSearch: glassdoor.com "<company>" interview questions site:glassdoor.com/Interview
```

The URL pattern is:
```
https://www.glassdoor.com/Interview/<Company-Slug>-Interview-Questions-E<ID>.htm
```

Try WebFetch on the result URL. The first page is sometimes publicly accessible and shows recent interview reports.

---

## Step 2: Get Auth Token (if WebFetch returns a login wall)

**Never ask the user to paste a session cookie or curl command into chat.** Session tokens are live credentials — once pasted into a conversation they're exposed for good. Instead, check for a locally-stored cookie file first:

```
~/.config/interview-research/cookies/glassdoor.txt
```

This file should contain just the Cookie header value (everything after `Cookie:` in a captured request), on one line. If the file exists and is non-empty, read it directly with the Read tool and use its contents as the `-b` value below — do not echo the contents back to the user.

If the file is missing or empty, tell the user:

```
I need a Glassdoor session cookie to access interview data, but I won't take it in chat.
Please update it yourself:

1. Log into glassdoor.com in your browser
2. Navigate to: https://www.glassdoor.com/Interview/<company>-Interview-Questions-E<ID>.htm
3. Open DevTools → Network tab (F12), reload, click a request to glassdoor.com/graph
4. Copy the Cookie header value
5. Write it to ~/.config/interview-research/cookies/glassdoor.txt (chmod 600), replacing any old value
6. Tell me once it's updated — I'll pick it up from the file.
```

Then stop and wait — do not proceed with a stale or missing cookie.

---

## Step 3: Fetch Interview Data

Once the cookie file is populated, run this curl to get the company ID and recent interviews.

**Find company ID:**
```bash
curl 'https://www.glassdoor.com/autocomplete/employer?term=<COMPANY>&preferredOnly=false&limit=10' \
  -H 'Accept: application/json' \
  -H 'Cookie: <PASTE_COOKIE_HERE>' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
```

Response contains `id` — the employer ID. Note it.

**Fetch interview questions (GraphQL):**
```bash
curl 'https://www.glassdoor.com/graph' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: <PASTE_COOKIE_HERE>' \
  -H 'gd-csrf-token: <PASTE_CSRF_TOKEN_FROM_COOKIE>' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
  --data '{
    "operationName": "InterviewsPageGraphQL",
    "variables": {
      "employerId": <EMPLOYER_ID>,
      "jobTitle": null,
      "pageNum": 1,
      "numPerPage": 20,
      "sort": "DATE"
    },
    "query": "query InterviewsPageGraphQL($employerId: Int!, $jobTitle: String, $pageNum: Int!, $numPerPage: Int!, $sort: String) { employerInterviews(employerId: $employerId, jobTitle: $jobTitle, pageNum: $pageNum, numPerPage: $numPerPage, sort: $sort) { filteredInterviewCount interviews { interviewId interviewDateTime jobTitle interviewType interviewDifficulty overallExperience processSteps { stepType description } interviewQuestions { questionId question } } } }"
  }'
```

Replace `<PASTE_CSRF_TOKEN_FROM_COOKIE>` with the `GASC` or `gdsid` value found in the Cookie string.

---

## Step 4: Parse the Response

From the JSON response, extract:
- `interviewDateTime` → convert to YYYY-MM-DD, filter to cutoff date
- `interviewQuestions[].question` → the actual problem text
- `processSteps[].description` → may contain additional problem details
- Build source URL: `https://www.glassdoor.com/Interview/interview-review-?reviewId=<interviewId>`

---

## Fallback: WebSearch

If auth is unavailable, use:
```
WebSearch: glassdoor.com "<company>" software engineer interview questions 2026
```

WebFetch the top 3 result pages. Extract any quoted interview questions. Only include results with a visible Glassdoor URL as the source.
