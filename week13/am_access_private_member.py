class Employee:
    """documentation: There are three types of access modifiers in Python.
    Public: accessible from anywhere
    Protected: accessible from same class and child class
    Private: accessible from only same class"""

    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary


# creating object of a class
emp = Employee('Jessa', 10000)

# accessing private data members
print('Name: ', emp.name)
# direct access to private member using name mangling
print('Salary: ', emp._Employee__salary)
