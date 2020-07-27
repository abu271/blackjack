import random
from card import Card

class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = (
        'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace'
    )

    def __init__(self):
        self.all_cards = [
            Card(suit, rank) for rank in Deck.ranks for suit in Deck.suits
        ]

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        return self.all_cards.pop()
