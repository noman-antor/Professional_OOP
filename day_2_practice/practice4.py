from pydantic import BaseModel


class MyAccount(BaseModel):
    account_number: int
    account_name: str
    balance: float


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
    def transfer_funds(from_account, amount: float, to_account: int):
        if amount > from_account.balance:
            raise ValueError("Insufficient funds for transfer")
        from_account.balance -= amount
        print(f"Transferred {amount} from account {from_account.account_number} to account {to_account} \nYour new balance is {from_account.balance}")


my_account = MyAccount(account_name="Antor", account_number=65874123, balance=60000000)

try:
    balance = MyBank.withdraw(my_account, 2000.0)
    print(f"Balance after withdrawal: {balance}")
    balance = MyBank.deposit(my_account, 200.0)
    print(f"Balance after deposit: {balance}")
    MyBank.transfer_funds(my_account, amount=500, to_account=56893214)
except ValueError as e:
    print(f"Error: {e}")