from datetime import date


class License:
    def __init__(self, owner_name: str, car_model: str, license_number: str, registration_date: date, expiration_date: date):
        self.car_owner = owner_name
        self.car_model = car_model
        self.__license_number = license_number
        self.registration_date = registration_date
        self.expiration_date = expiration_date
