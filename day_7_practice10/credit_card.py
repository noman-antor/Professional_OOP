from datetime import date
from bankaccount import BankAccount


class CreditCard:
    def __init__(self, pin: int, card_number: int, card_type: str, card_holder: str, date_of_birth: date):
        self.date_of_birth = date_of_birth
        if date.today().year - self.date_of_birth.year < 18:
            raise ValueError("Cardholder must be at least 18 years old")

        self.__pin = pin
        self.__card_number = card_number
        self.card_type = card_type
        self.card_holder = card_holder
        self.__balance = 2000.0  # Initial balance
        self.expiry_date = date(2025, 12, 31)


