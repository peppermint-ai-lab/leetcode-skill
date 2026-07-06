# Domain Catalog (generation seed)

Backend / systems, language-agnostic. Each entry is a **seed**, not a fixed problem — vary names, semantics, and test data every session so no two runs are identical. Never copy proprietary questions.

Columns: `id` · typical seniority · one-line · 4-part arc. The arc is the *spine*; author precise signatures, semantics, and tests from `authoring.md`. Parts must **build on the same code object** — Part N extends the class/module from Part N-1.

Seniority calibrates scope, not a different problem: `mid` = 3 clean parts + a stretch; `senior`/`staff` = all 4 parts land, with the 4th genuinely hard (concurrency sim, rollback, optimization).

---

## Stores & storage

- **kv-store** · mid · In-memory key-value store.
  1. `set/get/delete` with overwrite + missing-key semantics
  2. prefix search / top-N keys by some order
  3. TTL / expiration via an injected clock
  4. snapshots + rollback to a prior snapshot

- **file-host** · mid–senior · Mini file hosting service (metadata only, no real bytes). **⭐ Flagship arc** — the cleanest embodiment of the Industry Coding Framework escalation (`authoring.md` §Framework arc). Use it to calibrate what a well-formed problem feels like.
  1. `upload/get/copy` files by name (basic ops + missing/overwrite semantics)
  2. `search(prefix)` → top-N files by size desc, tie-break by name (data processing)
  3. timestamped/TTL variants — `upload_at(timestamp, name, size, ttl)` plus `get_at/copy_at/search_at`, via injected clock (refactor Part 1 to be time-aware)
  4. `rollback(timestamp)` restoring prior state with all TTLs recalculated (capstone: reuse + backward compat)
  *(Vary names/semantics/limits each session — never reproduce a proprietary prompt verbatim.)*

- **cache-evict** · mid–senior · Cache with eviction.
  1. bounded key-value cache
  2. LRU eviction at capacity
  3. per-entry TTL
  4. stats (hit rate), dynamic `resize` that evicts correctly

- **url-shortener** · mid · URL shortener.
  1. `shorten/expand` with collision-free codes
  2. custom aliases (reject taken/invalid)
  3. expiry via injected clock
  4. per-code analytics + basic abuse throttling

- **inventory** · mid–senior · Inventory / warehouse.
  1. add/remove stock per SKU
  2. reserve items (hold vs available)
  3. multiple warehouses
  4. fulfill an order across warehouses minimizing splits/cost

## Scheduling & intervals

- **calendar** · mid–senior · Calendar scheduler.
  1. add events (start/end)
  2. detect conflicts
  3. recurring events (daily/weekly/count or until)
  4. mutual free-slot finder across N calendars

- **meeting-rooms** · mid–senior · Meeting-room booking.
  1. book a room for an interval
  2. auto-pick the smallest room that fits capacity
  3. recurring bookings
  4. cancellation + waitlist promotion

- **parking-lot** · mid · Parking lot.
  1. assign cars to spots
  2. vehicle sizes ↔ spot sizes
  3. pricing by duration (injected clock)
  4. reservations + overbooking resolution

- **elevator** · senior · Elevator system (simulated, stepwise clock).
  1. single car moves toward one request
  2. queue of pickup/dropoff requests, SCAN-style
  3. multiple cars
  4. dispatch to minimize total/att wait time

## Queues, jobs, limits

- **task-queue** · senior · Task queue.
  1. enqueue/dequeue FIFO
  2. priorities
  3. delayed jobs (injected clock)
  4. retry with backoff + dead-letter queue

- **rate-limiter** · mid–senior · Rate limiter (injected clock).
  1. fixed-window limiter
  2. per-user limits
  3. sliding-window
  4. multi-node simulation (merge counts / eventual consistency)

- **job-worker** · senior · Background job worker (`--repo`-friendly too).
  1. pull job, run handler, ack
  2. failure → retry, max attempts
  3. exponential backoff (injected clock)
  4. dead-letter queue + replay

