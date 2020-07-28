def print_hand(hand):
    for card in hand:
        if not card.hidden:
            print(card)

def sum_hand(hand):
    values = [card.value for card in hand]
    return sum(values)
