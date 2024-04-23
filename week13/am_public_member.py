class Employee:
    """documentation: There are three types of access modifiers in Python.
    Public: accessible from anywhere
    Protected: accessible from same class and child class
    Private: accessible from only same class"""

    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.salary = salary

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary: ', self.salary)


# creating object of a class
emp = Employee('Jessa', 10000)

# accessing public data members
print("#" * 50)
print("accessing public data members:")
print("Name: ", emp.name, 'Salary: ', emp.salary)
print("#" * 50)

# calling public method of the class
print("#" * 50)
print("calling public method of the class:")
emp.show()
print("#" * 50)
