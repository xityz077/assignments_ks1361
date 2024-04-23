class Employee:
    """documentation: There are three types of access modifiers in Python.
    Public: accessible from anywhere
    Protected: accessible from same class and child class
    Private: accessible from only same class"""

    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary: ', self.__salary)


# creating object of a class
emp = Employee('Jessa', 10000)

# accessing private data members
emp.show()
