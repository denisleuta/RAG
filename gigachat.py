import requests


def ask(prompt, token):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "GigaChat",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0
    }

    r = requests.post(url, headers=headers, json=payload, verify=False)

    data = r.json()

    if "choices" not in data:
        raise RuntimeError(f"GIGACHAT ERROR: {data}")

    return data["choices"][0]["message"]["content"]
