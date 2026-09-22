from pathlib import Path
from datetime import datetime
import re


ROOT = Path(__file__).resolve().parent.parent
DIARY_DIR = ROOT / "diary"

ENTRIES_DIR = DIARY_DIR / "entries"
INCIDENTS_DIR = DIARY_DIR / "incidents"
TROUBLESHOOTING_DIR = DIARY_DIR / "troubleshooting"
PROJECTS_DIR = DIARY_DIR / "projects"

README = ROOT / "README.md"

LATEST_START_MARKER = "<!-- LATEST:START -->"
LATEST_END_MARKER = "<!-- LATEST:END -->"

PIT_INDEX_START_MARKER = "<!-- PIT-INDEX:START -->"
PIT_INDEX_END_MARKER = "<!-- PIT-INDEX:END -->"

LATEST_COUNT = 3


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


def parse_date(path: Path, date: str):
    """Parse a repository metadata date."""

    try:
        return datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(
            f"Skipping {path}: "
            f"invalid date '{date}'"
        )
        return None


def load_projects():
    """
    Discover projects from metadata in their README files.

    The root index therefore does not need to know about individual
    projects such as Home Display in advance.
    """

    projects = {}

    if not PROJECTS_DIR.exists():
        return projects

    for project_dir in PROJECTS_DIR.iterdir():
        if not project_dir.is_dir():
            continue

        project_readme = project_dir / "README.md"

        if not project_readme.exists():
            continue

        metadata = read_frontmatter(project_readme)

        project = metadata.get("project")
        title = metadata.get("title")
        icon = metadata.get("icon", "🧪")

        if not project or not title:
            print(
                f"Skipping project {project_dir}: "
                "missing project or title metadata"
            )
            continue

        projects[project] = {
            "project": project,
            "title": title,
            "icon": icon,
            "path": project_dir,
        }

    return projects


def find_diary_records():
    """Find numbered main diary entries."""

    records = []

    for path in ENTRIES_DIR.glob(
        "[0-9][0-9][0-9][0-9]-*.md"
    ):
        metadata = read_frontmatter(path)

        entry = metadata.get("entry")
        date = metadata.get("date")
        title = metadata.get("title")

        if not entry or not date or not title:
            print(
                f"Skipping {path}: "
                "missing entry, date, or title"
            )
            continue

        if not entry.isdigit():
            print(
                f"Skipping {path}: "
                "invalid diary entry number"
            )
            continue

        parsed_date = parse_date(path, date)

        if not parsed_date:
            continue

        records.append(
            {
                "entry": entry,
                "date": parsed_date,
                "title": title,
                "type": "📖 Diary",
                "path": path,
            }
        )

    return records


def find_incident_records():
    """Find infrastructure incident records."""

    records = []

    for path in INCIDENTS_DIR.glob("II*.md"):
        metadata = read_frontmatter(path)

        entry = metadata.get("entry")
        date = metadata.get("date")
        title = metadata.get("title")

        if not entry or not date or not title:
            print(
                f"Skipping {path}: "
                "missing entry, date, or title"
            )
            continue

        if not entry.startswith("II"):
            print(
                f"Skipping {path}: "
                "invalid incident entry"
            )
            continue

        parsed_date = parse_date(path, date)

        if not parsed_date:
            continue

        records.append(
            {
                "entry": entry,
                "date": parsed_date,
                "title": title,
                "type": "🚨 Incident",
                "path": path,
            }
        )

    return records


def find_troubleshooting_records():
    """Find troubleshooting records."""

    records = []

    for path in TROUBLESHOOTING_DIR.glob("TS*.md"):
        metadata = read_frontmatter(path)

        entry = metadata.get("entry")
        date = metadata.get("date")
        title = metadata.get("title")

        if not entry or not date or not title:
            print(
                f"Skipping {path}: "
                "missing entry, date, or title"
            )
            continue

        if not entry.startswith("TS"):
            print(
                f"Skipping {path}: "
                "invalid troubleshooting entry"
            )
            continue

        parsed_date = parse_date(path, date)

        if not parsed_date:
            continue

        records.append(
            {
                "entry": entry,
                "date": parsed_date,
                "title": title,
                "type": "🔧 Troubleshooting",
                "path": path,
            }
        )

    return records


