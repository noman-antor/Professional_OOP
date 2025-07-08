from license import License
from datetime import date
from registrar import Registrar

try:
    license = License(
        owner_name="John Doe",
        car_model="Toyota Camry",
        license_number="ABC123",
        registration_date=date(2020, 1, 1),
        expiration_date=date(2025, 1, 1)
    )
    registrar = Registrar(
        car_manufacturer="Toyota",
        year_of_manufacturer=date(2022, 1, 1),
        license=license
    )
    registrar.validate_car()
    print(registrar.check_expiration())
except ValueError as e:
    print(f"Error: {e}")