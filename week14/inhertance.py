"""

class BaseClass:
    Body of base class
class DerivedClass(BaseClass)
    Body of derived class

    """


# Base class
class Vehicle:
    def vehicle_info(self):
        print('Inside Vehicle class')

# Child
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')


# car object
car = Car()

# access Vechile info using car object
car.vehicle_info()
car.car_info()
