from pathlib import Path
from datetime import datetime
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = ROOT / "diary" / "projects"

START_MARKER = "<!-- PROJECT-INDEX:START -->"
END_MARKER = "<!-- PROJECT-INDEX:END -->"


def read_frontmatter(path: Path) -> dict:
    """Read simple YAML frontmatter fields."""

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


def find_projects():
    """Discover projects from their README metadata."""

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

        if not project or not title:
            print(
                f"Skipping {project_dir}: "
                "missing project or title metadata"
            )
            continue

        projects.append(
            {
                "project": project,
                "title": title,
                "path": project_dir,
                "readme": project_readme,
            }
        )

    return projects


def find_journal_entries(project):
    """Find journal entries belonging to a project."""

    journal_dir = project["path"] / "journal"

    if not journal_dir.exists():
        return []

    entries = []

    for path in journal_dir.glob("*.md"):
        metadata = read_frontmatter(path)

        entry = metadata.get("entry")
        record_project = metadata.get("project")
        title = metadata.get("title")
        date = metadata.get("date")
        record_type = metadata.get("type", "journal")
        status = metadata.get("status")

        if not all(
            [
                entry,
                record_project,
                title,
                date,
                status,
            ]
        ):
            print(
                f"Skipping {path}: "
                "missing entry, project, title, date, or status"
            )
            continue

        if record_project != project["project"]:
            print(
                f"Skipping {path}: "
                f"project '{record_project}' does not match "
                f"parent project '{project['project']}'"
            )
            continue

        if record_type != "journal":
            print(
                f"Skipping {path}: "
                f"unsupported type '{record_type}'"
            )
            continue

        try:
            parsed_date = datetime.strptime(
                date,
                "%Y-%m-%d",
            )
        except ValueError:
            print(
                f"Skipping {path}: "
                "invalid date"
            )
            continue

        entries.append(
            {
                "entry": entry,
                "title": title,
                "date": parsed_date,
                "type": record_type,
                "status": status,
                "path": path,
            }
        )

    return sorted(
        entries,
        key=lambda item: (
            item["date"],
            item["entry"],
        ),
        reverse=True,
    )


def build_index(project, entries):
    """Generate the index for one project."""

    lines = [
        "> 🤖 **Generated automatically:** "
        "This index is rebuilt from project metadata.",
        "",
        "| Type | # | Date | Entry | Status |",
        "|---|---:|---|---|---|",
    ]

    for item in entries:
        relative_path = item["path"].relative_to(
            project["path"]
        ).as_posix()

        date = item["date"].strftime("%Y-%m-%d")
        status = item["status"].replace("-", " ").title()

        if item["type"] == "journal":
            record_type = "📖 Journal"
        else:
            record_type = item["type"].title()

        lines.append(
            f"| {record_type} | "
            f"`{item['entry']}` | "
            f"{date} | "
            f"[{item['title']}]({relative_path}) | "
            f"{status} |"
        )

    return "\n".join(lines)


def update_project_readme(project, index):
    """Replace only the generated index in one project README."""

    readme = project["readme"]
    text = readme.read_text(encoding="utf-8")

    pattern = re.compile(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        re.DOTALL,
    )

    if not pattern.search(text):
        raise RuntimeError(
            f"Could not find PROJECT-INDEX markers "
            f"in {readme}"
        )

    replacement = (
        f"{START_MARKER}\n\n"
        f"{index}\n\n"
        f"{END_MARKER}"
    )

    readme.write_text(
        pattern.sub(replacement, text),
        encoding="utf-8",
    )


def main():
    projects = find_projects()

    if not projects:
        raise RuntimeError("No valid projects found.")

    updated = 0

    for project in projects:
        entries = find_journal_entries(project)
        index = build_index(project, entries)

        update_project_readme(
            project,
            index,
        )

        updated += 1

        print(
            f"Updated {project['readme'].relative_to(ROOT)} "
            f"with {len(entries)} record(s)."
        )

    print(
        f"Updated {updated} project index(es)."
    )


if __name__ == "__main__":
    main()