## Abstraction (Using Abstract Base Class)
from abc import ABC, abstractmethod
class Payment(ABC):
        @abstractmethod
        def payment_process(self, amount):
            pass
        

class CreditCardPayment(Payment):
    def payment_process(self, amount):
        print(f"Payment of rs {amount} made using Credit Card")

class UpiPayment(Payment):
    def payment_process(self, amount):
        print(f"Payment of rs{amount} made using UPI")        
        

credit = CreditCardPayment()
credit.payment_process(2000)

upi = UpiPayment()
upi.payment_process(500)


