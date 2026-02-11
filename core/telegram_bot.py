import requests


def send_jobs(token, chat_id, jobs):
    for job in jobs:
        msg = f"📦 {job['title']}\n{job['url']}"

        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": msg
            },
            timeout=10
        )