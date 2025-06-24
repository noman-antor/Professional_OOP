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
        account.balance -= amount
        print(f"Withdrew {amount} from account {account.account_number}")
        return account.balance

    @staticmethod
    def deposit(account, amount: float):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        account.balance += amount
        print(f"Deposited {amount} to account {account.account_number}")
        return account.balance

    @staticmethod
    def transfer_funds(from_account, to_account, amount: float):
        if amount > from_account.balance:
            raise ValueError("Insufficient funds for transfer")
        from_account.balance -= amount
        to_account.balance += amount
        print(f"Transferred {amount} from account {from_account.account_number} to account {to_account.account_number} \nYour new balance is {from_account.balance}")


my_account = MyAccount(account_name="Antor", account_number=65874123)
to_account = MyAccount(account_name="John Doe", account_number=56893214)

try:
    balance = MyBank.deposit(my_account, 200000.0)
    print(f"Balance after deposit: {balance}")
    balance = MyBank.withdraw(my_account, 2000.0)
    print(f"Balance after withdrawal: {balance}")
    MyBank.transfer_funds(my_account, to_account, amount=500)
except ValueError as e:
    print(f"Error: {e}")