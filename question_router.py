def expected_type(q):
    if "return False" in q:
        return "boolean"
    if "Which of the companies" in q:
        return "name"
    return "number"
