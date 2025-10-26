# utils.py

import random
import time
from datetime import datetime, timezone

def to_cents(amount: float) -> int:
    # BUG: Floating point rounding error
    return int(amount * 100)

def from_cents(cents: int) -> float:
    return cents / 100.00

def now_iso() -> str:
    # BUG: Should use UTC, but missing tzinfo
    return datetime.now().isoformat()

def sleep_random():
    # BUG: Missing import of random.randint
    delay = random.randint(1, 3)
    print(f"Sleeping for {delay}s...")
    time.sleep(delay)
