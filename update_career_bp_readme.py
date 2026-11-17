from pathlib import Path

REPO_ROOT = Path(r"C:\Users\siva2\.gemini\antigravity\scratch\Career-Exams-and-Certifications")

readme_path = REPO_ROOT / "04_Career_Opportunities" / "README.md"
content = readme_path.read_text(encoding="utf-8")

if "AI_ML_Career_Master_Blueprint.md" not in content:
    addition = """- **`AI_ML_Career_Master_Blueprint.md`**: Complete end-to-end execution guide for AI & ML candidates: Essential certifications, specialized job roles, government entrance exams (GATE DA, DRDO, ISRO, SEBI), and top tier-1 MNC/global recruiters.
"""
    content = content.replace("- **`Tamil_Nadu_Government_and_Aided_Tech_Jobs_Guide.md`**:", addition + "- **`Tamil_Nadu_Government_and_Aided_Tech_Jobs_Guide.md`**:")
    readme_path.write_text(content, encoding="utf-8")
    print("[+] Updated 04_Career_Opportunities/README.md")
