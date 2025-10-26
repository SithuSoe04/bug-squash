# tests/test_api.py

from api import post_payment, post_refund

def test_post_payment_success():
    resp = post_payment({"customer": 1, "amount": 10})
    assert "status" in resp
    assert resp["status"] == "complete"

def test_post_payment_missing_customer():
    resp = post_payment({"customer": 999, "amount": 10})
    assert resp["error"] == "Customer not found"

def test_post_refund_success():
    payment_resp = post_payment({"customer": 1, "amount": 5})
    if "id" in payment_resp:
        refund_resp = post_refund({"id": payment_resp["id"]})
        assert refund_resp["status"] == "refunded"
