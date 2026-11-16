# Changelog

All notable changes to the **Career-Exams-and-Certifications** repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-11-16

### Added
- **Repository Architecture:** Initialized 10 core architectural modules covering competitive exams, professional certifications, exam parameters, career mappings, preparation resources, active tracking dashboards, relational JSON databases, standardized templates, research reports, and CI automation.
- **Competitive Examination Dossiers:** Detailed, 11-section standardized dossiers for:
  - Central Government: UPSC Civil Services, UPSC Engineering Services, UPSC CDS, UPSC NDA, SSC CGL, SSC CHSL, SSC JE, SSC MTS, SSC CPO.
  - Banking: IBPS PO, IBPS Clerk, IBPS SO, SBI PO, SBI Clerk, RBI Grade B, RBI Assistant, NABARD Grade A.
  - Railway: RRB NTPC, RRB JE, RRB ALP, RRB Group D.
  - Defence: AFCAT, INET, Agniveer Scheme.
  - Tamil Nadu State Government: TNPSC Group I, TNPSC Group II & IIA, TNPSC Group IV, TNPSC Combined Technical Services, TNUSRB Sub-Inspector, TNUSRB Police Constable, TN TRB Assistant Professor.
  - Technical & Engineering: GATE (CS, DA, EC), ISRO Scientist/Engineer 'SC', DRDO RAC Scientist 'B', DRDO CEPTAM, BARC OCES/DGFS, NIC Scientist 'B', Maharatna/Navratna PSU recruitment.
  - International Examinations: GRE General Test, GMAT Focus Edition, TOEFL iBT, IELTS Academic.
- **Professional Certification Dossiers:** Detailed, 9-section standardized dossiers for:
  - Cloud Computing: AWS Solutions Architect Associate, Microsoft Azure Solutions Architect Expert, Google Cloud Professional Cloud Architect.
  - Cybersecurity: CompTIA Security+, CompTIA CySA+, CompTIA PenTest+, CEH, OSCP, CISSP.
  - Networking: Cisco CCNA (200-301), Cisco CCNP Enterprise, CompTIA Network+.
  - Artificial Intelligence & ML: TensorFlow Developer, AWS Certified Machine Learning Specialty, DeepLearning.AI GenAI Professional.
  - DevOps & Operating Systems: CKA (Certified Kubernetes Administrator), HashiCorp Terraform Associate, RHCSA.
  - Programming & Databases: Oracle Certified Professional Java SE, Python Institute PCAP, MongoDB Certified Developer.
  - Academic & Management: NPTEL Elite Gold Domain, SWAYAM Credit Transfer, PMP, CFA.
- **Structured Relational Database:**
  - `exams.json`: 30+ structured examination entities.
  - `certifications.json`: 20+ structured certification entities.
  - `organizations.json`: Authoritative directory of conducting bodies.
  - `careers.json`: Standardized career trajectories and salary structures.
  - `sources.json`: Master index of official verified URLs.
- **Automation & Schemas:**
  - 5 formal JSON Schemas (`exam`, `certification`, `organization`, `career`, `source`).
  - `validate_database.py` automated validation and referential integrity script.
  - `generate_summary_metrics.py` analytical engine.
  - `build_search_index.py` Markdown search index generator.
  - GitHub Actions CI workflow for automated schema checks.
- **Tracking Dashboards:**
  - `Upcoming_Exams.md`, `Application_Deadlines.md`, `Annual_Exam_Calendar.md`, `Certification_Expiry.md`, `Notification_Tracker.md`.
- **Career Eligibility Matrix:** Comprehensive qualification-to-opportunity roadmap spanning 10th pass, 12th pass, Diploma, B.E./B.Tech, B.Sc./BCA/B.Com, M.Tech/MCA/M.Sc, and working professionals.
