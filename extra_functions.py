
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Please enter your bet: "))
        except TypeError:
            print("Whoops, please enter an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you dont have enough chips! You have {} chips!".format(chips.total))
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.check_aces()

def hit_or_stand(deck,hand):
    global playing
    
    while True: 
        x = input("Hit or Stand? enter h or s: ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player stands, Dealers turn")
            playing = False
            break
        else:
            print("Sorry, please enter h or s only")
            continue
        break

def show_some(player,dealer):
    print("\n Dealer's hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    
    print("\n Players hand:")
    for card in player.cards:
        print(card)
    
    
def show_all(player,dealer):
    print("\n Dealer's hand: ",*dealer.cards,sep='\n')
       
    print(f"Values of dealers hand is: {dealer.value}")
    
    print("\n Players hand:",*player.cards,sep='\n')
    
    print(f"Value of players hand is {player.value}")



def player_busts(player,dealer,chips):
    print("Player BUST!")
    chips.lose_bet()
        
def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()
    
def dealer_bust(player,dealer,chips):
    print("Dealer BUST! Player wins!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
        
        
def push(player,dealer):
    print("Dealer and Player tie! PUSH!")