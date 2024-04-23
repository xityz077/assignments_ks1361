class Employee:
    """documentation: encapsulation in python"""
    # constructor
    def __init__(self, name, salary, project):
        # class properties or, data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data number
        print("Name: ", self.name, 'Salary: ', self.salary)

    def work(self):
        print(self.name, ' is working on ', self.project)


# creating object of a class
emp = Employee('Kumar', 80000, 'NLP')

# calling public method of the class
emp.show()
emp.work()
