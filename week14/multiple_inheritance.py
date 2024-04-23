class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name: ', name, 'Age: ', age)


class Company:
    def company_info(self, company_name, location):
        print('Inside Compnay class')
        print('Name: ', company_name, 'location: ', location)


class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary: ', salary, 'Skill: ', skill)


emp = Employee()

emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')
