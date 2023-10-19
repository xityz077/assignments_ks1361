# open file
# filename = input('Enter filename: ')
out_file = open('my_file1.txt', 'w')



# if line exists, print it and read next line
# while line != '':
#     count = count + 1
#     print(f"{line}".rstrip("\n"), " ", end=f"{count}"  "\n")
#     line = in_file.readline()


#
count = 1
house_value = 400000
for line in range(2):
    out_file.write("$\t" + format(house_value, '1,.2f') + "\n")
#     print(line, end='')

# close file
out_file.close()
