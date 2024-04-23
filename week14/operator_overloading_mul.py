class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        print(f"worked for {other.days} days")
        return self.salary * other.days


class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days


emp = Employee("Jessa", 100)
timesheet = TimeSheet("Jessa", 10)
print(f"salary is {emp * timesheet}")
