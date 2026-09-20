# Repository Instructions

## GH-300 Markdown and HTML synchronization

For the GH-300 study guide, treat these files as a synchronized pair:

- Source Markdown: `certifcations/GH-300/GH-300-study-notes.md`
- Print view: `certifcations/GH-300/gh-300-print.html`

When either file is edited:

1. Keep the Markdown file as the single source of truth for study-note content.
2. Ensure the HTML loads the sibling Markdown file with `const sourceUrl = "GH-300-study-notes.md"` and renders that content; do not maintain a separate copied version of the notes in HTML.
3. Keep the HTML print controls and `@media print` rules intact unless the task explicitly changes print behavior.
4. Refresh the Markdown `Last updated:` line for guide changes. The HTML must derive its displayed timestamp from that Markdown line rather than hardcoding a second timestamp.
5. Keep `.github/workflows/deploy-gh300-pages.yml` publishing both the HTML print view as `site/index.html` and the Markdown source as `site/GH-300-study-notes.md`.
6. After editing, verify the Markdown source path, HTML source URL, matching timestamp behavior, Pages copy commands, balanced Markdown fences, and balanced HTML `script`/`style` tags.
7. Do not replace the synchronized source-driven design with manually duplicated Markdown content in the HTML.

## GH-300 objective organization

Use the current Microsoft GH-300 study guide as the authority for organizing new exam material:

<https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300>

When adding any GH-300 content:

1. Identify the matching exam domain and skill from Microsoft's current **Skills measured** section before writing the material.
2. Place the material under the matching domain and skill in `GH-300-study-notes.md`; do not append new material to an arbitrary location.
3. Preserve this exam order:
	- Use GitHub Copilot responsibly
	- Use GitHub Copilot features
	- Understand GitHub Copilot data and architecture
	- Apply prompt engineering and context crafting
	- Improve developer productivity with GitHub Copilot
	- Configure privacy, content exclusions, and safeguards
4. Use the Microsoft skill wording for the nearest subsection when practical, including skills such as responsible AI, IDE and CLI usage, Copilot features and organization policies, data flow and lifecycle, prompt crafting and performance, productivity/testing/security, and privacy/safeguards/troubleshooting.
5. If material fits multiple skills, place the main explanation under the best match and add a short cross-reference rather than duplicating the full content.
6. If the Microsoft study guide has changed, verify the current domains and skill names before reorganizing notes and record the source date or change in the study guide when appropriate.
7. After adding material, update the Markdown `Last updated:` line and ensure the HTML print view still renders the same Markdown source.
