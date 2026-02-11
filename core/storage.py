import json
from pathlib import Path


BASE = Path("data/users")


def load_user_config(username):
    with open(BASE / f"{username}.json") as f:
        return json.load(f)


def seen_file(username):
    return BASE / f"{username}_seen.json"


def filter_new_jobs(username, jobs):
    sf = seen_file(username)

    if sf.exists():
        seen = set(json.loads(sf.read_text()))
    else:
        seen = set()

    new = [j for j in jobs if j["url"] not in seen]
    return new


def save_seen(username, jobs):
    sf = seen_file(username)

    seen = {j["url"] for j in jobs}
    sf.write_text(json.dumps(list(seen)))