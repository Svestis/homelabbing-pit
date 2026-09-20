from pathlib import Path
from datetime import datetime
import re


ROOT = Path(__file__).resolve().parent.parent
DIARY_DIR = ROOT / "diary"
ENTRIES_DIR = DIARY_DIR / "entries"
INCIDENTS_DIR = DIARY_DIR / "incidents"
TROUBLESHOOTING_DIR = DIARY_DIR / "troubleshooting"

README = ROOT / "README.md"

LATEST_START_MARKER = "<!-- LATEST:START -->"
LATEST_END_MARKER = "<!-- LATEST:END -->"

PIT_INDEX_START_MARKER = "<!-- PIT-INDEX:START -->"
PIT_INDEX_END_MARKER = "<!-- PIT-INDEX:END -->"

LATEST_COUNT = 3


def read_frontmatter(path: Path) -> dict:
    """Read the YAML frontmatter fields needed for the indexes."""

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


def get_record_type(path: Path, entry: str):
    """Determine the record type from its location and entry prefix."""

    if path.parent == INCIDENTS_DIR or entry.startswith("II"):
        return "🚨 Incident"

    if path.parent == TROUBLESHOOTING_DIR or entry.startswith("TS"):
        return "🔧 Troubleshooting"

    if path.parent == ENTRIES_DIR and entry.isdigit():
        return "📖 Diary"

    return None


def find_records():
    """Find all diary, incident, and troubleshooting records."""

    paths = []

    # Main diary entries.
    paths.extend(
        ENTRIES_DIR.glob("[0-9][0-9][0-9][0-9]-*.md")
    )

    # Infrastructure incidents.
    paths.extend(
        INCIDENTS_DIR.glob("II*.md")
    )

    # Troubleshooting records.
    paths.extend(
        TROUBLESHOOTING_DIR.glob("TS*.md")
    )

    records = []

    for path in paths:
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

        record_type = get_record_type(path, entry)

        if not record_type:
            print(
                f"Skipping {path}: "
                "unrecognized record type"
            )
            continue

        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print(f"Skipping {path}: invalid date")
            continue

        records.append(
            {
                "entry": entry,
                "date": parsed_date,
                "title": title,
                "type": record_type,
                "path": path,
            }
        )

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
        relative_path = item["path"].relative_to(ROOT).as_posix()
        date = item["date"].strftime("%Y-%m-%d")

        lines.append(
            f"| {item['type']} | `{item['entry']}` | "
            f"{date} | [{item['title']}]({relative_path}) |"
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
        relative_path = item["path"].relative_to(ROOT).as_posix()
        date = item["date"].strftime("%Y-%m-%d")

        lines.append(
            f"| {item['type']} | `{item['entry']}` | "
            f"{date} | [{item['title']}]({relative_path}) |"
        )

    return "\n".join(lines)


def replace_section(text, start_marker, end_marker, content):
    """Replace a generated section between two markers."""

    pattern = re.compile(
        rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
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

    return pattern.sub(replacement, text)


def update_readme(latest, pit_index):
    """Update the generated sections in the root README."""

    text = README.read_text(encoding="utf-8")

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
        raise RuntimeError("No valid records found.")

    latest = build_latest(records)
    pit_index = build_pit_index(records)

    update_readme(latest, pit_index)

    print(
        f"Updated root README with "
        f"{min(LATEST_COUNT, len(records))} latest record(s) "
        f"and {len(records)} total record(s)."
    )


if __name__ == "__main__":
    main()
