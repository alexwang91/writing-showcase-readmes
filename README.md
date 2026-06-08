<div align="center">

<pre>
+------------------------------------------------------------+
| SHOWCASE README WRITER                                     |
| badges | proof | star history | quickstarts | story        |
+------------------------------------------------------------+
</pre>

# Showcase README Writer

_A Codex skill for turning sparse repos and agent skills into honest, high-conversion GitHub front pages._

<p align="center">
  <a href="skills/writing-showcase-readmes/SKILL.md"><img src="https://img.shields.io/badge/Codex-skill-111827?logo=openai&logoColor=white" alt="Codex skill"></a>
  <a href="https://github.com/alexwang91/writing-showcase-readmes/actions/workflows/validate.yml"><img src="https://github.com/alexwang91/writing-showcase-readmes/actions/workflows/validate.yml/badge.svg" alt="Validate skill"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/alexwang91/writing-showcase-readmes?logo=opensourceinitiative&logoColor=white" alt="License"></a>
  <a href="https://github.com/alexwang91/writing-showcase-readmes/stargazers"><img src="https://img.shields.io/github/stars/alexwang91/writing-showcase-readmes?style=social" alt="GitHub stars"></a>
  <a href="llms.txt"><img src="https://img.shields.io/badge/llms.txt-ready-blue?logo=readme&logoColor=white" alt="llms.txt ready"></a>
</p>

<p align="center">
  <a href="#get-started">Install</a> |
  <a href="#what-it-does">What it does</a> |
  <a href="#proof">Proof</a> |
  <a href="#star-history">Star History</a> |
  <a href="#documentation">Docs</a>
</p>

<p align="center"><sub>
  <b>AI agents / LLMs:</b> read <a href="llms.txt"><code>/llms.txt</code></a> for a compact index of this skill.
</sub></p>

</div>

Showcase README Writer packages the README patterns behind repos like `mattpocock/skills`, `chopratejas/headroom`, and `aaif-goose/goose` into one reusable Codex skill: rich badges, small visual signals, star charts, proof tables, compatibility matrices, install paths, collapsible depth, and a story that does not make up evidence.

## What It Does

- **Audits the project first** - reads `README*`, manifests, workflows, docs, license files, skill metadata, screenshots, and package clues before writing.
- **Builds the above-the-fold trust block** - title, tagline, badges, navigation, LLM hint, pitch, and first action.
- **Adds proof without bluffing** - benchmark tables, validation output, compatibility matrices, Star History, and comparison tables only when evidence exists.
- **Handles skills and normal repos** - works for Codex skills, skill collections, CLIs, libraries, apps, and open source launch pages.
- **Uses collapsible depth** - keeps advanced integrations, internals, and long feature lists available without crowding the first read.
- **Checks the final README** - verifies badge slugs, Star History links, local image paths, commands, claims, and anchors.

## How It Works

```text
Repo, skill folder, or GitHub URL
        |
        v
Inspect files, docs, workflows, metadata, and assets
        |
        v
Choose README mode: skill, library, CLI, app, or foundation project
        |
        v
Apply the README element library
        |
        v
Draft README.md, then verify claims, links, badges, and commands
```

The skill has two layers:

- `SKILL.md` gives the agent the workflow: inspect, find the promise, choose the README mode, draft, and verify.
- `references/readme-elements.md` gives the reusable element library: badge recipes, Star History snippet, proof tables, compatibility matrices, docs tables, comparison tables, and a full showcase skeleton.

## Get Started

Clone the repo:

```bash
git clone https://github.com/alexwang91/writing-showcase-readmes.git
cd writing-showcase-readmes
```

Install into Codex on macOS or Linux:

```bash
mkdir -p ~/.codex/skills
cp -R skills/writing-showcase-readmes ~/.codex/skills/
```

