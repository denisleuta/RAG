import pdfplumber
import hashlib
import json
import os
import time

PDF_DIR = "data/pdfs"
OUT = "data/parsed_pages.json"

def parse_all():
    pages = []

    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]
    total_pdfs = len(pdf_files)

    total_pages = 0
    extracted_pages = 0

    print(f"[START] Found {total_pdfs} PDF files\n")

    for pdf_idx, file in enumerate(pdf_files, start=1):
        path = os.path.join(PDF_DIR, file)
        print(f"[PDF {pdf_idx}/{total_pdfs}] Parsing: {file}")

        with open(path, "rb") as f:
            sha1 = hashlib.sha1(f.read()).hexdigest()

        try:
            with pdfplumber.open(path) as pdf:
                num_pages = len(pdf.pages)
                print(f"  Pages: {num_pages}")

                for i, page in enumerate(pdf.pages, start=1):
                    total_pages += 1
                    if i % 5 == 0 or i == 1:
                        print(f"    Page {i}/{num_pages}")

                    try:
                        text = page.extract_text()
                    except Exception as e:
                        print(f"    [WARN] Page {i}: extract failed ({e})")
                        continue

                    if text and len(text.strip()) > 50:
                        extracted_pages += 1
                        pages.append({
                            "text": text,
                            "page": i - 1,
                            "pdf_sha1": sha1
                        })

        except Exception as e:
            print(f"[ERROR] Failed to parse {file}: {e}")

        print(f"[PDF {pdf_idx}] Done\n")
        time.sleep(0.1)

    print("=" * 50)
    print(f"[SUMMARY]")
    print(f"Total PDFs: {total_pdfs}")
    print(f"Total pages scanned: {total_pages}")
    print(f"Pages with extracted text: {extracted_pages}")

    if extracted_pages == 0:
        raise RuntimeError(
            "NO TEXT EXTRACTED FROM PDFs. PDFs are likely scanned. OCR required."
        )

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(pages, f, ensure_ascii=False, indent=2)

    print(f"[DONE] Saved parsed pages to {OUT}")

if __name__ == "__main__":
    parse_all()
