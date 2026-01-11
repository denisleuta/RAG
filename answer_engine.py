from retrieve import retrieve
from gigachat import ask
from prompts import STRICT_PROMPT
from config import GIGACHAT_TOKEN


def normalize_answer(ans, question, context):
    ans = ans.strip()

    # boolean
    if "true" in ans.lower():
        return True
    if "false" in ans.lower():
        return False

    # explicit N/A
    if ans.upper() in ["N/A", "NA", "NOT AVAILABLE"]:
        return "N/A"

    # защита от галлюцинаций
    if ans.lower() not in context.lower():
        if "return false" in question.lower():
            return False
        return "N/A"

    return ans


def answer(question):
    ctx_chunks = retrieve(question, top_k=5)

    if not ctx_chunks:
        return "N/A", []

    context = "\n\n".join(f"[Page {c['page']}]\n{c['text']}" for c in ctx_chunks)

    prompt = STRICT_PROMPT.format(context=context, question=question)

    try:
        raw = ask(prompt, GIGACHAT_TOKEN)
    except Exception:
        return "N/A", []

    value = normalize_answer(raw, question, context)

    return value, ctx_chunks
