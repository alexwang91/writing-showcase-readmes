---
name: writing-showcase-readmes
description: Use when creating, rewriting, or polishing GitHub README files for repositories, portable agent skills, Codex skills, Claude/Hermes/OpenClaw-style instruction packs, CLIs, libraries, apps, or open source launches; especially when the user asks for badges, small icons, screenshots, demos, star history charts, proof tables, install steps, runtime compatibility tables, comparison tables, community links, or an attractive README.
---

# Writing Showcase READMEs

## Overview

Create a README that works like a strong open source front page: fast trust above the fold, concrete proof in the middle, and clear paths to install, import into agents, learn, contribute, and join.

Use every attractive element the project can honestly support. Never invent metrics, screenshots, package names, CI status, adoption numbers, benchmarks, or compatibility claims.

## Workflow

1. Inspect the input:
   - For a local repository, read `README*`, manifests, docs, `.github/workflows`, `LICENSE`, `CONTRIBUTING*`, releases, package metadata, CLI help, screenshots, GIFs, and docs links.
   - For a skill folder, read `SKILL.md`, optional agent metadata such as `agents/openai.yaml`, references, scripts, examples, and any runtime-specific rules or memory files.
   - For a GitHub URL, fetch the current README and use the repo slug for badges and star history.
2. Identify the promise:
   - Audience: who should care.
   - Outcome: what changes after installation or use.
   - Proof: benchmark, demo, adoption signal, compatibility matrix, test status, package distribution, or real examples.
   - First action: download, install, import into an agent, copy command, run skill, read docs, or join community.
3. Choose the README mode:
   - **Skill collection or agent workflow**: hero image, one sharp claim, quickstart, "why this exists", problem/fix sections, reference catalog.
   - **Library, CLI, product, or developer tool**: centered hero, badges, nav row, demo media, what it does, how it works diagram, quickstart, proof tables, compatibility/integrations, install, docs, comparison, community.
   - **Established app or foundation project**: status banner if needed, centered name/tagline, trust badges, concise positioning, get started, quick links, help, community.
4. Load `references/readme-elements.md` before drafting the README. Use it as a checklist and snippet source.
5. Draft the README in this order:
   - Above-the-fold trust block: optional notice, logo/ASCII art/title, tagline, badge row, nav links, one-sentence pitch, primary CTA.
   - Value and proof: demo image/GIF, "What it does", "How it works", quickstart, proof tables, star history, compatibility.
   - Depth without clutter: `details` blocks for integrations, internals, package variants, or long feature lists.
   - Practical finish: docs, install variants, comparison table, contributing, community, license.
6. Keep the style full but not bloated:
   - Use short paragraphs, scannable tables, and bullets with concrete verbs.
   - Put advanced detail behind collapsible sections.
   - Prefer project-specific language over generic hype.
   - Include a small human or brand moment only when it fits the project.
7. Verify before finalizing:
   - Links and anchors resolve.
   - Badge URLs use the correct owner, repo, package, workflow, and branch.
   - Star History uses the exact GitHub slug.
   - Local image paths exist and have useful alt text.
   - Commands match the actual package manager, runtime, and repository structure.
   - Claims are backed by files, docs, tests, benchmarks, or explicit user input.

## Output Rules

If the user asks to update a repository, edit `README.md` directly. If they ask for a draft, provide complete Markdown. If important assets or proof are missing, include a short "Needed to finish" note instead of fabricating the missing evidence.
