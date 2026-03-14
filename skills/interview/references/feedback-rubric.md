# Interview Feedback Rubric

Use this rubric when evaluating user solutions and providing feedback.

---

## Scoring Dimensions

### 1. Code Quality - PASS/FAIL

| Result | Criteria |
|--------|----------|
| **PASS** | Flawless: Clean, readable code with excellent naming, optimal structure, handles ALL edge cases, no redundancy, production-ready |
| **FAIL** | Any issues present: poor naming, missing edge cases, suboptimal structure, magic numbers, redundancy, hard to follow, or wouldn't pass code review |

**Any of these = FAIL:**
- Suboptimal time or space complexity (must be optimal for the problem)
- Poor naming (single letters except loop counters)
- Improper indentation or inconsistent formatting
- Magic numbers (use named constants)
- Functions not single-responsibility or too large (>20 lines without reason)
- Any unhandled edge case (empty input, single element, duplicates, negatives, overflow)
- Unnecessary code, dead code, or excessive comments
- Inefficient data structure choices
- Code duplication/redundancy
- Overly complex logic (nested ternaries, deep nesting >3 levels)
- Unnecessarily clever/hard to read code
- Missing early returns (deep nesting instead)
- Overengineered solution

---

### 2. Testing & Verification - PASS/FAIL

| Result | Criteria |
|--------|----------|
| **PASS** | Code runs correctly on first attempt, all test cases pass, no bugs, comprehensive edge case coverage |
| **FAIL** | Any bugs, failed test cases, runtime errors, multiple attempts needed, or missed edge cases |

**Any of these = FAIL:**
- More than 1 run/attempt needed
- Any missed test case
- Any bug discovered in code
- Runtime error or crash
- Infinite loop or timeout
- Off-by-one errors
- Boundary condition failures
- Type errors or exceptions
- Logic errors

---

### 3. Problem-Solving Process - PASS/FAIL

| Result | Criteria |
|--------|----------|
| **PASS** | Wrote clear comments, discussed trade-offs, responded thoughtfully to follow-ups |
| **FAIL** | Missing comments, gaps in reasoning, or unclear thought process |

**Any of these = FAIL:**
- Missing comments for non-obvious logic
- Did not discuss trade-offs when asked
- Did not respond thoughtfully to follow-up questions
- Gaps in reasoning or unclear explanations

---

**Language Internals (warning, then fail):**
Hidden complexity from language internals (e.g., string concatenation in Java vs StringBuilder, list slicing in Python) does not count against the user for the **first 2 occurrences**. Provide feedback each time. After 2 warnings, it becomes a FAIL.

**Check `interview/performance/feedback_{problem_name}.md` for prior warnings before evaluating.**

Examples:
- Java: `str += char` in a loop is O(n²) - use StringBuilder
- Python: `list[1:]` slicing creates a copy - O(n) each time
- JavaScript: `array.shift()` is O(n) - consider different approach

---

## Feedback Categories

### Positive Feedback Examples

**Problem Solving:**
- "Great job breaking down the problem into smaller steps"
- "Excellent edge case identification before coding"
- "Good instinct to sort the input first"

**Code Quality:**
- "Clean variable naming makes the code easy to follow"
- "Good use of helper functions to improve readability"
- "Well-structured solution with clear logic flow"

**Problem-Solving Process:**
- "Great job explaining your approach before coding"
- "Good questions to clarify requirements"
- "Clear comments made the code easy to follow"

### Constructive Feedback Examples

**Approach:**
- "Consider using [pattern] for this type of problem"
- "Think about how sorting might simplify the problem"
- "This is O(n²) - can you reduce it with a hash map?"

**Code Quality:**
- "Variable names like 'x' and 'temp' could be more descriptive"
- "Consider extracting this logic into a helper function"
- "The nested loops make this hard to follow - can you simplify?"

**Testing:**
- "Remember to test edge cases like empty input"
- "Trace through your solution with a small example first"
- "What happens when all elements are the same?"

---

## Actionable Improvement Templates

### For Algorithm Knowledge Gaps:
```
Study: [Algorithm name]
Why: [How it applies to this problem]
Resource: [Specific problem or article]
Practice: [Similar problems to try]
```

### For Code Quality Issues:
```
Issue: [Specific problem]
Better approach: [Example of improved code]
Benefit: [Why this is better]
```

### For Time Management:
```
Observation: [What took too long]
Suggestion: [How to speed up]
Target: [Time goal for similar problems]
```

---

## Overall Rating

```
Overall = PASS only if ALL three dimensions pass

Code Quality: PASS/FAIL
Testing & Verification: PASS/FAIL
Problem-Solving Process: PASS/FAIL

Final Result: PASS (all three pass) or FAIL (any dimension fails)
```

**Note:** This is a strict evaluation. Unless the code is spick and span across all dimensions, it's a fail. There is no partial credit.

### Result Interpretation

| Result | Meaning | Recommendation |
|--------|---------|----------------|
| **PASS** | Interview-ready | Maintain skills, ready for real interviews |
| **FAIL** | Not ready | Review feedback, identify gaps, practice more |

---

## Personalized Cheat Sheet Generation

After providing feedback, generate a **minimal, actionable cheat sheet** based on the user's specific weaknesses. Cheat sheets are saved to the user's profile for future reference.

### Process:
1. Identify 1-2 key areas where the user struggled
2. Propose a specific cheat sheet recommendation to the user
3. **Ask for confirmation** before adding to their profile
4. Keep cheat sheets concise (max 5-7 bullet points each)

### Cheat Sheet Categories:

**Problem-Solving Approach:**
- Step-by-step frameworks for specific problem types
- When to use which data structure
- Common patterns and when to apply them

**Code Writing Patterns:**
- Cleaner ways to write specific constructs
- Idiomatic code patterns for the user's language
- Refactoring techniques for common issues

**Alternative Implementations:**
- Different approaches to the same problem
- Trade-offs between solutions
- When to choose one approach over another

### Example Prompt to User:
```
Based on your solution, I noticed [specific issue].

I recommend adding a cheat sheet on: "[Topic]"

Example content:
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

Would you like me to add this to your profile? (yes/no)
```

### Rules:
- Never add cheat sheets without user confirmation
- Keep recommendations specific, not generic
- One cheat sheet per session maximum
- Update existing cheat sheets rather than creating duplicates
