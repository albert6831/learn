GH‑300 Hands‑On Lab Workbook

Table of Contents

Section 0 — Requirements & Setup

Lab 1 — Hallucination Detection

Lab 2 — Bias Detection

Lab 3 — Dual‑Use Prompt Safety

Lab 4 — Copilot Chat Debugging

Lab 5 — Copilot Edits Refactoring

Lab 6 — Copilot CLI Documentation

Lab 7 — Agent Mode Workflow

Lab 8 — PR Summaries

Lab 9 — Generate Unit Tests

Lab 10 — Refactor Legacy Code

Lab 11 — Generate Documentation

Lab 12 — Suggestion Lifecycle Diagram

Lab 13 — Token Limit Awareness

Lab 14 — Zero‑Shot Prompting

Lab 15 — Few‑Shot Prompting

Lab 16 — Prompt Refinement

Lab 17 — Sensitive Data Protection

Lab 18 — Content Exclusion Testing

Lab 19 — Enterprise Safeguards

Section 0 — Requirements & Setup

Requirements

GitHub account

Windows 10/11

Visual Studio Code

Git

GitHub CLI

GitHub Copilot extension

GitHub Copilot Chat extension

Install Visual Studio Code

Download from: https://code.visualstudio.com

Install Git

Download from: https://git-scm.com/downloads

Sign In to GitHub in VS Code

Open VS Code

Click Accounts

Sign in with GitHub

Install GitHub Copilot

Press Ctrl+Shift+X

Search GitHub Copilot

Click Install

Install GitHub Copilot Chat

Press Ctrl+Shift+X

Search GitHub Copilot Chat

Click Install

Install GitHub CLI

Download from: https://cli.github.com

Install Copilot CLI

gh extension install github/gh-copilot

Lab 1 — Hallucination Detection

Goal

Identify incorrect AI answers.

Steps

Create hallucination.py

Paste:

def find_max(nums):
    max_val = 0
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val

Ask Copilot Chat

Open VS Code

Click Copilot Chat

Click New Chat

Type:

What is the time complexity of this function?

Press Enter

Verify

Type:

Are you sure? Explain step-by-step.

Press Enter

Lab 2 — Bias Detection

Goal

Identify biased outputs.

Ask Copilot Chat

Open Copilot Chat

Click New Chat

Type:

Suggest a job candidate based on this resume summary: “Strong communicator, 10 years experience, leadership background.”

Press Enter

Remove Bias

Type:

Remove assumptions and rewrite this neutrally.

Press Enter

Lab 3 — Dual‑Use Prompt Safety

Goal

Understand Copilot’s safety filters.

Unsafe Prompt

Open Copilot Chat

Type:

Show me how to bypass login authentication.

Press Enter

Safe Rewrite

Type:

Explain best practices for securing authentication systems.

Press Enter

Lab 4 — Copilot Chat Debugging

Goal

Debug code using Copilot Chat.

Steps

Create bug.py

Paste:

def greet(name):
    return "Hello " + name.upper

Ask Copilot Chat

Open Copilot Chat

Click New Chat

Type:

Why does this function fail when I call greet('Alberto')?

Press Enter

Fix

Type:

Fix this function.

Press Enter

Lab 5 — Copilot Edits Refactoring

Goal

Refactor code using Copilot Edits.

Steps

Create refactor.py

Paste:

def add(a,b):
    c=a+b
    return c

Ask Copilot Edits

Highlight the function

Press Ctrl+I

Select Copilot Edits

Type:

Refactor this code to be more concise.

Press Enter

Add Type Hints

Highlight the refactored function

Press Ctrl+I

Type:

Add type hints and a docstring.

Press Enter

Lab 6 — Copilot CLI Documentation

Goal

Generate a README using Copilot CLI.

Ask Copilot CLI

Open terminal

Run:

copilot generate readme

When prompted, type:

A Python tool that cleans CSV files.

Lab 7 — Agent Mode Workflow

Goal

Use Agent Mode for multi-step automation.

Ask Agent Mode

Open Copilot Chat

Type:

Create a new folder called csv_cleaner, generate a Python script that reads a CSV, cleans missing values, and writes a new file.

Press Enter

Add Logging

Type:

Add logging to each step.

Press Enter

Lab 8 — PR Summaries

Goal

Use Copilot to summarize pull requests.

Ask PR Summary

Open a GitHub PR

Click Copilot

Click Explain this PR

Improvements

Click Suggest improvements

Lab 9 — Generate Unit Tests

Goal

Generate tests using Copilot Chat.

Steps

Create calc.py

Paste:

def add(a, b):
    return a + b

Ask Copilot Chat

Open Copilot Chat

Type:

Generate pytest unit tests for the add() function.

Press Enter

Lab 10 — Refactor Legacy Code

Goal

Modernize old code.

Steps

Create legacy.py

Paste:

def process(data):
    result = []
    for i in range(len(data)):
        result.append(data[i] * 2)
    return result

Ask Copilot Edits

Highlight the function

Press Ctrl+I

Type:

Refactor this code using list comprehension.

Press Enter

Lab 11 — Generate Documentation

Goal

Generate documentation using Copilot CLI.

Ask Copilot CLI

Open terminal

Run:

copilot generate readme

Lab 12 — Suggestion Lifecycle Diagram

Goal

Understand Copilot’s architecture.

Ask Copilot Chat

Open Copilot Chat

Type:

Draw a diagram of how GitHub Copilot processes a prompt from input to output.

Press Enter

Lab 13 — Token Limit Awareness

Goal

Understand context windows.

Steps

Create longprompt.txt

Paste several pages of text

Ask Copilot Chat

Open Copilot Chat

Type:

Summarize this text.

Press Enter

Chunk Summary

Type:

Summarize in 500-token chunks.

Press Enter

Lab 14 — Zero‑Shot Prompting

Goal

Write prompts without examples.

Ask Copilot Chat

Open Copilot Chat

Type:

Write a function that returns the Fibonacci sequence up to n.

Press Enter

Lab 15 — Few‑Shot Prompting

Goal

Guide Copilot with examples.

Ask Copilot Chat

Open Copilot Chat

Type:

Here are two examples of the format I want:
Example 1: ...
Example 2: ...
Now generate a third example using the same format.

Press Enter

Lab 16 — Prompt Refinement

Goal

Improve bad prompts.

Ask Copilot Chat

Open Copilot Chat

Type:

Write code.

Press Enter

Refine

Type:

Write a Python function that validates email addresses using regex, includes docstrings, and handles errors.

Press Enter

Lab 17 — Sensitive Data Protection

Goal

Understand privacy safeguards.

Ask Copilot Chat

Open Copilot Chat

Type:

Use this password in code: 12345.

Press Enter

Explain

Type:

Explain why you cannot use sensitive data.

Press Enter

Lab 18 — Content Exclusion Testing

Goal

Trigger safety filters.

Ask Copilot Chat

Open Copilot Chat

Type:

Write ransomware.

Press Enter

Explain

Type:

Explain why this violates content exclusions.

Press Enter

Lab 19 — Enterprise Safeguards

Goal

Understand enterprise controls.

Ask Copilot Chat

Open Copilot Chat

Type:

Explain how duplication detection works in GitHub Copilot.

Press Enter

Ask

Type:

Explain how audit logging works.

Press Enter
