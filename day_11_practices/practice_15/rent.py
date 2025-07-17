from vehicleinfo import VehicleInfo


class Rent:
    _rent_price_bikes = 15
    _rent_price_cars = 50
    _rent_price_trucks = 100

    def __init__(self, vehicle: VehicleInfo, customer_name: str, days: int):
        self.vehicle = vehicle
        self.customer_name = customer_name
        self.days = days

    def get_rent_price(self):
        if self.vehicle.vehicle_type == "bike":
            return "Bikes have $15 per day"
        if self.vehicle.vehicle_type == "car":
            return "Cars have $50 per day"
        if self.vehicle.vehicle_type == "truck":
            return "Trucks have $100 per day"

    def total_costing(self, price):
        if self.vehicle.vehicle_type == "bike":
            return "Bikes have $15 per day with (15%) discount for more than 7 days rental period"
        if self.vehicle.vehicle_type == "car":
            return "Cars have $50 per day with (10%) discount for older than 5 years"
        if self.vehicle.vehicle_type == "truck":
            return "Trucks have $100 per day with an additional fee $100 per day for maintenance"