import random

def deal_card():
    return random.randint(1, 10)

def get_score(player_hand):
    score = 0
    for card in player_hand:
        score += card
    return score

def hit(player_hand):
    new_card = deal_card()
    player_hand.append(new_card)
    return get_score(player_hand)

def stay(player_hand):
    return get_score(player_hand)

def blackjack():
    player_hand = []
    dealer_hand = [deal_card(), deal_card()]
    print("Your hand:", player_hand)
    print("Dealer's up card:", dealer_hand[0])
    while True:
        player_decision = input("Do you want to hit or stay? ")
        if player_decision.lower() == 'hit':
            player_hand.append(deal_card())
            score = get_score(player_hand)
            print("Your hand:", player_hand)
            print("Your score:", score)
            if score > 21:
                print("You busted!")
                return
        elif player_decision.lower() == 'stay':
            score = get_score(player_hand)
            print("Your hand:", player_hand)
            print("Your score:", score)
            if score > dealer_hand[0]:
                print("You win!")
                return
            else:
                print("The dealer wins.")
                return
        else:
            print("Invalid input. Please enter 'hit' or 'stay'.")

blackjack()
