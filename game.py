from dealer import Dealer
from player import Player
from deck import Deck 

def start_game():
    play_game = input('Would you like to play a game of Blackjack? ')
    if play_game == 'yes':
        deck = Deck()
        deck.shuffle_deck()
        player_intial_hand = [deck.deal_one_card(), deck.deal_one_card()]
        dealer_intial_hand = [deck.deal_one_card(), deck.deal_one_card()]
        player = Player(100, player_intial_hand)
        dealer = Dealer(dealer_intial_hand)

        while play_game == 'yes':
            chips = input('How many chips do you want to bet: ')
            while int(chips) > player.bankroll:
                print(f"You don't have sufficient funds! Your balance {player.bankroll}")
                chips = input('Please enter appropiate amount of chips: ')
            player.print_hand(player.hand)
            dealer.print_hand(dealer.hand)
            play_game = 'over'


if __name__ == '__main__':
    start_game()
