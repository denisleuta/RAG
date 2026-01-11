import json
from answer_engine import answer

questions = json.load(open("questions.json", encoding="utf-8"))

answers = []

for q in questions:
    val, ctx = answer(q["text"])

    answers.append({
        "question_text": q["text"],
        "value": val,
        "references": [
            {
                "pdf_sha1": c["pdf_sha1"],
                "page_index": c["page_index"]
            } for c in ctx
        ]
    })

submission = {
    "team_email": "mashatrunina2508@gmail.com",
    "submission_name": "rag_gigachat_strict_v1",
    "answers": answers
}

with open("submission.json", "w", encoding="utf-8") as f:
    json.dump(submission, f, ensure_ascii=False, indent=2)
