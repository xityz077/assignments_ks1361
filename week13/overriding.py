class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details: ', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150 mph')

    def change_gear(self):
        print('Vehicle changes 6 gears')


# Inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240 mph')

    def change_gear(self):
        print('Car change 7 gears')


# car object
car = Car('Car x1', 'Red', 20000)
car.show()

# calls method from car class
car.max_speed()
car.change_gear()

print("\n", ("# " * 25), "\n")

# vehicle object
vehicle = Vehicle('Truck x1', 'brown', 75000)
vehicle.show()

# calls method from vehicle class
vehicle.max_speed()
vehicle.change_gear()
