from rent import Rent
from vehicleinfo import VehicleInfo
from datetime import date


class Truck(Rent):

    def __init__(self, vehicle: VehicleInfo, customer: str, days: int):
        if vehicle.vehicle_type != "truck" or days <=0 :
            raise ValueError("Unexpected Error Occured")
        super().__init__(vehicle, customer, days)

    def get_rent_price(self):
        return self._rent_price_trucks * self.days

    def total_costing(self, price):
        return f"{price +(100 * self.days)} USD is applied for {self.vehicle.brand} {self.vehicle.model} {self.vehicle.vehicle_type} for {self.days} days rented by {self.customer_name}"