import requests
from bs4 import BeautifulSoup


def scrape_jobs(keywords, location):
    print("🔍 Scraping demo site")

    url = "https://example.com/jobs"

    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    results = []

    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        href = a.get("href")

        if not text or not href:
            continue

        if any(k.lower() in text.lower() for k in keywords):
            results.append({
                "title": text,
                "url": href
            })

    return results