# Domain 3 — Understand Copilot Data and Architecture

**Exam weight:** 10–15%

## Lab Index

- [Lab 3.1 — Suggestion Lifecycle Diagram](#lab-31--suggestion-lifecycle-diagram)
- [Lab 3.2 — Token Limit Awareness](#lab-32--token-limit-awareness)

## Lab 3.1 — Suggestion Lifecycle Diagram

### Goal

Understand Copilot's architecture.

### What This Is

Understanding the path from a prompt to a suggestion makes it easier to reason about context, filtering, and model output. This lab asks Copilot to represent that process visually, helping you identify the main stages of a response.

### Ask Copilot Chat

1. Open Copilot Chat
2. Type:

```text
Draw a diagram of how GitHub Copilot processes a prompt from input to output.
```

3. Press Enter

### What You Should See

Copilot should return a diagram or diagram markup showing a flow from the user's prompt through context gathering and model processing to a suggestion or response. Treat the diagram as a high-level explanation, not an implementation detail.

### What You Should Have Learned

- Describe Copilot's suggestion lifecycle as a high-level flow from prompt and context to output.
- Avoid treating a generated conceptual diagram as an exact product implementation.

---

## Lab 3.2 — Token Limit Awareness

### Goal

Understand context windows.

### What This Is

AI tools have limits on how much text they can process in one request. This lab demonstrates why long inputs may need to be summarized in smaller chunks and gives you a way to compare a broad summary with chunked summaries.

### Steps

1. Create:

```text
longprompt.txt
```

2. Paste several pages of text

### Ask Copilot Chat

1. Open Copilot Chat
2. Type:

```text
Summarize this text.
```

3. Press Enter

### What You Should See

Copilot should return a shorter summary that captures the main ideas of the text. If the input is too large, it may warn about context limits, omit details, or ask you to provide less text.

### Chunk Summary

1. Type:

```text
Summarize in 500-token chunks.
```

2. Press Enter

### What You Should See

Copilot should organize the response into successive summaries for roughly 500-token sections. Chunk boundaries and token counts may be approximate, so compare the chunks with the source for missing details.

### What You Should Have Learned

- Context-window limits can affect what an AI system can process and retain.
- Split long material into manageable chunks and check summaries against the source.
