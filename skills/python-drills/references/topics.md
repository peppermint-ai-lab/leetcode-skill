# Python Drills — Topic Reference

Read this file at the start of every session. Pick drills in order per topic, rotating across sessions.

**Rule for presenting drills:** Describe the task in plain English. Never name the method, function, or import the user should use. Say what to accomplish, not how.

---

## Topic: deque

**Import:** `from collections import deque`

### drill-1: Basic operations
- Create an empty queue. Then create one initialized from the list `[1, 2, 3]`.
- Add 4 to the back.
- Add 0 to the front.
- Remove and print the front element.
- Remove and print the back element.
- Print how many elements remain.
- Print whether the queue is empty.
- Look at the front element without removing it.
- Look at the back element without removing it.

### drill-2: BFS skeleton
Write a complete BFS on an undirected graph. Use a queue. Track which nodes you've already visited so you don't revisit them. Return all visited nodes in the order you visited them.

Input: `graph = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}`, start at node 0.

### drill-3: Bounded queue
Create a queue that holds at most 3 items. Add the numbers 1 through 6 to the back one at a time — after each add, print the current contents. Notice what happens when it's full.

Then: given `nums = [2,1,5,3,6,4]`, use a bounded queue of size 3 to find the largest value in each group of 3 consecutive numbers.

### drill-4: Sliding window maximum
Given `nums = [1,3,-1,-3,5,3,6,7]` and window size `k = 3`, find the maximum in each window.
Expected: `[3,3,5,5,6,7]`

Store positions (not values) in your queue. Keep the queue so the front always points to the maximum of the current window. Drop positions that fall outside the window from the front; drop positions whose values are smaller than the current number from the back.

### drill-5: Shift all elements
Given the sequence `[1,2,3,4,5]`, do two independent operations (each starting from the original):
- Shift right by 2 → `[4,5,1,2,3]`
- Shift left by 2 → `[3,4,5,1,2]`

Print both results. Use a deque — it has a single built-in method for this.

---

## Topic: defaultdict

**Import:** `from collections import defaultdict`

### drill-1: Frequency count
Given `s = "aabbcddee"`, count how many times each character appears. You must not write any `if` check to see whether a key exists before incrementing.

### drill-2: Group anagrams
Given `words = ["eat","tea","tan","ate","nat","bat"]`, group words that are anagrams of each other. Two words are anagrams if they have the same characters. Print the groups.

### drill-3: Build adjacency list
Given undirected edges `[(0,1),(0,2),(1,2),(2,3)]`, build a graph where you can look up all neighbors of any node. Since edges are undirected, each edge goes both ways. Print all neighbors of node 0.

### drill-4: Three frequency methods
Count `s = "mississippi"` character frequencies three different ways (without Counter):
1. A dict that never raises a KeyError when a key is missing — give it a default of 0
2. A regular dict using the method that sets a default if the key is absent
3. A regular dict using `.get()` with a fallback value

Print all three results and verify they match.

### drill-5: Nested frequency map
For `s = "abacab"`, build a table where you can look up how many times a character appears at a specific index position. Neither level of the table should raise a KeyError on a missing key. Print how many times 'a' appears at positions 0, 2, and 4.

---

## Topic: counter

**Import:** `from collections import Counter`

### drill-1: Basic frequency
Given `"mississippi"`:
- Find the 3 most frequent characters
- Count how many distinct characters appear
- Look up the count of 'x' — it should return 0, not raise an error

### drill-2: Anagram check
Write `is_anagram(s, t)` with a one-line body. It should return True if the two strings are anagrams. Test: `("anagram","nagaram")` → True, `("rat","car")` → False.

### drill-3: Counter arithmetic
Given `a = Counter("aab")` and `b = Counter("bbc")`, compute:
- Combined counts (add both together)
- What's left in `a` after removing `b`'s counts (any result ≤ 0 disappears)
- The overlap — minimum count of each shared character
- The union — maximum count of each character across both

Predict the output before running.

### drill-4: Top and bottom
Given `words = ["the","cat","sat","on","the","mat","the","cat"]`:
- Find the 2 most frequent words
- Find the least frequent word

### drill-5: Sliding window anagram detection
Return True if any permutation of `p = "ab"` appears as a substring of `s = "eidbaooo"`. Expected: True.

