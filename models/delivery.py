from models.order import Order
from models.driver import Driver
from database.db_connection import create_connection
from database.queries import SELECT_AVAILABLE_DRIVERS


class Delivery:
    def __init__(self):
        self.drivers = []

    def load_available_drivers(self):
        connection = create_connection()
        drivers = []
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(SELECT_AVAILABLE_DRIVERS)
                drivers = cursor.fetchall()
            except Exception as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
        return drivers

    def assign_order(self, order_id):
        order = Order.get_order_by_id(order_id)
        if order:
            available_drivers = self.load_available_drivers()
            if available_drivers:
                # Assign the first available driver
                driver_id = available_drivers[0][0]  # Assume driver_id is the first column in result
                order.driver_id = driver_id
                order.update_status(order_id, "Assigned")
                Driver.set_availability(driver_id, False)  # Mark the driver as unavailable
                print(f"Order {order_id} assigned to driver {driver_id}.")
            else:
                print(f"No available driver for order {order_id}. Please try again later.")

