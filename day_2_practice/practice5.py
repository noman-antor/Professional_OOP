from datetime import date
from pydantic import BaseModel

class MyAccount(BaseModel):
    account_number: str
    account_name: str
    balance: float


class CreditCard:

    __secret_pin = None
    daily_limit = 100000
    maximum_limit = 500000

    __last_withdrawal_date = None

    @classmethod
    def set_daily_limit(cls):
        if date.today() != cls.__last_withdrawal_date:
            cls.daily_limit = 100000

    @classmethod
    def create_pin(cls, pin: int):
        if len(str(pin)) != 4:
            raise ValueError("PIN must be a 4-digit integer")
        cls.__secret_pin = pin
    
    @classmethod
    def withdraw(cls, my_account, amount: float, pin: int):

        if pin != CreditCard.__secret_pin:
            raise ValueError("Incorrect PIN")
        else:
            if amount > cls.maximum_limit:
                raise ValueError("Withdrawal limit exceeded: Maximum withdrawal is 500,000")
            
            if amount > my_account.balance:
                raise ValueError("Insufficient funds")
            
            if amount < 0:
                raise ValueError("Withdrawal amount must be positive")

            if amount > 20000:
                raise ValueError("Daily Withdrawal limit exceeded: Maximum withdrawal is 20,000")
        
            if date.today() != CreditCard.__last_withdrawal_date or date.today() == CreditCard.__last_withdrawal_date and CreditCard.daily_limit>= amount:
                CreditCard.__last_withdrawal_date = date.today()
                my_account.balance -= amount
                cls.daily_limit -= amount
                print(f"Withdrew {amount} from account {my_account.account_number} new balance is {my_account.balance}")
                
            else:
                raise ValueError("Daily withdrawal limit exceeded")

    @classmethod
    def payment(cls, my_account, amount: float):
        if amount > my_account.balance:
            raise ValueError("Insufficient funds for payment")

        if amount < 0:
            raise ValueError("Payment amount must be positive")

        if amount > cls.maximum_limit:
            raise ValueError("Payment limit exceeded: Maximum payment is 500,000")
        
        my_account.balance -= amount
        print(f"Payment of {amount} made from account {my_account.account_number} new balance is {my_account.balance}")


my_account = MyAccount(account_number="65874123", account_name="Antor", balance=500000.0)
if CreditCard._CreditCard__secret_pin is None:
    CreditCard.create_pin(1234)
CreditCard.set_daily_limit()
for _ in range(7):
    try:
        CreditCard.withdraw(my_account, amount=20000.0, pin=1234)
    except ValueError as e:
        print(f"Error: {e}")
    try:

        CreditCard.payment(my_account, amount=10000.0)
    except ValueError as e:
        print(f"Error: {e}")