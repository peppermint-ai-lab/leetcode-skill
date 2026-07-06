# Pattern Recognition & Canonical Templates

Each entry: recognition cues (what in the problem description signals this pattern) + minimal Python template.

---

## Two Pointers

**Recognize when:**
- Sorted array, find pair/triplet with target sum
- "Remove duplicates in-place"
- Palindrome check
- Two arrays to merge/compare

**Template:**
```python
l, r = 0, len(nums) - 1
while l < r:
    if condition:
        l += 1
    else:
        r -= 1
```

---

## Sliding Window

**Recognize when:**
- "Subarray/substring of length k"
- "Longest/shortest subarray satisfying condition"
- Window grows right, shrinks left

**Fixed window:**
```python
window_sum = sum(nums[:k])
for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]
```

**Variable window:**
```python
l = 0
for r in range(len(nums)):
    # expand: add nums[r]
    while not valid:
        # shrink: remove nums[l]
        l += 1
```

---

## Binary Search

**Recognize when:**
- Sorted array, O(log n) required
- "Find minimum/maximum that satisfies condition"
- Search space is monotone (once true, stays true)

**Classic:**
```python
l, r = 0, len(nums) - 1
while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target: return mid
    elif nums[mid] < target: l = mid + 1
    else: r = mid - 1
```

**First-true template:**
```python
l, r = lo, hi
while l < r:
    mid = (l + r) // 2
    if ok(mid): r = mid
    else: l = mid + 1
return l
```

---

## BFS

**Recognize when:**
- Shortest path in unweighted graph/grid
- Level-order traversal
- "Minimum steps/moves"

**Template:**
```python
from collections import deque
q = deque([start])
seen = {start}
steps = 0
while q:
    for _ in range(len(q)):
        node = q.popleft()
        if node == target: return steps
        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei)
                q.append(nei)
    steps += 1
```

---

## DFS / Backtracking

**Recognize when:**
- "All combinations/permutations/subsets"
- Explore all paths in tree/graph
- Constraint satisfaction (N-Queens, Sudoku)

**Template:**
```python
def backtrack(start, path):
    if base_case:
        result.append(path[:])
        return
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
```

---

## Dynamic Programming (1D)

**Recognize when:**
- "Maximum/minimum/count ways"
- Overlapping subproblems
- Decision at each step affects future

**Template:**
```python
dp = [0] * (n + 1)
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = f(dp[i-1], dp[i-2], ...)
return dp[n]
```

---

## Dynamic Programming (2D)

**Recognize when:**
- Two sequences (LCS, edit distance)
- Grid paths
- Knapsack variants

**Template:**
```python
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if match: dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
return dp[m][n]
```

---

## Heap / Priority Queue

**Recognize when:**
- "K largest/smallest"
- "Always process minimum/maximum next"
- Dijkstra, merge K sorted lists

**Template:**
```python
import heapq
heap = []
heapq.heappush(heap, (priority, item))
priority, item = heapq.heappop(heap)
# Max-heap: negate values
heapq.heappush(heap, (-val, item))
```

---

## Monotonic Stack

**Recognize when:**
- "Next greater/smaller element"
- "Previous greater/smaller element"
- Histogram area problems

**Template:**
```python
stack = []  # stores indices
for i, val in enumerate(nums):
    while stack and nums[stack[-1]] < val:  # adjust comparison per problem
        idx = stack.pop()
        # process idx — next greater is i
    stack.append(i)
```

---

## Greedy

**Recognize when:**
- Local optimal = global optimal
- "Minimum number of X to cover Y"
- Interval scheduling, jump game

**Template:**
```python
# Sort by relevant key first
items.sort(key=lambda x: x[1])
end = float('-inf')
count = 0
for start, finish in items:
    if start >= end:
        count += 1
        end = finish
```

---

## Intervals

**Recognize when:**
- "Merge overlapping intervals"
- "Insert interval"
- Meeting rooms, scheduling

**Template:**
```python
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
```

---

## Linked List

**Recognize when:**
- Reverse, cycle detection, merge
- "In-place" with O(1) space

**Fast/slow pointers:**
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is at midpoint
```

---

## Trees

**Recognize when:**
- Any binary tree traversal, path sum, LCA

**DFS recursive:**
```python
def dfs(node):
    if not node: return base
    left = dfs(node.left)
    right = dfs(node.right)
    return f(left, right, node.val)
```