def find_project_records(projects):
    """
    Find journal records belonging to discovered projects.

    Only project journal entries are promoted to the root chronological
    indexes. Designs, examples, screenshots, and other supporting files
    remain inside their project indexes.
    """

    records = []

    for project_name, project in projects.items():
        journal_dir = project["path"] / "journal"

        if not journal_dir.exists():
            continue

        for path in journal_dir.glob("*.md"):
            metadata = read_frontmatter(path)

            entry = metadata.get("entry")
            date = metadata.get("date")
            title = metadata.get("title")
            record_project = metadata.get("project")
            record_type = metadata.get("type", "journal")

            if not entry or not date or not title or not record_project:
                print(
                    f"Skipping {path}: "
                    "missing entry, date, title, or project"
                )
                continue

            if record_project != project_name:
                print(
                    f"Skipping {path}: "
                    f"project '{record_project}' does not match "
                    f"parent project '{project_name}'"
                )
                continue

            if record_type != "journal":
                print(
                    f"Skipping {path}: "
                    f"unsupported project record type "
                    f"'{record_type}'"
                )
                continue

            parsed_date = parse_date(path, date)

            if not parsed_date:
                continue

            records.append(
                {
                    "entry": entry,
                    "date": parsed_date,
                    "title": title,
                    "type": (
                        f"{project['icon']} "
                        f"{project['title']}"
                    ),
                    "path": path,
                }
            )

    return records


def find_records():
    """Find every chronological record included in the root indexes."""

    projects = load_projects()

    records = []

    records.extend(find_diary_records())
    records.extend(find_incident_records())
    records.extend(find_troubleshooting_records())
    records.extend(find_project_records(projects))

    return sorted(
        records,
        key=lambda item: (
            item["date"],
            item["entry"],
        ),
        reverse=True,
    )


def build_latest(records):
    """Generate the Latest from the pit section."""

    latest = records[:LATEST_COUNT]

    lines = [
        "> 🤖 **Generated automatically:** "
        "The latest entries from across the pit.",
        "",
        "| Type | # | Date | Entry |",
        "|---|---:|---|---|",
    ]

    for item in latest:
        relative_path = item["path"].relative_to(
            ROOT
        ).as_posix()

        date = item["date"].strftime("%Y-%m-%d")

        lines.append(
            f"| {item['type']} | "
            f"`{item['entry']}` | "
            f"{date} | "
            f"[{item['title']}]({relative_path}) |"
        )

    return "\n".join(lines)


def build_pit_index(records):
    """Generate the complete Everything in the pit index."""

    lines = [
        "> 🤖 **Generated automatically:** "
        "This index is rebuilt from repository metadata.",
        "",
        "| Type | # | Date | Entry |",
        "|---|---:|---|---|",
    ]

    for item in records:
        relative_path = item["path"].relative_to(
            ROOT
        ).as_posix()

        date = item["date"].strftime("%Y-%m-%d")

        lines.append(
            f"| {item['type']} | "
            f"`{item['entry']}` | "
            f"{date} | "
            f"[{item['title']}]({relative_path}) |"
        )

    return "\n".join(lines)


def replace_section(
    text,
    start_marker,
    end_marker,
    content,
):
    """Replace a generated section between two markers."""

    pattern = re.compile(
        rf"{re.escape(start_marker)}"
        rf".*?"
        rf"{re.escape(end_marker)}",
        re.DOTALL,
    )

    if not pattern.search(text):
        raise RuntimeError(
            f"Could not find markers: "
            f"{start_marker} / {end_marker}"
        )

    replacement = (
        f"{start_marker}\n\n"
        f"{content}\n\n"
        f"{end_marker}"
    )

    return pattern.sub(
        replacement,
        text,
    )


def update_readme(latest, pit_index):
    """Update the generated sections in the root README."""

    text = README.read_text(
        encoding="utf-8"
    )

    text = replace_section(
        text,
        LATEST_START_MARKER,
        LATEST_END_MARKER,
        latest,
    )

    text = replace_section(
        text,
        PIT_INDEX_START_MARKER,
        PIT_INDEX_END_MARKER,
        pit_index,
    )

    README.write_text(
        text,
        encoding="utf-8",
    )


def main():
    records = find_records()

    if not records:
        raise RuntimeError(
            "No valid records found."
        )

    latest = build_latest(records)
    pit_index = build_pit_index(records)

    update_readme(
        latest,
        pit_index,
    )

    print(
        f"Updated root README with "
        f"{min(LATEST_COUNT, len(records))} "
        f"latest record(s) and "
        f"{len(records)} total record(s)."
    )


if __name__ == "__main__":
    main()