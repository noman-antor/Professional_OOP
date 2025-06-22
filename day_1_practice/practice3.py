from pydantic import BaseModel
import pandas as pd
from typing import Optional


class Grocery(BaseModel):
    id: str
    quantity: int
    price: float
    total: Optional[float] = 0.0


class CheckoutManager:
    vat = 0.05
    total = 0.0
    net_total = 0.0
    groceries = []
    quantity = 0

    @classmethod
    def add_grocery(cls, grocery):
        cls.groceries.append(Grocery(
            id=grocery.id,
            quantity=grocery.quantity,
            price=grocery.price,
            total=grocery.quantity * grocery.price))

    @classmethod
    def calculate_total(cls):
        for grocery in cls.groceries:
            cls.total += grocery.total

    @classmethod
    def total_quantity(cls):
        cls.quantity = sum(grocery.quantity for grocery in cls.groceries)

    @classmethod
    def include_vat(cls):
        cls.vat = (cls.total * cls.vat)

    @classmethod
    def display_vouchar(cls):
        cls.net_total = cls.total - cls.vat
        print("Voucher:")
        print("ID\t\tQuantity\tPrice\tTotal")
        for grocery in cls.groceries:
            print(f"{grocery.id}\t{grocery.quantity}\t\t{grocery.price}\t{grocery.total:.2f}")
        print("-------------------------------------------------")
        print(f"Total\t\t{cls.quantity}\t\tGrand Total: {cls.total:.2f}")
        print(f"\t\t\t\tTotal (including VAT): {cls.vat:.2f}")
        print(f"\t\t\t\tNet Total: {cls.net_total:.2f}")

    @classmethod
    def check_duplicacy_error(cls):
        ids = [grocery.id for grocery in cls.groceries]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate IDs found in the grocery list. Please ensure all products are unique.")


file = pd.read_csv("files/groceryitems.csv")
for index, row in file.iterrows():
    CheckoutManager.add_grocery(Grocery(
        id=row['id'],
        quantity=row['quantity'],
        price=row['price']
    ))
    CheckoutManager.check_duplicacy_error()

CheckoutManager.total_quantity()
CheckoutManager.calculate_total()
CheckoutManager.include_vat()
CheckoutManager.display_vouchar()
