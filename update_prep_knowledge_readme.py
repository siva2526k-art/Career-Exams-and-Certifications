from pathlib import Path

REPO_ROOT = Path(r"C:\Users\siva2\.gemini\antigravity\scratch\Career-Exams-and-Certifications")

readme_path = REPO_ROOT / "05_Preparation_Resources" / "README.md"
content = readme_path.read_text(encoding="utf-8")

if "AI_ML_Foundational_Knowledge_Requirements.md" not in content:
    addition = """  - `AI_ML_Foundational_Knowledge_Requirements.md`: The 5 core knowledge pillars (Math, CS Algorithms, Classical ML Mechanics, Deep Learning Theory, Systems) with equations, intuition, and self-test checkpoints.
"""
    target = "- `Programming_Languages_Mastery_for_AI_and_ML.md`"
    content = content.replace(target, addition + "  " + target)
    readme_path.write_text(content, encoding="utf-8")
    print("[+] Updated 05_Preparation_Resources/README.md")
