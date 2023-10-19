# open file
in_file = open('census-first-names.txt', 'r')

line = in_file.readline()
count = 1

# looping until name is found
for line in in_file:
    count += 1
    # print(line, end='')
    line = line.rstrip("\n")
    if line == "PATRICIA":
        print(line, " is the ", count, " ranked name")
        break


# close file
in_file.close()
