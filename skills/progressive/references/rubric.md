# Evaluation Rubric — progressive build problems

Grade the **whole problem** at wrap-up, not just the final part. These rounds test incremental design under time, so weight *how the code grew* as heavily as whether it passes.

## Per-part gate (during the run)

A part passes only if **visible + hidden tests are all green**. Hidden failure = part failure = next part stays locked. No partial passes on the gate — but record *why* in notes.

## How real ICA scoring works (framing for feedback)

On an actual CodeSignal certified assessment the output is an **Overall Coding Score, 200–600** (higher = more requirements completed; the old 300–850 / 600–850 bands are legacy scales — don't cite an 850 ceiling). Crucially, **candidates are not expected to finish all four levels** — partial completion is normal and still scores. Reflect that in feedback:
- Reaching **Part 3 cleanly** is a genuinely solid result; **all 4** is strong-hire territory. Don't frame a stop at Part 3 as failure.
- Score reflects *how far you got, correctly* — a rushed, buggy Part 4 is worth less than a clean Part 3. Reward correctness-per-level over racing ahead.
- Map the run to an informal band at wrap-up: 1–2 parts = "below screen bar", 3 parts clean = "passes screen", 4 parts clean = "strong". Keep it directional, not a fake numeric score.

## Final scoring (wrap-up, all 4 parts passed)

Score each dimension 1–5. Lead with correctness, but the differentiator is design.

| Dimension | Weight | 5 = | 1 = |
|---|---|---|---|
| **Correctness** | high | all visible + hidden green every part, edges handled | leaned on visible tests, hidden failures fixed late |
| **Incremental design** | high | Part 1 anticipated growth; parts 2–4 extended cleanly with little rework | each part hacked on; later parts forced rewrites they didn't see coming |
| **Data structure & complexity** | high | right structure per op; O(1)/O(log n) where expected; no needless scans | O(n) scans where a map/heap/trie was called for |
| **API / semantics** | med | clear contracts, consistent errors, sensible return values | ambiguous returns, silent failure, inconsistent missing-key handling |
| **Edge handling** | med | boundaries (exact expiry, empty, ties, capacity N+1) correct without prompting | only happy path until hidden tests forced it |
| **Clarity** | low | readable, named well, no dead code | works but hard to follow |

Overall verdict = weighted read, not an average. State it in one paragraph: would this pass the round, and at what level (no-hire / mixed / hire / strong-hire), with the single biggest lever to improve.

Also report:
- **Time:** total vs budget, per-part splits, where they lost time.
- **Hints:** count; each hint caps the ceiling on Incremental design.
- **Growth story:** the one early decision that most helped or hurt later parts — this is the takeaway to remember.

## Repo mode adjustments

Swap **Incremental design** for **Diagnosis & minimal diff**:
- Did they find the root cause or patch the symptom / game the test?
- Was the diff minimal and targeted, or a rewrite?
- Any regression in previously-passing tests? (Any regression caps the score at 2.)
- Public API preserved as required?
Keep Correctness, Complexity, Edge handling, Clarity.

## Follow-up discussion questions (always give 3–5 at wrap-up)

Talk-through, not code. Tailor to the problem; draw from:
- **Concurrency:** "This is single-threaded. Where are the races if two callers hit it at once? How would you make it safe?"
- **Persistence:** "It's in-memory. How would you persist and recover without losing the last N writes?"
- **Scale:** "10× the keys/orders/events — what breaks first, and what's your first structural change?"
- **Failure modes:** "A node dies mid-transfer/mid-fill/mid-rollback — how do you keep state consistent?"
- **Distribution:** "Shard this across nodes — how do you keep [rate windows / rankings / counts] correct?"
- **API evolution:** "A new requirement lands (versioned TTLs, per-tenant limits) — what in your design absorbs it, what fights it?"

Frame each to the specific problem's nouns. These mirror what a real interviewer asks after the coding is done — the design conversation is often what separates levels.
