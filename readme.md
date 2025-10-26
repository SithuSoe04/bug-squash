# Stripe Bug Squash Interview Simulator 🐞

Welcome to your **bug squash practice project** — inspired by Stripe’s real engineering interview format.

In this exercise, you’ll debug and fix a minimal payment system.  
The codebase intentionally contains **realistic production-style bugs** across modules.

---

## 🧩 Goal

Your mission is to make **all tests pass** ✅ by identifying and fixing bugs in:

| File | Theme | Example Bug |
|------|--------|-------------|
| `models.py` | Data modeling | Mutable defaults, incorrect refund logic |
| `utils.py` | Helpers | Floating-point rounding, missing import |
| `payments.py` | Business logic | Missing balance checks, wrong state |
| `api.py` | Integration | Wrong key names, bad customer lookups |
| `main.py` | CLI integration | Incorrect payloads |

---

## 🧪 Running Tests

1. Install dependencies (just `pytest`):
   ```bash
   pip install pytest
