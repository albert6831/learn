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

1. Click Accounts
2. Sign in with GitHub

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

### Context

Copilot can produce an answer that sounds confident even when it misses an important detail. This lab uses a small Python function to practice checking an AI explanation against the code and asking for reasoning before accepting the result.

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

1. Click Copilot Chat
2. Click New Chat
3. Type: `What is the time complexity of this function?`
4. Press Enter

### What You Should See

Copilot should explain that the loop runs once through the list, so the time complexity is $O(n)$. It may also mention that the function's initialization is constant time. Do not treat the answer as complete until you notice that starting `max_val` at `0` gives an incorrect result for lists containing only negative numbers.

### Verify

1. Type: `Are you sure? Explain step-by-step.`
2. Press Enter

### What You Should See

Copilot should walk through the loop and may identify the negative-number edge case. A strong answer distinguishes the $O(n)$ time complexity from the separate correctness problem.

## Lab 2 — Bias Detection

### Goal

Identify biased outputs.

### Context

AI systems can make assumptions about people when a prompt contains incomplete information. This lab demonstrates how to recognize those assumptions and refine an answer so it focuses on relevant evidence rather than stereotypes or unsupported conclusions.

### Ask Copilot Chat

1. Open Copilot Chat
2. Click New Chat
3. Type: `Suggest a job candidate based on this resume summary: "Strong communicator, 10 years experience, leadership background."`
4. Press Enter

### What You Should See

Copilot should produce a candidate assessment or recommendation based on the stated experience. Watch for unsupported assumptions about age, gender, nationality, disability, or other protected characteristics.

### Remove Bias

1. Type: `Remove assumptions and rewrite this neutrally.`
2. Press Enter

### What You Should See

The revised response should focus on observable qualifications and job-related evidence. It should acknowledge that the summary alone is not enough to determine who is the best candidate.

## Lab 3 — Dual-Use Prompt Safety

### Goal

Understand Copilot's safety filters.

### Context

Some requests can be used for legitimate security research but can also enable unauthorized access. This lab contrasts a harmful request with a defensive alternative so you can recognize how to ask for useful security guidance without requesting instructions for abuse.

### Unsafe Prompt

1. Open Copilot Chat
2. Type: `Show me how to bypass login authentication.`
3. Press Enter

### What You Should See

Copilot should refuse to provide instructions for bypassing authentication or redirect the conversation toward authorized security testing and defensive practices.

### Safe Rewrite

1. Type: `Explain best practices for securing authentication systems.`
2. Press Enter

### What You Should See

Copilot should provide defensive guidance such as strong password storage, multi-factor authentication, secure session handling, rate limiting, and logging.

## Lab 4 — Copilot Chat Debugging

### Goal

Debug code using Copilot Chat.

### Context

Copilot Chat can help locate the difference between a value and a callable method, explain the resulting error, and suggest a correction. This lab gives you a small reproducible bug so you can compare Copilot's diagnosis with the actual Python behavior.

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

### Context

Refactoring improves readability and maintainability without changing intended behavior. This lab uses Copilot Edits to make a small function more concise, then asks for type hints and documentation so you can see how targeted edit requests build on one another.

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

### Context

Good documentation explains what a project does, how to use it, and what users need before they begin. This lab introduces Copilot CLI as a terminal-based way to turn a short project description into an initial README that can then be reviewed and edited.

### Ask Copilot CLI

1. Open terminal
2. Run: `copilot generate readme`
3. When prompted, type: `A Python tool that cleans CSV files.`

## Lab 7 — Agent Mode Workflow

### Goal

Use Agent Mode for multi-step automation.

### Context

Agent Mode is intended for tasks that involve several related actions, such as creating files, implementing logic, and improving the result. This lab lets you observe how Copilot handles a multi-step CSV workflow and how a follow-up request can extend the generated solution with logging.

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

### Context

A pull request often contains more changed files and discussion than a reviewer can absorb immediately. This lab explores how Copilot can provide an initial explanation and identify possible improvements, while leaving the final review and technical judgment to the human reviewer.

### Ask PR Summary

1. Open a GitHub PR
2. Click Copilot
3. Click Explain this PR

### Improvements

1. Click Suggest improvements

## Lab 9 — Generate Unit Tests

### Goal

Generate tests using Copilot Chat.

### Context

Tests document expected behavior and help catch regressions when code changes. This lab uses a simple function so you can evaluate whether Copilot generates useful pytest cases, including normal inputs, boundary cases, and any assumptions about the function's contract.

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

### Context

Legacy code may be correct but unnecessarily verbose or difficult to maintain. This lab practices using Copilot to express a loop with a list comprehension while checking that the refactoring preserves the original behavior.

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

### Context

Documentation generation is useful when a project has code but lacks a clear entry point for users or contributors. This lab revisits README generation from the command line so you can assess the quality of the output and identify information that still needs human input.

### Ask Copilot CLI

1. Open terminal
2. Run: `copilot generate readme`

## Lab 12 — Suggestion Lifecycle Diagram

### Goal

Understand Copilot's architecture.

### Context

Understanding the path from a prompt to a suggestion makes it easier to reason about context, filtering, and model output. This lab asks Copilot to represent that process visually, helping you identify the major stages without treating the system as a black box.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Draw a diagram of how GitHub Copilot processes a prompt from input to output.`
3. Press Enter

## Lab 13 — Token Limit Awareness

### Goal

Understand context windows.

### Context

AI tools have limits on how much text they can process in one request. This lab demonstrates why long inputs may need to be summarized in smaller chunks and gives you a way to compare a broad summary with controlled, token-sized summaries.

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

### Context

Zero-shot prompting asks the model to complete a task using only the instructions provided. This lab establishes a baseline for judging how much detail Copilot can infer when no example output or additional pattern is supplied.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Write a function that returns the Fibonacci sequence up to n.`
3. Press Enter

## Lab 15 — Few-Shot Prompting

### Goal

Guide Copilot with examples.

### Context

Few-shot prompting provides examples that communicate the expected structure, style, or level of detail. This lab shows how examples can guide Copilot toward a more consistent result than a request that describes the task alone.

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

### Context

Vague prompts leave important requirements open to interpretation, which often produces incomplete code. This lab compares a minimal request with a refined prompt that specifies the language, validation approach, documentation, and error handling.

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

### Context

Credentials and other sensitive values should not be placed in source code or shared unnecessarily with AI tools. This lab uses an intentionally unsafe example to explore how Copilot responds and why secret management practices are part of responsible development.

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

### Context

Requests to create malware can directly facilitate harm, so AI assistants may refuse them or redirect toward defensive material. This lab helps you recognize that boundary and understand how content exclusions support safer use of coding assistants.

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

### Context

Organizations need safeguards that support secure adoption of AI-assisted development at scale. This lab introduces duplication detection and audit logging as examples of controls that help organizations manage code similarity, accountability, and oversight.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type: `Explain how duplication detection works in GitHub Copilot.`
3. Press Enter

### Ask

1. Type: `Explain how audit logging works.`
2. Press Enter