- **notification** · mid–senior · Notification service.
  1. send a notification
  2. channels (email/sms/push) as pluggable senders
  3. per-user channel preferences + quiet hours
  4. retry on failure + dedupe within a window

## Ledgers, markets, commerce

- **banking-ledger** · mid–senior · Banking ledger.
  1. create account, deposit, withdraw (no overdraft)
  2. transfer between accounts (atomic)
  3. per-account transaction history
  4. scheduled payments + rollback of a failed transfer chain

- **order-matching** · senior–staff · Order matching engine.
  1. record buy/sell orders
  2. match by price then time priority
  3. partial fills
  4. cancel / modify resting orders

- **shopping-cart** · mid · Shopping cart / checkout.
  1. add/remove items with quantities
  2. coupons / discounts (stackable rules)
  3. inventory reservation on add
  4. checkout with partial-failure rollback

- **leaderboard** · mid–senior · Leaderboard.
  1. add/update scores
  2. top-K users
  3. rank lookup for a user
  4. time-windowed leaderboard (injected clock)

## Parsers, engines, tools

- **spreadsheet** · senior · Spreadsheet engine.
  1. set/get cell literals
  2. formulas like `=A1+B1`
  3. dependency graph + recalc on change
  4. cycle detection + correct recalculation order

- **expr-eval** · mid–senior · Expression evaluator.
  1. parse + evaluate `+ - * /`
  2. parentheses + precedence
  3. variables / environment
  4. functions + structured error reporting

- **autocomplete** · mid–senior · Search autocomplete.
  1. prefix suggestions (trie)
  2. rank by frequency
  3. personalized boost per user history
  4. typo tolerance (edit-distance ≤ 1)

- **markdown** · mid · Markdown parser → HTML/AST.
  1. headings, bold, italic
  2. nested lists
  3. links + fenced code blocks
  4. sanitize unsafe HTML/attributes

- **json-diff** · mid–senior · JSON diff / patch.
  1. diff flat objects
  2. nested objects
  3. arrays (index-based)
  4. emit a patch + apply it (round-trip)

- **csv-query** · mid–senior · CSV query engine.
  1. parse CSV (quotes, embedded commas)
  2. filter rows by predicate
  3. sort + group-by with aggregates
  4. tiny SQL-ish query string parser

- **log-ingest** · mid–senior · Log ingestion.
  1. parse log lines to records
  2. filter by service / time range
  3. aggregate counts + error rates
  4. alerting rules (threshold over window)

## Versioning & dependencies

- **mini-git** · senior · Mini version store.
  1. store file versions (content-addressed)
  2. commits + linear history
  3. branches
  4. detect merge conflicts between branches

- **dep-resolver** · senior · Package dependency resolver.
  1. install a package + its deps (order)
  2. detect missing deps
  3. version constraints (ranges)
  4. conflict resolution / report unsatisfiable

- **feature-flags** · mid–senior · Feature-flag service.
  1. enable/disable flags
  2. user targeting rules
  3. percentage rollout (stable hashing)
  4. audit log + rollback to a prior flag state

- **config-mgr** · mid · Config management service.
  1. load key/values
  2. environment overrides (base ← env)
  3. schema validation (types/required)
  4. layered merge + provenance ("which layer set this")

## Concurrency / collab (senior+)

- **movie-booking** · senior · Movie ticket booking.
  1. seat map
  2. reserve seats
  3. holds expire (injected clock)
  4. concurrent booking conflict resolution (stepwise interleaving)

- **chat-room** · mid–senior · Chat room / message store.
  1. send messages (ordered)
  2. users join/leave
  3. per-user unread counts
  4. edit/delete with an edit-history trail

- **collab-doc** · staff · Realtime collaborative document.
  1. apply local edits to a text buffer
  2. represent edits as operations
  3. transform/merge concurrent ops (OT-lite)
  4. version history + revert

---

## Custom domains (`--custom "<desc>"`)

Accept any backend/systems domain the user proposes that can be split into 4 building parts where Part N extends Part N-1's code. Reject: pure UI/frontend, ML training, or anything that can't grow across parts. Design the arc using `authoring.md`.
