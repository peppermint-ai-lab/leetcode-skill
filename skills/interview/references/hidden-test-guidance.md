# Hidden Test Case Generation Guide

When evaluating user solutions, generate hidden test cases that thoroughly validate correctness beyond the visible examples.

## Test Case Categories

### 1. Edge Cases (Required)
Every problem should test these where applicable:

| Category | Examples |
|----------|----------|
| Empty input | `[]`, `""`, `None` |
| Single element | `[1]`, `"a"` |
| Two elements | `[1, 2]` - minimum for pair operations |
| All same values | `[5, 5, 5, 5]` |
| All different values | `[1, 2, 3, 4, 5]` |
| Sorted input | `[1, 2, 3, 4, 5]` |
| Reverse sorted | `[5, 4, 3, 2, 1]` |
| Negative numbers | `[-5, -1, 0, 3]` |
| Zero values | `[0, 0, 0]`, target=0 |
| Maximum constraints | Near upper bound of stated constraints |

### 2. Boundary Conditions
Test at the limits of constraints:

```python
# If constraint says: 1 <= n <= 10^5
test_min = [1]           # n = 1
test_near_max = [...]    # n = 1000 (reasonable for hidden test)

# If constraint says: -10^9 <= val <= 10^9
test_large_positive = [10**9, 10**9 - 1]
test_large_negative = [-10**9, -10**9 + 1]
test_overflow_prone = [10**9, 10**9]  # Sum would overflow in some languages
```

### 3. Pattern-Specific Cases

#### Arrays/Strings
- First element is answer
- Last element is answer
- Answer doesn't exist (return -1, None, or empty)
- Duplicates at critical positions

#### Two Pointers
- Pointers meet immediately
- Pointers never meet (no solution)
- Multiple valid answers

#### Sliding Window
- Window size equals array length
- Window size is 1
- All elements satisfy/don't satisfy condition

#### Trees/Graphs
- Single node
- Linear tree (all left or all right children)
- Complete/balanced tree
- Disconnected components (for graphs)

#### Dynamic Programming
- Base case only (n=0, n=1)
- Repeated subproblems with same value
- Maximum recursion depth scenario

### 4. Correctness Traps
Cases that catch common bugs:

```python
# Off-by-one errors
test_boundary = [1, 2, 3, 4, 5], target=5  # Last element
test_boundary = [1, 2, 3, 4, 5], target=1  # First element

# Integer overflow (hint in feedback if applicable)
test_overflow = [10**9, 10**9]  # Sum > 32-bit int

# Floating point
test_float_trap = [1, 3], need_avg=True  # 2.0 vs 2

# Modifying input while iterating
test_mutation = [1, 2, 3, 4, 5]  # Verify input unchanged if required
```

### 5. Large Input Tests (Optional)
Test with larger inputs to verify correctness at scale:

```python
# Larger input to catch subtle bugs
large_input = list(range(1000))  # 1k elements
# Verifies solution handles bigger inputs correctly
```

**Note:** Complexity analysis is done by the AI during evaluation,
not by automated timeouts. The AI will push back if solution is suboptimal.

## Generation Template

For each problem, generate 3-5 hidden tests:

```python
# Hidden Test 1: Edge case - empty/minimal input
assert solution([]) == expected

# Hidden Test 2: Edge case - boundary condition
assert solution([extreme_value]) == expected

# Hidden Test 3: Correctness trap - common bug catcher
assert solution([trap_input]) == expected

# Hidden Test 4: Pattern-specific edge case
assert solution([pattern_edge]) == expected

# Hidden Test 5 (optional): Stress test for complexity
assert solution([large_input]) == expected  # Must complete quickly
```

## What NOT to Test

- Don't test invalid inputs (assume inputs meet constraints)
- Don't test implementation details (multiple correct approaches OK)
- Don't create "gotcha" cases unrelated to the algorithm
- Don't make stress tests so large they timeout legitimate solutions

## Scoring Hidden Tests

| Result | Meaning |
|--------|---------|
| All pass | Full credit |
| 1-2 fail | Partial - identify which category failed |
| Most fail | Fail - likely fundamental algorithm issue |
| Timeout | Note complexity issue in feedback |
