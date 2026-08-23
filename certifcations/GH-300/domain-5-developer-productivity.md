# Domain 5 — Improve Developer Productivity

**Exam weight:** 10–15%

## Lab Index

- [Lab 5.1 — Generate Unit Tests](#lab-51--generate-unit-tests)
- [Lab 5.2 — Refactor Legacy Code](#lab-52--refactor-legacy-code)
- [Lab 5.3 — Generate Documentation](#lab-53--generate-documentation)
- [Lab 5.4 — Verification Before Acceptance](#lab-54--verification-before-acceptance)

## Lab 5.1 — Generate Unit Tests

### Goal

Generate tests using Copilot Chat.

### Context

Tests document expected behavior and help catch regressions when code changes. This lab uses a simple function so you can evaluate whether Copilot generates useful pytest cases, including normal and edge cases.

### Steps

1. Create:

```text
calc.py
```

2. Paste:

```python
def add(a, b):
    return a + b
```

### Ask Copilot Chat

1. Open Copilot Chat
2. Type:

```text
Generate pytest unit tests for the add() function.
```

3. Press Enter

### What You Should See

Copilot should generate pytest code that imports or calls `add()` and checks expected sums, commonly including positive, negative, zero, or boundary-style inputs. Save the tests and run them to verify the behavior.

---

## Lab 5.2 — Refactor Legacy Code

### Goal

Modernize old code.

### Context

Legacy code may be correct but unnecessarily verbose or difficult to maintain. This lab practices using Copilot to express a loop with a list comprehension while checking that the refactoring preserves behavior.

### Steps

1. Create:

```text
legacy.py
```

2. Paste:

```python
def process(data):
    result = []
    for i in range(len(data)):
        result.append(data[i] * 2)
    return result
```

### Ask Copilot Edits

1. Highlight the function
2. Press Ctrl+I
3. Type:

```text
Refactor this code using list comprehension.
```

4. Press Enter

### What You Should See

Copilot Edits should replace the indexed loop with a list comprehension equivalent to `[value * 2 for value in data]`. The function should still return a new list with every input value doubled.

---

## Lab 5.3 — Generate Documentation

### Goal

Generate documentation using Copilot CLI.

### Context

Documentation generation is useful when a project has code but lacks a clear entry point for users or contributors. This lab revisits README generation from the command line so you can assess the quality of the output after Copilot inspects the repository.

### Ask Copilot CLI

1. Open terminal
2. Change to the project folder.
3. Run:

```text
copilot
```

4. Ask Copilot CLI to create or improve the README after it inspects the repository.

### What You Should See

Copilot CLI should ask for project context or propose an initial README from the files it can inspect. The result may be incomplete if the project has no clear metadata, entry point, or usage instructions.

---

### Domain 3 — Understand Copilot Data and Architecture

## Lab 5.4 — Verification Before Acceptance

### Goal

Practice checking generated code before using it.

### Context

Copilot can suggest code that looks correct but still fails tests or misses edge cases. This lab focuses on the habit of verifying generated output with a test run or by reading the diff carefully.

### Steps

1. Create:

```text
divide.py
```

2. Paste:

```python
def divide(a, b):
    return a / b
```

3. Ask Copilot Chat:

```text
Write tests for divide().
```

### What You Should See

Copilot should produce tests for normal input and at least one edge case such as division by zero.

### Verify

1. Run the tests.
2. If Copilot suggests code changes, inspect the diff before accepting.

### What You Should See

You should confirm whether the tests pass and whether the generated implementation handles edge cases the way you expect.

---
