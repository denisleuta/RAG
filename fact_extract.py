import re

def extract_number(text, keywords):
    for k in keywords:
        if k.lower() in text.lower():
            nums = re.findall(r"\d[\d,\.]*", text)
            if nums:
                return nums[0]
    return None

def boolean_mention(text, keywords):
    return any(k.lower() in text.lower() for k in keywords)
