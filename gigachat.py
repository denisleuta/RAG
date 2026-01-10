import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


GIGACHAT_URL = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

def ask(prompt: str, token: str) -> str:
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "GigaChat",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.0
    }

    try:
        r = requests.post(
            GIGACHAT_URL,
            headers=headers,
            json=payload,
            timeout=30,
            verify=False
        )
    except Exception as e:
        print(f"[GIGACHAT ERROR] Request failed: {e}")
        return "N/A"

    try:
        data = r.json()
    except Exception:
        print("[GIGACHAT ERROR] Invalid JSON response")
        return "N/A"

    try:
        return (
            data["result"]["alternatives"][0]
            ["message"]["content"]
            .strip()
        )
    except KeyError:
        print("[GIGACHAT ERROR] Unexpected response format:")
        print(data)
        return "N/A"
