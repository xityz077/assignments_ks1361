class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print(f"Details: {self.name}, {self.color}, {self.price}")

    def max_speed(self):
        print("Vehicle max speed is 150 mph")

    def change_gear(self):
        print("Vehicle change 6 gears")


# Inherit from Vehicle class
class Car(Vehicle):
    def max_speed(self):
        print("Car max speed is 250 mph")

    def change_gear(self):
        print("car changes 7 gears")


# Car Object
car = Car("Car1", "Red", "$40k")
car.show()
car.max_speed()
car.change_gear()
print(("#" * 9) * 3)
# Vehicle Object
vehicle = Vehicle("Vehicle1", "Mud_color", "$71K")
vehicle.show()
vehicle.max_speed()
vehicle.change_gear()
