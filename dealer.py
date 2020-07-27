import helper

class Dealer:
    def __init__(self, hand):
        self.hand = hand

    def hit(self, card):
        self.hand.append(card)

    def print_hand(self, hand):
        print('===============DEALER=================')
        helper.print_hand(hand)
