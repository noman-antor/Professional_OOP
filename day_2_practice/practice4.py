from pydantic import BaseModel
from typing import Optional


class MyAccount(BaseModel):
    account_number: int
    account_name: str
    balance: Optional[float]=0.0


class MyBank:

    @staticmethod
    def withdraw(account, amount: float):
        if amount > account.balance:
            raise ValueError("Insufficient funds")
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        account.balance -= amount
        return amount

    @staticmethod
    def deposit(account, amount: float):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        account.balance += amount
        return amount
    
    @staticmethod
    def transfer_funds(from_account, to_account, amount: float):
        if amount > from_account.balance:
            raise ValueError("Insufficient funds for transfer")
        from_account.balance -= amount
        to_account.balance += amount
        return amount


my_account = MyAccount(account_name="Antor", account_number=65874123)
to_account = MyAccount(account_name="John Doe", account_number=56893214)

try:
    amount = MyBank.deposit(my_account, 200000.0)
    print(f"Deposited {amount} to account {my_account.account_number}")
    print(f"Balance after deposit: {my_account.balance}")
    withdraw_amount = MyBank.withdraw(my_account, 2000.0)
    print(f"Withdrew {withdraw_amount} from account {my_account.account_number}")
    print(f"Balance after withdrawal: {my_account.balance}")
    amount = MyBank.transfer_funds(my_account, to_account, amount=500)
    print(f"Transferred {amount} from account {my_account.account_number} to account {to_account.account_number} \nYour new balance is {my_account.balance}")
except ValueError as e:
    print(f"Error: {e}")