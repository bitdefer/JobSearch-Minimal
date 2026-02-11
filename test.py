import re
import csv
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Page recherche
    page.goto(
        "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=Analyste%20SOC&typesConvention=143684&typesConvention=143685&typesConvention=143686&typesConvention=143687&typesConvention=143706&page=0&lieux=596247&distance=15"
    )

    # Refuser les cookies si nécessaire
    try:
        page.get_by_role("button", name="Refuser tous les cookies").click()
    except:
        pass  # si pas de popup, continue

    # ---------------------
    # Récupération de tous les liens contenant SOC ou Analyste
    jobs = page.get_by_role("link", name=re.compile("SOC|Analyste", re.I))

    results = []
    base_url = "https://www.apec.fr"

    for i in range(jobs.count()):
        el = jobs.nth(i)
        title = el.inner_text()
        href = el.get_attribute("href")

        if href and href.startswith("/"):
            href = base_url + href

        results.append((title, href))
        print(title, href)  # debug rapide

    # ---------------------
    # Export CSV
    with open("soc_jobs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "link"])
        for row in results:
            writer.writerow(row)

    print(f"\n✅ {len(results)} jobs exportés dans soc_jobs.csv")

    # ---------------------
    context.close()
    browser.close()

# ---------------------
with sync_playwright() as playwright:
    run(playwright)
