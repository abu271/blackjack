import helper

class Player:
    def __init__(self, bankroll, hand):
        self.bankroll = bankroll
        self.hand = hand
    
    def hit(self, card):
        self.hand.append(card)

    def update_bankroll(self, action, amount):
        if action == 'add':
            self.bankroll += amount
        if action == 'subtract':
            self.bankroll -= amount

    def print_hand(self, hand):
        print('===============PLAYER=================')
        helper.print_hand(hand)
    