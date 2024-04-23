# Base class
class Vehicle:
    def vehicle_info(self):
        print('Inside Vehicle class')


# Child
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')


# Child
class Truck(Vehicle):
    def truck_info(self):
        print('Inside Truck class')


# Child
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print('Inside SportsCar class')


# car object
s_car = SportsCar()

# access Vehicle info using car object
s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()
