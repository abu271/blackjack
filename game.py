from dealer import Dealer
from player import Player
from deck import Deck 
import helper

def start_game():
    play_game = input('Would you like to play a game of Blackjack? ')
    deck = Deck()
    deck.shuffle_deck()
    player_intial_hand = [deck.deal_one_card(), deck.deal_one_card()]
    dealer_intial_hand = [deck.deal_one_card(), deck.deal_one_card()]
    player = Player(100, player_intial_hand)
    dealer = Dealer(dealer_intial_hand)

    while play_game == 'yes':
        chips = int(input('How many chips do you want to bet: '))
        while chips > player.bankroll:
            print(f"You don't have sufficient funds! Your balance {player.bankroll}")
            chips = int(input('Please enter appropiate amount of chips: '))
        player.print_hand(player.hand)
        dealer.print_hand(dealer.hand)

        player_option = input('hit or stay: ')
        while player_option == 'hit':
            card = deck.deal_one_card()
            player.hit(card)
            player.print_hand(player.hand)
            dealer.print_hand(dealer.hand)
            player_sum = helper.sum_hand(player.hand)
            if player_sum > 21:
                print('Game Over! Dealer Won!!!')
                player.update_bankroll('subtract', chips)
                play_game = input('Would you like to play again? ')
                break
            else:
                player_option = input('Hit or Stay: ')
                break
        
        while player_option == 'stay':
            player_sum = helper.sum_hand(player.hand)
            dealer_sum = helper.sum_hand(dealer.hand)
            while dealer_sum <= 17:
                card = deck.deal_one_card()
                dealer.hit(card)
                player.print_hand(player.hand)
                dealer.print_hand(dealer.hand)
                dealer_sum = helper.sum_hand(dealer.hand)
                if player_sum > dealer_sum or dealer_sum > 21:
                    print('Game Over!! Player Won!!')
                    chips *= 2
                    player.update_bankroll('add', chips)
                else:
                    print('Game Over! Dealer Won!!!')
                    player.update_bankroll('subtract', chips)

            play_game = input('Would you like to play again? ')
            if play_game == 'yes':
                deck.shuffle_deck()
                player_intial_hand = [deck.deal_one_card(), deck.deal_one_card()]
                dealer_intial_hand = [deck.deal_one_card(), deck.deal_one_card()]
                player = Player(player.bankroll, player_intial_hand)
                dealer = Dealer(dealer_intial_hand)
            break

if __name__ == '__main__':
    start_game()
