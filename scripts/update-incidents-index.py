from pathlib import Path
from datetime import datetime


ROOT = Path(__file__).resolve().parent.parent
INCIDENTS_DIR = ROOT / "diary" / "incidents"
README = INCIDENTS_DIR / "README.md"


def read_frontmatter(path: Path) -> dict:
    """Read the YAML frontmatter fields needed for the incidents index."""

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


def find_incidents():
    """Find incident records under diary/incidents/."""

    incidents = []

    for path in INCIDENTS_DIR.glob("II[0-9][0-9]*.md"):
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
            entry_number = int(entry.removeprefix("II"))
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print(f"Skipping {path}: invalid entry number or date")
            continue

        incidents.append(
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
        incidents,
        key=lambda item: item["entry_number"],
        reverse=True,
    )


def build_readme(incidents):
    """Generate the complete incidents README from scratch."""

    lines = [
        "# 🚨 Infrastructure Incidents",
        "",
        "> Sometimes I don't do anything to the homelab. Sometimes the homelab — or the infrastructure around it — does something to me.",
        "",
        "Unexpected outages, failures, and other things that decided to become part of the story.",
        "",
        "> 🤖 **Generated automatically:** This index is rebuilt from the metadata in the incident records.",
        "",
        "| # | Date | Incident | Status |",
        "|---:|---|---|---|",
    ]

    for item in incidents:
        relative_path = item["path"].relative_to(INCIDENTS_DIR).as_posix()
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
            "[← Back to the diary](../)",
            "",
        ]
    )

    return "\n".join(lines)


def main():
    incidents = find_incidents()

    if not incidents:
        raise RuntimeError("No valid incident records found.")

    content = build_readme(incidents)

    README.write_text(content, encoding="utf-8")

    print(
        f"Generated diary/incidents/README.md "
        f"with {len(incidents)} incident(s)."
    )


if __name__ == "__main__":
    main()