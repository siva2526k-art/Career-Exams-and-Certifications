import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

def generate_metrics():
    db_dir = REPO_ROOT / "07_Database"
    with open(db_dir / "exams.json", "r", encoding="utf-8") as f:
        exams = json.load(f)
    with open(db_dir / "certifications.json", "r", encoding="utf-8") as f:
        certs = json.load(f)
    with open(db_dir / "organizations.json", "r", encoding="utf-8") as f:
        orgs = json.load(f)
    with open(db_dir / "careers.json", "r", encoding="utf-8") as f:
        careers = json.load(f)

    cat_counts = {}
    for e in exams:
        cat = e.get("category", "Other")
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    cert_cat_counts = {}
    for c in certs:
        cat = c.get("category", "Other")
        cert_cat_counts[cat] = cert_cat_counts.get(cat, 0) + 1

    print("==================================================")
    print("CAREER-EXAMS-AND-CERTIFICATIONS METRICS DASHBOARD")
    print("==================================================")
    print(f"Total Competitive Examinations Indexed : {len(exams)}")
    print(f"Total Professional Certifications      : {len(certs)}")
    print(f"Total Conducting Organizations Tracked : {len(orgs)}")
    print(f"Total Career Trajectories Mapped       : {len(careers)}")
    print("--------------------------------------------------")
    print("Exams by Category:")
    for k, v in sorted(cat_counts.items()):
        print(f"  - {k:<25}: {v}")
    print("--------------------------------------------------")
    print("Certifications by Domain:")
    for k, v in sorted(cert_cat_counts.items()):
        print(f"  - {k:<25}: {v}")
    print("==================================================")

if __name__ == "__main__":
    generate_metrics()
