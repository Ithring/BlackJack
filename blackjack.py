from deck import *
from hand import *
from chips import *
from extra_functions import  player_busts, player_wins, dealer_bust, dealer_wins, push
#take_bet, hit, hit_or_stand, show_all, show_some,













def main():
    global playing
    playing = True

    def take_bet(chips):
        while True:
            try:
                chips.bet = int(input("Please place your bet: "))
            except:
                print("Whoops, please enter an integer")
            else:
                if chips.bet > chips.total:
                    print("Sorry, you dont have enough chips! You have {} chips!".format(chips.total))
                else:
                    break

    def hit(deck,hand):
        hand.add_card(deck.deal())
        hand.check_aces()

    def hit_or_stand(deck, hand):
        global playing
    
        while True: 
            x = input("Hit or Stand? enter h or s: ").strip().lower()  # Trim any leading/trailing whitespace and convert to lowercase
            
            if x == 'h':
                hit(deck, hand)
            elif x == 's':
                print("Player stands, Dealers turn")
                playing = False
                
            else:
                print("Sorry, please enter h or s only")
                continue
            break


    def show_some(player,dealer):
        print("\n Dealer's hand: ")
        print("<First card hidden>")
        print(dealer.cards[1])
        
        print("\n Players hand:")
        for card in player.cards:
            print(card)
        
        
    def show_all(player,dealer):
        print("\n Dealer's hand: ",*dealer.cards,sep='\n')
        
        print(f"Total: {dealer.value}")
        
        print("\n Players hand:",*player.cards,sep='\n')
        
        print(f"Total: {player.value}")


    

        
    player_chips = Chips()
    print("WELCOME TO BLACKJACK!!\nGet as close as you can to 21 without going over. Dealer hits until their total is 17 or over & aces count as 11.")
    print(f"You have {player_chips.total} Chips, use them wisely!")
    
    while True:

        deck = Deck()
        deck.shuffle()

        dealer_hand = Hand()
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        
        take_bet(player_chips)

        show_some(player_hand,dealer_hand)

        while playing:
            hit_or_stand(deck, player_hand)

            show_some(player_hand,dealer_hand)
            

            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)
                break
        

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)
            
            show_all(player_hand,dealer_hand)

            if dealer_hand.value > 21:
                dealer_bust(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)
        print(f'You now have {player_chips.total} chips!')
        if player_chips.total <=0:
            print("Game over!")
            print("Thank you for playing!")
            playing = False
            break
        
        
        
        new_game = input("Would you like to play another hand? y/n ")
        if new_game.lower() == 'y':
            playing = True
            continue
        elif new_game.lower() == 'n':
            print("Thank you for playing!")
            playing = False
            break
    

        else:
            while new_game.lower() != 'y' and new_game.lower() != 'n':
                new_game = input("Whoops, plesae enter y or n: ")
                if new_game.lower() == 'y':
                    playing = True
                    continue
                elif new_game.lower() == 'n':
                    print("Thank you for playing!")
                    playing = False
                    break
                
            

           

            

        




    



if __name__ == '__main__':
    main()