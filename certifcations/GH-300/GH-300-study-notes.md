# GH-300 Unified Deep Dive

Last updated: September 20, 2026 - 07:23 AM EDT

[Open the clean print view](gh-300-print.html)

These notes follow the GH-300 skills outline in exam order. Product names, menus, plans, and feature availability can change, so confirm version-specific behavior in the current GitHub documentation and in the tenant used for practice.

## Exam at a Glance

| Domain | Weight | Central question |
| --- | --- | --- |
| 1. Use GitHub Copilot responsibly | 15-20% | Can I use and validate AI output safely? |
| 2. Use GitHub Copilot features | 25-30% | Can I select and operate the right Copilot surface? |
| 3. Understand Copilot data and architecture | 10-15% | What happens to context, prompts, and responses? |
| 4. Apply prompt engineering and context crafting | 10-15% | Can I give Copilot useful, bounded context? |
| 5. Improve developer productivity | 10-15% | Can I use Copilot to improve delivery quality and speed? |
| 6. Configure privacy, content exclusions, and safeguards | 10-15% | Can I configure and troubleshoot organizational protection? |

### Core study loop

Use this loop for every Copilot response or code change:

1. **Prepare:** define the goal, constraints, inputs, outputs, and relevant context.
2. **Ask:** choose the smallest Copilot surface that fits the task.
3. **Review:** inspect the answer, diff, permissions, assumptions, and sources.
4. **Verify:** run tests, linters, security checks, or a manual comparison.
5. **Own:** accept only what you understand and can maintain.

---

## 1. Use GitHub Copilot Responsibly (15-20%)

### Understand responsible AI principles

#### Describe risks and limitations of generative AI tools

Generative AI predicts likely content; it does not guarantee truth, intent, originality, security, or fitness for purpose. Common risks include:

- **Hallucination:** confident but false explanations, APIs, citations, package names, or commands.
- **Inaccuracy:** code that compiles but mishandles errors, permissions, edge cases, or business rules.
- **Bias:** unsupported assumptions or unequal recommendations based on incomplete data.
- **Security weaknesses:** injection flaws, insecure defaults, exposed secrets, unsafe dependencies, or excessive permissions.
- **Privacy and confidentiality exposure:** sensitive prompts or files may be processed according to the applicable product and organization data controls.
- **License and attribution concerns:** generated output can resemble public code; follow the organization's review and licensing process.
- **Public-code similarity:** duplication or public-code matching controls can warn about output that resembles publicly available code; a warning does not decide whether the output is legally or technically suitable.
- **Automation risk:** an agent may modify files or run commands with unintended consequences if permissions and scope are too broad.
- **Context and model limits:** relevant files may be omitted, truncated, summarized, or misunderstood when the context is large.

Mitigations include least-privilege access, content exclusions, secret scanning, dependency and license review, tests, static analysis, human approval, and clear ownership of the final result.

Copilot does not automatically have access to every private file or repository. What it can use depends on the feature, explicitly supplied context, workspace or repository permissions, policy, and client. Data-use and training treatment also depends on the applicable GitHub product, plan, terms, and organization settings; do not memorize an unconditional statement such as "private code is never used for training" without checking the current policy.

#### Describe ethical and responsible AI usage

- Use Copilot for authorized work and respect organizational policy, privacy, intellectual property, and applicable law.
- Do not submit credentials, tokens, personal data, proprietary material, or regulated data unless the approved configuration explicitly permits it.
- Keep a human accountable for decisions, especially code that affects security, safety, finances, access, or people.
- Be transparent when AI assistance is relevant to a review or decision process.
- Give Copilot only the context and permissions needed for the task.
- Treat generated content as a draft or suggestion until it has been reviewed and tested.

Microsoft's commonly taught Responsible AI principles are:

- **Fairness:** treat people fairly and avoid unjustified bias.
- **Reliability and safety:** perform consistently and avoid unacceptable harm.
- **Privacy and security:** protect data and systems from unauthorized use.
- **Inclusiveness:** design for and support people with diverse needs and abilities.
- **Transparency:** make capabilities, limitations, and relevant AI use understandable.
- **Accountability:** assign people responsibility for outcomes and remediation.

#### Identify potential harms and mitigation strategies

| Potential harm | Practical mitigation |
| --- | --- |
| Incorrect production behavior | Tests, staged rollout, code review, monitoring, rollback plan |
| Biased recommendation | Remove irrelevant personal attributes; use job-related evidence; review outcomes |
| Secret disclosure | Never paste secrets; use secret managers or environment configuration; rotate exposed secrets |
| Vulnerable implementation | Threat model, secure coding review, dependency scanning, security tests |
| Unapproved file or command changes | Use a trusted folder, narrow scope, review the plan and diff, approve permissions individually |
| Unlicensed or copied code | Review public-code matching signals and licensing requirements |
| Overreliance on an answer | Ask for assumptions, inspect the source, reproduce the result, and seek expert review |