Build an initial frequency snapshot from the first `len(p)` characters of `s`. As the window moves right one step at a time, update by counting in the new character and counting out the old one — do not rebuild from scratch each step.

---

## Topic: heapq

**Import:** `import heapq`
**Note for AI:** Never tell the user this is a min-heap or that they need to negate for max — let them figure it out or ask for a hint.

### drill-1: Priority queue basics
Given `[3,1,4,1,5,9,2,6]`, rearrange it in-place so it satisfies the heap property. Then remove the smallest element 4 times, printing each one. They should come out in ascending order.

### drill-2: Largest elements
Find the 3 largest values in `[3,1,4,1,5,9,2,6]` using a heap. The heap always gives you the smallest first — figure out how to flip that behavior. Do not use any built-in "find largest" shortcut function.

### drill-3: Task scheduler
Given tasks `[("send email",3),("fix bug",1),("write tests",2),("deploy",1)]` where the number is priority (1 = most urgent), process them in priority order using a heap. Pop and print each task.

### drill-4: K closest points
Given `points = [[1,3],[-2,2],[5,8],[0,1]]`, return the 2 points closest to the origin. Use a heap with a distance-based ordering.

### drill-5: Merge K sorted lists
Merge `[[1,4,7],[2,5,8],[3,6,9]]` into one sorted list using a heap. At each step, take the globally smallest remaining element, then bring in the next element from the same source list.
Expected: `[1,2,3,4,5,6,7,8,9]`

### drill-6: Atomic push-pop
Given a valid heap `h = [1,3,5,7,9]`:
- Add 4 and immediately get back the smallest — in one operation. What comes out?
- Get the smallest and then put in 0 — in one operation. What comes out?

Write a comment on how these two differ.

---

## Topic: sorting

### drill-1: Sort by length, then alphabetically
Sort `["banana","apple","cherry","fig","date","kiwi"]` so shorter words come first, and words of equal length appear alphabetically. Do it in a single call with a tuple key.

### drill-2: Multi-key sort with a non-negatable field
Sort `pairs = [(1,'b'),(3,'a'),(1,'a'),(2,'c'),(3,'b')]`:
- First number ascending
- For ties, the letter descending (z before a)

You can't negate a string. Think about what Python's sort stability lets you do.

### drill-3: Positions of sorted order
Given `nums = [3,1,4,1,5,9,2,6]`, find the positions you'd visit if you read the list in sorted order.
Expected: `[1,3,6,0,2,4,7,5]`

### drill-4: Sort custom objects
Create a `Task` class with a `name` and a `priority`. Create a list of Tasks and sort them by priority from lowest to highest number. Do it two ways: with a lambda and with `attrgetter` from the `operator` module.

### drill-5: Descending sort — three ways
Sort `nums = [3,1,4,1,5,9]` from largest to smallest three different ways. Add a comment on which you'd reach for in an interview and why.

---

## Topic: comprehensions

### drill-1: Filter and transform
Given `nums = [1,2,3,4,5,6,7,8,9,10]`:
- Build a list of squares of only the even numbers
- Build a list where each element is the string `"even"` or `"odd"` — inline, not a separate if-block

### drill-2: Flatten
Given `matrix = [[1,2,3],[4,5,6],[7,8,9]]`, produce `[1,2,3,4,5,6,7,8,9]` in one line.

### drill-3: Dict and set comprehensions
Given `words = ["hello","world","python","hi","code"]`:
- A mapping from each word to its length
- The reverse mapping (length → word, last one wins on collision)
- A collection of all distinct word lengths

### drill-4: Matrix transpose
Transpose `matrix = [[1,2,3],[4,5,6],[7,8,9]]` two ways:
1. A nested one-liner — build each new row by picking one element from each original row
2. A one-liner using a built-in that pairs up elements across multiple iterables — add a comment explaining what the `*` does here

### drill-5: Generator expression
Compute the sum of squares of 1 through 1,000,000 without building a list in memory. Add a comment explaining the memory difference.

### drill-6: Conditional dict comprehension
Given `students = [("Alice",85),("Bob",92),("Carol",78),("Dave",95)]`:
- A list of names of students who scored above 90
- A score map for students who scored above 80
- A map of every student to `"pass"` or `"fail"` (pass if score ≥ 80)

