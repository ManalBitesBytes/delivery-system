from models.user import User
from models.order import Order
from database.db_connection import create_connection
from database.queries import  INSERT_CUSTOMER, SELECT_CUSTOMER

class Customer(User):
    def __init__(self,customer_id, first_name, last_name, phone, address):
        super().__init__( first_name, last_name, phone)
        self.address = address
        self.customer_id = customer_id
        self.save_to_db()

    def save_to_db(self):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(INSERT_CUSTOMER, (self.customer_id, self.first_name, self.last_name, self.phone, self.address))
                connection.commit()
                print(f"Customer {self.first_name} {self.last_name} with ID: {self.customer_id} saved to database.")
            except Exception as e:
                print(f"The error '{e}' occurred")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
    @staticmethod
    def place_order(order_id, price, customer_id):
        # Ensure that the customer ID exists before placing an order
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(SELECT_CUSTOMER, (customer_id,))
        customer_exists = cursor.fetchone()
        if customer_exists:
            order = Order(order_id, price, customer_id)
            print(f"Order {order_id} placed by {customer_exists[1]} {customer_exists[2]}")
            return order
        else:
            print(f"Customer with ID {customer_id} does not exist.")
            return None