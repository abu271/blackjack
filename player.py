import helper

class Player:
    def __init__(self, bankroll, hand):
        self.bankroll = bankroll
        self.hand = hand
    
    def hit(self, card):
        print('Player chose hit')
        self.hand.append(card)

    def stay(self):
        print('Player chose stay') 

    def print_hand(self, hand):
        print('===============PLAYER=================')
        helper.print_hand(hand)
