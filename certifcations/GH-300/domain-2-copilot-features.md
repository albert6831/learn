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
- [Lab 2.11 — Chat Slash Commands](#lab-211--chat-slash-commands)
- [Lab 2.12 — Editor Code Actions](#lab-212--editor-code-actions)

## Lab 2.1 — Copilot Chat Debugging

### Goal

Debug code using Copilot Chat.

### What This Is

Copilot Chat can help locate the difference between a value and a callable method, explain the resulting error, and suggest a correction. This lab gives you a small reproducible bug so you can compare the explanation with the source code.

### Steps

1. Create:

```text
bug.ps1
```

2. Paste:

```powershell
function Get-Greeting {
    param([string]$Name)

    $upperName = $Name.ToUpper
    return "Hello " + $upperName.Trim()
}
```

### Ask Copilot Chat

1. Open Copilot Chat
2. Click New Chat
3. Type:

```text
Why does this function fail when I call Get-Greeting -Name 'Alberto'?
```

4. Press Enter

### What You Should See

Copilot should point out that `$Name.ToUpper` refers to a method and needs parentheses. Calling `Get-Greeting -Name 'Alberto'` should therefore fail when the script tries to call `Trim()` on that method object.

### Fix

1. Type:

```text
Fix this function.
```

2. Press Enter

### What You Should See

Copilot should change the expression to `$Name.ToUpper()` and explain that calling the method returns the uppercase string `ALBERTO`.

### What You Should Have Learned

- Use Copilot Chat to explain a reproducible bug, then confirm the explanation in the source.
- Distinguish a method reference from the value returned by invoking that method.

---

## Lab 2.2 — Copilot Edits Refactoring

### Goal

Refactor code using Copilot Edits.

### What This Is

Refactoring improves readability and maintainability without changing intended behavior. This lab uses Copilot Edits to make a small function more concise, then asks for type hints and documentation.

### Steps

1. Create:

```text
refactor.ps1
```

2. Paste:

```powershell
function Add-Numbers {
    param(
        [int]$First,
        [int]$Second
    )

    $sum = $First + $Second
    return $sum
}
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

Copilot Edits should propose a shorter implementation, such as returning `$First + $Second` directly. The result should preserve the function's behavior and should be shown as an editable change for you to review.

### Add Help

1. Highlight the refactored function
2. Press Ctrl+I
3. Type:

```text
Add comment-based help that documents the parameters and return value.
```

4. Press Enter

### What You Should See

The function should gain comment-based help describing the addition operation, its parameters, and its output. Review the help text before accepting the edit.

### What You Should Have Learned

- Use Copilot Edits for focused refactoring and documentation changes.
- Confirm that a refactor preserves behavior before accepting it.

---

## Lab 2.3 — Copilot CLI Documentation

### Goal

Generate a README using Copilot CLI.

### What This Is

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
Create or update README.md for this repository. Describe a PowerShell tool that cleans CSV files. Inspect the project files first and do not invent unsupported commands.
```

### What You Should See

Copilot CLI should propose README content with a project description and likely sections such as usage, installation, and examples. Review the proposed changes and approve them only after checking that they match the repository.

### What You Should Have Learned

- Use Copilot CLI to draft documentation from inspected repository context.
- Reject unsupported commands or claims in generated documentation.

---

## Lab 2.4 — Agent Mode Workflow

### Goal

Use Agent Mode for multi-step automation.

### What This Is

Agent Mode is intended for tasks that involve several related actions, such as creating files, implementing logic, and improving the result. This lab lets you observe how Copilot handles a multi-step request.

### Ask Agent Mode

1. Open Copilot Chat
2. Type:

```text
Create a new folder called csv_cleaner, generate a PowerShell script that reads a CSV, cleans missing values, and writes a new file.
```

3. Press Enter

### What You Should See

Agent Mode should propose or perform several steps: create the `csv_cleaner` folder, add a PowerShell script, and implement CSV input, missing-value handling, and output writing. Review any planned file changes before accepting them.

### Add Logging

1. Type:

```text
Add logging to each step.
```

2. Press Enter

### What You Should See

The script should be updated with logging around the main workflow, such as reading the input, cleaning values, and writing the output. The generated code should use appropriate log levels and remain readable.

### What You Should Have Learned

- Use Agent Mode for connected implementation tasks that span files and steps.
- Review the plan, generated changes, and operational details such as logging.

---

## Lab 2.5 — PR Summaries

### Goal

Use Copilot to summarize pull requests.

### What This Is

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
clean_orders.ps1
```

7. Paste:

```powershell
param(
    [string]$InputFile,
    [string]$OutputFile
)

Import-Csv -LiteralPath $InputFile |
    Where-Object { $_.email } |
    ForEach-Object {
        $_.email = $_.email.ToLowerInvariant()
        $_
    } |
    Export-Csv -LiteralPath $OutputFile -NoTypeInformation
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

### What You Should Have Learned

- Request Copilot review to surface potential bugs, security concerns, and test gaps.
- Validate each review comment against the diff before acting on it.

---

## Lab 2.6 — Inline Completion Review

### Goal

Practice accepting, rejecting, and editing inline completions.

### What This Is

Inline completion is code that Copilot suggests as you type in the editor. Accept it with Tab, reject it by continuing to type, or ignore it. It can be useful, but it still needs review for correctness and unintended assumptions.

### Steps

1. Create:

```text
inline_demo.ps1
```

2. Paste:

```powershell
function ConvertTo-SquaredList {
    param([int[]]$Values)
```

3. On the next line, begin typing `$result = foreach ($value in $Values) {` so Copilot can suggest an inline completion.

### What You Should See

Copilot may suggest a full implementation inline in the editor.

### Verify

1. Accept the suggestion once.
2. Then deliberately reject the next suggestion and finish the function yourself.

### What You Should See

You should be able to compare how Copilot behaves when accepted versus rejected. A good result is one that matches the intended behavior without extra logic.

### What You Should Have Learned

- Treat inline completions as editable suggestions, not automatic decisions.
- Compare accepted suggestions with the intended behavior and reject unnecessary code.

---

## Lab 2.7 — Agent Sessions and Sub-agents

### Goal

Use Agent Mode for a multi-step task.

### What This Is

An agent session is a task conversation that can plan work, use tools, and keep results in context. A sub-agent is a helper that handles a focused part of the task.

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

### What You Should Have Learned

- Agent sessions retain task context while sub-agents can investigate focused questions.
- Confirm that the final recommendation is grounded in the files actually inspected.

---

## Lab 2.8 — Custom Agents and Instructions

### Goal

Customize Copilot's behavior.

### What This Is

Custom agents use a profile file to define their name, purpose, and instructions. Repository instructions provide shared guidance for Copilot responses.

### Steps

1. Create `.github/agents/reviewer.agent.md`.
2. Add:

```markdown
---
name: Reviewer
description: Reviews PowerShell changes briefly.
---

Review PowerShell changes for bugs and missing tests. Be concise.
```

3. Open Copilot Chat and select the custom agent if it appears.
4. Ask it to review a PowerShell file.

### What You Should See

The agent should follow the profile instructions. Custom agents may be unavailable in some environments.

### Verify

Check that the response is concise and mentions bugs or tests.

### What You Should Have Learned

- Custom-agent profiles and repository instructions shape Copilot's behavior.
- Verify that an agent follows its stated scope and review criteria.

---

## Lab 2.9 — MCP and External Tools

### Goal

Understand MCP tool access.

### What This Is

MCP, or Model Context Protocol, lets Copilot connect to external tools and services. Each tool may require permissions, so review access before approving it.

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

### What You Should Have Learned

- MCP tools extend Copilot with external capabilities that require deliberate permission review.
- Understand a tool's purpose and access before approving it.

---

## Lab 2.10 — Copilot CLI Sessions

### Goal

Use context across a Copilot CLI session.

### What This Is

A Copilot CLI session keeps related requests together so follow-up prompts can use earlier context and results.

### Steps

1. Open PowerShell in the repository folder.
2. Run:

```powershell
copilot
```

3. Ask:

```text
List the PowerShell files in this repository.
```

4. Ask:

```text
Summarize the purpose of each file you found.
```

### What You Should See

The second response should use the first response's context.

### Verify

Compare both responses with the repository.

### What You Should Have Learned

- Copilot CLI can retain useful context across related prompts in one session.
- Check session-grounded responses against the repository for completeness and accuracy.

---

## Lab 2.11 — Chat Slash Commands

### Goal

Use a supported Copilot Chat slash command in VS Code.

### What This Is

Slash commands provide shortcuts for common chat tasks. The available commands can vary by VS Code and Copilot version, so use the command picker instead of assuming a particular command is installed.

### Steps

1. Open `bug.ps1` from Lab 2.1.
2. Open Copilot Chat and start a new conversation.
3. Type `/` in the chat input.
4. Inspect the slash commands shown in the picker.
5. Select a command that explains code, such as `/explain` if it is available.
6. Submit the selected command with this request:

```text
Explain the Get-Greeting function and identify the error it contains.
```

### What You Should See

Copilot should run the selected command and explain the code or the error. If `/explain` is not available, select another displayed command and follow its input prompt.

### Verify

Confirm that the response identifies `$Name.ToUpper` as a method reference rather than the uppercase string returned by `$Name.ToUpper()`.

### What You Should Have Learned

- Use the chat command picker to discover the slash commands available in your installed version.
- Treat slash commands as task shortcuts and still verify their output against the source.

---

## Lab 2.12 — Editor Code Actions

### Goal

Use a VS Code editor Code Action to apply a language-aware refactoring.

### What This Is

Code Actions are provided by VS Code extensions and language services. They are separate from Copilot prompts: use them for well-defined editor transformations, then use Copilot when you need explanation, broader changes, or review.

### Steps

1. Open `refactor.ps1` from Lab 2.2.
2. Place the cursor on the `$sum` assignment or the `return $sum` statement.
3. Open the Code Actions menu with `Ctrl+.` or select the lightbulb in the editor gutter.
4. Inspect the available actions.
5. Apply a refactoring action only if the installed PowerShell extension offers one that simplifies the function without changing its result.

### What You Should See

The Code Actions menu may offer diagnostics, quick fixes, or refactorings. The exact actions depend on the PowerShell extension and the code at the cursor; it is valid for no suitable refactoring to be available.

### Verify

Run the function before and after any applied action with the same inputs. Confirm that `Add-Numbers -First 2 -Second 3` still returns `5`.

### What You Should Have Learned

- Open Code Actions from the lightbulb or `Ctrl+.` to find extension-provided fixes and refactorings.
- Choose a language-aware Code Action for a bounded transformation and use Copilot for conversational or multi-file work.

---
