class Student:
    """documentation: constructor in python"""

    # constructor
    # initialize instance variable
    def __init__(self, name):
        self.name = name
        print('All variables initialized')

    # instance Method
    def show(self):
        print('Hello, my name is ', self.name)


# create object using constructor
s1 = Student('Kumar')
s1.show()
