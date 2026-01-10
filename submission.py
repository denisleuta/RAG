def build(q, value, ctx):
    refs = []
    if value not in ["N/A", False]:
        c = ctx[0]
        refs.append({
            "pdf_sha1": c["pdf_sha1"],
            "page_index": c["page"]
        })

    return {
        "question_text": q["text"],
        "value": value,
        "references": refs
    }
