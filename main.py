import json
from answer_engine import answer
from submission import build
from config import TEAM_EMAIL, SUBMISSION_NAME

questions = json.load(open("questions.json", "r", encoding="utf-8"))
answers = []

for q in questions:
    val, ctx = answer(q)
    answers.append(build(q, val, ctx))

submission = {
    "team_email": TEAM_EMAIL,
    "submission_name": SUBMISSION_NAME,
    "answers": answers
}

json.dump(submission, open("submission.json", "w", encoding="utf-8"), indent=2)
