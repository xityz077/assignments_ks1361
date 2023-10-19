# open file
# filename = input('Enter filename: ')
in_file = open('census-first-names.txt', 'r')

# prime loop by reading first line
line = in_file.readline()
count = 0
# if line exists, print it and read next line
# while line != '':
#     count = count + 1
#     print(f"{line}".rstrip("\n"), " ", end=f"{count}"  "\n")
#     line = in_file.readline()


#
for line in in_file:
    print(line, end='')

# close file
in_file.close()
