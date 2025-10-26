# tests/test_payments.py

from models import Customer
from payments import process_payment, refund_payment

def test_process_payment_completes():
    c = Customer(id=1, email="a@b.com", balance=100)
    p = process_payment(c, 20)
    assert p.status == "complete"

def test_balance_decreases_after_payment():
    c = Customer(id=2, email="b@c.com", balance=50)
    p = process_payment(c, 10)
    assert c.balance == 40  

def test_refund_restores_balance():
    c = Customer(id=3, email="x@y.com", balance=100)
    p = process_payment(c, 20)
    refund_payment(p, c)
    assert c.balance == 100  
