# open file
# filename = input('Enter filename: ')
with open('census-first-names.txt') as in_file:

    # prime loop by reading first line
    line = in_file.readline()
    count = 0
    for line in in_file:
        print(line, end='')
# if line exists, print it and read next line
# while line != '':
#     count = count + 1
#     print(f"{line}".rstrip("\n"), " ", end=f"{count}"  "\n")
#     line = in_file.readline()