Install into Codex on Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\writing-showcase-readmes" "$env:USERPROFILE\.codex\skills\writing-showcase-readmes"
```

Start a fresh Codex thread, then invoke it:

```text
Use $writing-showcase-readmes to rewrite this repository README into a polished showcase.
```

## Proof

This repo includes a real validation script and GitHub Actions workflow, so the CI badge checks the skill instead of decorating the page.

| Check | What It Verifies | Command |
|-------|------------------|---------|
| Skill structure | `SKILL.md`, `agents/openai.yaml`, and references exist | `python scripts/validate_skill.py` |
| Frontmatter | Skill name and trigger description are present | `python scripts/validate_skill.py` |
| Element library | Badge recipes, Star History, proof, comparison, and skeleton sections exist | `python scripts/validate_skill.py` |
| Markdown fences | Code fences in Markdown files are balanced | `python scripts/validate_skill.py` |

## Star History

<a href="https://www.star-history.com/?repos=alexwang91%2Fwriting-showcase-readmes&type=date&legend=top-left">
  <picture>
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=alexwang91/writing-showcase-readmes&type=date&legend=top-left" />
  </picture>
</a>

## Compatibility

| Surface | Status | Notes |
|---------|:------:|-------|
| Codex local skills | Ready | Install under `~/.codex/skills/writing-showcase-readmes` |
| Skill repositories | Ready | Reads `SKILL.md`, `agents/openai.yaml`, references, scripts, and examples |
| GitHub repositories | Ready | Uses repo slug for badges and Star History |
| CLIs and libraries | Ready | Looks for install commands, package metadata, docs, and workflows |
| Other agent skill systems | Portable | Adapt the install path and invocation syntax |

## When To Use / When To Skip

**Great fit if you...**

- want a README that feels like a real open source front page, not a note taped to a folder
- have a repo or skill with useful substance but weak presentation
- need badges, small icons, Star History, proof tables, quickstart steps, and community links in one pass
- want the agent to avoid fake claims while still making the README feel full

**Skip it if you...**

- only need a two-line internal README
- do not want HTML badges, centered hero blocks, or visual GitHub README elements
- cannot provide enough evidence for proof sections and do not want placeholders

<details>
<summary><b>What's inside</b></summary>

| Path | Purpose |
|------|---------|
| [`skills/writing-showcase-readmes/SKILL.md`](skills/writing-showcase-readmes/SKILL.md) | The workflow future Codex sessions load |
| [`skills/writing-showcase-readmes/references/readme-elements.md`](skills/writing-showcase-readmes/references/readme-elements.md) | The reusable README component library |
| [`skills/writing-showcase-readmes/agents/openai.yaml`](skills/writing-showcase-readmes/agents/openai.yaml) | Codex UI metadata |
| [`scripts/validate_skill.py`](scripts/validate_skill.py) | Local and CI validation |
| [`llms.txt`](llms.txt) | Compact agent-readable repo index |

</details>

<details>
<summary><b>README elements this skill knows how to compose</b></summary>

| Element | Use |
|---------|-----|
| Status notice | Migration, beta, support, governance, or archival context |
| Hero block | Centered title, logo, ASCII art, tagline, and metric strip |
| Badge row | CI, license, package, docs, stars, Discord, model, Docker, coverage |
| Navigation row | Install, Proof, Docs, Examples, Community, Enterprise |
| LLM hint | `llms.txt` and docs blob links for agent-facing projects |
| Demo media | Screenshots, GIFs, captions, and placeholders when assets are missing |
| Proof table | Benchmarks, validation output, adoption signals, compatibility |
| Star History | GitHub star growth chart with the exact repo slug |
| Collapsible sections | Integrations, internals, advanced install paths, long capability lists |
| Comparison table | Honest positioning against real alternatives |

</details>

## Documentation

| Start here | Go deeper |
|------------|-----------|
| [Skill workflow](skills/writing-showcase-readmes/SKILL.md) | [Element library](skills/writing-showcase-readmes/references/readme-elements.md) |
| [Install commands](#get-started) | [Compatibility matrix](#compatibility) |
| [Validation](scripts/validate_skill.py) | [Agent index](llms.txt) |

## Compared To

| | Scope | Evidence-Aware | Visual Elements | Reusable By Agents |
|-|-------|:--------------:|:---------------:|:------------------:|
| **Showcase README Writer** | Whole README strategy and draft | Yes | Yes | Yes |
| Generic README template | Section checklist | No | Sometimes | No |
| Badge generator | Badge snippets only | No | Yes | No |
| Marketing copy prompt | Persuasive prose | Rarely | No | Sometimes |

## Contributing

Run the validator before opening a pull request:

```bash
python scripts/validate_skill.py
```

Useful contribution ideas:

- Add more README patterns from strong open source repos.
- Tighten badge recipes for package ecosystems.
- Add validation for broken local links.
- Improve install instructions for more agent runtimes.

## Community

- [Open an issue](https://github.com/alexwang91/writing-showcase-readmes/issues) for missing README patterns or broken install notes.
- [Star the repo](https://github.com/alexwang91/writing-showcase-readmes) if this helps your next launch page get read.

## License

MIT - see [LICENSE](LICENSE).
