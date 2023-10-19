import random

# Get a number from Player 1
player1_number = random.randint(0,100)
print("Welcome to the Number Guessing Game!")
print("Player 1 has chosen a number between 0 and 100.")

# Initialize Player 2's guess
player2_guess = None
attempts = 0

# Game loop
while player2_guess != player1_number:
    try:
        player2_guess = int(input("Player 2, guess the number: "))
        attempts += 1
        if player2_guess < player1_number:
            print("Too low!! Try again.")
        elif player2_guess > player1_number:
            print("Too high!, Try again.")
        else:
            print(f"Congratulations, Player 2! You guessed the number {player1_number} in {attempts}!")
            break
    except ValueError:
        print("Please enter a valid number between 0 and 100.")
