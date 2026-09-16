from pathlib import Path
from datetime import datetime
import re


ROOT = Path(__file__).resolve().parent.parent
DIARY_DIR = ROOT / "diary"
README = ROOT / "README.md"

START_MARKER = "<!-- LATEST:START -->"
END_MARKER = "<!-- LATEST:END -->"

LATEST_COUNT = 3


def read_frontmatter(path: Path) -> dict:
    """Read the YAML frontmatter fields needed for the latest entries."""

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

    if path.parent == DIARY_DIR / "incidents" or entry.startswith("II"):
        return "🚨 Incident"

    if path.parent == DIARY_DIR / "troubleshooting" or entry.startswith("TS"):
        return "🔧 Troubleshooting"

    return "📖 Diary"


def find_records():
    """Find all diary, incident, and troubleshooting records."""

    paths = []

    # Main diary entries.
    paths.extend(
        DIARY_DIR.glob("20[0-9][0-9]/[0-9][0-9]/*.md")
    )

    # Infrastructure incidents.
    paths.extend(
        (DIARY_DIR / "incidents").glob("II*.md")
    )

    # Troubleshooting records.
    paths.extend(
        (DIARY_DIR / "troubleshooting").glob("TS*.md")
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
                "type": get_record_type(path, entry),
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
    """Generate the latest entries section."""

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


def update_readme(latest):
    """Replace only the generated Latest from the pit section."""

    text = README.read_text(encoding="utf-8")

    pattern = re.compile(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        re.DOTALL,
    )

    if not pattern.search(text):
        raise RuntimeError(
            "Could not find LATEST markers in README.md"
        )

    replacement = (
        f"{START_MARKER}\n\n"
        f"{latest}\n\n"
        f"{END_MARKER}"
    )

    README.write_text(
        pattern.sub(replacement, text),
        encoding="utf-8",
    )


def main():
    records = find_records()

    if not records:
        raise RuntimeError("No valid records found.")

    latest = build_latest(records)
    update_readme(latest)

    print(
        f"Updated root README with "
        f"{min(LATEST_COUNT, len(records))} latest record(s)."
    )


if __name__ == "__main__":
    main()