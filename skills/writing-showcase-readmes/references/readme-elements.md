# README Element Library

Use this checklist to build rich GitHub READMEs inspired by high-performing open source front pages. Adapt the structure; do not copy another project's wording or art.

## Source Pattern Map

- `mattpocock/skills`: branded hero image, concise thesis, newsletter CTA, 30-second quickstart, "why this exists", problem/fix storytelling, quotes, tips, collapsible examples, categorized reference index.
- `chopratejas/headroom`: centered ASCII hero, bold metric line, badge row, nav row, LLM/docs link, trend badge, demo GIF, proof tables, architecture diagram, Star History, compatibility matrix, when-to-use/skip, collapsible integrations/internals, docs table, comparison table.
- `aaif-goose/goose`: migration/status notice, centered title and tagline, trust/community badges, concise product positioning, desktop/CLI/API install paths, quick links, help links, community links, small brand personality moment.

## Above-The-Fold Components

Use most of these when the project can support them:

1. **Status notice**: migration, beta, archived, renamed, security notice, or governance status.
2. **Hero**: logo via `<picture>`, centered title block, or ASCII art for terminal-native tools.
3. **Tagline**: one italic or bold sentence that names the category and outcome.
4. **Metric strip**: compact proof such as "60-95% fewer tokens", "desktop + CLI + API", "local-first", "reversible".
5. **Badge row**: CI, coverage, package versions, docs, license, Discord, health, packaging, model, Docker, release.
6. **Navigation row**: Docs, Install, Proof, Agents, Examples, Discord, llms.txt, Enterprise.
7. **LLM hint**: link to `llms.txt` or docs blob when the project targets agents.
8. **One-sentence pitch**: concrete nouns, concrete audience, no abstract marketing fog.
9. **Primary CTA**: install command, download link, docs link, or run command.

## Badge Recipes

Replace placeholders exactly. Use `logo=` for small icon badges when useful.

```md
<p align="center">
  <a href="https://github.com/OWNER/REPO/actions/workflows/ci.yml"><img src="https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://codecov.io/gh/OWNER/REPO"><img src="https://codecov.io/gh/OWNER/REPO/graph/badge.svg" alt="Coverage"></a>
  <a href="https://pypi.org/project/PACKAGE/"><img src="https://img.shields.io/pypi/v/PACKAGE.svg?logo=pypi&logoColor=white" alt="PyPI"></a>
  <a href="https://www.npmjs.com/package/PACKAGE"><img src="https://img.shields.io/npm/v/PACKAGE.svg?logo=npm" alt="npm"></a>
  <a href="https://hub.docker.com/r/OWNER/IMAGE"><img src="https://img.shields.io/docker/v/OWNER/IMAGE?logo=docker&label=docker" alt="Docker"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-LICENSE-blue.svg" alt="License"></a>
  <a href="DOCS_URL"><img src="https://img.shields.io/badge/docs-online-blue.svg" alt="Docs"></a>
  <a href="DISCORD_URL"><img src="https://img.shields.io/discord/SERVER_ID?logo=discord&logoColor=white&label=Discord" alt="Discord"></a>
</p>
```

Skill repositories can add a skills badge when published:

```md
[![skills.sh](https://skills.sh/b/OWNER/REPO)](https://skills.sh/OWNER/REPO)
```

## Trend And Star History

Use Star History for public GitHub repositories. Encode slashes in the link query as `%2F`; keep the image `repos` value as `OWNER/REPO`.

```md
<a href="https://www.star-history.com/?repos=OWNER%2FREPO&type=date&legend=top-left">
  <picture>
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=OWNER/REPO&type=date&legend=top-left" />
  </picture>
</a>
```

Use a Trendshift badge only when the repository has a valid Trendshift repository id:

```md
<p align="center">
  <a href="https://trendshift.io/repositories/ID"><img src="https://trendshift.io/api/badge/repositories/ID" alt="OWNER/REPO | Trendshift" width="250" height="55"></a>
</p>
```

## Core Sections

### What It Does

