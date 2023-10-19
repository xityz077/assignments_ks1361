# open file
given_num = None

while given_num == None:
    try:
        given_num = int(input("Enter a name between 1 and 10:"))
        if given_num < 1:
            print(given_num, " is Too small? ")
        elif given_num > 10:
            print(given_num, " is Too big? ")
        else:
            print("you entered: ", given_num)
    except ValueError:
        print("Not an integer! Please try again.")
        given_num = None
print("Thanks for entering", given_num)