Avoid using Copilot as the sole authority for high-impact decisions or as a substitute for qualified legal, medical, security, compliance, or accessibility expertise. Do not use it to generate or process competitor proprietary code, sensitive communications, or excluded repository content unless the applicable authorization and policy explicitly allow the activity.

### Validate and operate AI tools

#### Explain the need to validate AI output

Validation is necessary because fluent output is not evidence of correctness. Check:

- Does the response answer the stated requirement rather than a nearby one?
- Are APIs, commands, files, dependencies, and citations real and available in this environment?
- Does the code handle invalid input, empty values, boundaries, failures, and authorization?
- Do tests cover normal paths and meaningful edge cases?
- Does the diff preserve behavior and avoid unrelated changes?
- Does the result meet security, privacy, performance, accessibility, and licensing requirements?

Ask Copilot to explain its reasoning or list assumptions, but verify the claims independently. Explanation is useful evidence to investigate, not proof.

#### Human oversight checklist

Humans remain accountable for the accepted result. Review the code and logic, test normal and edge-case behavior, check security and privacy implications, confirm compliance and licensing, and ensure the output is maintainable. Generated tests also require review: they may contain incorrect assertions, miss important cases, or merely reproduce the implementation's mistake.

For security-sensitive code, guide Copilot with secure coding requirements, validate input handling, avoid hardcoded secrets and unsafe operations, and run approved security scanning such as GitHub Advanced Security where available.

#### Identify how to operate GitHub Copilot responsibly

Use a trusted workspace, sign in with the correct account, and understand whether the current feature can read, write, or execute. Before accepting an agent action:

1. Review the proposed plan and affected files.
2. Confirm the task is authorized and the scope is minimal.
3. Inspect tool permissions and commands.
4. Approve only expected actions.
5. Review the resulting diff and run validation.

Reframe dual-use requests toward authorized defensive outcomes. For example, ask for authentication hardening or a test plan rather than instructions to bypass authentication.

#### Responsible-use memory aids

**SAFE** summarizes the goal of responsible Copilot use:

- **S** — Safeguards
- **A** — Accountability
- **F** — Fairness
- **E** — Ethics

**HINT** summarizes common limitations:

- **H** — Hallucinations
- **I** — Incomplete context
- **N** — Not automatically trained on or given access to private code; verify current data policy and permissions
- **T** — Testing required

