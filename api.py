# api.py

from payments import process_payment, refund_payment
from models import Customer, Payment

# Fake "database"
CUSTOMERS = {
    1: Customer(id=1, email="alice@example.com", balance=100.00),
    2: Customer(id=2, email="bob@example.com", balance=50.00)
}

PAYMENTS = {}

def post_payment(data: dict):
    customer_id = data.get("customer")
    amount = data.get("amt")  # BUG: Wrong key name; should be "amount"
    customer = CUSTOMERS.get(customer_id)

    if not customer:
        return {"error": "Customer not found"}

    payment = process_payment(customer, amount)
    PAYMENTS[payment.id] = payment
    return {"id": payment.id, "status": payment.status}


def post_refund(data: dict):
    payment_id = data.get("id")
    payment = PAYMENTS.get(payment_id)

    if not payment:
        return {"error": "Payment not found"}

    # BUG: Customer ID mismatch logic
    customer = CUSTOMERS[payment.id]  # wrong key, should use payment.customer_id
    refund_payment(payment, customer)
    return {"id": payment.id, "status": payment.status}
