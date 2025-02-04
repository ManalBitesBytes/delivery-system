
from models.user import User
from database.db_connection import create_connection
from database.queries import INSERT_DRIVER, UPDATE_AVILABILTY

class Driver(User):
    def __init__(self, driver_id, first_name, last_name, phone):
        super().__init__(first_name, last_name, phone)
        self.driver_id = driver_id
        self.is_available = 1
        self.save_to_db()

    def save_to_db(self):
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(INSERT_DRIVER, (self.driver_id, self.first_name, self.last_name, self.phone, self.is_available))
                conn.commit()
                print(f"Driver {self.first_name} {self.last_name} with ID: {self.driver_id} saved to the database")
            except Exception as e:
                print(f"Error: {e}")
                conn.rollback()
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def set_availability(driver_id, available: bool):
        is_available = 1 if available else 0
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(UPDATE_AVILABILTY, (is_available, driver_id))
            connection.commit()
            print(f"Driver availability updated to {is_available}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
