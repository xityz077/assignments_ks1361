# open file
search_name = input("Enter a name:").upper()
with open('census-first-names.txt', 'r') as in_file:

    line = in_file.readline()
    count = 1

    # looping until name is foundS
    for line in in_file:
        count += 1
        # print(line, end='')
        line = line.rstrip("\n")
        if line == search_name:
            print(line, " is the ", count, " ranked name")
            exit()

    print(f"{search_name} was not found in the list")
