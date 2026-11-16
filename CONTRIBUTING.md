# Contributing to Career-Exams-and-Certifications

Thank you for your interest in contributing to **Career-Exams-and-Certifications**! This repository is designed to be an authoritative, continuously maintained, community-driven knowledge base.

To ensure extreme data fidelity, discoverability, and maintainability, all contributions must adhere to the standardized guidelines described below.

---

## 📋 Table of Contents
1. [Code of Conduct](#code-of-conduct)
2. [Contribution Workflow](#contribution-workflow)
3. [Document Standards](#document-standards)
   - [Examination Template Standards (11 Sections)](#examination-template-standards)
   - [Certification Template Standards (9 Sections)](#certification-template-standards)
4. [Database & Schema Integrity](#database--schema-integrity)
5. [Verification & Official Sources Policy](#verification--official-sources-policy)

---

## 1. Code of Conduct
We are committed to providing a welcoming, constructive, and inclusive environment. Please communicate professionally in all issues, pull requests, and discussions.

---

## 2. Contribution Workflow

1. **Fork the Repository:** Create your own feature branch (`git checkout -b feature/add-new-exam`).
2. **Consult Existing Templates:** Always consult files in [`08_Templates/`](08_Templates/).
3. **Draft Markdown Document:** Populate every required section. Do not leave placeholder sections empty; mark unknown items explicitly with `*Pending official notification*`.
4. **Update Relational Database:** When adding an exam or certification, you **must** update the corresponding JSON file in [`07_Database/`](07_Database/).
5. **Run Local Validation:** Ensure all schema checks pass:
   ```bash
   python 10_Automation/scripts/validate_database.py
   ```
6. **Commit & Push:** Submit a clean, atomic Pull Request describing the changes and citing official gazette or notification sources.

---

## 3. Document Standards

### Examination Template Standards
Every examination document in `01_Competitive_Exams/` MUST follow the 11-section format specified in [`08_Templates/Exam_Template.md`](08_Templates/Exam_Template.md):
1. **Overview:** Full name, short name, category, conducting organization, official portal, examination purpose.
2. **Eligibility:** Qualifications, eligible degrees, minimum marks, age criteria, relaxations, nationality, final-year eligibility.
3. **Examination Pattern:** Mode, duration, marks, question count, question types, negative marking, sections.
4. **Syllabus:** Comprehensive topic breakdown, core subjects, link to official syllabus document.
5. **Application:** Procedure, application fee, document requirements, portal URL, critical cycle dates.
6. **Selection Process:** Written test, interview, physical endurance/medical tests, document verification, final merit rules.
7. **Career Opportunities:** Designation, pay scales (7th CPC / IDA / Gross), promotional ladder, higher education avenues.
8. **Preparation:** Official past papers, standard reference books, free lecture portals, practice tests.
9. **Historical Information:** Previous cut-offs, vacancy trends, recent structural changes in pattern.
10. **Official Sources:** Hyperlinked primary sources (Gazette, notification PDF, official portal).
11. **Verification:** Last verified date, cycle year, verification status, and pending items.

### Certification Template Standards
Every certification document in `02_Professional_Certifications/` MUST follow the 9-section format specified in [`08_Templates/Certification_Template.md`](08_Templates/Certification_Template.md):
1. **Overview:** Name, issuing organization, category, credential level, official website.
2. **Eligibility:** Prerequisites, recommended hands-on experience, educational background.
3. **Examination:** Exam code, duration, question count, format, passing score, fee.
4. **Curriculum:** Domains, weightage percentages, learning objectives.
5. **Validity:** Validity duration (e.g. 3 years), recertification requirements, renewal cost, CEU/CPE credits.
6. **Preparation:** Official training courses, free study guides, recommended literature, mock tests.
7. **Career Value:** Target job roles, market prestige, salary impact, prerequisite skills.
8. **Comparison:** Alternatives (AWS vs Azure, Security+ vs CEH, etc.), stepping stones.
9. **Verification:** Official exam guide URL, last verified date, current exam code version.

---

## 4. Database & Schema Integrity

All changes to `07_Database/*.json` must strictly validate against the JSON Schemas in `10_Automation/schemas/`:
- `exam.schema.json`
- `certification.schema.json`
- `organization.schema.json`
- `career.schema.json`
- `source.schema.json`

Key rules:
- **Unique Identifiers:** All IDs must follow canonical patterns (e.g., `UPSC_CSE`, `CERT_AWS_SAA`, `ORG_UPSC`, `SRC_UPSC_OFFICIAL`).
- **Referential Integrity:** Conducting organization IDs and Source IDs referenced in records must exist in `organizations.json` and `sources.json`.
- **No Fabrications:** Every statement regarding cutoffs, vacancies, or syllabus changes must cite an official source.

---

## 5. Verification & Official Sources Policy

- **Primary Sources Only:** Acceptable sources include official government portals (`.gov.in`, `.nic.in`), university domains (`.ac.in`, `.edu`), and official vendor portals (`aws.amazon.com`, `learn.microsoft.com`, `cisco.com`).
- **No Third-Party Coaching Blogs:** Do not cite unverified coaching blogs or speculative social media rumors.
