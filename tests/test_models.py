# tests/test_models.py

import pytest
from models import Customer, Payment
from datetime import datetime

def test_customer_charge_reduces_balance():
    c = Customer(id=1, email="test@example.com", balance=100)
    c.charge(20)
    assert c.balance == 80  

def test_payment_datetime_is_unique():
    p1 = Payment(id=1, customer_id=1, amount=10)
    p2 = Payment(id=2, customer_id=1, amount=10)
    assert p1.created_at != p2.created_at

def test_refund_changes_status():
    p = Payment(id=1, customer_id=1, amount=10)
    p.refund()
    assert p.status == "refunded" 
