import random


# Define function "deal_card" to generate random card value
def deal_card():
    return random.randint(1, 10)


# Define function "get_score" to compute score and handle hits
def get_score(hand):
    score = 0
    for card in hand:
        score += card
    return score


# Define functions
def main():
    # Initialize variables
    player_score = 0
    dealer_score = 0
    player_hand = []
    dealer_hand = []

    # Deal two cards to player and dealer
    player_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    dealer_hand.append(deal_card())

    # Compute scores and ask player if they want to hit
    player_score = get_score(player_hand)
    dealer_score = get_score(dealer_hand)
    print(f"Your hand of two cards has a total value of {player_score}.")
    print("Would you like to take another card? (y/n)")

    # Loop until player decides to stay or busts
    while True:
        answer = input().lower()
        if answer == 'y':
            player_hand.append(deal_card())
            player_score = get_score(player_hand)
            # Check if player busted
            if player_score > 21:
                print(f"You BUSTED with a total value of {player_score}!")
                break
            else:
                print(f"Your hand now has a total value of {player_score}")
                print("Would you like to take another card? (y/n)")
        elif answer == 'n':
            print(f"Your have stopped taking more cards with a hand value of {player_score}.")
            break
        else:
            print("Error! Invalid input, please enter valid input i.e. (y/n)")

    # Deal cards to dealer until they have a hand value closest to 21
    while dealer_score < 21:
        dealer_hand.append(deal_card())
        dealer_score = get_score(dealer_hand)
    print(f"The dealer was dealt a hand with a value of {dealer_score}.")

    # Compare scores and determine winner
    if (21 < dealer_score) and (player_score <= 21):
        print("\n** You win! **\n")
    else:
        print("\n** You lose! **\n")

    # Ask player if they want to play again
    print("Would you like to play again? (y/n)")
    answer = input().lower()
    if answer == 'y':
        main()
    else:
        return


# Main function
main()
