# Company Peer Groups and Role Domains

Used by the research-agent expansion phase to find peer companies when coverage is thin.

---

## Peer Groups

When a company has sparse results, search the top 2 peers in the same group. Mark results `[PEER: <company>]`.

### FAANG / Top Tier
Companies: Google, Meta, Amazon, Apple, Microsoft, Netflix
Peers for any: the others in this list

### Finance / Quant / HFT
Companies: Jane Street, Two Sigma, Citadel, DE Shaw, Jump Trading, Hudson River Trading, Renaissance, Optiver, Virtu, IMC Trading
Peers for any: the others in this list

### Enterprise SaaS / Cloud
Companies: Salesforce, ServiceNow, Workday, Oracle, SAP, Snowflake, Databricks
Peers for Snowflake/Databricks: each other + Confluent, dbt Labs
Peers for Salesforce/Workday: each other + Oracle

### Growth / Scale-ups
Companies: Stripe, Airbnb, Uber, Lyft, DoorDash, Instacart, Coinbase, Robinhood
Peers for payment/fintech: Stripe, Coinbase, Robinhood, Square
Peers for marketplace: Airbnb, Uber, Lyft, DoorDash

### AI / ML Infra
Companies: OpenAI, Anthropic, Cohere, Mistral, Scale AI, Weights & Biases, Hugging Face
Peers for any: the others in this list + Google DeepMind, Meta AI

### Gaming
Companies: Riot Games, Epic Games, Valve, Unity, Roblox, EA, Activision Blizzard
Peers for any: the others in this list

### Crypto / Web3
Companies: Coinbase, Kraken, Binance, Chainlink, Alchemy, Consensus
Peers for any: the others in this list

---

## Role Family → Domain Keywords

Used to generate supplementary search terms when role-specific coverage is thin.

| Role family | Domain keywords for search |
|---|---|
| swe | data structures, algorithms, system design |
| ml-engineer | machine learning, model training, feature store, embeddings, recommendation, GPU, CUDA, distributed training |
| data-engineer | ETL, pipeline, Spark, Kafka, Airflow, data warehouse, streaming, SQL, dbt |
| quant | financial algorithms, trading, pricing, Monte Carlo, combinatorics, optimization, probability |
| sre | observability, incident response, distributed systems, reliability, Kubernetes, monitoring, on-call |
| frontend | DOM, React, rendering performance, browser APIs, CSS layout, accessibility, hydration |
| ios-android | concurrency, memory management, lifecycle, UIKit, SwiftUI, Jetpack Compose, background tasks |
| security | authentication, encryption, XSS, CSRF, penetration testing, OWASP, secrets management |
| pm | product sense, metrics, A/B testing, prioritization, roadmap |

---

## Known LeetCode Company Slugs

Use these exact slugs in the GraphQL `companySlug` filter (from `../research/sources/leetcode-problems.md`).

```
Google        → google
Meta          → facebook
Amazon        → amazon
Apple         → apple
Microsoft     → microsoft
Netflix       → netflix
Uber          → uber
Airbnb        → airbnb
Stripe        → stripe
Lyft          → lyft
DoorDash      → doordash
Snowflake     → snowflake
Databricks    → databricks
Twitter/X     → twitter
LinkedIn      → linkedin
Salesforce    → salesforce
Two Sigma     → two-sigma
Jane Street   → jane-street
Coinbase      → coinbase
Roblox        → roblox
```

If the company is not in this list, try: lowercase name with hyphens. If the GraphQL query returns 0 results, the company is likely not in LeetCode's tag system — fall back to forum search.

---

## Common Vague → LeetCode Mappings (Fast Lookup)

Before running a WebSearch, check here first. These are high-confidence common mappings.

| Vague description | LeetCode problem | LC # | Difficulty |
|---|---|---|---|
| design a cache | LRU Cache | 146 | Medium |
| least recently used | LRU Cache | 146 | Medium |
| design a rate limiter | (no LC) — System Design | — | — |
| merge overlapping intervals | Merge Intervals | 56 | Medium |
| find kth largest | Kth Largest Element in an Array | 215 | Medium |
| kth largest in stream | Kth Largest Element in a Stream | 703 | Easy |
| top k frequent | Top K Frequent Elements | 347 | Medium |
| design twitter / news feed | Design Twitter | 355 | Medium |
| shortest path in grid | Shortest Path in Binary Matrix | 1091 | Medium |
| word break | Word Break | 139 | Medium |
| balanced parentheses | Valid Parentheses | 20 | Easy |
| longest substring without repeat | Longest Substring Without Repeating Characters | 3 | Medium |
| two numbers sum to target | Two Sum | 1 | Easy |
| find cycle in linked list | Linked List Cycle | 141 | Easy |
| reverse a linked list | Reverse Linked List | 206 | Easy |
| lowest common ancestor | LCA of a Binary Tree | 236 | Medium |
| serialize/deserialize tree | Serialize and Deserialize Binary Tree | 297 | Hard |
| design URL shortener | (no LC) — System Design | — | — |
| design key-value store | (no LC) — System Design | — | — |
| search in rotated array | Search in Rotated Sorted Array | 33 | Medium |
| median of two sorted arrays | Median of Two Sorted Arrays | 4 | Hard |
| maximum subarray | Maximum Subarray | 53 | Medium |
| buy and sell stock | Best Time to Buy and Sell Stock | 121 | Easy |
| trap water / rain water | Trapping Rain Water | 42 | Hard |
| decode ways | Decode Ways | 91 | Medium |
| number of islands | Number of Islands | 200 | Medium |
| clone graph | Clone Graph | 133 | Medium |
| course schedule / detect cycle | Course Schedule | 207 | Medium |
| alien dictionary / topological sort | Alien Dictionary | 269 | Hard |
| word search in grid | Word Search | 79 | Medium |
| permutations / all combinations | Permutations | 46 | Medium |
| subset sum | Subsets | 78 | Medium |
| edit distance | Edit Distance | 72 | Hard |
| regular expression matching | Regular Expression Matching | 10 | Hard |
| jump game | Jump Game | 55 | Medium |
| container with most water | Container With Most Water | 11 | Medium |
| 3sum / triplets | 3Sum | 15 | Medium |
| meeting rooms / schedule overlap | Meeting Rooms II | 253 | Medium |
| task scheduler | Task Scheduler | 621 | Medium |
| sliding window maximum | Sliding Window Maximum | 239 | Hard |
| find median from data stream | Find Median from Data Stream | 295 | Hard |
| word ladder / BFS shortest path | Word Ladder | 127 | Hard |
| alien dictionary | Alien Dictionary | 269 | Hard |
| design file system | Design File System | 1166 | Medium |
| trie / prefix tree | Implement Trie | 208 | Medium |
| add and search words | Add and Search Word | 211 | Medium |
| minimum window substring | Minimum Window Substring | 76 | Hard |
| longest palindromic substring | Longest Palindromic Substring | 5 | Medium |
| palindrome partitioning | Palindrome Partitioning | 131 | Medium |
| find all anagrams | Find All Anagrams in a String | 438 | Medium |
| group anagrams | Group Anagrams | 49 | Medium |
| valid sudoku | Valid Sudoku | 36 | Medium |
| spiral matrix | Spiral Matrix | 54 | Medium |
| rotate matrix/image | Rotate Image | 48 | Medium |
| maximum product subarray | Maximum Product Subarray | 152 | Medium |
```
