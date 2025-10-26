# payments.py

from models import Customer, Payment
from utils import to_cents, now_iso

def process_payment(customer: Customer, amount: float) -> Payment:
    print(f"[Payment] Processing {amount} for {customer.email}")

    payment = Payment(
        id=hash(customer.email + now_iso()),
        customer_id=customer.id,
        amount=amount,
    )

    try:
        customer.charge(amount)
        payment.mark_completed()
    except Exception as e:
        payment.status = "failed"
        print(f"[Payment] Failed: {e}")

    return payment


def refund_payment(payment: Payment, customer: Customer):
    print(f"[Payment] Refunding payment {payment.id}")

    payment.refund()
    print(f"Refunded {payment.amount} to customer {customer.email}")
