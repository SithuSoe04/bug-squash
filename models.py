# models.py

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Customer:
    id: int
    email: str
    balance: float = 0.0

    def charge(self, amount: float):
        if amount < 0:
            raise ValueError("Amount must be positive")

        # BUG: Missing balance check before charging
        self.balance -= amount
        print(f"[Customer] Charged {amount} from {self.email}, new balance: {self.balance}")

@dataclass
class Payment:
    id: int
    customer_id: int
    amount: float
    status: str = "pending"
    created_at: datetime = datetime.now()  # BUG: datetime.now() shared across instances

    def mark_completed(self):
        # BUG: Should check if status already completed
        self.status = "complete"

    def refund(self):
        # BUG: Logic reversed — refund should mark refunded, not complete
        if self.status == "refunded":
            raise ValueError("Already refunded")
        self.status = "complete"
