# GH-300 Unified Deep Dive

Last updated: September 20, 2026 - 07:23 AM EDT

[Open the clean print view on GitHub Pages](https://albert6831.github.io/learn/)

For local use before GitHub Pages is enabled, open [the local print view](gh-300-print.html) through a local web server.

These notes follow the GH-300 exam order. **Product behavior can change by version, plan, editor, and policy.** Always verify with current GitHub docs and your tenant settings.

## Exam at a Glance

| Domain | Weight | Core exam question |
| --- | --- | --- |
| 1. Use GitHub Copilot responsibly | 15-20% | Can I use AI output safely and verify it? |
| 2. Use GitHub Copilot features | 25-30% | Can I pick and use the right Copilot surface? |
| 3. Understand Copilot data and architecture | 10-15% | Do I understand context, flow, and limits? |
| 4. Apply prompt engineering and context crafting | 10-15% | Can I write clear prompts with useful context? |
| 5. Improve developer productivity | 10-15% | Can I ship faster without lowering quality? |
| 6. Configure privacy, content exclusions, and safeguards | 10-15% | Can I apply policy and troubleshoot protection? |

### Core study loop (use this every time)

1. **Prepare**: define goal, constraints, inputs, outputs.
2. **Ask**: use the smallest Copilot feature that fits.
3. **Review**: inspect answer, plan, commands, and diff.
4. **Verify**: run tests, lint, and security checks.
5. **Own**: accept only what you understand.

---

## 1. Use GitHub Copilot Responsibly (15-20%)

**Key exam idea:** Copilot helps you, but **you are still responsible** for correctness, safety, and compliance.

### What can go wrong (and what to do)

- **Hallucination** (made-up facts): verify APIs, commands, and links.
- **Inaccuracy** (logic bugs): test normal and edge cases.
- **Bias** (unfair output): remove irrelevant personal attributes and review outcomes.
- **Security risk**: scan for injection, secret leaks, and weak auth.
- **Privacy/confidentiality risk**: do not paste secrets or restricted data.
- **License risk**: review public-code similarity and follow licensing policy.
- **Automation risk**: keep permissions narrow; review tool actions before approval.

| Harm | Mitigation |
| --- | --- |
| Wrong behavior in production | Code review, tests, staged rollout, rollback plan |
| Secret exposure | Do not paste secrets, rotate exposed keys, use secret managers |
| Vulnerable code | Threat model, security checks, dependency scanning |
| Unwanted file/command changes | Review plan, scope, and permissions before approval |
| Copied/public code risk | Check match warnings and follow license process |

### Responsible AI principles (common Microsoft framing)

- **Fairness**
- **Reliability and safety**
- **Privacy and security**
- **Inclusiveness**
- **Transparency**
- **Accountability**

### Human oversight checklist

Before accepting output:

1. Does it solve the real requirement?
2. Are APIs/files/commands real in this environment?
3. Are edge cases and failures handled?
4. Is security/privacy/licensing acceptable?
5. Did I run validation and understand the diff?

### Safety warnings

- Do **not** use Copilot as sole authority for legal, medical, compliance, or high-impact security decisions.
- Do **not** submit credentials, tokens, personal data, or proprietary content unless policy explicitly allows it.
- Data handling and training treatment depend on product, plan, and policy. Do not memorize absolute statements without checking current docs.

### Memory aids

- **SAFE**: Safeguards, Accountability, Fairness, Ethics
- **HINT**: Hallucinations, Incomplete context, Not automatic private-code access/training assumptions, Testing required

More safeguards appear in [Domain 6](#6-configure-privacy-content-exclusions-and-safeguards-10-15).

---

## 2. Use GitHub Copilot Features (25-30%)

**Key exam idea:** choose the right Copilot surface for the task, then review everything before accepting.

### Copilot in the IDE

#### Basic setup (example: VS Code)

1. Install/enable Copilot and Copilot Chat extensions.
2. Sign in with a licensed GitHub account.
3. Open a trusted folder.
4. Confirm Copilot status.
5. If missing, check policy, extension version, editor support, and language support.

#### Which surface to use?

| Surface | Best use |
| --- | --- |
| **Inline suggestions** | Fast code completion while typing |
| **Chat** | Explain, debug, discuss design, generate tests |
| **Edits / inline edit** | Small focused changes with visible diff |
| **Agent mode** | Multi-step tasks with plans/tools/file changes |
| **CLI** | Terminal-first help, scripts, command explanation |

**Rule:** smallest useful surface first.

### Content exclusions (app knowledge)

**Content exclusions** = policy rules that block selected files/paths from supported Copilot context.

- Configure at supported scopes (user/repo/org/enterprise, based on plan).
- Test with harmless markers.
- Keep patterns precise.
- Remember: exclusions are **not** a secret-removal tool.

**Version warning:** support differs by feature and client. Current docs identify **Edit** and **Agent** modes in Visual Studio Code and other editors as unsupported for content exclusions, and IDEs may still expose indirect semantic data (for example type info). Verify the current support matrix before relying on exclusions.

### Copilot CLI

**Copilot CLI** is terminal-based Copilot help.

- Use for command explanation, script drafts, repo questions, and file operations.
- It is distinct from normal repository/admin `gh` commands, even when surfaced through GitHub CLI integrations.
- Install/auth/command syntax is version-dependent.
- Depending on release, you may use a standalone `copilot` command or a GitHub CLI Copilot integration.
- Check current official docs, then use the installed help command (such as `/help` or equivalent) to confirm available commands.

**Safety:** review every command and file change before running.

### Agent Mode, MCP, sessions, and sub-agents

- **Agent Mode**: Copilot plans and runs connected steps with your approval.
- **MCP (Model Context Protocol)**: standard way to connect tools/resources/prompts to Copilot.
- **Agent session**: multi-step task context over one session.
- **Sub-agent**: delegated smaller task where supported.

**Exam focus:** understand permissions, scope, and review duties.

### Other feature knowledge

- **PR summaries/review help**: useful, but not approval.
- **Spaces**: curated context for conversations, not auto test/runtime.
- **Spark**: natural-language app building where available; still review outputs.
- **Copilot + Actions**: helps author/troubleshoot workflows, but you must check permissions, untrusted input, secret handling, action pinning, and deployment safety.

### Organization policy and governance

Admins may control:

- feature availability,
- public-code matching/duplication controls,
- content exclusions,
- audit logging,
- subscription/seat behavior (including REST API automation where supported).

Use least privilege and test policy changes safely.

### Domain 2 memory sheet

**IDE + CLI + Chat + Edits + Agents + MCP + PR + Actions + Governance**

---

## 3. Understand GitHub Copilot Data and Architecture (10-15%)

**Key exam idea:** know the request flow and know that policy, permissions, and limits shape what context is used.

### Core data-flow model

| Stage | Meaning |
| --- | --- |
| **Input** | prompt text, selected code, files, history, metadata |
| **Processing** | context selection, prompt build, policy/filter checks, model inference |
| **Output** | completion, chat answer, diff, command, review comment |
| **Controls** | permissions, exclusions, filtering, retention, audit, feedback settings |

### Suggestion lifecycle (conceptual)

1. User asks or places cursor.
2. Copilot gathers relevant available context.
3. Request is built with product instructions.
4. Auth/policy/safety filtering is applied.
5. Model generates output.
6. Service post-processes output.
7. User reviews, accepts/rejects, and verifies.

### Important limits

- **LLM (Large Language Model)**: predicts likely patterns, not guaranteed truth.
- Context is limited; not all repo content is always included.
- Output can be stale, non-deterministic, insecure, or incomplete.
- Copilot does not replace domain experts, testing, security review, or legal review.

### Policy warning

Retention, training use, and data sharing depend on product/plan/terms/settings. Verify current documentation; do not rely on old blanket statements.

---

## 4. Apply Prompt Engineering and Context Crafting (10-15%)

**Key exam idea:** clear prompt + relevant context + clear constraints = better output.

### Prompt structure (high-yield)

1. **Task**: one clear outcome.
2. **Context**: relevant files/errors/rules.
3. **Constraints**: language, versions, boundaries.
4. **Inputs/outputs**: expected behavior and format.
5. **Examples**: when needed.
6. **Verification**: tests or acceptance checks.

### Zero-shot vs few-shot

| Type | What it means | Trade-off |
| --- | --- | --- |
| **Zero-shot** | instructions only | fast, but more ambiguity |
| **Few-shot** | include examples | more consistent, may copy bad patterns |

### Prompt best practices

- Ask for one result at a time.
- Name exact files/versions/constraints.
- Include only needed context.
- Request tests and edge cases.
- Ask Copilot to list assumptions.
- Refine in short iterations.
- Never include secrets.

### Chat-history caution

History helps, but old context can become wrong or disappear due to limits. Restate critical constraints when accuracy matters.

---

## 5. Improve Developer Productivity with GitHub Copilot (10-15%)

**Key exam idea:** Copilot reduces repetitive work, but quality still depends on your review and verification.

### Where Copilot helps in SDLC

| SDLC phase | Useful help |
| --- | --- |
| Requirements | summaries, acceptance criteria, clarifying questions |
| Design | options, trade-offs, modernization ideas |
| Implementation | generation, refactor, translation, debugging help |
| Testing | unit/integration tests, edge-case ideas |
| Deployment | workflow/manifests/runbook drafts |
| Maintenance | docs, deprecated API updates, debt cleanup ideas |

### High-yield productivity uses

- Generate/refactor code with behavior constraints.
- Draft documentation from real code.
- Explain unfamiliar code quickly.
- Create synthetic sample data (never production personal data).
- Modernize legacy code in small steps with tests.

### Testing and edge-case focus

Ask for and verify:

- null/empty/min/max values,
- invalid input and error paths,
- auth/permission failures,
- partial failures and retries,
- concurrency and malformed input.

Generated tests can be wrong or shallow. Run them and review assertions.

### Security and performance guidance

- Security: check injection, auth flaws, secret leaks, unsafe dependencies, missing validation.
- Performance: measure first; then optimize complexity, I/O, memory, batching, and caching.
- Never trade correctness/security for unmeasured speed.

---

## 6. Configure Privacy, Content Exclusions, and Safeguards (10-15%)

**Key exam idea:** controls reduce risk, but they do not replace access control, secure coding, or human review.

### Content exclusions and settings

- Configure exclusions at correct scope (user/repo/org/enterprise as supported).
- Validate pattern syntax, inheritance, casing, and feature support.
- Test safely with non-sensitive files.
- Keep secrets out of source control even with exclusions enabled.

### Public-code matching / duplication controls

These controls decide how matching suggestions are handled (block, warn, or review path based on policy). Exact behavior depends on plan and settings.

### Ownership and legal caution

Generated output may be non-unique or resemble public code. Review current GitHub terms, org policy, and legal guidance before use.

### Troubleshooting order

1. Confirm correct signed-in account and Copilot entitlement.
2. Check org/enterprise policy and repository access.
3. Verify supported client/editor/extension/CLI versions.
4. Check file type, folder trust, and local settings.
5. Check exclusion patterns and scope inheritance.
6. Test outside excluded paths.
7. Review logs/status without exposing sensitive data.
8. Reproduce with minimal prompt and record expected vs actual behavior.

Common causes: wrong account, missing seat, policy block, unsupported feature, stale extension, network issue, exclusion mismatch, or misunderstanding of feature support.

---

## High-Yield Review (Fast Recall)

### Ultra-high-yield facts

- **LLMs predict patterns; they do not guarantee correctness.**
- **Human review + testing are mandatory.**
- Copilot uses relevant available context, not always the whole repo.
- Plan/policy/client/version control what is available.
- CLI/Agent actions can change files or run commands; approve carefully.
- Security/privacy/licensing checks are always required.

### Quick memory sheet

- **Behavior:** Predict, not prove.
- **Flow:** Context -> request -> filter -> model -> output -> human verify.
- **Limits:** hallucination, stale info, limited context, bias toward common patterns.
- **Governance:** policy, exclusions, public-code controls, audit, accountability.

### Final review checklist

- Can I explain why Copilot output must be validated?
- Can I pick the right surface (inline, chat, edits, agent, MCP, CLI)?
- Can I describe context flow and safeguards?
- Can I write prompts with clear constraints and checks?
- Can I use Copilot for code/tests/docs while keeping quality high?
- Can I explain exclusions, public-code controls, policy scopes, and limitations?
- Can I troubleshoot missing suggestions safely?

### Local practice material

- [Domain 1 — Responsible Use](domain-1-responsible-use.md)
- [Domain 2 — Copilot Features](domain-2-copilot-features.md)
- [Domain 3 — Data and Architecture](domain-3-data-and-architecture.md)
- [Domain 4 — Prompt Engineering](domain-4-prompt-engineering.md)
- [Domain 5 — Developer Productivity](domain-5-developer-productivity.md)
- [Domain 6 — Privacy and Safeguards](domain-6-privacy-and-safeguards.md)
- [Hands-On Lab Workbook](GH-300-Hands-On-Lab-Workbook.md)
