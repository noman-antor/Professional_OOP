from car import Car
from bike import Bike
from truck import Truck
from vehicleinfo import VehicleInfo
from datetime import date

try:
    car = VehicleInfo(category="car", brand="nissan", model="gtr", year_of_manufacturer=date(2014, 5, 6))
    bike = VehicleInfo(category="bike", brand="Hero Honda", model="Glammour", year_of_manufacturer=date(2004, 1, 1))
    truck = VehicleInfo(category="truck", brand="TATA", model="1613", year_of_manufacturer=date(2012, 4, 4))
    
    bike1 = Bike(vehicle=bike, customer="Rahman", days=8)
    price = bike1.get_rent_price()
    print(bike1.total_costing(price))

    car1 = Car(vehicle=car, customer="Zaman", days=2)
    price = car1.get_rent_price()
    print(car1.total_costing(price))

    truck1 = Truck(vehicle=truck, customer="Adam", days=5)
    price = truck1.get_rent_price()
    print(truck1.total_costing(price))


except Exception as e:
    print(e)