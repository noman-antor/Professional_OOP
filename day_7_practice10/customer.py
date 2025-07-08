from credit_card import CreditCard
from bankaccount import BankAccount
from datetime import date


class Customer:

    def __init__(self, customer_name: str, address: str, phone: str, card: CreditCard):
        self.customer_name = customer_name
        self.address = address
        self.phone = phone
        self.card = card

    def expiration(self):
        if self.card.expiry_date < date.today():
            raise ValueError("Card has expired")
        return self.card.expiry_date

    def get_balance(self):
        return f"your current balance limit : {self.card._CreditCard__balance}"

    def withdraw(self, pin: int, amount: float):
        if self.card._CreditCard__pin != pin:
            raise ValueError("Invalid PIN")
        else:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            if amount > self.card._CreditCard__balance:
                raise ValueError("Insufficient balance")
            self.card._CreditCard__balance -= amount

    def payment(self, pin: int, amount: float, to: BankAccount):
        if self.card._CreditCard__pin != pin:
            raise ValueError("Invalid PIN") 
        else:
            if amount <= 0:
                raise ValueError("Purchase amount must be positive")
            if amount > self.card._CreditCard__balance:
                raise ValueError("Insufficient balance")
            self.card._CreditCard__balance -= amount
            try:
                to.deposit(amount)
            except ValueError as e:
                self.card._CreditCard.__balance += amount
                raise e