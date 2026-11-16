name: Bug Report / Inaccurate Data
description: Report inaccurate cutoffs, dead links, or schema validation failures
title: "[DATA BUG]: <Summary of inaccurate record>"
labels: ["bug", "data-integrity"]
body:
  - type: textarea
    id: bug_desc
    attributes:
      label: Description of Issue
      description: Point out the exact file, line number, or JSON record with inaccurate data.
    validations:
      required: true
  - type: input
    id: correct_info
    attributes:
      label: Correct Official Information
      description: What should the record state according to official notifications?
    validations:
      required: true
