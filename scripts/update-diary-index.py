from pathlib import Path
from datetime import datetime


ROOT = Path(__file__).resolve().parent.parent
DIARY_DIR = ROOT / "diary"
README = DIARY_DIR / "README.md"


def read_frontmatter(path: Path) -> dict:
    """Read the simple YAML frontmatter fields needed for the index."""

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


def find_entries():
    """Find numbered diary entries under diary/YYYY/MM/."""

    entries = []

    for path in DIARY_DIR.glob("20[0-9][0-9]/[0-9][0-9]/*.md"):
        metadata = read_frontmatter(path)

        entry = metadata.get("entry")
        date = metadata.get("date")
        title = metadata.get("title")

        if not entry or not date or not title:
            print(f"Skipping {path}: missing entry, date, or title")
            continue

        try:
            entry_number = int(entry)
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print(f"Skipping {path}: invalid entry number or date")
            continue

        entries.append(
            {
                "entry": entry,
                "entry_number": entry_number,
                "date": parsed_date,
                "title": title,
                "path": path,
            }
        )

    return sorted(entries, key=lambda item: item["entry_number"])


def build_readme(entries):
    """Generate the complete diary README."""

    lines = [
        "# 📖 The Diary",
        "",
        "> From one innocent Ubuntu VM to... whatever this has become.",
        "",
        "The main diary follows the homelab roughly in the order it happened.",
        "",
        "> [!NOTE]",
        "> This file is generated automatically from the metadata in the diary entries.",
        "",
        "| # | Date | Entry |",
        "|---:|---|---|",
    ]

    for item in entries:
        relative_path = item["path"].relative_to(DIARY_DIR).as_posix()
        date = item["date"].strftime("%Y-%m-%d")

        lines.append(
            f"| `{item['entry']}` | {date} | "
            f"[{item['title']}]({relative_path}) |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "🕳️ **Status:** still digging. ⛏️",
            "",
        ]
    )

    return "\n".join(lines)


def main():
    entries = find_entries()

    if not entries:
        raise RuntimeError("No valid diary entries found.")

    content = build_readme(entries)

    README.write_text(content, encoding="utf-8")

    print(f"Generated diary/README.md with {len(entries)} entries.")


if __name__ == "__main__":
    main()