---

## Topic: string-ops

### drill-1: join and split
Given `words = ["the","quick","brown","fox"]`:
- Combine into one string with a space between each word
- Combine with `", "` between each
- Combine with nothing between each

Given `s = "  hello   world  "`:
- Split it two different ways. Print both and add a comment on how they differ.

### drill-2: Slicing tricks
Given `s = "Hello, World!"`:
- Reverse it using slicing
- Every other character
- Last 6 characters — two different ways
- Check if it's a palindrome in one line

### drill-3: Common string methods
Given `s = "  Hello, World!  "`: strip whitespace, lowercase it, replace "world" with "python". Also: count how many times 'l' appears, find the position of "world", check if it starts with "hello" (after stripping).

### drill-4: f-strings
Given `name = "Alice"`, `score = 95.678`, `rank = 3`:
1. Print: `Alice scored 95.68 (rank #3)` — score must show exactly 2 decimal places
2. Print a table row: name left-aligned in 20 characters, score right-aligned in 8 characters with 2 decimal places

### drill-5: String analysis
Given `s = "racecar"`:
- Is it a palindrome? One line.
- Are all characters unique? One line.
- What is the most frequent character? Use the right tool. Also write the naive one-liner and add a comment on why it's slow.

---

## Topic: iteration

### drill-1: Indexed iteration
Given `fruits = ["apple","banana","cherry","date"]`:
- Print each with its position, starting from 0
- Print each with its position, starting from 1
- Find the position of "cherry" without using the list's built-in search method — write a one-liner that stops as soon as it finds the answer

### drill-2: Paired iteration
Given `names = ["Alice","Bob","Carol"]` and `scores = [85,92,78]`:
- Combine into a list of pairs
- Build a name-to-score dictionary in one line
- Find the name with the highest score in one line

### drill-3: Unequal length pairing
Given `a = [1,2,3]` and `b = [10,20]`, combine them element-by-element treating missing values as 0. First do it manually (to understand the behavior), then use the standard library version.

### drill-4: Range patterns
Write the range expression for:
- Counting down from 10 to 1 inclusive
- Generating 0, 2, 4, 6, 8, 10
- Reversed indices for a list of length n

### drill-5: Unpacking
Demonstrate:
1. Swap two variables without a temp variable
2. Pull the first element off a list and collect the rest
3. Get just the first and last elements of `[1,2,3,4,5]`, ignoring the middle
4. Transpose `rows = [(1,2,3),(4,5,6)]` into columns — add a comment explaining what the `*` does here

---

## Topic: graph-templates

Drills here are about typing the skeleton from memory. Focus on getting the Python structure right, not explaining the algorithm.

### drill-1: BFS shortest path
Find the shortest path from node 0 to node 3 in `graph = {0:[1,2], 1:[0,3,4], 2:[0,4], 3:[1], 4:[1,2]}`. Return it as a list of nodes. Return `[]` if no path exists. Use a queue. Track how you reached each node so you can reconstruct the path at the end.

### drill-2: DFS recursive
Find all nodes reachable from node 0 in `graph = {0:[1,2], 1:[0,3], 2:[0], 3:[1]}`. Return them as a set. Write it recursively. There's a common Python bug with default function arguments — avoid it and write a comment explaining what the bug is.

### drill-3: DFS iterative
Same goal as drill-2. Write it without recursion using a plain list as a stack. Python's default call stack limit is around 1000 frames — iterative DFS is the safe default on interview platforms.

Key detail: check `if u in seen: continue` at the top of the loop (not before pushing neighbors), and push neighbors in reversed order if you want to match recursive visit order.

### drill-4: Dijkstra with stale-entry skip
Find the shortest distance from node 0 to every other node:
```python
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
```
Each tuple is `(neighbor, cost)`. Return a distances list indexed by node. Expected: `[0, 3, 1, 4]`.

Push `(cost, node)` tuples. When you pop, check if the popped distance matches the recorded distance — if not, skip it (stale entry). This is the correct production pattern.

### drill-5: Topological sort (Kahn's)
Given `edges = [(0,1),(0,2),(1,3),(2,3),(3,4)]` for a 5-node DAG, return a valid ordering where every node appears before the nodes it points to. Start with nodes that have nothing pointing at them and work outward. If a cycle exists, return an empty list.