Use 5-8 bullets. Start with bold capability labels and describe concrete actions:

```md
- **Library** - call `api()` inside an app.
- **CLI** - run `tool command` from any shell.
- **Proxy** - drop in without changing application code.
- **MCP server** - expose `tool_action` to agent clients.
- **Local-first storage** - keep user data on the machine.
```

### How It Works

Use an ASCII diagram when architecture matters:

```md
 Your app / agent
      |
      v
  Tool layer
    |-- Router
    |-- Processor
    `-- Store
      |
      v
 Provider / runtime
```

Follow with 3-5 bullets explaining the named parts.

### Quickstart

Give the fastest path to value in 30-60 seconds:

````md
```bash
# 1. Install
PACKAGE_MANAGER install PACKAGE

# 2. Run
COMMAND

# 3. Verify
COMMAND --check
```
````

### Proof

Prefer tables over claims. Include a reproduce command when possible.

```md
| Workload | Before | After | Result |
|----------|-------:|------:|-------:|
| Example task | 100 | 25 | **75% better** |

Reproduce: `COMMAND`
```

### Compatibility Matrix

```md
| Platform / Agent | Supported | Notes |
|------------------|:---------:|-------|
| macOS | Yes | Tested on latest stable |
| Windows | Yes | Requires PowerShell 7 |
| Codex | Yes | Uses shared config |
```

### When To Use / When To Skip

Make fit explicit:

```md
**Great fit if you...**
- need X without Y
- use A, B, or C daily

**Skip it if you...**
- only need the provider-native feature
- cannot run local services
```

### Collapsible Depth

Use details blocks for long lists:

```md
<details>
<summary><b>Integrations</b></summary>

| Your setup | Hook in with |
|------------|--------------|
| Framework | `adapter()` |

</details>
```

### Documentation Table

```md
| Start here | Go deeper |
|------------|-----------|
| [Quickstart](DOCS_URL) | [Architecture](DOCS_URL) |
| [Install](DOCS_URL) | [Configuration](DOCS_URL) |
```

### Compared To

Only compare against real alternatives and cite links:

```md
| | Scope | Deployment | Local | Open source |
|-|-------|------------|:-----:|:-----------:|
| **This project** | Full workflow | CLI + API | Yes | Yes |
| Alternative | Narrow task | Hosted | No | No |
```

## Full Showcase Skeleton

```md
> **Status:** Optional migration, beta, or support note.

<div align="center">

# PROJECT

_TAGLINE_

<p align="center">
  BADGES
</p>

<p align="center">
  <a href="DOCS_URL">Docs</a> |
  <a href="#get-started">Install</a> |
  <a href="#proof">Proof</a> |
  <a href="#community">Community</a>
</p>

</div>

ONE_SENTENCE_PITCH.

<p align="center">
  <img src="DEMO.gif" alt="PROJECT in action" width="820">
  <br><sub>Short caption with concrete result.</sub>
</p>

## What It Does

FEATURE_BULLETS

## How It Works

ARCHITECTURE_DIAGRAM

## Get Started

INSTALL_AND_FIRST_RUN

## Proof

PROOF_TABLES

STAR_HISTORY

## Compatibility

COMPATIBILITY_MATRIX

## When To Use / When To Skip

FIT_GUIDANCE

<details>
<summary><b>Integrations</b></summary>

INTEGRATION_TABLE

</details>

## Documentation

DOCS_TABLE

## Compared To

COMPARISON_TABLE

## Contributing

CONTRIBUTING_COMMANDS

## Community

COMMUNITY_LINKS

## License

LICENSE_LINE
```

## Integrity Rules

- Do not fake benchmarks, screenshots, stars, package publication, CI, compatibility, or governance.
- Do not use another repository's logo, screenshots, or copy without permission.
- Do not include every visual ornament if it makes a small project look fraudulent.
- If evidence is missing but the user wants a maximal scaffold, leave clear placeholders such as `TODO: add demo GIF after recording`.
- Keep "personality" small: a one-line joke, motto, or signoff can help; a long gimmick distracts.
