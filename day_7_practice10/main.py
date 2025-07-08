from customer import Customer
from credit_card import CreditCard
from datetime import date
from bankaccount import BankAccount

try:
    customer_card = CreditCard(
        pin=1234,
        card_number=1234567890123456,
        card_type="Visa",
        card_holder="John Doe",
        date_of_birth=date(2000, 1, 1)
    )

    customer = Customer(
        customer_name="John Doe",
        address="123 Main St",
        phone="123-456-7890",
        card=customer_card
    )
    print("Customer created successfully.")

    customer.withdraw(pin=1234, amount=3000)
    print("Withdrawal successful. New balance:", customer.get_balance())

    customer.payment(pin=1234, amount=1000, to=BankAccount(
        account_number=987654321, account_holder="Jane Smith",
        routing_number=123456789, account_type="savings"))
    print("Payment successful. New balance:", customer.get_balance())
except ValueError as e:
    print(f"Error: {e}")