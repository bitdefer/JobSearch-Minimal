from core.scraper_demo import scrape_jobs
from core.telegram_bot import send_jobs
from core.storage import load_user_config, filter_new_jobs, save_seen


def run_for_user(username: str):
    print(f"🚀 Run for user: {username}")

    config = load_user_config(username)

    jobs = scrape_jobs(config["keywords"], config["location"])

    new_jobs = filter_new_jobs(username, jobs)

    if not new_jobs:
        print("Aucune nouvelle offre")
        return

    send_jobs(config["telegram_token"], config["chat_id"], new_jobs)

    save_seen(username, new_jobs)

    print(f"✅ {len(new_jobs)} offres envoyées")