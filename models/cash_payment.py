from models.payment import Payment

class CashPayment(Payment):
    def __init__(self, order):
        super().__init__(order)
        self.amount = order.price
    def pay(self):
        print(f"Paid ${self.amount} on Cash on Delivery.")
