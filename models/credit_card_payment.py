from models.payment import Payment
class CreditCardPayment(Payment):
    def __init__(self,order,card_number, expiry_date, cvv):
        super().__init__(order, 'Credit Card')
        self.amount = order.price
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.__cvv = cvv

    def pay(self):

        print(f"Paid ${self.amount} using Credit Card with Number: {self.card_number} and Expiry Date: {self.expiry_date}")
