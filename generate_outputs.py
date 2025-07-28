#!/usr/bin/env python3

import os
import json
from pathlib import Path
from pdf_extractor import PDFExtractor

def generate_outputs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")

    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_file in sorted(input_dir.glob("*.pdf")):
        output_file = output_dir / (pdf_file.stem + ".json")

        print(f"Processing {pdf_file.name}...")

        try:
            extractor = PDFExtractor(str(pdf_file))
            result = extractor.extract_data()
            extractor.close()

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=4, ensure_ascii=False)

            print(f"✓ Generated {output_file.name}")
            print(f"  Title: {result['title']}")
            print(f"  Headings: {len(result['outline'])}")
            print()

        except Exception as e:
            print(f"✗ Error processing {pdf_file.name}: {e}")
            print()

if __name__ == "__main__":
    generate_outputs()
