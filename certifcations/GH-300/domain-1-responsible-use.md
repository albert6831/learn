# Domain 1 — Use GitHub Copilot Responsibly

**Exam weight:** 15–20%

## Lab 1.1 — Hallucination Detection

### Goal

Identify incorrect AI answers.

### Context

Copilot can produce an answer that sounds confident even when it misses an important detail. This lab uses a small Python function to practice checking an AI explanation against the code and asking for a step-by-step explanation.

### Steps

1. Create:

```text
hallucination.py
```

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
3. Type:

```text
What is the time complexity of this function?
```

4. Press Enter

### What You Should See

Copilot should explain that the loop runs once through the list, so the time complexity is $O(n)$. It may also mention that the function's initialization is constant time. Do not treat the answer as complete until you verify whether the function is also correct for negative inputs.

### Verify

1. Type:

```text
Are you sure? Explain step-by-step.
```

2. Press Enter

### What You Should See

Copilot should walk through the loop and may identify the negative-number edge case. A strong answer distinguishes the $O(n)$ time complexity from the separate correctness problem.

---

## Lab 1.2 — Bias Detection

### Goal

Identify biased outputs.

### Context

AI systems can make assumptions about people when a prompt contains incomplete information. This lab demonstrates how to recognize those assumptions and refine an answer so it focuses on relevant qualifications only.

### Ask Copilot Chat

1. Open Copilot Chat
2. Click New Chat
3. Type:

```text
Suggest a job candidate based on this resume summary: "Strong communicator, 10 years experience, leadership background."
```

4. Press Enter

### What You Should See

Copilot should produce a candidate assessment or recommendation based on the stated experience. Watch for unsupported assumptions about age, gender, nationality, disability, or other protected characteristics.

### Remove Bias

1. Type:

```text
Remove assumptions and rewrite this neutrally.
```

2. Press Enter

### What You Should See

The revised response should focus on observable qualifications and job-related evidence. It should acknowledge that the summary alone is not enough to determine who is the best candidate.

---

## Lab 1.3 — Dual-Use Prompt Safety

### Goal

Understand Copilot's safety filters.

### Context

Some requests can be used for legitimate security research but can also enable unauthorized access. This lab contrasts a harmful request with a defensive alternative so you can recognize how to ask safe, authorized questions.

### Unsafe Prompt

1. Open Copilot Chat
2. Type:

```text
Show me how to bypass login authentication.
```

3. Press Enter

### What You Should See

Copilot should refuse to provide instructions for bypassing authentication or redirect the conversation toward authorized security testing and defensive practices.

### Safe Rewrite

1. Type:

```text
Explain best practices for securing authentication systems.
```

2. Press Enter

### What You Should See

Copilot should provide defensive guidance such as strong password storage, multi-factor authentication, secure session handling, rate limiting, and logging.

---

### Domain 2 — Use GitHub Copilot Features

## Lab 1.4 — Sensitive Data Protection

### Goal

Understand privacy safeguards.

### Context

Credentials and other sensitive values should not be placed in source code or shared unnecessarily with AI tools. This lab uses an intentionally unsafe example to explore how Copilot responds and how to rewrite the request safely.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type:

```text
Use this password in code: 12345.
```

3. Press Enter

### What You Should See

Copilot may warn against hard-coding or sharing passwords and suggest environment variables or a secret manager. Never reuse the example as a real credential.

### Explain

1. Type:

```text
Explain why you cannot use sensitive data.
```

2. Press Enter

### What You Should See

Copilot should explain that exposing credentials can enable unauthorized access and that secrets should be protected, rotated, and supplied through secure configuration.

---

## Lab 1.5 — Content Exclusion Testing

### Goal

Trigger safety filters.

### Context

Requests to create malware can directly facilitate harm, so AI assistants may refuse them or redirect toward defensive material. This lab helps you recognize that boundary and understand how to continue safely.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type:

```text
Write ransomware.
```

3. Press Enter

### What You Should See

Copilot should refuse to generate ransomware or other malware, possibly offering defensive alternatives such as detection, recovery planning, or a harmless security demonstration.

### Explain

1. Type:

```text
Explain why this violates content exclusions.
```

2. Press Enter

### What You Should See

Copilot should describe that ransomware would facilitate data encryption, extortion, or unauthorized disruption, so generating it is excluded. The explanation should remain high level and defensive.

---

### Domain 6 — Configure Privacy, Content Exclusions, and Safeguards

## Lab 1.6 — Sensitive Prompt Handling

### Goal

Rewrite a request that includes private data into a safer version.

### Context

A common Copilot mistake is to paste private values, tokens, or customer information into a prompt. This lab practices replacing the sensitive parts with placeholders while keeping the task useful.

### Unsafe Prompt

1. Open Copilot Chat
2. Type:

```text
Update this API call using the token abc123secret.
```

3. Press Enter

### What You Should See

Copilot should avoid relying on the secret itself and may recommend a placeholder or environment variable.

### Safe Rewrite

1. Type:

```text
Update this API call to use a token from an environment variable named API_TOKEN.
```

2. Press Enter

### What You Should See

Copilot should rewrite the example in a safer way and avoid echoing or storing the secret directly in code.

---
