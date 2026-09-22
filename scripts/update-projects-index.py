from pathlib import Path
from datetime import datetime
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = ROOT / "diary" / "projects"
README = PROJECTS_DIR / "README.md"

START_MARKER = "<!-- PROJECTS-INDEX:START -->"
END_MARKER = "<!-- PROJECTS-INDEX:END -->"


def read_frontmatter(path: Path) -> dict:
    """Read simple YAML frontmatter fields from a Markdown file."""

    text = path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        return {}

    parts = text.split("---", 2)

    if len(parts) < 3:
        return {}

    frontmatter = parts[1]
    metadata = {}

    for line in frontmatter.splitlines():
        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if value:
            metadata[key] = value

    return metadata


def find_last_updated(project_dir: Path):
    """
    Find the latest dated Markdown record inside a project.

    Project README files are ignored because they describe the project
    itself rather than representing dated project activity.
    """

    dates = []

    for path in project_dir.rglob("*.md"):
        if path.name == "README.md":
            continue

        metadata = read_frontmatter(path)
        date = metadata.get("date")

        if not date:
            continue

        try:
            parsed_date = datetime.strptime(
                date,
                "%Y-%m-%d",
            )
        except ValueError:
            print(
                f"Skipping date in {path}: "
                "invalid date"
            )
            continue

        dates.append(parsed_date)

    if not dates:
        return None

    return max(dates)


def find_projects():
    """Discover projects from metadata in project README files."""

    projects = []

    for project_dir in PROJECTS_DIR.iterdir():
        if not project_dir.is_dir():
            continue

        project_readme = project_dir / "README.md"

        if not project_readme.exists():
            continue

        metadata = read_frontmatter(project_readme)

        project = metadata.get("project")
        title = metadata.get("title")
        description = metadata.get("description")
        status = metadata.get("status")
        started = metadata.get("started")
        icon = metadata.get("icon", "🧪")

        if not all(
            [
                project,
                title,
                description,
                status,
                started,
            ]
        ):
            print(
                f"Skipping {project_dir}: "
                "missing project, title, description, "
                "status, or started"
            )
            continue

        try:
            parsed_started = datetime.strptime(
                started,
                "%Y-%m-%d",
            )
        except ValueError:
            print(
                f"Skipping {project_dir}: "
                "invalid started date"
            )
            continue

        last_updated = find_last_updated(project_dir)

        projects.append(
            {
                "project": project,
                "title": title,
                "description": description,
                "status": status,
                "started": parsed_started,
                "last_updated": last_updated,
                "icon": icon,
                "path": project_dir,
            }
        )

    return sorted(
        projects,
        key=lambda item: (
            item["last_updated"] or item["started"],
            item["title"].lower(),
        ),
        reverse=True,
    )


def build_index(projects):
    """Generate the projects index section."""

    lines = [
        "> 🤖 **Generated automatically:** "
        "This index is rebuilt from project metadata.",
        "",
        "| Project | Status | Started | Last updated | Description |",
        "|---|---|---|---|---|",
    ]

    for item in projects:
        relative_path = item["path"].relative_to(
            PROJECTS_DIR
        ).as_posix()

        started = item["started"].strftime("%Y-%m-%d")

        if item["last_updated"]:
            last_updated = item["last_updated"].strftime(
                "%Y-%m-%d"
            )
        else:
            last_updated = "—"

        status = item["status"].replace("-", " ").title()

        lines.append(
            f"| {item['icon']} "
            f"[{item['title']}]({relative_path}/) | "
            f"{status} | "
            f"{started} | "
            f"{last_updated} | "
            f"{item['description']} |"
        )

    return "\n".join(lines)


def update_readme(index):
    """Replace only the generated projects index section."""

    text = README.read_text(encoding="utf-8")

    pattern = re.compile(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        re.DOTALL,
    )

    if not pattern.search(text):
        raise RuntimeError(
            "Could not find PROJECTS-INDEX markers "
            "in diary/projects/README.md"
        )

    replacement = (
        f"{START_MARKER}\n\n"
        f"{index}\n\n"
        f"{END_MARKER}"
    )

    README.write_text(
        pattern.sub(replacement, text),
        encoding="utf-8",
    )


def main():
    projects = find_projects()

    if not projects:
        raise RuntimeError("No valid projects found.")

    index = build_index(projects)
    update_readme(index)

    print(
        f"Updated diary/projects/README.md with "
        f"{len(projects)} project(s)."
    )


if __name__ == "__main__":
    main()