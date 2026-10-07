---
description: "Review Python code and add concise comments above each function explaining why it exists and how it works technically without changing behavior."
---

# Add Why/How Comments to Functions

Use the current file or the selected code as the source of truth.

Review every function or method in scope and add comments directly above each one.

## Required comment pattern

For each function, add two short comment lines in this format:

```python
# Why: explains the purpose of the function and the problem it solves.
# How: explains the technical flow, key inputs, outputs, and any important dependencies.
```

## Rules

* Preserve the current code exactly; do not change logic, behavior, variable names, signatures, or return values.
* Only add comments; do not refactor or rewrite the implementation.
* Keep comments concise, clear, and practical for future maintainers.
* Explain purpose and mechanism for both helper functions and orchestration functions.
* If a function is simple, keep the comment brief but still cover both intent and mechanics.
* If the function is complex, mention the main data flow and any important side effects.
* Do not add generic filler comments like "this function does something".

## Output

Return the updated code with the new comments inserted inline, and nothing else.
