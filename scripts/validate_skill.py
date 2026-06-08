from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / "skills" / "writing-showcase-readmes"
SKILL_FILE = SKILL_DIR / "SKILL.md"
REFERENCE_FILE = SKILL_DIR / "references" / "readme-elements.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"
README_FILE = REPO_ROOT / "README.md"
LLMS_FILE = REPO_ROOT / "llms.txt"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def read(path: Path) -> str:
    require(path.is_file(), f"Missing required file: {path.relative_to(REPO_ROOT)}")
    return path.read_text(encoding="utf-8")


def frontmatter(markdown: str) -> str:
    match = re.match(r"^---\n(.*?)\n---\n", markdown, re.DOTALL)
    require(match is not None, "SKILL.md must start with YAML frontmatter")
    return match.group(1)


def assert_balanced_fences(path: Path, text: str) -> None:
    inside = False
    fence_len = 0
    start_line = 0

    for line_number, line in enumerate(text.splitlines(), start=1):
        opener = re.match(r"^(`{3,}|~{3,})", line)
        if not inside and opener:
            inside = True
            fence_len = len(opener.group(1))
            start_line = line_number
            continue

        if inside:
            closer = re.match(r"^(`{3,}|~{3,})\s*$", line)
            if closer and len(closer.group(1)) >= fence_len:
                inside = False
                fence_len = 0
                start_line = 0

    require(not inside, f"Unclosed Markdown fence in {path.relative_to(REPO_ROOT)} starting on line {start_line}")


def main() -> None:
    skill = read(SKILL_FILE)
    reference = read(REFERENCE_FILE)
    openai_yaml = read(OPENAI_YAML)
    readme = read(README_FILE)
    llms = read(LLMS_FILE)

    fm = frontmatter(skill)
    require("name: writing-showcase-readmes" in fm, "Skill frontmatter must name writing-showcase-readmes")
    require("description:" in fm and "README" in fm and "star history" in fm.lower(), "Skill description must cover README and Star History triggers")
    require("references/readme-elements.md" in skill, "SKILL.md must tell agents to load the element library")
    require("$writing-showcase-readmes" in openai_yaml, "openai.yaml default prompt must invoke the skill")

    required_reference_sections = [
        "Badge Recipes",
        "Trend And Star History",
        "Proof",
        "Compatibility Matrix",
        "Full Showcase Skeleton",
        "Integrity Rules",
    ]
    for section in required_reference_sections:
        require(section in reference, f"Element library missing section: {section}")

    required_readme_sections = [
        "What It Does",
        "Get Started",
        "Proof",
        "Star History",
        "Compatibility",
        "Compared To",
    ]
    for section in required_readme_sections:
        require(section in readme, f"README missing section: {section}")

    require("alexwang91/writing-showcase-readmes" in readme, "README must use the published GitHub repository slug")
    require("Integrity rule" in llms, "llms.txt must include the integrity rule")

    runtime_names = [
        "Codex",
        "Claude Code",
        "Hermes",
        "OpenClaw",
        "Goose",
        "Cursor",
        "Aider",
        "Gemini CLI",
    ]
    for runtime in runtime_names:
        require(runtime in readme, f"README must mention runtime: {runtime}")
    require("portable" in llms.lower(), "llms.txt must explain portable agent usage")
    require("runtime compatibility" in skill.lower(), "SKILL.md must mention runtime compatibility README work")

    for path, text in [
        (SKILL_FILE, skill),
        (REFERENCE_FILE, reference),
        (README_FILE, readme),
        (LLMS_FILE, llms),
    ]:
        assert_balanced_fences(path, text)

    require("[TODO" not in skill, "SKILL.md contains unresolved placeholder syntax")
    print("Skill validation passed")


if __name__ == "__main__":
    main()
