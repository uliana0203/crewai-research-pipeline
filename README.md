# CrewAI Research Pipeline

This repository contains an automated research pipeline built with **CrewAI** for generating structured scientific manuscripts from data-driven analysis.

The project demonstrates how multi-agent orchestration can be used to organize complex analytical workflows, coordinate research tasks, and produce reproducible research artifacts, including a complete manuscript and document exports.

---

## Prerequisites

Before running the pipeline, ensure the following are installed:

- **Python 3.10 or newer**
- **Pandoc** (required for document conversion)
  - Download from: https://pandoc.org/installing.html

> ⚠️ Pandoc must be installed system-wide and available in your PATH.  
> `pypandoc` is only a Python wrapper and does **not** include Pandoc itself.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/uliana0203/crewai-research-pipeline.git
cd crewai-research-pipeline
```

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

3. Install Python dependencies:

```bash
pip install -r requirements.txt
```

This will install CrewAI, `pypandoc`, and all required Python packages.

---

## Overview

The pipeline coordinates multiple specialized agents to perform sequential research tasks:

- Literature review and contextualization
- Methodology specification
- Data analysis and validation
- Results and discussion drafting
- Ethics and integrity checks
- Internal peer-review simulation
- Assembly of a complete manuscript
- Conversion of Markdown outputs into DOCX using Pandoc

All intermediate and final artifacts are preserved in the `outputs/` directory.

---

## Repository Structure

```text
.
├── data/
│   └── WHO-COVID-19-global-daily-data.csv
│
├── src/
│   └── research_team/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── tools/
│       │   └── export_doc.py
│       ├── crew.py
│       └── main.py
│
├── outputs/
│   ├── 00_manuscript.md
│   ├── 00_manuscript.docx
│   ├── 01_outline.md
│   ├── 02_literature_review.md
│   ├── 03_methodology.md
│   ├── 04_data_analysis.md
│   ├── 05_results_discussion.md
│   ├── 06_edited_manuscript.md
│   ├── 07_references.md
│   ├── 08_ethics_checklist.md
│   ├── 09_peer_review.md
│   ├── 10_submission_checklist.md
│   └── 11_cover_letter.md
│
├── requirements.txt
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Running the Pipeline

### Using CrewAI CLI (recommended)

```bash
crewai run
```

This executes the full research workflow and generates all intermediate and final artifacts.

---

### Direct execution

```bash
python src/research_team/main.py
```

---

## Data

The `data/` directory contains the dataset used by the pipeline:

- `WHO-COVID-19-global-daily-data.csv` — publicly available daily global COVID-19 statistics provided by the World Health Organization (WHO).

---

## Outputs

The `outputs/` directory is intentionally committed to the repository.  
It contains all generated research artifacts, including intermediate stages and the final manuscript in both Markdown and DOCX formats.

---

## Notes and Limitations

- The pipeline is research-oriented and exploratory by design
- Generated content may require human review before real-world use
- PDF export is not enabled by default and may require additional LaTeX tooling

---

## License

This repository is provided for research, demonstration, and educational purposes.
