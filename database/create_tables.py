from db_connection import create_connection


def execute_query(query):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            print ('query executed successfully')
        except Exception as e:
            print (e)
        finally:
            cursor.close()
            conn.close()


# creating tables:

create_customers_table = """
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    address TEXT NOT NULL
);
"""

create_drivers_table = """
CREATE TABLE IF NOT EXISTS drivers (
    driver_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    is_available INT DEFAULT 1
);
"""

create_orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) CHECK (status IN ('pending','Payed', 'out for delivery', 'delivered')),
    customer_id INT REFERENCES customers(customer_id)
);
"""


if __name__ == "__main__":
    execute_query(create_customers_table)
    execute_query(create_drivers_table)
    execute_query(create_orders_table)

