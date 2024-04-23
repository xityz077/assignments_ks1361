# Open the file
filename = input('Enter the filename: ')
in_file = open(filename, 'r')

# Prime the loop by reading the first line
line = in_file.readline()

# If the line exists, print it and read the next line.
while line != '':
    print(line, end='')
    line = in_file.readline()

# Close the file
in_file.close()
