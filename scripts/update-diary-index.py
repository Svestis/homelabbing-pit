from pathlib import Path
from datetime import datetime
import re


ROOT = Path(__file__).resolve().parent.parent
DIARY_DIR = ROOT / "diary"
ENTRIES_DIR = DIARY_DIR / "entries"
README = DIARY_DIR / "README.md"

START_MARKER = "<!-- DIARY-INDEX:START -->"
END_MARKER = "<!-- DIARY-INDEX:END -->"


def read_frontmatter(path: Path) -> dict:
    """Read the YAML frontmatter fields needed for the diary index."""

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
    """Find numbered diary entries under diary/entries/."""

    entries = []

    for path in ENTRIES_DIR.glob("[0-9][0-9][0-9][0-9]-*.md"):
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
            entry_number = int(entry)
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print(
                f"Skipping {path}: "
                "invalid entry number or date"
            )
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

    # Newest numbered entry first.
    return sorted(
        entries,
        key=lambda item: item["entry_number"],
        reverse=True,
    )


def build_index(entries):
    """Generate the diary index section."""

    lines = [
        "> 🤖 **Generated automatically:** "
        "This index is rebuilt from the metadata in the diary entries.",
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

    return "\n".join(lines)


def update_readme(index):
    """Replace only the generated diary index section."""

    text = README.read_text(encoding="utf-8")

    pattern = re.compile(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        re.DOTALL,
    )

    if not pattern.search(text):
        raise RuntimeError(
            "Could not find DIARY-INDEX markers in diary/README.md"
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
    entries = find_entries()

    if not entries:
        raise RuntimeError("No valid diary entries found.")

    index = build_index(entries)
    update_readme(index)

    print(
        f"Updated diary/README.md with "
        f"{len(entries)} diary entries."
    )


if __name__ == "__main__":
    main()
