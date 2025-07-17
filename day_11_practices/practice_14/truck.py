from rent import Rent
from vehicleinfo import VehicleInfo
from datetime import date


class Truck(Rent):

    def __init__(self, vehicle: VehicleInfo, customer: str, days: int):
        if vehicle.vehicle_type != "truck":
            raise ValueError("Please give the valid vehicle type")
        super().__init__(vehicle, customer, days)

    def get_rent_price(self):
        return self._rent_price_trucks * self.days

    def maintenance_cost(self, price):
        return f"{price + (100 * self.days)} tk maintenance cost for {self.days} days"

