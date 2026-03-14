# Problem Patterns Guide

Use this reference when generating problems and recognizing patterns. Users can add custom patterns at the end.

---

## 1. Sliding Window

**When to use:**
- Problems involving contiguous subarrays or substrings
- "Find longest/shortest subarray with condition"
- "Find all subarrays that match criteria"

**Key indicators:**
- Contiguous sequence required
- Window size may be fixed or variable
- Often involves optimization (max/min)

**Template:**
```python
def sliding_window(arr, k):
    window_start = 0
    result = 0
    window_state = {}  # or other tracking structure

    for window_end in range(len(arr)):
        # Add element at window_end to window state

        # Shrink window if condition violated
        while condition_violated:
            # Remove element at window_start from state
            window_start += 1

        # Update result

    return result
```

**Example problems:**
- Maximum Sum Subarray of Size K
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Find All Anagrams in a String

---

## 2. Two Pointers

**When to use:**
- Sorted arrays or linked lists
- Finding pairs with certain conditions
- Comparing elements from both ends
- In-place array modifications

**Key indicators:**
- Array is sorted or can be sorted
- Need to find pairs/triplets
- Comparing elements at different positions

**Template:**
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return []
```

**Example problems:**
- Two Sum II (sorted array)
- 3Sum
- Container With Most Water
- Remove Duplicates from Sorted Array

---

## 3. Fast & Slow Pointers

**When to use:**
- Cycle detection in linked lists or arrays
- Finding middle of linked list
- Finding cycle length or start

**Key indicators:**
- Linked list problems
- Need to detect loops
- Finding a specific position (middle, nth from end)

**Template:**
```python
def fast_slow_pointers(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True  # Cycle found

    return False
```

**Example problems:**
- Linked List Cycle
- Find Middle of Linked List
- Happy Number
- Palindrome Linked List

---

## 4. Merge Intervals

**When to use:**
- Problems with overlapping intervals
- Scheduling or time-based problems
- Merging or inserting intervals

**Key indicators:**
- Input is list of intervals [start, end]
- Need to merge, insert, or check overlap
- Often involves sorting by start time

**Template:**
```python
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:  # Overlapping
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged
```

**Example problems:**
- Merge Intervals
- Insert Interval
- Meeting Rooms I & II
- Interval List Intersections

---

## 5. Cyclic Sort

**When to use:**
- Array contains numbers in range 1 to n
- Finding missing or duplicate numbers
- Placing each number at its correct index

**Key indicators:**
- Numbers in range [1, n] or [0, n]
- Find missing/duplicate numbers
- O(n) time complexity expected

**Template:**
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1  # Where this number should be

        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    return nums
```

**Example problems:**
- Find Missing Number
- Find All Duplicates
- Find the First Missing Positive
- Find Corrupt Pair

---

## 6. In-place Linked List Reversal

**When to use:**
- Reversing linked list without extra space
- Reversing portions of linked list
- Rearranging linked list nodes

**Key indicators:**
- Must reverse in O(1) space
- Reverse entire list or sublist
- Modify links, not values

**Template:**
```python
def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
```

**Example problems:**
- Reverse Linked List
- Reverse Linked List II (between positions)
- Reverse Nodes in k-Group
- Swap Nodes in Pairs

---

## 7. Tree BFS (Breadth-First Search)

**When to use:**
- Level-order traversal
- Finding shortest path in unweighted graph/tree
- Processing nodes level by level

**Key indicators:**
- "Level by level" in problem
- Shortest path in unweighted structure
- Need to process all nodes at same depth together

**Template:**
```python
from collections import deque

def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

**Example problems:**
- Binary Tree Level Order Traversal
- Minimum Depth of Binary Tree
- Binary Tree Zigzag Level Order
- Average of Levels in Binary Tree

---

## 8. Tree DFS (Depth-First Search)

**When to use:**
- Path-related problems
- Tree traversals (preorder, inorder, postorder)
- Problems requiring backtracking in trees

**Key indicators:**
- Find all paths, any path, specific path
- Root-to-leaf traversal
- Need to explore all branches

**Template:**
```python
def dfs(root, target, path, result):
    if not root:
        return

    path.append(root.val)

    # Check if leaf and matches condition
    if not root.left and not root.right and sum(path) == target:
        result.append(list(path))

    # Recurse
    dfs(root.left, target, path, result)
    dfs(root.right, target, path, result)

    # Backtrack
    path.pop()
```

**Example problems:**
- Path Sum I, II, III
- Maximum Depth of Binary Tree
- Diameter of Binary Tree
- Lowest Common Ancestor

---

## 9. Two Heaps

**When to use:**
- Finding median in data stream
- Problems needing smallest and largest simultaneously
- Scheduling with priorities

**Key indicators:**
- "Median" in problem
- Need to track both ends of sorted data
- Continuous updates with queries

**Template:**
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negated values)
        self.large = []  # Min heap

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

**Example problems:**
- Find Median from Data Stream
- Sliding Window Median
- IPO (maximize capital)

---

## 10. Subsets / Backtracking

**When to use:**
- Generate all combinations/permutations
- Power set generation
- Problems with "all possible" solutions

**Key indicators:**
- "All combinations" or "all permutations"
- Need to explore all possibilities
- Generate subsets of input

**Template:**
```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(list(current))

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

**Example problems:**
- Subsets I & II
- Permutations I & II
- Combination Sum
- Generate Parentheses

---

## 11. Modified Binary Search

**When to use:**
- Searching in sorted/rotated arrays
- Finding boundaries or positions
- Search space reduction problems

**Key indicators:**
- Sorted array (possibly rotated)
- O(log n) required
- Finding specific position, not just existence

**Template:**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # or left for insertion point
```

**Example problems:**
- Search in Rotated Sorted Array
- Find First and Last Position
- Search a 2D Matrix
- Find Peak Element

---

## 12. Top K Elements

**When to use:**
- Finding K largest/smallest elements
- K most frequent elements
- K closest points

**Key indicators:**
- "K largest/smallest/frequent"
- Need partial sorting
- Priority queue natural fit

**Template:**
```python
import heapq

def top_k_frequent(nums, k):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Min heap of size k
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]
```

**Example problems:**
- Kth Largest Element
- Top K Frequent Elements
- K Closest Points to Origin
- Sort Characters by Frequency

---

## 13. K-way Merge

**When to use:**
- Merging multiple sorted lists
- Finding smallest range covering K lists
- External sorting scenarios

**Key indicators:**
- Multiple sorted arrays/lists
- Need to merge into one sorted output
- Finding elements across K sorted inputs

**Template:**
```python
import heapq

def merge_k_lists(lists):
    heap = []

    # Add first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result
```

**Example problems:**
- Merge K Sorted Lists
- Kth Smallest Element in Sorted Matrix
- Smallest Range Covering Elements from K Lists

---

## 14. Topological Sort

**When to use:**
- Task scheduling with dependencies
- Course prerequisites
- Build order problems

**Key indicators:**
- Dependencies between tasks
- Need to find valid ordering
- Directed acyclic graph (DAG) problems

**Template:**
```python
from collections import deque

def topological_sort(num_vertices, edges):
    # Build graph and count incoming edges
    graph = {i: [] for i in range(num_vertices)}
    in_degree = {i: 0 for i in range(num_vertices)}

    for parent, child in edges:
        graph[parent].append(child)
        in_degree[child] += 1

    # Start with nodes that have no incoming edges
    queue = deque([v for v in in_degree if in_degree[v] == 0])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == num_vertices else []  # Empty if cycle
```

**Example problems:**
- Course Schedule I & II
- Alien Dictionary
- Task Scheduler
- Minimum Height Trees

---

## Custom Patterns

Add your own patterns below. Follow the same format:
- When to use
- Key indicators
- Template code
- Example problems

<!-- Add custom patterns here -->
