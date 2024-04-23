class Student:
    def __init__(self, name, roll_no, age):
        self.name = name
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details', self.name, self.__roll_no)

    # getter method
    def get_roll_no(self):
        return self.__roll_no

    # Setter method
    def set_roll_no(self, number):
        if number > 50:
            print('Invalid roll no. Please set correct roll number')
        else:
            self.__roll_no = number


stud = Student("Jessa", 10, 15)

# before Modify
print("\nbefore Modify:")
stud.show()

# changing roll number using setter to 120
print("\nchanging roll number using setter to 120:")
stud.set_roll_no(120)
stud.show()

stud.set_roll_no(25)
print("\nchanging roll number using setter to 25:")
stud.show()
