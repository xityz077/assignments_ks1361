import random

print("Welcome to the card drawing Game!")

def draw_card():
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King']
    suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

    value = random.choice(values)
    suit = random.choice(suits)

    return f'{value} of {suit}'


def simulate_cards():
    last_draw = None
    attempts = 0

    # Game loop
    while True:
        attempts += 1
        print(f"This is your attempt: {attempts}")
        card = draw_card()
        print(f'You got the {card}')

        if card == last_draw:
            print(f"Congratulations, It took {attempts} draw to get same card two times in a row")
            break
        last_draw = card


simulate_cards()
