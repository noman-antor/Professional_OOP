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

    def total_costing(self, price):
        if self.days > 7:
            return f"{price*0.1} USD is applied for {self.vehicle.brand} {self.vehicle.model} {self.vehicle.vehicle_type} for {self.days} days rented by {self.customer_name}"
        else:
            return "No discount applied. Total {self.price}"