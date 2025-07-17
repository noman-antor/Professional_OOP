from rent import Rent
from vehicleinfo import VehicleInfo
from datetime import date


class Bike(Rent):

    def __init__(self, vehicle: VehicleInfo, customer: str, days: int):
        if vehicle.vehicle_type != "bike":
            raise ValueError("Please give the valid vehicle type")
        super().__init__(vehicle, customer, days) 

    def get_rent_price(self):
        return self._rent_price_bikes * self.days

    def get_discount(self, price):
        if self.days > 7:
            return self._apply_discount(price, 0.1)
        else:
            return "No discount applied. Total {self.price}"

