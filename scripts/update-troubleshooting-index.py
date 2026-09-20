from pathlib import Path
from datetime import datetime


ROOT = Path(__file__).resolve().parent.parent
TROUBLESHOOTING_DIR = ROOT / "diary" / "troubleshooting"
README = TROUBLESHOOTING_DIR / "README.md"


def read_frontmatter(path: Path) -> dict:
    """Read the YAML frontmatter fields needed for the troubleshooting index."""

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


def find_troubleshooting():
    """Find troubleshooting records under diary/troubleshooting/."""

    records = []

    for path in TROUBLESHOOTING_DIR.glob("TS[0-9][0-9]*.md"):
        metadata = read_frontmatter(path)

        entry = metadata.get("entry")
        date = metadata.get("date")
        title = metadata.get("title")
        status = metadata.get("status")

        if not entry or not date or not title or not status:
            print(
                f"Skipping {path}: "
                "missing entry, date, title, or status"
            )
            continue

        try:
            entry_number = int(entry.removeprefix("TS"))
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print(f"Skipping {path}: invalid entry number or date")
            continue

        records.append(
            {
                "entry": entry,
                "entry_number": entry_number,
                "date": parsed_date,
                "title": title,
                "status": status,
                "path": path,
            }
        )

    return sorted(
        records,
        key=lambda item: item["entry_number"],
        reverse=True,
    )


def build_readme(records):
    """Generate the complete troubleshooting README from scratch."""

    lines = [
        "# 🔧 Troubleshooting",
        "",
        "> Problems that turned into investigations of their own.",
        "",
        "Things that didn't necessarily break on their own, but somehow ended with me testing cables, reading documentation, or questioning previous decisions.",
        "",
        "> 🤖 **Generated automatically:** This index is rebuilt from the metadata in the troubleshooting records.",
        "",
        "| # | Date | Investigation | Status |",
        "|---:|---|---|---|",
    ]

    for item in records:
        relative_path = item["path"].relative_to(
            TROUBLESHOOTING_DIR
        ).as_posix()

        date = item["date"].strftime("%Y-%m-%d")
        status = item["status"].replace("-", " ").title()

        lines.append(
            f"| `{item['entry']}` | {date} | "
            f"[{item['title']}]({relative_path}) | {status} |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "[← Back to the diary](../README.md)",
            "",
        ]
    )

    return "\n".join(lines)


def main():
    records = find_troubleshooting()

    if not records:
        raise RuntimeError("No valid troubleshooting records found.")

    content = build_readme(records)

    README.write_text(content, encoding="utf-8")

    print(
        f"Generated diary/troubleshooting/README.md "
        f"with {len(records)} record(s)."
    )


if __name__ == "__main__":
    main()