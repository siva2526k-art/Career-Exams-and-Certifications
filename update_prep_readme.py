from pathlib import Path

REPO_ROOT = Path(r"C:\Users\siva2\.gemini\antigravity\scratch\Career-Exams-and-Certifications")

readme_path = REPO_ROOT / "05_Preparation_Resources" / "README.md"
content = readme_path.read_text(encoding="utf-8")

if "Programming_Languages_Mastery_for_AI_and_ML.md" not in content:
    addition = """  - `Programming_Languages_Mastery_for_AI_and_ML.md`: The "Power Trio" programming guide (Python, C++, SQL) for AI/ML engineering, GATE DA, GATE CS, and MNC LeetCode rounds.
"""
    target = "- `Linux_for_AI_and_Machine_Learning_Guide.md`"
    content = content.replace(target, addition + "  " + target)
    readme_path.write_text(content, encoding="utf-8")
    print("[+] Updated 05_Preparation_Resources/README.md")
