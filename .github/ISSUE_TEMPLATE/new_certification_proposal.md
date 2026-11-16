name: New Professional Certification Proposal
description: Propose adding a new recognized professional certification
title: "[NEW CERT]: <Certification Name> (<Vendor/Org>)"
labels: ["certification-proposal", "needs-research"]
body:
  - type: markdown
    attributes:
      value: Please propose high-yield industry certifications following repository rubrics.
  - type: input
    id: cert_name
    attributes:
      label: Certification Name
      description: Full name and exam code (e.g. CompTIA Security+ SY0-701).
    validations:
      required: true
  - type: input
    id: vendor
    attributes:
      label: Issuing Vendor / Organization
      description: Name of the vendor or accredited body.
    validations:
      required: true
  - type: dropdown
    id: category
    attributes:
      label: Certification Category
      options:
        - Cloud Computing
        - Cybersecurity
        - Networking
        - Artificial Intelligence & ML
        - Data Science
        - DevOps & Systems
        - Database
        - Academic (NPTEL/SWAYAM)
        - Management & Finance
    validations:
      required: true
  - type: input
    id: official_link
    attributes:
      label: Official Certification Page
      description: Hyperlink to official exam blueprint and page.
    validations:
      required: true
