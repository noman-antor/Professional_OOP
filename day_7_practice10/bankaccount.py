from pydantic import BaseModel, PrivateAttr


class BankAccount(BaseModel):
    account_number: int
    account_holder: str
    routing_number: int
    account_type: str

    __balance: float = PrivateAttr(default=10000.0)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance
