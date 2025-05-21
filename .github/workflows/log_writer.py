# log_writer.py
from datetime import datetime
import os

actor = os.getenv("GITHUB_ACTOR", "unknown")

with open("log.txt", "a") as f:
    f.write(f"✅ pushed by: {actor} at {datetime.now()}\n")

print("🔔 로그 기록 완료")
