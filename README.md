# Coding Interview Prep - Claude Code Skills

AI-powered coding interview practice for [Claude Code](https://claude.ai/claude-code). LeetCode-style problems with follow-ups and detailed feedback.

## Features

- **AI-Generated Questions** - Problems based on 14 common patterns
- **Optimization Push-back** - AI challenges suboptimal solutions
- **Dynamic Follow-ups** - Context-aware questions about your approach
- **Company Targeting** - Focus on company-specific patterns
- **Performance Tracking** - Track progress across patterns
- **Progressive Difficulty** - Unlock harder problems as you improve

## Installation

```bash
# Clone and open in VS Code
git clone https://github.com/peppermint-ai-lab/leetcode-skill.git
cd leetcode-skill
code .
# Click "Reopen in Container" when prompted
```

Or copy `skills/` to your project's `.claude/skills/` directory.

## Usage

```bash
/interview                    # Random problem
/interview sliding window     # Specific pattern
/interview --company google   # Company-specific patterns
/interview --growth           # Focus on weak areas
/interview --profile          # View/edit settings
```

### Focus Mode

```bash
/focus-mode on      # Disable autocomplete + list AI extensions to disable
/focus-mode off     # Restore settings
/focus-mode status  # Check current state
```

### Learning Notes

```bash
/notes Two pointers work from both ends   # Add note
/notes review                              # Review due notes
/notes list sliding-window                 # List by tag
/notes search edge case                    # Search
```

### Company Questions

```bash
/update-company-questions google meta amazon
```

## Session Flow

1. **Question** - AI generates a problem at your level
2. **Solve** - Implement in `solution.py`, run tests
3. **Evaluation** - AI checks solution, may ask for optimization
4. **Follow-ups** - Answer questions about your approach
5. **Feedback** - Scores, complexity analysis, next steps

## Directory Structure

| Folder | Purpose |
|--------|---------|
| `skills/` | Skill definitions - SKILL.md files that Claude Code reads |
| `.interview/` | Runtime data - user profile, performance tracking (created on first use) |
| `example-data/` | Sample files showing what generated data looks like |

```
├── skills/                  # Skill definitions
│   ├── interview/
│   ├── study-plan/
│   ├── notes/
│   ├── focus-mode/
│   └── update-company-questions/
├── .interview/              # Runtime data (created on use)
│   ├── user-profile.md
│   ├── notes/
│   ├── company_question_cache/
│   └── performance/
├── example-data/            # Sample generated files
└── solution.py              # Your solution file
```

## The 14 Patterns

| Pattern | Use When |
|---------|----------|
| Sliding Window | Contiguous subarray problems |
| Two Pointers | Sorted arrays, pair finding |
| Fast & Slow Pointers | Cycle detection |
| Merge Intervals | Overlapping intervals |
| Cyclic Sort | Arrays with numbers 1-n |
| In-place Linked List Reversal | Reverse without extra space |
| Tree BFS | Level-order traversal |
| Tree DFS | Path problems |
| Two Heaps | Median finding |
| Subsets | Combinations, permutations |
| Modified Binary Search | Rotated arrays |
| Top K Elements | K largest/smallest |
| K-way Merge | Merge sorted lists |
| Topological Sort | Task ordering |

## Requirements

- [Claude Code](https://claude.ai/claude-code)
- Python 3.x (or use included Dev Container)

## License

MIT
