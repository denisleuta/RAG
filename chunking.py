import json

IN = "data/parsed_pages.json"
OUT = "data/chunks.json"

CHUNK_SIZE = 400
OVERLAP = 100


def chunk():
    pages = json.load(open(IN, encoding="utf-8"))
    chunks = []

    total_pages = len(pages)
    print(f"[START] Chunking {total_pages} pages")

    for idx, p in enumerate(pages, start=1):
        if idx % 100 == 0 or idx == 1:
            print(f"  Processing page {idx}/{total_pages}")

        words = p["text"].split()
        step = CHUNK_SIZE - OVERLAP

        for i in range(0, len(words), step):
            chunk = " ".join(words[i : i + CHUNK_SIZE])
            if len(chunk.strip()) < 50:
                continue

            chunks.append(
                {
                    "text": chunk,
                    "page_index": p["page_index"],
                    "pdf_sha1": p["pdf_sha1"],
                }
            )

    print(f"[DONE] Created {len(chunks)} chunks")

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    chunk()
