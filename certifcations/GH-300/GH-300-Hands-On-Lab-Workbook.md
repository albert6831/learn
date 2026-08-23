# GH-300 Hands-On Lab Workbook

> **Purpose**
> Use this workbook to practice responsible GitHub Copilot usage through short, observable exercises. Each lab includes the action to take and the result you should look for.

> **Recommended rhythm**
> **Prepare** the code or workspace → **Ask** Copilot → **Review** the response or proposed change → **Verify** it against the source, diff, or tests.

> **Study tip**
> Choose a domain below, complete its labs, and verify each result before moving on.

<details>
<summary><strong>Open the lab index</strong></summary>

## Table of Contents

- [Study by Exam Domain](#study-by-exam-domain)
- [Section 0 — Requirements & Setup](#section-0--requirements--setup)

- [Domain 1 — Use GitHub Copilot Responsibly](domain-1-responsible-use.md)
- [Domain 2 — Use GitHub Copilot Features](domain-2-copilot-features.md)
- [Domain 3 — Understand Copilot Data and Architecture](domain-3-data-and-architecture.md)
- [Domain 4 — Apply Prompt Engineering and Context Crafting](domain-4-prompt-engineering.md)
- [Domain 5 — Improve Developer Productivity](domain-5-developer-productivity.md)
- [Domain 6 — Configure Privacy, Content Exclusions, and Safeguards](domain-6-privacy-and-safeguards.md)

</details>

## Study by Exam Domain

| Domain | Focus | Exam weight |
| --- | --- | --- |
| 1 | Use GitHub Copilot Responsibly | 15–20% |
| 2 | Use GitHub Copilot Features | 25–30% |
| 3 | Understand Copilot Data and Architecture | 10–15% |
| 4 | Apply Prompt Engineering and Context Crafting | 10–15% |
| 5 | Improve Developer Productivity | 10–15% |
| 6 | Configure Privacy, Content Exclusions, and Safeguards | 10–15% |

## Section 0 — Requirements & Setup

### Requirements

- GitHub account
- Windows 10/11
- Active GitHub Copilot subscription
- Visual Studio Code
- Git
- PowerShell 6 or later
- GitHub Copilot extension
- GitHub Copilot Chat extension

### Install Visual Studio Code

Download from:

```text
https://code.visualstudio.com
```

### Install Git

Download from:

```text
https://git-scm.com/downloads
```

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

Download from:

```text
https://cli.github.com
```

### Install Copilot CLI

Copilot CLI is installed separately from GitHub CLI. Do not install it through the older GitHub CLI extension workflow.

#### Option 1: Install with WinGet

Open PowerShell and run:

```powershell
winget source update
winget install --id GitHub.Copilot --source winget
```

If WinGet cannot find the package, search for the current package ID:

```powershell
winget search GitHub.Copilot
```

Close and reopen PowerShell and VS Code after installation. Verify the installation:

```powershell
copilot --version
Get-Command copilot -All
```

### Sign In to Copilot CLI

1. Open a terminal in a trusted project folder.
2. Start Copilot CLI by running `copilot`.
3. If prompted, confirm that you trust the current folder.
4. Enter `/login` in the Copilot CLI prompt.
5. Complete the GitHub sign-in in your browser.

Copilot CLI may read, modify, or execute files below its current folder. Use it only in folders whose contents you trust.

### Use Copilot CLI in VS Code

1. Open the project folder in VS Code.
2. Open **Terminal > New Terminal**.
3. Run `copilot` in the integrated PowerShell terminal.
4. Review and approve file or command permissions individually.

The GitHub Copilot and GitHub Copilot Chat extensions provide the VS Code editor and chat integration. The `copilot` command runs separately in the integrated terminal.
