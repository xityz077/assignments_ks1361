import random

print("Welcome to the dice rolling Game!")


#
def roll_dices():
    return random.randint(1, 6)


def simulate_rolls():
    last_roll = None
    attempts = 0

    # Game loop
    while True:
        attempts += 1
        print(f"This is your attempt: {attempts}")
        roll1 = roll_dices()
        roll2 = roll_dices()
        total = roll1 + roll2
        print(f"You rolled a {roll1} and {roll2} = {total}")

        if total == last_roll:
            print(f"Congratulations, It took {attempts} rolls to get same value two times in a row")
            break
        last_roll = total


simulate_rolls()
