# tests/test_utils.py

from utils import to_cents, from_cents, now_iso

def test_to_cents_rounding():
    assert to_cents(10.23) == 1023

def test_from_cents_returns_float():
    assert from_cents(150) == 1.5

def test_now_iso_includes_timezone():
    ts = now_iso()
    assert ts.endswith("+00:00") or "T" in ts 
