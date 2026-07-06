# Authoring Guide — how to generate a well-formed problem

Read this every session. It turns a domain seed into a precise, testable, progressively-revealed problem.

## Required fields (author all of them before presenting Part 1)

Even though you reveal one part at a time, author the whole thing first so Part 1 is *honestly* under-designed:

- **title** — original, not a proprietary name
- **role / seniority** — from the domain; scales scope (see `domains.md`)
- **time estimate** — total budget + per-part target (guidance below)
- **language** — from `--lang`, default `python`
- **signatures** — a language-neutral signature block per part (class + methods, args, return types, error behavior)
- **Part 1–4 specs** — each a self-contained increment on the same code object
- **visible tests** — 3–6 per part, shown, deterministic
- **hidden tests** — 3–5 per part, unseen, edge-focused (see §Edge cases)
- **rubric** — grade from `rubric.md`
- **edge cases** — the traps §Edge cases lists for the archetype
- **follow-up questions** — 3–5 talk-through prompts for the final wrap-up

## Progressive design — the core skill

The value of these problems is that **Part 1 must be designed without seeing Part 3**. Author so that:

- Each part **reuses the same class/object** — Part 2 adds methods; it does not restart.
- A naive Part 1 still passes Part 1, but a *thoughtful* Part 1 makes Part 3/4 far easier. Example (kv-store): storing raw values passes Part 1, but wrapping each value in an entry record makes TTL (Part 3) and snapshots (Part 4) trivial. Don't hint this — let them feel the cost.
- Later parts should sometimes **force a refactor** of earlier code. That's intended friction; the "GROWTH RISK" feedback line and the final rubric reward those who anticipated it.
- Never leak a later part's spec in an earlier part's wording or signature. If Part 1's signature must accommodate Part 3, keep it minimal and let them discover the gap.

## Framework arc — the canonical 4-level escalation

