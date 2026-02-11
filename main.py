import json
from pathlib import Path
from core.runner import run_for_user

USERS_DIR = Path("users")

for user_dir in USERS_DIR.iterdir():
    if user_dir.is_dir():
        print(f"\n👤 traitement {user_dir.name}")
        run_for_user(user_dir)