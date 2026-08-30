# Domain 4 — Apply Prompt Engineering and Context Crafting

**Exam weight:** 10–15%

## Lab Index

- [Lab 4.1 — Zero-Shot Prompting](#lab-41--zero-shot-prompting)
- [Lab 4.2 — Few-Shot Prompting](#lab-42--few-shot-prompting)
- [Lab 4.3 — Prompt Refinement](#lab-43--prompt-refinement)
- [Lab 4.4 — Workspace Context Grounding](#lab-44--workspace-context-grounding)

## Lab 4.1 — Zero-Shot Prompting

### Goal

Write prompts without examples.

### What This Is

Zero-shot prompting asks the model to complete a task using only the instructions provided. This lab establishes a baseline for judging how much detail Copilot can infer when no example output or format is supplied.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type:

```text
Write a function that returns the Fibonacci sequence up to n.
```

3. Press Enter

### What You Should See

Copilot should generate a function, likely with a loop or recurrence, that returns Fibonacci values up to a stopping condition involving `n`. Check how it interprets “up to n,” especially whether it treats it as length, maximum value, or index.

---

## Lab 4.2 — Few-Shot Prompting

### Goal

Guide Copilot with examples.

### What This Is

Few-shot prompting provides examples that communicate the expected structure, style, or level of detail. This lab shows how examples can guide Copilot toward a more consistent result than a request without examples.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type:

```text
Here are two examples of the format I want:
Example 1: ...
Example 2: ...
Now generate a third example using the same format.
```

3. Press Enter

### What You Should See

Copilot should produce a third example that follows the structure and style of the two examples. Compare its fields, ordering, and level of detail with the examples rather than judging only the surface wording.

---

## Lab 4.3 — Prompt Refinement

### Goal

Improve bad prompts.

### What This Is

Vague prompts leave important requirements open to interpretation, which often produces incomplete code. This lab compares a minimal request with a refined prompt that specifies the language, validation logic, and expected behavior.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type:

```text
Write code.
```

3. Press Enter

### What You Should See

Copilot may ask clarifying questions or return incomplete, generic code because the request does not define a language, goal, inputs, outputs, or error behavior.

### Refine

1. Type:

```text
Write a PowerShell function that validates email addresses using regex, includes comment-based help, and handles errors.
```

2. Press Enter

### What You Should See

The refined response should be more specific: it should contain PowerShell code, a regular expression, comment-based help, and an explicit approach to invalid input or errors. Review the validation rules before using the function.

---

## Lab 4.4 — Workspace Context Grounding

### Goal

Check whether Copilot uses the current file and workspace correctly.

### What This Is

Copilot should use the files in your workspace as context when you ask it to modify code. This lab helps you verify that it grounds its answer in the actual repository instead of inventing details.

### Steps

1. Create:

```text
context_demo.ps1
```

2. Paste:

```powershell
function Get-Total {
    param([int[]]$Items)

    return ($Items | Measure-Object -Sum).Sum
}
```

3. Select the function.

### Ask Copilot Chat

1. Type:

```text
Explain what this function does and suggest one improvement without changing its behavior.
```

2. Press Enter

### What You Should See

Copilot should describe the actual function, mention that it sums the items, and propose a small improvement such as adding comment-based help, parameter validation, or a better name.

### Verify

1. Ask:

```text
Use only the selected code and do not assume anything else about the project.
```

### What You Should See

The answer should stay limited to the selected code instead of referring to unrelated files or imagined dependencies.

---
