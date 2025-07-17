from datetime import date


class VehicleInfo:
    def __init__(self, category: str, brand: str, model: str, year_of_manufacturer: date):
        self.vehicle_type = category
        self.brand = brand
        self.model = model
        self.year_of_manufacturer = year_of_manufacturer
