import pypandoc
from pathlib import Path


def build_doc():
    input_md = Path("outputs/00_manuscript.md")
    output_docx = Path("outputs/00_manuscript.docx")

    if not input_md.exists():
        raise FileNotFoundError(f"{input_md} not found")

    print("Building DOCX via Pandoc...")

    pypandoc.convert_file(input_md, 'docx', outputfile=output_docx)

    print(f"DOCX created: {output_docx.resolve()}")



