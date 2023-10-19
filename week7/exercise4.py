# open file

while True:
    try:
        given_num = int(input("Enter a name between 1 and 10:"))
        if 1 <= given_num <= 10:
            print(given_num, " is Valid ")
        else:
            print(given_num, " is out of range (1-10). Try again.", )
    except Exception as err:
        if "bye" in str(err):
            print("Thanks for entering", given_num)
            exit()
        else:
            print("Not an integer! Please try again.")

