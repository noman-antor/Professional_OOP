from vehicleinfo import VehicleInfo


class Rent:
    _rent_price_bikes = 15
    _rent_price_cars = 50
    _rent_price_trucks = 100

    def __init__(self, vehicle: VehicleInfo, customer_name: str, days: int):
        self.vehicle = vehicle
        self.customer_name = customer_name
        self.days = days

    def _apply_discount(self, price, discount):
        return f"{price*discount} USD is applied for {self.vehicle.brand} {self.vehicle.model} {self.vehicle.vehicle_type} for {self.days} days rented by {self.customer_name}"