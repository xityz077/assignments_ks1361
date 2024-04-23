# Base class
class Vehicle:
    def vehicle_info(self):
        print('This is Vehicle')


# Child
class Car(Vehicle):
    def car_info(self, name):
        print('Car name is ', name)


# Child
class Truck(Vehicle):
    def truck_info(self, name):
        print('Truck name is ', name)


# car object
obj1 = Car()
# access Vehicle info using car object
obj1.vehicle_info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.vehicle_info()
obj2.truck_info('Ford')
