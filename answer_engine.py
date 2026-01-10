from retrieve import retrieve
from fact_extract import extract_number, boolean_mention
from gigachat import ask
from config import GIGACHAT_TOKEN, TOP_K

def answer(question):
    ctx = retrieve(question["text"], TOP_K)
    context_text = "\n".join(c["text"] for c in ctx)

    kind = question["kind"]

    if kind == "boolean":
        value = boolean_mention(
            context_text,
            ["merger", "acquisition", "dividend"]
        )
        return value, ctx

    if kind == "number":
        value = extract_number(
            context_text,
            ["employees", "assets", "revenue", "patents", "hotels"]
        )
        return value if value else "N/A", ctx

    if kind == "name":
        prompt = f"""
Answer strictly based on the context.
If the answer is not present, return N/A.

Context:
{context_text}

Question:
{question['text']}
"""
        value = ask(prompt, GIGACHAT_TOKEN)
        if not value:
            value = "N/A"
        return value, ctx

    return "N/A", ctx
