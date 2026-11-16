# 10. Automation & Data Validation Framework

CI/CD automation suite and formal schemas ensuring data integrity:
- **`schemas/`**: Formal JSON Schema definitions conforming to Draft-07.
- **`scripts/validate_database.py`**: Referential integrity validator verifying IDs and document paths.
- **`scripts/generate_summary_metrics.py`**: Computes category distributions and index counts.
- **`scripts/build_search_index.py`**: Compiles `03_Exam_Information/Master_Search_Index.md`.
