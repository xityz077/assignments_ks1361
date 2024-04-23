all_students = {}

# Get as many students as the user wants to enter,
# Store each in "students" EUID as key.

student_name = {}
start = 'y'
while start == 'y':
    student_name = input('Enter student name: ')
    one_student = {'name': student_name}
    euid = input('Enter EUID: ')
    one_student['EUID'] = euid
    email = input('Enter email: ')
    one_student['email'] = email

    # Store this "one_student" in the all students dictionary
    all_students[euid] = one_student
    print(all_students)
    start = input("Do you want to continue: (y/n)").lower()

# How many things do we know about given dictionary
key_count = len(all_students)
print(f"key_count of 'all_students': {key_count}")

# Look for a student_name with EUID 'ks1361'
if 'ks1361' in all_students:
    print(all_students['ks1361']['name'])

for key in all_students:
    print(key)
    print(all_students[key])
print('---------------------------')
print("all_students.get(euid): ", all_students.get(euid))
print("all_students.get(euid, 0))", all_students.get(euid, 0))
print("all_students.get(euid, 1))", all_students.get(euid, 1))
print("all_students.get(euid, None))", all_students.get(euid, None))
print("all_students.get(euid, 'Huh?'))", all_students.get(euid, 'Huh?'))
all_students.clear()
print("all_students.get(euid) after CLEAR: ", all_students.get(euid))
