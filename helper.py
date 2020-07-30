def print_hand(hand):
    for card in hand:
        if not card.hidden:
            print(card)
        else:
            print('Hidden card')

def sum_hand(hand):
    values = [card.value for card in hand]
    return sum(values)

def print_ascii_art():
    print("\n" * 100)
    print("""\
888888b.   888                   888       d8b                   888      
888  "88b  888                   888       Y8P                   888      
888  .88P  888                   888                             888      
8888888K.  888  8888b.   .d8888b 888  888 8888  8888b.   .d8888b 888  888 
888  "Y88b 888     "88b d88P"    888 .88P "888     "88b d88P"    888 .88P 
888    888 888 .d888888 888      888888K   888 .d888888 888      888888K  
888   d88P 888 888  888 Y88b.    888 "88b  888 888  888 Y88b.    888 "88b 
8888888P"  888 "Y888888  "Y8888P 888  888  888 "Y888888  "Y8888P 888  888 
                                           888                            
                                          d88P                            
                                        888P" 
        """)
