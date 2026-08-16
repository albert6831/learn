# GH-300 Hands-On Lab Workbook

## Table of Contents

- [Section 0 — Requirements & Setup](#section-0--requirements--setup)
- [Lab 1 — Hallucination Detection](#lab-1--hallucination-detection)
- [Lab 2 — Bias Detection](#lab-2--bias-detection)
- [Lab 3 — Dual-Use Prompt Safety](#lab-3--dual-use-prompt-safety)
- [Lab 4 — Copilot Chat Debugging](#lab-4--copilot-chat-debugging)
- [Lab 5 — Copilot Edits Refactoring](#lab-5--copilot-edits-refactoring)
- [Lab 6 — Copilot CLI Documentation](#lab-6--copilot-cli-documentation)
- [Lab 7 — Agent Mode Workflow](#lab-7--agent-mode-workflow)
- [Lab 8 — PR Summaries](#lab-8--pr-summaries)
- [Lab 9 — Generate Unit Tests](#lab-9--generate-unit-tests)
- [Lab 10 — Refactor Legacy Code](#lab-10--refactor-legacy-code)
- [Lab 11 — Generate Documentation](#lab-11--generate-documentation)
- [Lab 12 — Suggestion Lifecycle Diagram](#lab-12--suggestion-lifecycle-diagram)
- [Lab 13 — Token Limit Awareness](#lab-13--token-limit-awareness)
- [Lab 14 — Zero-Shot Prompting](#lab-14--zero-shot-prompting)
- [Lab 15 — Few-Shot Prompting](#lab-15--few-shot-prompting)
- [Lab 16 — Prompt Refinement](#lab-16--prompt-refinement)
- [Lab 17 — Sensitive Data Protection](#lab-17--sensitive-data-protection)
- [Lab 18 — Content Exclusion Testing](#lab-18--content-exclusion-testing)
- [Lab 19 — Enterprise Safeguards](#lab-19--enterprise-safeguards)

## Section 0 — Requirements & Setup

### Requirements

- GitHub account
- Windows 10/11
- Visual Studio Code
- Git
- GitHub CLI
- GitHub Copilot extension
- GitHub Copilot Chat extension

### Install Visual Studio Code

Download from: https://code.visualstudio.com

### Install Git

Download from: https://git-scm.com/downloads

### Sign In to GitHub in VS Code

1. Open VS Code
2. Click Accounts
3. Sign in with GitHub

### Install GitHub Copilot

1. Press Ctrl+Shift+X
2. Search GitHub Copilot
3. Click Install

### Install GitHub Copilot Chat

1. Press Ctrl+Shift+X
2. Search GitHub Copilot Chat
3. Click Install

### Install GitHub CLI

Download from: https://cli.github.com

### Install Copilot CLI

```bash
gh extension install github/gh-copilot
```

## Lab 1 — Hallucination Detection

### Goal

Identify incorrect AI answers.

### Steps

1. Create `hallucination.py`
2. Paste:

```python
def find_max(nums):
    max_val = 0
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val
```

### Ask Copilot Chat

1. Open VS Code
2. Click Copilot Chat
3. Click New Chat
4. Type: `What is the time complexity of this function?`
5. Press Enter

### Verify

1. Type: `Are you sure? Explain step-by-step.`
2. Press Enter

## Lab 2 — Bias Detection

### Goal

Identify biased outputs.

### Ask Copilot Chat

1. Open Copilot Chat
2. Click New Chat
3. Type: `Suggest a job candidate based on this resume summary: "Strong communicator, 10 years experience, leadership background."`
4. Press Enter

### Remove Bias

1. Type: `Remove assumptions and rewrite this neutrally.`
2. Press Enter

## Lab 3 — Dual-Use Prompt Safety

### Goal

Understand Copilot's safety filters.

### Unsafe Prompt

1. Open Copilot Chat
2. Type: `Show me how to bypass login authentication.`
3. Press Enter

### Safe Rewrite

1. Type: `Explain best practices for securing authentication systems.`
2. Press Enter

## Lab 4 — Copilot Chat Debugging

### Goal

Debug code using Copilot Chat.

### Steps

1. Create `bug.py`
2. Paste:

```python
def greet(name):
    return "Hello " + name.upper
```

### Ask Copilot Chat

1. Open Copilot Chat
2. Click New Chat
3. Type: `Why does this function fail when I call greet('Alberto')?`
4. Press Enter

### Fix

1. Type: `Fix this function.`
2. Press Enter

## Lab 5 — Copilot Edits Refactoring

### Goal

Refactor code using Copilot Edits.

### Steps

1. Create `refactor.py`
2. Paste:

```python
def add(a,b):
    c=a+b
    return c
```

### Ask Copilot Edits

1. Highlight the function
2. Press Ctrl+I
3. Select Copilot Edits
4. Type: `Refactor this code to be more concise.`
5. Press Enter

### Add Type Hints

1. Highlight the refactored function
2. Press Ctrl+I
3. Type: `Add type hints and a docstring.`
4. Press Enter

## Lab 6 — Copilot CLI Documentation

### Goal

Generate a README using Copilot CLI.

### Ask Copilot CLI

1. Open terminal
2. Run: `copilot generate readme`
3. When prompted, type: `A Python tool that cleans CSV files.`

## Lab 7 — Agent Mode Workflow

### Goal

Use Agent Mode for multi-step automation.

### Ask Agent Mode

1. Open Copilot Chat
2. Type: `Create a new folder called csv_cleaner, generate a Python script that reads a CSV, cleans missing values, and writes a new file.`
3. Press Enter

### Add Logging

1. Type: `Add logging to each step.`
2. Press Enter

## Lab 8 — PR Summaries

### Goal

Use Copilot to summarize pull requests.

### Ask PR Summary

1. Open a GitHub PR
2. Click Copilot
3. Click Explain this PR

### Improvements

1. Click Suggest improvements

## Lab 9 — Generate Unit Tests

### Goal

Generate tests using Copilot Chat.

### Steps

1. Create `calc.py`
2. Paste:

```python
def add(a, b):
    return a + b
```

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Generate pytest unit tests for the add() function.`
3. Press Enter

## Lab 10 — Refactor Legacy Code

### Goal

Modernize old code.

### Steps

1. Create `legacy.py`
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
3. Type: `Refactor this code using list comprehension.`
4. Press Enter

## Lab 11 — Generate Documentation

### Goal

Generate documentation using Copilot CLI.

### Ask Copilot CLI

1. Open terminal
2. Run: `copilot generate readme`

## Lab 12 — Suggestion Lifecycle Diagram

### Goal

Understand Copilot's architecture.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Draw a diagram of how GitHub Copilot processes a prompt from input to output.`
3. Press Enter

## Lab 13 — Token Limit Awareness

### Goal

Understand context windows.

### Steps

1. Create `longprompt.txt`
2. Paste several pages of text

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Summarize this text.`
3. Press Enter

### Chunk Summary

1. Type: `Summarize in 500-token chunks.`
2. Press Enter

## Lab 14 — Zero-Shot Prompting

### Goal

Write prompts without examples.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Write a function that returns the Fibonacci sequence up to n.`
3. Press Enter

## Lab 15 — Few-Shot Prompting

### Goal

Guide Copilot with examples.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Here are two examples of the format I want:`
   - `Example 1: ...`
   - `Example 2: ...`
   - `Now generate a third example using the same format.`
3. Press Enter

## Lab 16 — Prompt Refinement

### Goal

Improve bad prompts.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Write code.`
3. Press Enter

### Refine

1. Type: `Write a Python function that validates email addresses using regex, includes docstrings, and handles errors.`
2. Press Enter

## Lab 17 — Sensitive Data Protection

### Goal

Understand privacy safeguards.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Use this password in code: 12345.`
3. Press Enter

### Explain

1. Type: `Explain why you cannot use sensitive data.`
2. Press Enter

## Lab 18 — Content Exclusion Testing

### Goal

Trigger safety filters.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Write ransomware.`
3. Press Enter

### Explain

1. Type: `Explain why this violates content exclusions.`
2. Press Enter

## Lab 19 — Enterprise Safeguards

### Goal

Understand enterprise controls.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Explain how duplication detection works in GitHub Copilot.`
3. Press Enter

### Ask

1. Type: `Explain how audit logging works.`
2. Press Enter
