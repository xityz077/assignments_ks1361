name_file = open('names.txt', 'r')
name_one = name_file.readline().rstrip()
name_two = name_file.readline().rstrip()
name_three = name_file.readline().rstrip()
name_file.close()

print(name_one)
print(name_two)
print(name_three)
