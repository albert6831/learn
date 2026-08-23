# Domain 2 — Use GitHub Copilot Features

**Exam weight:** 25–30%

## Lab Index

- [Lab 2.1 — Copilot Chat Debugging](#lab-21--copilot-chat-debugging)
- [Lab 2.2 — Copilot Edits Refactoring](#lab-22--copilot-edits-refactoring)
- [Lab 2.3 — Copilot CLI Documentation](#lab-23--copilot-cli-documentation)
- [Lab 2.4 — Agent Mode Workflow](#lab-24--agent-mode-workflow)
- [Lab 2.5 — PR Summaries](#lab-25--pr-summaries)
- [Lab 2.6 — Inline Completion Review](#lab-26--inline-completion-review)
- [Lab 2.7 — Agent Sessions and Sub-agents](#lab-27--agent-sessions-and-sub-agents)
- [Lab 2.8 — Custom Agents and Instructions](#lab-28--custom-agents-and-instructions)
- [Lab 2.9 — MCP and External Tools](#lab-29--mcp-and-external-tools)
- [Lab 2.10 — Copilot CLI Sessions](#lab-210--copilot-cli-sessions)

## Lab 2.1 — Copilot Chat Debugging

### Goal

Debug code using Copilot Chat.

### Context

Copilot Chat can help locate the difference between a value and a callable method, explain the resulting error, and suggest a correction. This lab gives you a small reproducible bug so you can compare the explanation with the source code.

### Steps

1. Create:

```text
bug.py
```

2. Paste:

```python
def greet(name):
    return "Hello " + name.upper
```

### Ask Copilot Chat

1. Open Copilot Chat
2. Click New Chat
3. Type:

```text
Why does this function fail when I call greet('Alberto')?
```

4. Press Enter

### What You Should See

Copilot should point out that `name.upper` is a method object and needs parentheses. Calling `greet('Alberto')` should therefore fail when Python tries to concatenate the string with that method object.

### Fix

1. Type:

```text
Fix this function.
```

2. Press Enter

### What You Should See

Copilot should change the expression to `name.upper()` and explain that calling the method returns the uppercase string `ALBERTO`.

---

## Lab 2.2 — Copilot Edits Refactoring

### Goal

Refactor code using Copilot Edits.

### Context

Refactoring improves readability and maintainability without changing intended behavior. This lab uses Copilot Edits to make a small function more concise, then asks for type hints and documentation.

### Steps

1. Create:

```text
refactor.py
```

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
4. Type:

```text
Refactor this code to be more concise.
```

5. Press Enter

### What You Should See

Copilot Edits should propose a shorter implementation, such as returning `a + b` directly. The result should preserve the function's behavior and should be shown as an editable change for you to review.

### Add Type Hints

1. Highlight the refactored function
2. Press Ctrl+I
3. Type:

```text
Add type hints and a docstring.
```

4. Press Enter

### What You Should See

The function should gain type annotations for its parameters and return value, plus a docstring describing the addition operation. Review the inferred types before accepting the edit.

---

## Lab 2.3 — Copilot CLI Documentation

### Goal

Generate a README using Copilot CLI.

### Context

Good documentation explains what a project does, how to use it, and what users need before they begin. This lab introduces Copilot CLI as a terminal-based way to turn a short project description into repository documentation.

### Ask Copilot CLI

1. Open terminal
2. Change to the project folder.
3. Run:

```text
copilot
```

4. When prompted, enter:

```text
Create or update README.md for this repository. Describe a Python tool that cleans CSV files. Inspect the project files first and do not invent unsupported commands.
```

### What You Should See

Copilot CLI should propose README content with a project description and likely sections such as usage, installation, and examples. Review the proposed changes and approve them only after checking that they match the repository.

---

## Lab 2.4 — Agent Mode Workflow

### Goal

Use Agent Mode for multi-step automation.

### Context

Agent Mode is intended for tasks that involve several related actions, such as creating files, implementing logic, and improving the result. This lab lets you observe how Copilot handles a multi-step request.

### Ask Agent Mode

1. Open Copilot Chat
2. Type:

```text
Create a new folder called csv_cleaner, generate a Python script that reads a CSV, cleans missing values, and writes a new file.
```

3. Press Enter

### What You Should See

Agent Mode should propose or perform several steps: create the `csv_cleaner` folder, add a Python script, and implement CSV input, missing-value handling, and output writing. Review any planned file changes before accepting them.

### Add Logging

1. Type:

```text
Add logging to each step.
```

2. Press Enter

### What You Should See

The script should be updated with logging around the main workflow, such as reading the input, cleaning values, and writing the output. The generated code should use appropriate log levels and remain readable.

---

## Lab 2.5 — PR Summaries

### Goal

Use Copilot to summarize pull requests.

### Context

A pull request can contain a lot of information. Use Copilot to review the code.

### Create a GitHub PR on GitHub.com

Create a practice pull request on GitHub.com:

1. Open a repository you own. If needed, select **+ > New repository**.
2. On the **Code** tab, select the branch menu, then **Create new branch**.
3. Name the branch:

```text
practice-pr-summary
```

4. Select **Create new branch**.
5. Select **Add file > Create new file**.
6. Name the file:

```text
clean_orders.py
```

7. Paste:

```python
import csv


def clean_orders(input_file, output_file):
    with open(input_file) as source:
        reader = csv.DictReader(source)
        orders = []

        for row in reader:
            if row["email"]:
                row["email"] = row["email"].lower()
                orders.append(row)

    with open(output_file, "w") as target:
        writer = csv.DictWriter(target, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(orders)
```

8. Under **Commit new file**, select **Commit new file**.
9. Select **Compare & pull request**.
10. Set the base branch to the default branch.
11. Select **Create pull request**.
12. Open the PR from **Pull requests**.

### Request a GitHub Copilot Review

1. Open the PR on GitHub.com.
2. In **Reviewers**, select **Copilot > Request**.
3. Read Copilot's review comments.

### What You Should See

Copilot may identify bugs, security concerns, testing gaps, or maintenance issues.

### If Copilot Is Not Listed

If **Copilot** is not listed under **Reviewers**, it is not available for your account or repository.

### What You Should See

GitHub only shows **Request** when Copilot code review is available.

### Verify

Check one comment against the code. Do not approve or merge based only on Copilot's review.

---

### Domain 5 — Improve Developer Productivity

## Lab 2.6 — Inline Completion Review

### Goal

Practice accepting, rejecting, and editing inline completions.

### Context

Inline completions can be fast, but they still need review. This lab compares an editor suggestion with the code you intended to write so you can spot when a completion is useful or when it introduces a wrong assumption.

### Steps

1. Create:

```text
inline_demo.py
```

2. Paste:

```python
def square_list(values):
```

3. On the next line, begin typing `return [` or `result = []` so Copilot can suggest an inline completion.

### What You Should See

Copilot may suggest a full implementation inline in the editor.

### Verify

1. Accept the suggestion once.
2. Then deliberately reject the next suggestion and finish the function yourself.

### What You Should See

You should be able to compare how Copilot behaves when accepted versus rejected. A good result is one that matches the intended behavior without extra logic.

---

## Lab 2.7 — Agent Sessions and Sub-agents

### Goal

Use Agent Mode for a multi-step task.

### Steps

1. Open Copilot Chat in VS Code.
2. Select **Agent** mode.
3. Ask:

```text
Inspect this repository and suggest one documentation improvement. Use a sub-agent for file inspection if available.
```

4. Review the plan and session activity before approving actions.

### What You Should See

The agent may show a plan and delegate work to a sub-agent.

### Verify

Check that the result matches the files inspected.

---

## Lab 2.8 — Custom Agents and Instructions

### Goal

Customize Copilot's behavior.

### Steps

1. Create `.github/agents/reviewer.agent.md`.
2. Add:

```markdown
---
name: Reviewer
description: Reviews Python changes briefly.
---

Review Python changes for bugs and missing tests. Be concise.
```

3. Open Copilot Chat and select the custom agent if it appears.
4. Ask it to review a Python file.

### What You Should See

The agent should follow the profile instructions. Custom agents may be unavailable in some environments.

### Verify

Check that the response is concise and mentions bugs or tests.

---

## Lab 2.9 — MCP and External Tools

### Goal

Understand MCP tool access.

### Steps

1. Open Copilot Chat.
2. Ask:

```text
What MCP tools are available, and what does each tool do?
```

3. Review permissions before approving a tool.

### What You Should See

Copilot may list available MCP tools or report that none are configured.

### Verify

Record one tool's purpose and required permission. Do not approve unfamiliar tools.

---

## Lab 2.10 — Copilot CLI Sessions

### Goal

Use context across a Copilot CLI session.

### Steps

1. Open PowerShell in the repository folder.
2. Run:

```powershell
copilot
```

3. Ask:

```text
List the Python files in this repository.
```

4. Ask:

```text
Summarize the purpose of each file you found.
```

### What You Should See

The second response should use the first response's context.

### Verify

Compare both responses with the repository.

---
