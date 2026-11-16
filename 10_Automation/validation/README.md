# Database Validation & Schema Architecture

This directory documents the automated test suite ensuring zero broken links, no orphaned relations, and strict schema compliance.

### How It Works:
1. `schemas/`: Contains JSON Schema specifications conforming to Draft-07.
2. `scripts/validate_database.py`:
   - Checks that all JSON files load properly.
   - Enforces referential integrity between `exams.json`, `certifications.json`, `organizations.json`, `careers.json`, and `sources.json`.
   - Confirms that every referenced Markdown file physically exists on disk.
3. CI Integration: Configured in `.github/workflows/validate_database.yml` to trigger on every push and pull request.
