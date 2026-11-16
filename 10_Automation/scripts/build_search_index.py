import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

def build_search_index():
    db_dir = REPO_ROOT / "07_Database"
    with open(db_dir / "exams.json", "r", encoding="utf-8") as f:
        exams = json.load(f)
    with open(db_dir / "certifications.json", "r", encoding="utf-8") as f:
        certs = json.load(f)
    with open(db_dir / "careers.json", "r", encoding="utf-8") as f:
        careers = json.load(f)

    output = ["# Master Search Index & Quick Navigation Matrix\n\n"]
    output.append("This document is generated automatically by `10_Automation/scripts/build_search_index.py`.\n\n")
    output.append("## 1. Competitive Examinations Quick Index\n\n")
    output.append("| ID | Exam Name | Category | Eligible Qualifications | Guide Link |\n")
    output.append("|---|---|---|---|---|\n")
    for e in exams:
        quals = ", ".join(e.get("eligible_qualifications", [])[:3])
        path = e.get("document_path")
        output.append(f"| `{e['id']}` | **{e['name']}** | {e['category']} | {quals} | [{e['short_name']}]({path}) |\n")

    output.append("\n## 2. Professional Certifications Quick Index\n\n")
    output.append("| ID | Certification Name | Category | Level | Guide Link |\n")
    output.append("|---|---|---|---|---|\n")
    for c in certs:
        output.append(f"| `{c['id']}` | **{c['name']}** | {c['category']} | {c['level']} | [Guide]({c['document_path']}) |\n")

    output_path = REPO_ROOT / "03_Exam_Information" / "Master_Search_Index.md"
    output_path.write_text("".join(output), encoding="utf-8")
    print(f"[+] Successfully generated Master Search Index at: {output_path}")

if __name__ == "__main__":
    build_search_index()
