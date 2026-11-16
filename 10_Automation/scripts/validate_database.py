import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

def load_json(p: Path):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def run_validations():
    print("[*] Starting Career-Exams-and-Certifications Database Validation...")
    db_dir = REPO_ROOT / "07_Database"
    
    sources = load_json(db_dir / "sources.json")
    orgs = load_json(db_dir / "organizations.json")
    exams = load_json(db_dir / "exams.json")
    certs = load_json(db_dir / "certifications.json")
    careers = load_json(db_dir / "careers.json")
    
    source_ids = {s["id"] for s in sources}
    org_ids = {o["id"] for o in orgs}
    exam_ids = {e["id"] for e in exams}
    cert_ids = {c["id"] for c in certs}
    career_ids = {ca["id"] for ca in careers}

    errors = []

    # Check Exams
    for e in exams:
        eid = e.get("id")
        org_id = e.get("conducting_organization_id")
        if org_id not in org_ids:
            errors.append(f"Exam '{eid}': conducting_organization_id '{org_id}' not found in organizations.json")
        for s in e.get("verification", {}).get("sources", []):
            if s not in source_ids:
                errors.append(f"Exam '{eid}': source '{s}' not found in sources.json")
        doc_path = REPO_ROOT / e.get("document_path", "")
        if not doc_path.exists():
            errors.append(f"Exam '{eid}': Document path '{e.get('document_path')}' does not exist on disk!")

    # Check Certifications
    for c in certs:
        cid = c.get("id")
        org_id = c.get("issuing_organization_id")
        if org_id not in org_ids:
            errors.append(f"Certification '{cid}': issuing_organization_id '{org_id}' not found in organizations.json")
        for s in c.get("verification", {}).get("sources", []):
            if s not in source_ids:
                errors.append(f"Certification '{cid}': source '{s}' not found in sources.json")
        doc_path = REPO_ROOT / c.get("document_path", "")
        if not doc_path.exists():
            errors.append(f"Certification '{cid}': Document path '{c.get('document_path')}' does not exist on disk!")

    # Check Careers
    for ca in careers:
        ca_id = ca.get("id")
        for ex in ca.get("entry_exams", []):
            if ex not in exam_ids:
                errors.append(f"Career '{ca_id}': Referenced exam '{ex}' not found in exams.json")
        for cr in ca.get("recommended_certifications", []):
            if cr not in cert_ids:
                errors.append(f"Career '{ca_id}': Referenced certification '{cr}' not found in certifications.json")

    if errors:
        print(f"[-] FAILED! Found {len(errors)} validation errors:")
        for err in errors:
            print(f"    - {err}")
        sys.exit(1)
    else:
        print("[+] SUCCESS! All records validated cleanly.")
        print(f"    Exams: {len(exams)} | Certifications: {len(certs)} | Organizations: {len(orgs)} | Careers: {len(careers)} | Sources: {len(sources)}")
        sys.exit(0)

if __name__ == "__main__":
    run_validations()
