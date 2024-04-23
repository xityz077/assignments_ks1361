import random

# Pick 6
answer = 'y'
while answer == 'y':
    # Initialize set_user and set_computer
    set_user = set()
    set_computer = set()

    # User picks 6 digits from 0 to 99
    while len(set_user) < 6:
        try:
            user_input = int(input("Enter unique number from 0 to 99: "))
            if user_input in set_user:
                print("Number already exist in set. Please enter unique number")
            else:
                set_user.add(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Computer randomly picks 6 unique numbers from 0 to 99
    def random_pick():
        return random.randint(0, 99)

    while len(set_computer) < 6:
        set_computer.add(random_pick())

    print(set_computer)

    # Determine how many numbers are in common for both user and computer
    common_set = set_user.intersection(set_computer)
    print(f"There are {len(common_set)} number/s common. They are {common_set}")
    print("Given university is not found!")
    answer = input("continue...(y/n)?").lower()
print("Thank you for playing.")
