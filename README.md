# Python Interview Practice

My Python solutions to data-structure and algorithm problems on NeetCode. Submissions are synced from NeetCode into this repository.

## Solutions

| Problem | Approach | Expected time | Extra space |
| --- | --- | --- | --- |
| [Contains Duplicate](Data%20Structures%20%26%20Algorithms/duplicate-integer/submission-0.py) | Track values in a hash set; return when a value repeats | O(n) | O(n) |

## Contains Duplicate: reasoning

The solution scans the input once and keeps a set of values already encountered. If the current value is already in the set, it returns `True`; otherwise, it adds the value and continues. Reaching the end without a repeated value returns `False`.

The expected running time is O(n), assuming average constant-time set operations. The set can hold up to n distinct values, so extra space is O(n).

Examples to reason through:

- `[1, 2, 3, 1]` returns `True`.
- `[1, 2, 3, 4]` returns `False`.
- An empty list or a single value returns `False`.
- Negative values are handled the same way as other integers.

## Repository structure

```text
Data Structures & Algorithms/
  duplicate-integer/
    submission-0.py
    submission-3.py
```

The two saved submissions currently contain the same solution. Files use NeetCode's `Solution` interface and are intended to run in the platform's environment.

## Sync

Submissions are managed through [NeetCode's GitHub integration](https://neetcode.io/profile/github). The problem index and explanations in this README are maintained separately.

For my application and data projects, see my [portfolio](https://pouyar81.github.io/).
