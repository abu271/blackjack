from dealer import Dealer
from player import Player
from deck import Deck 
import helper

def start_game():
    play_game = input('Would you like to play a game of Blackjack? ')
    play_again = ''
    
    while play_game == 'yes':
        deck = Deck()
        deck.shuffle_deck()
        player_intial_hand = [deck.deal_one_card(), deck.deal_one_card()]
        dealer_intial_hand = [deck.deal_one_card(), deck.deal_one_card()]
        dealer = Dealer(dealer_intial_hand)
        dealer.hide_one_card()

        if play_again == 'yes':
            player = Player(player.bankroll, player_intial_hand)
            play_again = 'no'
        elif play_again == 'no':
            play_game = 'no'
            break
        else:
            player = Player(100, player_intial_hand)
           
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
                dealer.reveal_hidden_card()
                dealer.print_hand(dealer.hand)
                print('Game Over! Dealer Won!!!')
                player.update_bankroll('subtract', chips)
                play_again = input('Would you like to play again? ')
                break
            player_option = input('Hit or Stay: ')
        
        while player_option != 'hit':
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
                play_again = input('Would you like to play again? ')
                break
            else:
                dealer.reveal_hidden_card()
                dealer.print_hand(dealer.hand)
                print('Game Over! Dealer Won!!!')
                player.update_bankroll('subtract', chips)
                play_again = input('Would you like to play again? ')
                break

if __name__ == '__main__':
    start_game()
