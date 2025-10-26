# main.py

from api import post_payment, post_refund

def simulate():
    print("=== Simulating Payment API ===")
    
    # BUG: Uses wrong key name
    res1 = post_payment({"customer": 1, "amount": 20.00})
    print("Payment Response:", res1)

    if "id" in res1:
        res2 = post_refund({"id": res1["id"]})
        print("Refund Response:", res2)

if __name__ == "__main__":
    simulate()
