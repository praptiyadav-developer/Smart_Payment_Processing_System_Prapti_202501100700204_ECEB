#Name - Prapti Yadav
#Roll No - 202501100700204
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        gateway_fee = 0.02 * amount
        gst = 0.18 * gateway_fee
        final_amount = amount + gateway_fee + gst
        
        print("Credit Card Payment")
        print(f"Original Amount: ₹{amount}")
        print(f"Gateway Fee (2%): ₹{gateway_fee}")
        print(f"GST on Fee (18%): ₹{gst}")
        print(f"Final Amount: ₹{final_amount}\n")

class UPIPayment(Payment):
    def pay(self, amount):
        cashback = 50 if amount > 1000 else 0
        final_amount = amount - cashback
        
        print("UPI Payment")
        print(f"Original Amount: ₹{amount}")
        print(f"Cashback: ₹{cashback}")
        print(f"Final Amount: ₹{final_amount}\n")

class PayPalPayment(Payment):
    def pay(self, amount):
        fee = 0.03 * amount
        conversion_fee = 20
        final_amount = amount + fee + conversion_fee
        
        print("PayPal Payment")
        print(f"Original Amount: ₹{amount}")
        print(f"International Fee (3%): ₹{fee}")
        print(f"Conversion Fee: ₹{conversion_fee}")
        print(f"Final Amount: ₹{final_amount}\n")

class WalletPayment(Payment):
    def __init__(self, balance):
        self.balance = balance
    
    def pay(self, amount):
        print("Wallet Payment")
        if amount > self.balance:
            print("Transaction Failed: Insufficient Balance\n")
        else:
            self.balance -= amount
            print(f"Payment Successful!")
            print(f"Amount Deducted: ₹{amount}")
            print(f"Remaining Balance: ₹{self.balance}\n")

def process_payment(payment, amount):
    payment.pay(amount)

cc = CreditCardPayment()
upi = UPIPayment()
paypal = PayPalPayment()
wallet = WalletPayment(1500)

process_payment(cc, 1000)
process_payment(upi, 1200)
process_payment(paypal, 2000)
process_payment(wallet, 500)
process_payment(wallet, 1200) 