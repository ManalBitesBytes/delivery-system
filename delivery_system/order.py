
from payment import Payment

class Order:
    def __init__(self, order_id, price, status : "pending"):
        self.order_id = order_id
        self.price = price
        self.status = status
    
        self.payment_method = None
        self.driver = None

    def update_status(self, status):
        self.status = status


    def set_payment_method(self, payment_strategy: Payment):

        self.payment_method = payment_strategy

    def process_payment(self):

        if self.payment_method:
            print(f"Processing payment for Order {self.order_id}...")
            self.payment_method.pay()
            self.update_status("Paid")
        else:
            print(f"No payment method set for Order {self.order_id}.")

    def complete_delivery(self):
        self.status = "Delivered"
        if self.driver:
            self.driver.remove_order(self)



