# base class
class Company:
    """documentation: There are three types of access modifiers in Python.
    Public: accessible from anywhere
    Protected: accessible from same class and child class
    Private: accessible from only same class"""

    # constructor
    def __init__(self):
        # protected data members
        self._project = "NLP"


# child class
class Employee(Company):
    # constructor
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    # public instance methods
    def show(self):
        print("Employee name: ", self.name)
        # Accessing protected member in child class
        print("working on project: ", self._project)


# creating object of a class
c = Employee('Jessa')
c.show()

# direct access to protected data member
print('Project: ', c._project)
