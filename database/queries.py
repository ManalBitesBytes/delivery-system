

# SQL queries for inserting data

INSERT_CUSTOMER = """
INSERT INTO customers (customer_id,first_name, last_name, phone, address)
VALUES (%s, %s, %s, %s, %s);
"""

INSERT_DRIVER = """
INSERT INTO drivers ( driver_id, first_name, last_name, phone, is_available)
VALUES (%s, %s, %s, %s, %s);
"""

INSERT_ORDER = """
INSERT INTO orders (order_id,  price, status, customer_id)
VALUES (%s, %s, %s, %s) RETURNING order_id;
"""

# SQL queries for selecting data
SELECT_CUSTOMER = """
SELECT * FROM customers WHERE customer_id = %s;
"""

SELECT_Driver = """
SELECT * FROM drivers WHERE driver_id = %s;
"""

SELECT_ORDER = """
SELECT * FROM orders WHERE order_id = %s;
"""

SELECT_AVAILABLE_DRIVERS = """
SELECT driver_id FROM drivers
where is_available = 1;
"""

UPDATE_AVILABILTY = """
        UPDATE drivers
        SET is_available = %s
        WHERE driver_id = %s;
            """

UPDATE_ORDER_STATUS = """
UPDATE orders SET status = %s WHERE order_id = %s;
"""


