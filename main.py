from models import *
from models.customer import Customer
from models.driver import Driver
from models.order import Order
from models.credit_card_payment import CreditCardPayment
from models.cash_payment import CashPayment
from models.delivery import Delivery
from database.db_connection import create_connection


delivery_system = Delivery()


def menu():

    while True:
        print("\nPlease pick what you want to do:")
        print("1. Add user (Customer/Driver)")
        print("2. Place order")
        print("3. Pay for order")
        print("4. Assign order to a driver")
        print("5. Show order info")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            user_type = input("Is the user a customer or a driver? ").lower()

            if user_type == 'customer':
                customer_id = input("Enter customer ID: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                phone = input("Enter phone number: ")
                address = input("Enter address for the customer: ")
                customer = Customer( customer_id, first_name, last_name, phone, address)
                if customer:
                    print(f"Customer {customer.first_name} {customer.last_name} added.")

            elif user_type == 'driver':
                driver_id = input("Enter driver ID: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                phone = input("Enter phone number: ")
                driver = Driver(driver_id, first_name, last_name, phone)
                if driver:
                    print(f"Driver {driver.first_name} {driver.last_name} added.")

            else:
                print("Invalid user type. Please choose either 'customer' or 'driver'.")

        elif choice == "2":
            customer_id = int(input("Enter customer ID: "))
            order_id = int(input("Enter order ID: "))
            price = float(input("Enter the order price: "))
            #customer = Customer(customer_id, "", "", "", "")
            order = Customer.place_order(order_id, price, customer_id)


        elif choice == "3":
            order_id = int(input("Enter order ID to pay for: "))
            order = Order.get_order_by_id(order_id)
            if order:
                payment_method = input("Enter payment method (CreditCard/Cash): ")

                if payment_method.lower() == "creditcard":
                    card_number = input("Enter card number: ")
                    expiry_date = input("Enter expiry date (MM/YY): ")
                    cvv = input("Enter CVV: ")
                    payment = CreditCardPayment(order, card_number, expiry_date, cvv)
                    payment.process_payment(payment)
                elif payment_method.lower() == "cash":
                    payment = CashPayment(order)
                    payment.process_payment(payment)
                else:
                    print("Invalid payment method. Please choose either 'CreditCard' or 'Cash'.")
            else:
                print(f"Order {order_id} not found.")

        elif choice == "4":
            order_id = int(input("Enter order ID to assign: "))
            order = Order.get_order_by_id(order_id)
            if order:
                delivery_system.assign_order(order_id)
            else:
                print(f"Order {order_id} not found.")

        elif choice == "5":
            order_id = int(input("Enter order ID to retrieve: "))
            order = Order.get_order_by_id(order_id)
            if order:
                print(f"Order ID: {order.order_id}")
                print(f"Price: ${order.price}")
                print(f"Status: {order.status}")
                print(f"Driver ID: {order.driver_id}")
            else:
                print(f"Order {order_id} not found.")

        elif choice == "6":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please select a valid option.")


if __name__ == "__main__":
    menu()
