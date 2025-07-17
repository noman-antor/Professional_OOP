from rent import Rent
from vehicleinfo import VehicleInfo
from datetime import date


class Car(Rent):

    def __init__(self, vehicle: VehicleInfo, customer: str, days: int):
        if vehicle.vehicle_type != "car":
            raise ValueError("Please give the valid vehicle type")
        super().__init__(vehicle, customer, days)

    def get_rent_price(self):
        return self._rent_price_cars * self.days

    def get_discount(self, price):
        if date.today().year - self.vehicle.year_of_manufacturer.year > 5:
            return self._apply_discount(price, 0.15)
        else:
            return "No discount applied. Total {price}"
