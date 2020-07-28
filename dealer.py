import helper

class Dealer:
    def __init__(self, hand):
        self.hand = hand

    def hit(self, card):
        self.hand.append(card)

    def print_hand(self, hand):
        print('===============DEALER=================')
        helper.print_hand(hand)
    
    def hide_one_card(self):
        self.hand[0].hidden = True
    
    def reveal_hidden_card(self):
        self.hand[0].hidden = False