Model every problem on the **CodeSignal Industry Coding Framework**. The four parts are not four unrelated tasks of rising difficulty (that's the *GCA*, a different product) — they are **one project that grows**, with a fixed thematic escalation. Author each part to its level's job:

| Part | Level theme | Job | Size guide |
|---|---|---|---|
| **1** | Initial Design & Basic Functions | 3–4 simple methods; basic implementation + corner cases. The design choice here decides how much Part 3/4 hurts. | ~15–20 lines, ~10–15 min |
| **2** | Data Structures & Data Processing | 1–2 methods that *process* what Part 1 stores: filter, aggregate, top-N, export, search. | ~20–30 min |
| **3** | Refactoring & Encapsulation | 3–5 methods that extend behavior — often a **time/versioned dimension** layered onto Part 1's operations. Forces reworking earlier code if it wasn't built to grow. | ~30–60 min |
| **4** | Extending Design & Functionality | 1–2 methods; a culminating extension that **reuses and encapsulates** everything prior for backward compatibility. | ends ~110–160 total lines, ~30–60 min |

**Recurring shapes worth reusing** (these are the framework's signature moves, seen across its problems — vary the domain, keep the pattern):
- **Level 3 = "same ops, now time-aware."** Introduce timestamped/TTL variants of the Part 1 operations (e.g. an `*_at(timestamp, …, ttl)` sibling of each basic op) via an **injected clock**. A candidate who wrapped values in an entry record at Part 1 extends trivially; one who stored raw values must refactor. Don't hint this.
- **Level 4 = "restore prior state."** A `rollback(timestamp)` / snapshot-revert that must correctly recompute derived state (e.g. recalculating remaining TTLs after rollback). This is the classic capstone.
- Backward compatibility is graded: **Part 1's method signatures must still work** after Parts 3–4 exist. New behavior arrives as new methods or optional params, not by breaking old contracts.

**Deliberately EXCLUDE** (the framework bars these — keep problems implementation/data-processing flavored, not algorithmic):
- Classic/niche algorithms: binary search, two pointers, dynamic programming, graph shortest-path, etc.
- Third-party libraries and non-built-in advanced data structures (implement what you need from built-ins).
- Anything whose difficulty is a *trick* rather than *accumulated implementation*. Difficulty comes from breadth and refactoring, not a clever insight.

The affirmative focus is: implementation, data processing, refactoring, encapsulation — real-world iterative development.

## Time budgets

Per-part targets **escalate** across the four levels (they are not flat) — mirror the framework: Part 1 short, Parts 3–4 the bulk of the budget.

| Seniority | Total | L1 · L2 · L3 · L4 (targets) |
|---|---|---|
| mid | ~45 min | ~8 · ~10 · ~14 · ~13 min |
| mid–senior | ~60 min | ~10 · ~13 · ~19 · ~18 min |
| senior / staff | ~75–90 min | ~12 · ~18 · ~28 · ~27 min |

Show the total and the current part's target at the start of every part. Enforce per-part strictly; going over doesn't fail the part but is recorded and called out. As in the real ICA, **finishing all four is not the bar** — reaching Part 3 cleanly is a solid result; make that framing clear at wrap-up.

## Language-agnostic specs

Describe operations in prose + a neutral signature block, e.g.:
```
class KVStore:
    set(key: str, value: any) -> None
    get(key: str) -> any | NOT_FOUND        # return a sentinel / raise; state which
    delete(key: str) -> bool                # True if a key was removed
```
State return values, the missing-key contract, ordering guarantees, and error behavior explicitly — ambiguity here is what makes tests unfair. For Python, realize the block as a real class stub the visible tests import.

## Test design

- **Visible tests** demonstrate the happy path + the one semantic subtlety of the part. Enough to make the spec unambiguous; not enough to enumerate every edge.
- **Hidden tests** target the traps below. Pass requires visible **and** hidden green.
- **Deterministic only.** No real wall-clock, sleeps, threads, or randomness in requirements:
  - **Time:** inject a clock — `Clock` object or a `now`/`at=` parameter the tests advance explicitly. TTL/expiry/backoff/rate-window all use it.
  - **Concurrency:** simulate with explicit step ordering or an interleaving list the test drives (e.g. two `begin_booking` holds then a `commit`), never real threads.
  - **Randomness/hashing:** require a *stable* hash (percentage rollout, short-code gen) so tests are reproducible; seed or derive from the key.
- Tests import from the solution file by its real symbols. Keep imports stable across parts so earlier tests keep passing.

## Edge cases by archetype

Pick the archetype(s) matching the domain and pull hidden tests from here.

- **Stateful store (kv, cache, file-host, inventory):** get after delete; overwrite returns/replaces correctly; delete of absent key; TTL boundary at *exactly* expiry vs one tick past; snapshot/rollback to a point that never existed or after further writes; capacity edge (evict at N+1, not N); resize below current size.
- **Intervals / scheduling (calendar, meeting-rooms, parking, elevator):** touching-but-not-overlapping intervals (`[1,2]` vs `[2,3]`); zero-length; fully-contained; identical intervals; recurrence that ends mid-window; no room fits; waitlist promotion order; free-slot finder when calendars are fully busy or fully free.
- **Queue / jobs / limits (task-queue, rate-limiter, job-worker, notification):** dequeue empty; priority tie → FIFO; delayed job not yet due vs due this tick; window boundary (Nth request allowed, N+1 rejected) at exact edge; retry hitting max → dead-letter; dedupe of identical events within/after the window.
- **Ledger / market / commerce (banking, order-matching, cart, leaderboard):** overdraft rejected and leaves balance unchanged; transfer failure is atomic (neither side moves); self-transfer; partial fill leaves correct remainder; cancel an already-filled order; coupon on empty cart / stacked coupons; score update changes rank; top-K when fewer than K exist; ties in ranking.
- **Parser / engine (spreadsheet, expr-eval, autocomplete, markdown, json-diff, csv, log):** empty input; single token; unbalanced parens/brackets; precedence (`2+3*4`); undefined variable/cell; self/mutual cell cycles; unknown function; deep nesting; quoted CSV field with commas/newlines; prefix with no matches; typo distance exactly 1 vs 2; unsafe HTML attribute stripped but safe text kept.
- **Versioning / deps (mini-git, dep-resolver, feature-flags, config):** commit with no changes; branch from mid-history; conflicting edits to same file/line; missing transitive dep; unsatisfiable version constraint; circular dependency; env override of an absent base key; percentage rollout stable across calls; rollback to prior flag state.
- **Concurrency sim (movie-booking, chat, collab-doc):** two holds on the same seat, second rejected; hold expires then seat rebookable; message ordering under interleaved sends; unread count after read then new message; edit after delete; concurrent ops on the same region merge deterministically.

## Repo mode (`--repo`)

Generate a small **backend** repo (3–6 files) that is broken or incomplete. Archetypes: fix-a-REST-API, implement-service-layer (routes exist, service stubbed), debug-failing-tests, refactor-legacy-module, package-resolver, migration-runner, background-worker, webhook-receiver (signature verify + dedupe), ETL bug-hunt, mini-ORM, search-service (inverted index). Requirements:
- Ship a **test suite with some tests failing on purpose**; the README lists tasks + the public API to preserve.
- Bugs are realistic: off-by-one, missing validation, wrong error handling, N+1, timezone/parse edge, non-idempotent handler — not typos.
- Keep it deterministic (injected clock, in-memory stores, mock gateway) — no network.
- Grade on: root-cause fix (not test-gaming), minimal correct diff, no regressions in previously-passing tests, hidden edge tests green, public API unchanged. Enforce read-before-edit.

## Guardrails

- Original domains and data only; never reproduce known company questions verbatim.
- One part visible at a time — author all four, reveal one.
- Every part extends the same object; imports stay stable.
- Deterministic, self-contained, no external services.
