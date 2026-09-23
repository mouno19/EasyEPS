#!/usr/bin/env python3
import json
import sys
from pathlib import Path

content_dir = Path(__file__).resolve().parents[1] / "content"
root = content_dir / "lessons"
issues = []
for path in sorted(root.glob("lesson-*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    for index, item in enumerate(data.get("practice", [])):
        for key in ("id", "type", "questionBn", "questionKo", "explanationBn"):
            if not isinstance(item.get(key), str) or not item.get(key):
                issues.append((path.name, f"practice[{index}]", key, repr(item.get(key))))
        if item.get("type") == "matching":
            if not isinstance(item.get("pairs"), list) or not item.get("pairs"):
                issues.append((path.name, f"practice[{index}]", "pairs", repr(item.get("pairs"))))
        else:
            if not isinstance(item.get("options"), list) or len(item.get("options", [])) < 2:
                issues.append((path.name, f"practice[{index}]", "options", repr(item.get("options"))))
            if not isinstance(item.get("answer"), int):
                issues.append((path.name, f"practice[{index}]", "answer", repr(item.get("answer"))))

# --- manifest sync ---------------------------------------------------------
# content/manifest.json is the resumability record (CONTINUATION.md): it tells a
# future session which chapters are complete and how large each one is. Bulk
# content edits — e.g. appending image-based EPS questions — have historically
# left its counts stale, so verify them against the lesson files, which are the
# public source of truth. Repair with `python3 scripts/update-manifest-eps.py`.
manifest_path = content_dir / "manifest.json"
if not manifest_path.is_file():
    issues.append(("manifest.json", "-", "missing", "run scripts/update-manifest-eps.py"))
else:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = manifest.get("completed", [])
    listed = set()
    for entry in entries:
        name = entry.get("file")
        listed.add(name)
        lesson_path = root / str(name)
        if not lesson_path.is_file():
            issues.append(("manifest.json", f"chapter {entry.get('chapter')}", "file-missing", repr(name)))
            continue
        lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
        for key, actual in (
            ("vocabulary", len(lesson.get("vocabulary", []))),
            ("practice", len(lesson.get("practice", []))),
            ("eps", len(lesson.get("epsQuestions", []))),
        ):
            if entry.get(key) != actual:
                issues.append(
                    (
                        name,
                        "manifest-count",
                        key,
                        f"manifest={entry.get(key)!r} actual={actual!r}",
                    )
                )
    for path in sorted(root.glob("lesson-*.json")):
        if path.name not in listed:
            issues.append(("manifest.json", path.name, "chapter-unlisted", "add to completed[]"))
    declared = manifest.get("totalChapters")
    actual_files = sorted(path.name for path in root.glob("lesson-*.json"))
    if isinstance(declared, int) and declared != len(actual_files):
        issues.append(
            (
                "manifest.json",
                "totalChapters",
                "count",
                f"declared={declared!r} lesson-files={len(actual_files)!r}",
            )
        )

for issue in issues:
    print("\t".join(issue))
print(f"issues={len(issues)}")
if issues:
    sys.exit(1)