### drill-6: Union-Find (DSU)
Implement a `DSU` (Disjoint Set Union) class for `n` nodes with:
- Path compression in find (use the two-step halving trick: `parent[x] = parent[parent[x]]` before moving up)
- Union by rank
- Returns `False` if the two nodes are already in the same set

Test: create DSU(5), union several pairs, verify that nodes in the same component return the same root.

---

## Topic: classes

### drill-1: Heap-compatible class
Create a `Task` class with a priority number and a name. Make it so you can push Task objects directly into a heap and have them come out in priority order — without wrapping them in tuples. Push `Task(2,"write tests")`, `Task(1,"fix bug")`, `Task(3,"deploy")` and pop all in order.

### drill-2: Auto-generated comparisons
Rewrite `Task` so Python generates the comparison methods for you automatically, based on priority. The name should not affect ordering. Add a comment explaining what the decorator flag does under the hood.

### drill-3: Two string representations
Create `Point(x, y)`. Make it so:
- When a Point appears inside a list it shows as `Point(3, 4)`
- When you print a Point directly it shows as `(3, 4)`

Show the difference with `repr(p)`, `str(p)`, `print(p)`, and `[p]`.

### drill-4: Immutable value object
Represent a 2D point in two different ways that are both immutable and let you access coordinates by name. Demonstrate: getting `x`, unpacking into two variables, and that assignment after creation fails for both.

### drill-5: Alternate constructors and validators
Create a `Temperature` class that stores a Celsius value.
- Add an alternate way to create one from a Fahrenheit value
- Add a way to check if a temperature value is physically valid (above absolute zero)

`Temperature.from_fahrenheit(212)` should give 100°C. `Temperature.is_valid(-300)` should return False.

---

## Topic: oop

Interview-focused OOP. Each drill tests one concept. All drills should include pytest tests.

### drill-1: Inheritance and override
Create a base class `Shape` with a method that returns its area (return 0 by default). Create two subclasses: `Rectangle(width, height)` and `Circle(radius)`. Each must return the correct area. Write tests confirming that a Rectangle and Circle both respond to the same area call and give different results.

Use `math.pi` for the circle. Show that calling the method on a plain `Shape` gives 0.

### drill-2: Abstract base class
Rewrite `Shape` so it's impossible to create a plain `Shape` instance — only subclasses with a real area implementation can be instantiated. Attempting `Shape()` should raise an error.

Keep the same `Rectangle` and `Circle` from drill-1. Write a test that confirms instantiating `Shape` directly raises the right kind of error.

### drill-3: Property with validation
Create a `BankAccount` with a balance. Make it so:
- Reading the balance works normally
- Setting the balance to a negative number raises a `ValueError`
- There's no public `_balance` or `__balance` attribute accessible from outside (use the right decorator)

Write tests: valid deposit raises no error, negative balance raises `ValueError`.

### drill-4: Magic methods — make a class behave like a built-in
Create a `Stack` class backed by a list. Make it so:
- `len(stack)` returns the number of items
- `str(stack)` prints the items in a readable way
- Two stacks with the same items compare as equal
- You can iterate over a stack with a for-loop

Write tests for each behavior.

### drill-5: Mixin
Create a `LogMixin` that adds a `log(message)` method storing messages in a list, and a `get_logs()` method returning them. Create a `Service` class that uses the mixin. `Service` should have its own `process(data)` method that does something and logs what it did.

Write a test: call `process` twice, then assert `get_logs()` has 2 entries.

### drill-6: Class variables vs instance variables
Create a `Counter` class (not collections.Counter) where:
- Every instance tracks its own count
- A class-level variable tracks how many `Counter` instances have ever been created

Write tests: create 3 counters, confirm the class-level total is 3. Increment one counter, confirm the others are unaffected.

### drill-7: __slots__
Create a `Point` class using `__slots__` to restrict it to only `x` and `y` attributes. Show that trying to add any other attribute raises an `AttributeError`. Write a test confirming this.

Add a comment explaining when you'd reach for `__slots__` in practice.

### drill-8: Operator overloading
Create a `Vector(x, y)` class. Make it so:
- Adding two vectors with `+` returns a new Vector
- Subtracting with `-` returns a new Vector
- Multiplying by a scalar with `*` returns a new Vector
- `str(v)` shows `Vector(3, 4)`

