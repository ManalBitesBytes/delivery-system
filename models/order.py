from database.db_connection import create_connection
from database.queries import INSERT_ORDER, SELECT_ORDER, UPDATE_ORDER_STATUS
from models.payment import Payment

class Order:
        def __init__(self, order_id, price, customer_id):
            self.order_id = order_id
            self.price = price
            self.status ="pending"
            self.customer_id = customer_id
            self.payment_method = None
            self.save_to_db()

        def save_to_db(self):
            connection = create_connection()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(INSERT_ORDER, (self.order_id, self.price, self.status, self.customer_id))
                    connection.commit()
                    print(f"Order {self.order_id} saved to database with status '{self.status}'.")
                except Exception as e:
                    print(f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()

        @staticmethod
        def update_status(order_id, new_status):
            connection = create_connection()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(UPDATE_ORDER_STATUS, (new_status, order_id))
                    connection.commit()
                    print(f"Order {order_id} status updated to '{new_status}'.")
                except Exception as e:
                    print(f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()

        @staticmethod
        def get_order_by_id(order_id):
            connection = create_connection()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(SELECT_ORDER, (order_id,))
                    order = cursor.fetchone()
                    if order:
                        return Order(order[0], order[1], order[2], order[3])
                    else:
                        print(f"Order with ID {order_id} not found.")
                        return None
                except Exception as e:
                    print(f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()

        def process_payment(self, payment_method):
            self.payment_method = payment_method
            if self.payment_method:
                print(f"Processing payment for Order {self.order_id}...")
                self.payment_method.pay()
                self.update_status(self.order_id, "Paid")
                print("Payment completed.")

        def complete_delivery(self):
            self.update_status(self.order_id, "Delivered")




