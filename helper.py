def print_hand(hand):
    for card in hand:
        print(card)

def sum_hand(hand):
    values = [card.value for card in hand]
    return sum(values)