Write tests: `Vector(1,2) + Vector(3,4)` should equal `Vector(4,6)`.

---

## Topic: bisect

**Import:** `from bisect import bisect_left, bisect_right`
**Warning:** The `key=` parameter on `bisect_left`/`bisect_right` was added in 3.10. For 3.8-safe code, pre-compute a key list and bisect that instead.

### drill-1: Existence check
Given a sorted array `arr = [1, 3, 5, 7, 9, 11]`, write a function that checks if a target value exists in it — using binary search, not `in`. It must be O(log n). Test with values that exist and values that don't.

### drill-2: Count occurrences
Given `arr = [1, 2, 2, 2, 3, 4, 4, 5]`, count how many times the value 2 appears — using two binary search calls, not by iterating. Test it. Also test with a value that appears 0 times.

### drill-3: Insertion point
Given `arr = [1, 3, 5, 7, 9]`:
- Find where you would insert 4 to keep the array sorted (the index, not inserting it)
- Find where you would insert 5 — there are two valid answers depending on whether you want to go left or right of existing 5s. Show both.

### drill-4: Find first element ≥ target
Given `arr = [1, 3, 5, 7, 9]` and `target = 6`, return the first element that is ≥ target. Expected: 7. Return -1 if none exists. Write a test.

### drill-5: Binary search on a condition (first-true template)
Write a generic binary search that finds the smallest integer `x` in `[lo, hi]` for which a predicate `ok(x)` is True — assuming `ok` is monotone (False then True, never goes back). Test it: find the smallest `x` where `x * x >= 25` in range `[0, 100]`. Expected: 5.

---

## Topic: functools

**Import:** `from functools import lru_cache, cmp_to_key`
**Version note:** Use `@lru_cache(None)` — NOT `@cache` which is 3.9+ only.

