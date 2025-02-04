from abc import ABC, abstractmethod
class Payment(ABC):

    def __init__(self,order, payment_method, payment_status = 'paid'):
        self.amount = order.price
        self.order_id = order.id
        self.payment_method = payment_method
        self.payment_status = payment_status


    @abstractmethod
    def pay(self):
        pass

