class Card:

    values = {
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "jack": 10,
        "queen": 10,
        "king": 10,
        "ace": 11
    }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Card.values[rank]

    def __str__(self):
        return f"{self.rank.capitalize()} of {self.suit.capitalize()}"
