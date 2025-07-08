from license import License
from datetime import date
from dateutil.relativedelta import relativedelta


class Registrar:
    def __init__(self, car_manufacturer: str, year_of_manufacturer: date, license: License):
        
        self.car_manufacturer = car_manufacturer
        self.year_of_manufacturer = year_of_manufacturer
        self.license_no = license

    def validate_car(self):
        age = relativedelta(date.today(), self.year_of_manufacturer)
        if age.years > 20:
            raise ValueError("This car is not valid for registration.")

    def check_expiration(self):
        if self.license_no.expiration_date < date.today():
            return "License expired. Renewal required."
        remains = relativedelta(self.license_no.expiration_date, date.today())
        return {
            "car_owner": self.license_no.car_owner,
            "car_model": self.license_no.car_model,
            "car_manufacturer": self.car_manufacturer,
            "year_of_manufacturer": self.year_of_manufacturer,
            "registration_date": self.license_no.registration_date,
            "expiration_date_remains": f"{remains.days} days {remains.months} months {remains.years} years"
        }