#!/usr/bin/env python
import warnings
import os
from datetime import datetime

from research_team.crew import ScientificPaperProject  
from research_team.tools.export_doc import build_doc


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

OUT_DIR = "outputs"
os.makedirs(OUT_DIR, exist_ok=True)

topic = "AI-driven forecasting of COVID-19 cases"
dataset_path = "./data"
target_journal = "IEEE Access"
style = "IEEE"
keywords = "time series, forecasting, AI, epidemiology, machine learning, COVID-19"
ethics_note = "No human subjects. Publicly available datasets. No conflicts of interest."

def run() -> None:
    inputs = {
        "topic": topic,
        "dataset_path": dataset_path,
        "target_journal": target_journal,
        "style": style,
        "keywords": keywords,
        "ethics_note": ethics_note,
        "timestamp": datetime.now().isoformat(),
    }

    result = ScientificPaperProject().crew().kickoff(inputs=inputs)

    try:
        build_doc()
    except Exception as e:
        print(f"[WARNING] DOCX was not generated: {e}")

    print(f"ScientificPaperProject finished. Check files in '{OUT_DIR}/'.")


if __name__ == "__main__":
    run()