### drill-1: Top-down DP with memoization
Given `nums = [2, 7, 9, 3, 1]` (house robber problem: can't rob adjacent houses), write a recursive solution with memoization that returns the maximum sum. Use a decorator to cache results — not a manual dict.

The function signature should be a nested function inside `solve(nums)` so the cache is scoped per call.

Write tests: `[2,7,9,3,1]` → 12, `[1,2,3,1]` → 4.

### drill-2: lru_cache on a method — the gotcha
Write a class `Fibonacci` that caches computed values. Try putting the memoization decorator directly on the instance method — then explain in a comment why this causes a memory leak (the instance never gets garbage collected). Show the correct pattern: use a module-level cached function instead.

### drill-3: Custom sort with cmp_to_key
Given `nums = [3, 30, 34, 5, 9]`, sort them so that concatenating them in order gives the largest possible number. Expected: `"9534330"`.

The comparison between two numbers `a` and `b` should check whether `str(a)+str(b)` is larger or smaller than `str(b)+str(a)`. Use `cmp_to_key` to convert this comparison function into a sort key.

Write a test.

### drill-4: Cache sizing
Write a function that computes the nth Fibonacci number using `lru_cache`. Then call it for n=0 through n=10 and print the cache info (hits, misses, cache size). Clear the cache and call again — show that misses reset.

---

## Topic: operator

**Import:** `from operator import itemgetter, attrgetter`

### drill-1: Sort by tuple field
Given `records = [(3,"banana"),(1,"apple"),(2,"cherry"),(1,"date")]`, sort by the first element ascending, then by the second element ascending for ties. Do it using `itemgetter` — not a lambda. Write a test.

### drill-2: Sort objects by attribute
Create a `Person` class with `name` and `age`. Sort a list of Persons by age ascending using `attrgetter`. Then sort by name. Do not use a lambda. Write a test.

### drill-3: Max by field
Given `scores = [("Alice",85),("Bob",92),("Carol",78)]`, find the tuple with the highest score using `max` and `itemgetter`. One line. Write a test asserting the result is `("Bob", 92)`.

---

## Topic: one-liners

These drills are about committing compact Python expressions to muscle memory. Each drill: read the task, write the one-liner from memory, verify it.

### drill-1: Deduplicate while preserving order
Given `arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]`, produce a list of unique elements in first-seen order. Expected: `[3, 1, 4, 5, 9, 2, 6]`. One line — no loop, no set comprehension.

Hint if asked: dicts have preserved insertion order since Python 3.7.

### drill-2: Transpose a matrix
Given `mat = [[1,2,3],[4,5,6],[7,8,9]]`, produce `[[1,4,7],[2,5,8],[3,6,9]]`. One line using a built-in that pairs elements across iterables. Add a comment explaining what the `*` does.

### drill-3: Reverse a list / string
Three one-liners:
- Reverse `arr = [1,2,3,4,5]` without modifying it
- Reverse the string `s = "hello"`
- Get every other character of `s` starting from the end

### drill-4: Sum of squares (generator)
Compute the sum of squares of 1 through 1,000,000. One expression — no list created in memory. Add a comment on why this uses less memory than a list comprehension.

### drill-5: any / all
Given `nums = [2, 4, 6, 7, 8]`:
- Check if any number is odd — one line
- Check if all numbers are positive — one line
- Check if no number is negative — one line (no `not any(...)` — use `all`)

### drill-6: String build from list
Given `parts = ["hello", "world", "python"]`, produce `"hello, world, python"` and also `"helloworldpython"`. One line each. No loops.

### drill-7: Flatten
Given `matrix = [[1,2],[3,4],[5,6]]`, flatten it to `[1,2,3,4,5,6]`. One line. Two ways: nested comprehension and `sum(..., [])`.

### drill-8: Conditional expression
Write these without if/else blocks — inline only:
- Return `"fizz"` if n divisible by 3, `"buzz"` if by 5, `"fizzbuzz"` if both, else the number as a string. One expression.
- Clamp a value `x` to `[lo, hi]`: one expression using `min`/`max`.

---

## Topic: tuples

### drill-1: Create and basic access
Create a tuple `point = (3, 4)`. Then:
- Access x and y by index
- Try to change x to 10 — catch the error and print its type
- Count how many times 4 appears
- Find the index of value 3

### drill-2: Tuple as dict key
You have a grid. Store a value at coordinate (2, 3) in a dict, then at (1, 0). Look up the value at (2, 3). Show that you cannot do the same with a list as the key — catch and print that error.

### drill-3: Named tuple
Create a `Point` named tuple with fields `x` and `y`. Create `p = Point(3, 4)`. Show:
- Access by name: `p.x`, `p.y`
- Access by index: `p[0]`, `p[1]`
- Unpack into two variables
- Show it's still immutable — trying to set `p.x = 10` should raise an error

### drill-4: Return multiple values
Write a function `min_max(nums)` that returns both the minimum and maximum of a list in a single return statement (no list, no dict). Call it and capture both values in one line. Print them. Test it.

### drill-5: Mixed-length tuples with star unpacking
Given `records = [(0, 1), (0, 2, 5), (1, 3), (1, 2, 8)]` where the optional third value is a weight, build an adjacency list where each neighbor entry is `(neighbor, weight)` — use 1 as the default weight when not provided. Use star unpacking in the loop, not indexing. Write a test.

---

## Topic: unpacking

### drill-1: Basic unpacking
Given `coords = (10, 20, 30)`, unpack into `x`, `y`, `z` in one line. Then swap `x` and `y` without a temp variable. Print both results. Write assertions.

### drill-2: Star unpacking — head and tail
Given `nums = [1, 2, 3, 4, 5]`:
- Capture the first element and the rest separately — one line
- Capture everything except the last element, and the last element — one line
- Capture first, last, and middle separately — one line
Write assertions for each.

### drill-3: Unpack in a loop
Given `pairs = [(0,1),(1,2),(2,3)]`, iterate and print each pair as `"0 -> 1"` using tuple unpacking in the for-statement — not indexing. Then do the same for `weighted = [(0,1,4),(1,2,1),(2,3,7)]` printing `"0 -> 1 (cost 4)"`.

### drill-4: Unpack function return
Write `stats(nums)` that returns mean, min, and max in one return. Call it on `[4, 1, 7, 2, 9]` and unpack all three into named variables in one line. Write a test.

### drill-5: Nested unpacking
Given `data = [((1, 2), "a"), ((3, 4), "b")]`, unpack each row so you have `x`, `y`, and `label` as separate variables inside the loop. Print `"1,2: a"` format. No indexing allowed.
