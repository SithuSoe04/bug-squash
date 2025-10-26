# utils.py

import random
import time
from datetime import datetime, timezone

def to_cents(amount: float) -> int:
    return int(amount * 100)

def from_cents(cents: int) -> float:
    return cents / 100.00

def now_iso() -> str:
    return datetime.now().isoformat()

def sleep_random():
    delay = random.randint(1, 3)
    print(f"Sleeping for {delay}s...")
    time.sleep(delay)
