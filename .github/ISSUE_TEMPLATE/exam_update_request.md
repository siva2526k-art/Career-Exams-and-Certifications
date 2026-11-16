name: Examination Information Update Request
description: Propose an update, correction, or new cycle data for an examination
title: "[EXAM UPDATE]: <Exam Name> (<Cycle Year>)"
labels: ["exam-update", "verification-needed"]
body:
  - type: markdown
    attributes:
      value: Thank you for helping keep the examination repository verified and up to date!
  - type: input
    id: exam_id
    attributes:
      label: Examination Identifier
      description: Enter the exam ID (e.g. UPSC_CSE, GATE_CS) or full exam name.
      placeholder: "e.g. GATE_CS"
    validations:
      required: true
  - type: textarea
    id: update_details
    attributes:
      label: Description of Changes
      description: Detail changes in dates, pattern, syllabus, eligibility, or cutoffs.
    validations:
      required: true
  - type: input
    id: official_source
    attributes:
      label: Official Source Link
      description: Provide the official gazette, notification PDF, or government portal URL.
      placeholder: "https://..."
    validations:
      required: true
