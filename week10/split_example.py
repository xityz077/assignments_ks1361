big_string = 'E295G Discovery Park'
tokens = big_string.split()
for s in tokens:
    print(s)

print("\n------------------------------------------\n")

big_string = 'E295G Discovery Park, E295H Discovery Park'
tokens = big_string.split(',')
for s in tokens:
    # Removes space
    print(s.strip())