Content exclusions and public-code matching are covered in more detail under [Domain 6](#6-configure-privacy-content-exclusions-and-safeguards-10-15). They reduce risk but do not replace access controls, secret removal, human review, or testing.

---

## 2. Use GitHub Copilot Features (25-30%)

### Use GitHub Copilot in the IDE

#### Enable Copilot in the IDE

Typical setup in VS Code:

1. Install or enable the GitHub Copilot and Copilot Chat extensions.
2. Sign in to GitHub with an account that has Copilot access.
3. Open a trusted project folder.
4. Confirm Copilot status in the Accounts/status area.
5. Check editor and organization policies if suggestions or chat are unavailable.

Availability can depend on the editor, extension versions, subscription, organization policy, language, and file state.

#### Trigger Copilot through inline suggestions, chat, CLI, and agent mode

- **Inline suggestions:** suggestions appear while typing; accept, reject, or edit them. They are not automatically correct.
- **Chat:** ask questions about selected code, files, workspace context, debugging, explanations, tests, or design. Use the command picker for available slash commands.
- **Inline chat / Edits:** select code or place the cursor, describe a focused change, review the proposed diff, and accept or reject it.
- **Agent mode:** delegate a multi-step task involving planning, tools, proposed file changes, and verification. Review the plan and permissions before approving actions.
- **Copilot CLI:** use the terminal for repository questions, scripts, documentation, file operations, and command suggestions. Review commands before execution.

Choose inline completion for local code, chat for explanation or discussion, Edits for bounded changes, Agent mode for connected multi-step work, and CLI for terminal-centered workflows.

**IDE memory tip:** Copilot in the IDE can **write, fix, explain, document, and test**. The exact commands and availability vary across VS Code, JetBrains IDEs, Visual Studio, extensions, languages, plans, and organization policy.

#### Configure content exclusions for specific files or repositories (app knowledge)

Content exclusions prevent configured files or paths from being used by supported Copilot features in supported environments. They are not a replacement for removing secrets from a repository.

- Configure exclusions at the scopes supported by your plan, which may include user, repository, organization, or enterprise.
- Use precise patterns for sensitive or restricted paths.
- Check whether the exclusion applies to the specific feature, editor, plan, policy, path syntax, and file casing.
- Test with a harmless marker or a request that should not reveal excluded content.
- Remember that exclusions do not erase data already shared, prevent every data path, or substitute for access controls.

Important limitation: content-exclusion support differs by Copilot surface. GitHub's current documentation identifies Edit and Agent modes in Visual Studio Code and other editors as unsupported for content exclusion, and notes that an IDE may still provide indirect semantic information such as type information or hover definitions. Check the current support matrix before relying on an exclusion.

### Use GitHub Copilot CLI

#### Define Copilot CLI and how it benefits developers

Copilot CLI is a terminal-based Copilot interface. It can inspect a trusted working directory, explain commands and files, draft scripts, edit files, and maintain context across a session. It is separate from the traditional GitHub CLI command set and should be installed and authenticated according to the current official instructions.

Benefits include working without leaving the terminal, repository-aware assistance, command explanation, script generation, and follow-up questions that retain session context.

#### Identify the steps for installing GitHub Copilot CLI

The exact installer varies by operating system and release. The general sequence is:

1. Check the current official Copilot CLI installation instructions.
2. Install the supported `copilot` package or binary using the approved method.
3. Reopen the terminal if required.
4. Verify with `copilot --version` and `Get-Command copilot -All` on PowerShell.
5. Start `copilot`, run `/login` if prompted, and complete GitHub authentication.
6. Confirm the account, plan, and organization policy permit the intended features.

#### Describe key Copilot CLI features and commands

The CLI can provide interactive conversation, repository inspection, command and script generation, file creation or modification, and session context. Common commands or interaction patterns include:

- `copilot` starts the interactive CLI.
- `/login` authenticates the CLI session when available.
- `/help` displays supported commands and options in the installed version.
- `/exit` or the installed quit command ends the session; confirm with `/help` because commands can change.
- Natural-language requests ask questions, explain files, draft changes, or propose commands.

Do not assume every slash command is available in every release. Use the in-product help and review any command before running it.

**CLI memory tip:** Copilot CLI helps **generate, explain, and troubleshoot** commands and scripts. It can propose file operations, so use a trusted folder and review commands before execution.

#### Use Copilot CLI interactively and in sessions

Start from a trusted project directory. Ask a focused question, inspect the response, then use follow-up prompts that refer to the earlier result. Session context is helpful but is not a guarantee that every file or detail remains available. Re-check the repository when accuracy matters.

#### Generate scripts and manage files with Copilot CLI

State the target shell, paths, inputs, outputs, error behavior, and constraints. Ask CLI to inspect existing files before generating a script. Before approval:

- inspect the exact diff and generated commands;
- check for destructive operations, secret handling, and path assumptions;
- run the script in a safe test directory with representative inputs;
- confirm that the result did not invent files, dependencies, or usage instructions.

### Use GitHub Copilot features and capabilities

#### Agent Mode, Copilot Edits, MCP, Agent Sessions, and sub-agents

- **Agent Mode:** plans and orchestrates a connected task using available tools. It may propose file changes or tool actions; the user remains responsible for approval and review before execution.
- **Copilot Edits:** proposes focused changes across selected code or files. It is useful for refactoring, documentation, and targeted fixes; review the diff before accepting.
- **MCP:** Model Context Protocol allows Copilot to use external tools or services. Understand each tool's purpose, inputs, outputs, and permissions before approval.
- **Agent session:** a multi-step agent task may preserve conversation context, task state, plans, and results; this varies by implementation and context limits.
- **Sub-agent:** where supported, an agent may delegate a focused investigation or implementation to reduce context burden. Verify delegated findings and how they were produced.

**Agent Mode memory tip:** **Think -> Plan -> Act with approval**. Copilot may break down a task, use tools, read files, propose writes, and orchestrate a multi-step workflow, but it does not remove the need for permission review, diff review, or testing.

MCP commonly exposes structured **tools**, **resources**, and **prompts**, with **sessions** carrying interaction state. Remember MCP as **tools/resources/prompts/sessions**. Treat MCP as an integration protocol, not an unrestricted plugin system: review the server, permissions, data access, tool side effects, and returned content before enabling it.

Use the least powerful surface that can complete the task, keep the scope explicit, and verify every externally observable change.

#### Use Copilot for code review and coding assistance

Copilot can explain code, find likely bugs, propose fixes, generate tests, suggest refactors, document APIs, and review a pull request. Ask for specific criteria such as correctness, security, performance, maintainability, or test gaps. Treat comments as hypotheses: confirm each one against the diff and run appropriate checks.

#### Use Spaces, Spark, PR summaries, and instruction files

- **Spaces:** organize and ground conversations with selected repositories, files, documents, or other relevant context where available.
- **Spark:** where available, use the product's natural-language app-building workflow. Availability and capabilities vary; inspect generated code, configuration, dependencies, and deployment behavior like any other generated output.
- **Pull request summaries:** provide a concise overview of changes, intent, and review focus. Compare the summary with the actual diff.
- **Instruction files:** repository or path-specific instructions establish project conventions, commands, boundaries, and review expectations. Keep them accurate, scoped, and non-conflicting.

Instructions guide behavior; they do not grant permissions, guarantee compliance, or replace code review.

Spaces are primarily a way to collect and share context for Copilot conversations. Spaces are not a cloud sandbox: code placed in a Space is not automatically executed or tested. Use an approved development or test environment to run generated code and apply the same privacy controls to the material added to a Space.

**PR memory tip:** Copilot for pull requests can **summarize, explain, suggest, and assist with review**. A generated summary or review comment is not approval and must be checked against the diff.

#### Use Copilot for GitHub Actions

Copilot can help create or explain workflow YAML, troubleshoot failed runs, suggest job or runner configuration, and clarify actions syntax. State the trigger, permissions, secrets, runner, dependencies, artifacts, environments, and deployment boundaries. Review generated workflows for:

- excessive `GITHUB_TOKEN` permissions;
- untrusted input in commands or expressions;
- unsafe use of third-party actions or floating versions;
- accidental secret exposure in logs;
- unnecessary privileged runners or deployment environments;
- missing timeouts, concurrency controls, tests, or failure handling.

Run workflow changes in a safe branch and inspect the Actions logs and resulting permissions before enabling production deployment.

#### Understand Chat limits, options, feedback, commands, and prompt files

Chat has limits involving context size, available files, model capability, latency, feature availability, and permissions. Use the model or mode selector and relevant attachments/context controls when available. Use thumbs-up/down or other feedback mechanisms to report useful or problematic results according to organizational policy.

Use the slash-command picker rather than memorizing commands. Prompt files can store reusable prompts for consistent tasks such as reviews, tests, or documentation. Keep reusable prompts explicit about inputs, output format, constraints, and verification steps.

### Manage organization-wide settings and policies

#### Configure organization-wide policy management

Organization and enterprise administrators can control feature availability, plans, policies, and access. Settings may include Copilot Chat, Agent Mode, Copilot for Pull Requests, public-code matching, content exclusions, audit, and availability across supported surfaces such as IDE, GitHub.com, and CLI. Exact controls depend on the plan and current GitHub administration interface.

Use a policy workflow of **identify scope -> change the smallest setting -> document owner and rationale -> test with a non-production account -> monitor audit events -> review periodically**.

#### Enable Copilot Code Review policies and manage availability

Confirm that the organization and repository are eligible, then enable or restrict Copilot for Pull Requests or AI-assisted review according to policy. Members may still need the correct license and repository permissions. Check the PR experience with a test repository and ensure reviewers understand that AI review does not replace human approval.

#### Utilize audit log events

Audit logs help administrators review relevant organization activity, investigate issues, and support compliance. Event names, fields, retention, and export capabilities vary by product and plan. Filter by actor, action, repository, and time; preserve the event details needed for the investigation without exposing unnecessary personal data.

#### Manage subscriptions using the REST API

Subscription and seat management may be automated through supported GitHub REST API endpoints. Exact endpoints and programmatic seat operations vary by plan and release. Before using an endpoint, verify the current documentation for the route, HTTP method, required scopes, organization permissions, request body, pagination, rate limits, and response schema. Use a least-privilege token, avoid logging tokens, test with a non-production scope, and handle errors and retries.

**Enterprise memory tip:** enterprise Copilot combines **control and compliance** through policy enforcement, content exclusions, public-code or duplication controls, audit logging, feature availability, and governance. These controls vary by plan and role; verify the effective policy at the enterprise, organization, repository, and user scopes.

### Domain 2 quick memory sheet

Copilot features span **IDE + CLI + PR + Agents + MCP + Spaces + Spark + Actions + Enterprise**.

A shorter workflow memory aid is **Write + Fix + Explain + Test + Plan + Act + Govern**. Use it to recall capabilities, not as a substitute for checking which features are enabled in a specific client or plan.

---

## 3. Understand GitHub Copilot Data and Architecture (10-15%)

### Describe data handling and flow

#### Explain data usage, flow, and sharing

At a high level, a Copilot request flows through a client or GitHub surface to service components that prepare context, apply policy and filtering, call an underlying model, post-process the result, and return a suggestion or response. The exact retention, training use, storage, subprocessors, and sharing rules depend on the product, plan, account type, and organization settings.

Study the distinction between:

- **Input:** prompt text, selected code, open files, repository context, chat history, and metadata used by the feature.
- **Processing:** context selection, prompt construction, policy checks, filtering, and model inference.
- **Output:** completion, chat response, proposed diff, command, review comment, or tool action.
- **Controls:** access permissions, policies, exclusions, filtering, audit, retention, and feedback settings.

Never infer data policy from the fact that a feature is AI-powered. Read the applicable GitHub terms, documentation, and organization policy.

#### Describe input processing and prompt building

Copilot does not necessarily send the entire repository. It selects relevant context based on the feature, cursor position, open and selected files, chat attachments, workspace signals, conversation history, and available limits. That context is combined with system or product instructions and the user's request to build a model input.

Relevance, privacy, size, and permissions all affect what is included. Explicitly selecting the right code and naming the source of truth improves grounding.

#### Explain proxy filtering and post-processing

Service-side layers can apply authentication, policy checks, safety filtering, public-code or duplication checks, and request routing before model inference. Post-processing can filter or transform returned content, attach metadata, apply formatting, and enforce feature-specific safeguards. These layers reduce risk but do not make output infallible.

### Understand lifecycle and limitations

#### Visualize the code suggestion lifecycle

Printable flow:

1. The user enters a prompt or places the cursor.
2. Copilot gathers relevant available context.
3. The client builds a request with product instructions.
4. Authentication, policy, safety, and proxy filtering are applied.
5. An available model generates a response.
6. The service post-processes the result and applies feature safeguards.
7. Copilot displays a suggestion, answer, diff, or tool proposal.
8. The user reviews, accepts, rejects, refines, and verifies the result.

The lifecycle is conceptual. Product implementations can differ by feature, client, plan, and release.

#### Describe limitations of LLMs and Copilot

LLMs can be probabilistic, stale, sensitive to wording, and unable to reliably infer hidden requirements. Copilot may omit context, misread code, produce non-deterministic alternatives, repeat insecure patterns, or fail on unusual inputs. It cannot replace domain expertise, tests, security review, legal review, or operational monitoring.

---

## 4. Apply Prompt Engineering and Context Crafting (10-15%)

### Craft effective prompts

#### Describe prompt structure and context

A strong coding prompt commonly includes:

1. **Role or perspective:** what kind of reviewer or implementer Copilot should be.
2. **Task:** the one result to produce.
3. **Context:** selected code, files, errors, constraints, and relevant conventions.
4. **Requirements:** inputs, outputs, language, behavior, security, performance, and compatibility.
5. **Examples:** representative inputs and expected outputs.
6. **Output format:** patch, code block, checklist, tests, table, or explanation.
7. **Boundaries:** what not to change, assumptions to avoid, and files to leave untouched.
8. **Verification:** tests, commands, acceptance criteria, or questions to answer.

#### Understand how context is determined

Context can come from the current file and cursor, selected text, open tabs, attached files, workspace or repository indexing, chat history, instructions, and the user's explicit prompt. Context is constrained by relevance, permissions, feature support, and context-window limits. More context is not always better: irrelevant or conflicting material can reduce accuracy.

#### Use zero-shot and few-shot prompting

- **Zero-shot:** provide instructions without examples. It is quick but leaves format and ambiguous terms open to interpretation.
- **Few-shot:** provide one or more examples of the desired input/output pattern. It improves consistency of format and style but can also reproduce mistakes or bias in the examples.

With either method, validate the result against explicit acceptance criteria.

#### Apply best practices for prompt crafting

- State one clear outcome and use concrete verbs.
- Specify language, framework, version, inputs, outputs, and error behavior.
- Include the smallest relevant code or files and identify the source of truth.
- Define non-functional requirements such as security, performance, accessibility, or compatibility.
- Ask for tests and edge cases, not only the implementation.
- Ask Copilot to state assumptions and ask clarifying questions when requirements conflict.
- Use an iterative prompt: draft, inspect, refine, test, and correct.
- Avoid pasting secrets or unnecessary private data.

Example:

```text
In PowerShell 7, add a function to the selected file that reads a CSV path and writes a cleaned CSV path. Treat blank email values as invalid, preserve all other columns, use parameter validation, and return a nonzero error on failure. Do not change unrelated functions. Add Pester tests for valid, blank, missing-file, and empty-input cases. Show the proposed diff and list assumptions before editing.
```

### Engineer prompts for performance

#### Explain prompt engineering principles

Prompt engineering is the deliberate design and refinement of instructions and context to improve relevance, correctness, consistency, and efficiency. The main levers are specificity, context quality, decomposition, examples, constraints, output format, and feedback from verification.

#### Describe prompt process flow and chat history usage

The typical process is:

1. Define the outcome and acceptance criteria.
2. Supply relevant context and constraints.
3. Ask for a first response or plan.
4. Review assumptions and gaps.
5. Refine the prompt or provide corrective information.
6. Apply and verify the result.

Chat history can preserve earlier requirements and responses, reducing repetition. It can also carry forward a wrong assumption, consume context, or make a later request ambiguous. Start a new chat when the topic, security boundary, or source of truth changes.

---

## 5. Improve Developer Productivity with GitHub Copilot (10-15%)

### Enhance productivity and code quality

#### Use Copilot for code generation, refactoring, and documentation

- **Generation:** specify behavior, interfaces, error handling, and tests before accepting code.
- **Refactoring:** state the behavior that must remain unchanged; compare before and after outputs and review the diff.
- **Documentation:** ask Copilot to derive documentation from the actual code and flag unknowns rather than inventing usage or APIs.

Copilot can reduce typing and search time, but review remains part of the task.

#### Accelerate learning and reduce context switching

Ask Copilot to explain an unfamiliar function, compare alternatives, define terminology, summarize a file, or create a focused learning example. Keep the question tied to the current code and verify explanations with documentation or experiments. Use chat, inline help, and reusable prompt files to avoid repeatedly reconstructing context.

#### Generate sample data and modernize legacy code

For sample data, define the schema, valid and invalid cases, volume, privacy constraints, and whether values must be deterministic. Use synthetic data; do not copy production personal or confidential data.

For legacy modernization, first capture current behavior with tests, then request a small refactor. Compare outputs, performance, error handling, compatibility, and dependencies before merging.

### Support testing and security

#### Generate unit and integration tests

Ask Copilot to identify the unit under test, setup, dependencies, expected behavior, cleanup, and framework conventions. Request normal, boundary, invalid, failure, authorization, and regression cases. For integration tests, define the real boundary such as a database, API, file system, or queue and specify isolation and cleanup.

Run the tests yourself. A generated test can be wrong, tautological, flaky, or too closely coupled to the implementation.

#### Identify edge cases and write assertions

Useful edge cases include empty and null values, minimum and maximum values, duplicates, unexpected types, Unicode, time zones, network failures, permission failures, retries, partial writes, concurrency, and malformed input. Assertions should verify observable behavior, not merely that code ran or that a mocked function was called.

#### Suggest security improvements and performance optimizations

Ask for a threat model or a review against a named standard, then validate suggestions with security tools and expert review. Look for injection, authentication and authorization flaws, secret exposure, unsafe deserialization, path traversal, insecure dependencies, logging of sensitive data, and missing validation.

For performance, measure a baseline first. Ask about algorithmic complexity, unnecessary I/O, repeated work, memory growth, batching, caching, and concurrency. Do not trade correctness or security for an unmeasured optimization.

---

## 6. Configure Privacy, Content Exclusions, and Safeguards (10-15%)

### Manage privacy settings and exclusions

#### Configure content exclusions and editor settings

Content exclusions are policy controls that restrict selected files or repositories from supported Copilot context. Configure them at the appropriate user, repository, organization, or enterprise level according to the current administration UI. Confirm the scope, pattern syntax, inherited policies, and supported features.

Editor settings can control suggestions, inline completions, chat behavior, telemetry or feedback choices, and language-specific enablement. A local editor setting cannot override an organization restriction or grant a missing license.

After changing settings, test with a non-sensitive marker and inspect Copilot's context behavior. Keep secrets out of source control regardless of exclusion configuration.

#### Describe ownership and limitations of outputs

Review the current GitHub terms, applicable plan terms, organization policy, and local legal guidance for ownership and use of generated output. Copilot output may not be unique, may resemble public code, and may require licensing or attribution review. The user or organization remains responsible for deciding whether output is suitable, compliant, secure, and maintainable.

Do not assume that generated output is automatically owned exclusively by one person, free of third-party obligations, or safe to publish.

### Apply safeguards and troubleshoot

#### Enable suggestions matching public code filtering

The public-code matching or duplication-detection control determines how suggestions that match or resemble publicly available code are handled. The available choices and policy scope depend on the plan and administration settings. Confirm the setting at the organization or enterprise level, understand whether matching suggestions are blocked or surfaced for review, and apply the organization's licensing process.

#### Resolve issues with suggestions and content exclusions

Use this troubleshooting order:

1. Confirm the user is signed in to the intended GitHub account and has an active Copilot entitlement.
2. Check organization or enterprise policy, repository access, and feature availability.
3. Verify the Copilot and Chat extensions, editor, CLI, and network state are supported and current.
4. Check whether the file language, location, trust state, or local editor setting disables suggestions.
5. Inspect content-exclusion patterns, inheritance, path casing, and feature support.
6. Test with a harmless file outside the excluded path and compare the behavior.
7. Review logs or status information without sharing secrets or sensitive source.
8. Reproduce with the smallest prompt and report the account, feature, client version, scope, and expected versus actual result.

Common causes include an incorrect account, missing seat, policy restriction, untrusted workspace, unsupported file type, stale extension, network or proxy issue, an exclusion that matches the file, or an exclusion that does not apply to the feature being tested.

---

## High-Yield Review: Chapters 1-13

This compact recap is for final revision. Feature availability, plan names, data handling, and administration controls are subject to the current GitHub product documentation and organization policy.

### 1. Responsible AI and limitations

- LLMs predict patterns; fluent output is not truth, intent, or correctness.
- Copilot output must be reviewed, tested, and checked for security, privacy, licensing, and maintainability.
- Common risks include outdated syntax, deprecated APIs, insecure patterns, hallucinations, bias, and missing edge cases.
- Responsible AI combines clear constraints, appropriate permissions, human accountability, and verification.
- Key principles include fairness, transparency, privacy and security, reliability and safety, inclusiveness, and accountability.

### 2. Copilot plans and controls

Individual, Business, and Enterprise offerings can differ in available administration, policy, privacy, support, and governance controls. Do not treat a plan comparison as permanent product behavior. In general, organizational plans provide more centralized policy and administration capabilities; Enterprise can add broader governance and GitHub Enterprise integration where supported.

For an exam scenario, identify the required control first, then ask which plan, role, organization setting, repository policy, and client support it requires. Content exclusions, audit, public-code matching, and feature availability are not guaranteed solely by a plan name.

Study model: Individual is oriented toward personal use, Business toward centralized organization controls, and Enterprise toward broader enterprise governance and integration. Treat this as a memory aid, then verify the current plan matrix for content exclusions, audit, code referencing, telemetry, GitHub Enterprise integration, and advanced compliance.

### 3. Copilot in the IDE

IDE surfaces include inline or ghost-text suggestions, Chat, slash commands, code actions, Edits, test generation, refactoring, and documentation generation. Use the IDE to write, fix, explain, document, and test, but remember that Copilot does not automatically repair deprecated syntax, enforce every best practice, or guarantee that a suggested API is current. Business or Enterprise policy may add filtering and enforcement depending on the feature and configuration.

### 4. Organization and policy management

Administrators may manage repository access, code-referencing or public-code settings, Chat and repository context, content exclusions, feature availability, code review, audit events, and subscriptions. The effective setting can be inherited across enterprise, organization, repository, and user scopes. REST API automation requires the current endpoint, correct permissions, least-privilege authentication, rate-limit handling, and careful secret handling.

Content exclusions are enforced by the applicable service and policy scope; a user-enabled IDE feature should not be treated as a supported bypass. Test exclusions with a harmless marker and confirm the feature, client, plan, and policy actually support the exclusion.

### 5. Copilot Chat

Chat and code completion follow the same conceptual path: gather relevant context, build a request, apply policy and filtering, route to a model, generate a response, post-process it, and present the result. Chat can explain, debug, refactor, summarize, generate tests, and answer repository questions. Context may come from selected code, open files, attachments, workspace signals, history, and instructions; repository context is feature- and client-dependent rather than universally manual or automatic.

Chat history and context windows are limited. Older instructions or messages may no longer be available, and Copilot may lose an earlier assumption. Restate critical constraints, start a fresh conversation when the source of truth changes, and verify any repository claim against the actual files.

### 6. Copilot CLI

Copilot CLI supports command generation, explanation, troubleshooting, script creation, testing, refactoring, repository inspection, and file changes. Its lifecycle is input and context -> request processing and model routing -> proposed output or action -> user refinement and verification. Use the installed help command to discover supported slash commands, and review every command or file change before execution.

Useful command intents include **explain**, **fix**, **generate**, **test**, and **refactor**. These describe common tasks, not a guarantee that every release exposes identical slash commands; use the installed CLI help to confirm syntax.

### 7. Code suggestion lifecycle

1. Gather relevant context.
2. Build a request with product instructions and the user's prompt.
3. Apply authentication, policy, safety, and filtering controls.
4. Route the request to an available model or service.
5. Generate a suggestion or response.
6. Apply post-processing and feature-specific safeguards.
7. Display the result for human review, acceptance, rejection, or refinement.

Copilot does not necessarily receive the entire repository or only the text typed in the prompt. It uses available relevant context subject to feature behavior, permissions, exclusions, context limits, and client settings.

### 8. Data handling and model behavior

Copilot data handling depends on the product surface, plan, account, terms, retention rules, and organization settings. Ask what input is processed, where it flows, how it is filtered, whether it is retained, and who can administer or audit the feature. Do not use the shorthand “data is discarded” or “private code is never used for training” without checking the applicable current policy.

Content exclusions can restrict supported Copilot features from using configured content as context, but they do not remove secrets, erase prior disclosures, or replace repository permissions and data governance.

### 9. Limitations and model behavior

- Copilot can produce outdated syntax, hallucinations, insecure patterns, and incomplete solutions.
- Context windows are limited; irrelevant or missing context can change the answer.
- Frequency bias can favor common patterns over the best pattern for the project.
- Pattern prediction is not reliable calculation or deep understanding.
- Output may resemble training or public code; review duplication and licensing concerns.
- Tests, static analysis, security review, documentation, and domain expertise remain necessary.

### 10. Prompt crafting

Zero-shot prompts provide instructions without examples; few-shot prompts provide examples of the desired pattern. Good prompts specify the task, relevant context, language and versions, constraints, inputs and outputs, examples, boundaries, output format, assumptions, and verification steps. Multimodal inputs, where supported, should be treated like any other supplied context and reviewed for privacy and accuracy.

Prompt parts to remember are **intent, context, constraints, examples, output format, and clarifications**. Few-shot examples can improve consistency because they demonstrate the requested pattern, but they can also pass along ambiguity or incorrect behavior. Break complex work into steps, use repository context deliberately, avoid ambiguity, and restate important constraints when history or context may be limited.

### 11. Boilerplate code: Terraform and GitHub Actions

Copilot is often useful for repetitive boilerplate because common structures are well represented in its learned patterns. It can draft:

- Terraform provider and `terraform` blocks, backend configuration, and resource skeletons;
- GitHub Actions workflow headers, triggers, jobs, checkout steps, and runtime setup for Node, Python, or Java.

Boilerplate still requires review for provider and action versions, state and secret handling, permissions, untrusted input, runner choice, deployment boundaries, and environment-specific configuration. Repetition makes a pattern easy to generate, not automatically safe or current.

### 12. Developer productivity and the SDLC

Copilot can reduce low-value work and context switching across the lifecycle while leaving high-value decisions with the developer:

| SDLC phase | Useful Copilot assistance |
| --- | --- |
| Requirements | Summaries, acceptance criteria, business rules, clarification questions |
| Design | Architecture options, tradeoff explanations, modernization plans |
| Implementation | Code generation, refactoring, translation, debugging |
| Testing | Unit and integration tests, edge cases, test explanation |
| Deployment | GitHub Actions, Terraform, Kubernetes manifests, runbook drafts |
| Maintenance | Documentation, deprecated API updates, modernization, technical debt analysis |

Other productivity uses include learning languages and frameworks, generating synthetic sample data, data-science assistance, documentation, and personalized context-aware explanations. Verify generated results against project conventions, tests, security requirements, and operational constraints.

### 13. Testing and edge cases

Copilot can draft unit and integration tests, explain failures, identify edge cases, and update tests after a code change. Ask for boundary values, null or undefined values, invalid input, exceptions, state transitions, authorization failures, partial failures, and regression cases where relevant.

Generated tests can miss domain-specific behavior, encode incorrect expectations, or assert implementation details rather than observable behavior. Run the tests, inspect their setup and assertions, and add cases based on the actual requirements and threat model.

### 14. SKUs and configuration

Individual, Business, and Enterprise offerings commonly differ in governance, administration, privacy controls, support, and integration. A useful study model is **Individual = personal use**, **Business = centralized organization controls**, and **Enterprise = broader enterprise governance and integration**. Confirm the current plan matrix before treating content exclusions, audit, code referencing, GitHub Enterprise integration, or advanced compliance as available.

Configuration can exist at multiple scopes, commonly enterprise, organization, repository, user, and editor or workspace. Higher-level policy may constrain lower-level settings. Check the effective configuration rather than assuming a local editor setting can override an organization restriction.

Instruction and configuration files can define repository conventions, allowed workflows, review expectations, languages, or path-specific guidance. They influence Copilot behavior but do not grant permissions, override platform policy, or guarantee that generated output follows every instruction.

For study questions that present only organization, repository, and user scopes, remember that a more specific setting may still be constrained by an inherited higher-level policy. Editor settings and instruction files are additional local guidance layers, not substitutes for administrative controls.

### Ultra-high-yield exam facts

- LLMs predict patterns, not correctness.
- Copilot may suggest outdated or deprecated code.
- Human review and testing are mandatory habits, not optional cleanup.
- Context is selected from available prompt, file, workspace, history, instruction, and feature context; it is not necessarily the whole repository.
- Business and Enterprise controls vary by plan, policy, and current product support; verify content exclusions, governance, audit, and public-code settings.
- Chat and completion share the same high-level data-flow stages.
- Copilot CLI supports model-routed, terminal-centered assistance, but command and file changes require approval.
- Limited context and missing requirements increase hallucination risk.

### Quick memory sheet

- **LLM behavior:** Predict -> not understand.
- **Copilot data flow:** Look -> collect -> send -> filter -> answer -> review. Retention depends on the product, plan, and organization settings; confirm the applicable retention policy.
- **Copilot limitations:** Outdated -> hallucinate -> limited context -> frequency bias.
- **Governance:** policy -> exclusion -> audit -> human accountability.

### Ultra-short memory version

- Copilot predicts patterns and can hallucinate.
- Plan and policy scope determine governance and privacy controls.
- Copilot uses relevant available context, not automatically the entire repository.
- Few-shot examples can improve consistency, but they can also reproduce errors.
- Copilot is effective at boilerplate and repetitive SDLC tasks, but generated infrastructure and workflows require security review.
- Copilot can generate tests and edge cases, but developers must validate assertions and coverage.
- Configuration scope and effective policy matter more than a single local editor setting.

---

## Final Review Checklist

- Can I explain why Copilot output must be validated?
- Can I choose between inline suggestions, Chat, Edits, Agent Mode, MCP, and CLI?
- Can I describe prompt context, filtering, model inference, post-processing, and human verification?
- Can I write a prompt with a clear task, constraints, examples, output format, and tests?
- Can I generate and verify code, tests, documentation, sample data, and refactors?
- Can I explain content exclusions, public-code matching, organization policies, audit events, and their limitations?
- Can I troubleshoot missing suggestions without exposing sensitive data?

### Local practice material

- [Domain 1 — Responsible Use](domain-1-responsible-use.md)
- [Domain 2 — Copilot Features](domain-2-copilot-features.md)
- [Domain 3 — Data and Architecture](domain-3-data-and-architecture.md)
- [Domain 4 — Prompt Engineering](domain-4-prompt-engineering.md)
- [Domain 5 — Developer Productivity](domain-5-developer-productivity.md)
- [Domain 6 — Privacy and Safeguards](domain-6-privacy-and-safeguards.md)
- [Hands-On Lab Workbook](GH-300-Hands-On-Lab-Workbook.md)
