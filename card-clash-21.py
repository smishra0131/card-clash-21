import random
# Global Configurations
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}

def create_deck():
    # This will create the deck
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank,suit))
    return deck

def shuffle_deck(deck):
    # This function will shuffle the deck
    random.shuffle(deck)
    

def deal_card(deck):
    # This function will give the cards
    return deck.pop()
def calculate_score(hand):
    # This will calculate the value of the aces and the total
    aces = 0
    total = 0
    for card in hand:
        rank = card[0]
        total = total + values[rank]
        if rank == "Ace":
            aces += 1
    
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def show_hand(player_name, hand, hide_first_card=False):
    #It hides the first card
    if hide_first_card:
        print("Hidden card")
        for card in hand [1:]:
            print(str(card[0]) + " of " + str(card[1]))
    else:
        for card in hand:
            print(str(card[0]) + " of " + str(card[1]))
        current_score = calculate_score(hand)
        print("Score: " + str(current_score))

def play_game():
# This is how the game will work
    game_deck = create_deck()
    shuffle_deck(game_deck)
    player_hand = [deal_card(game_deck), deal_card(game_deck)]
    dealer_hand = [deal_card(game_deck), deal_card(game_deck)]
    
    answer = True
    

    while answer:
        print("Player", player_hand)
        print("Dealer", dealer_hand,)
        current_score = calculate_score(player_hand)
        print("Player score: " + str(current_score))
        choice = input("Do you want to hit or stand? ")
        if choice == "hit":
           player_hand.append(deal_card(game_deck))
        elif choice == "stand" or current_score > 21:
             print("Dealer is playing.")
             while calculate_score(dealer_hand) < 17:
                dealer_hand.append(deal_card(game_deck))
        else:
            print("Please type hit or stand.")
        player_score = calculate_score(player_hand)
        print("Player", player_hand)
        print("Dealer", dealer_hand)
        dealer_score = calculate_score(dealer_hand)
        if player_score > 21:
            print("You busted! Dealer wins.")
        elif dealer_score > 21:
            print("Dealer busted! You win.")
        elif player_score == 21:
            print("You have 21, you won.")
        elif dealer_score == 21:
            print("Dealer has 21, dealer won.")
        elif player_score > dealer_score:
            print("You has a higher score. You won.")
        elif player_score < dealer_score:
            print("Dealer has a higher score. Dealer won.")
        else:
            print("It's a tie.")
        answer = False
       
       
       
       
       

    
   
    
    
if __name__ == "__main__":
    play_game()
    
   
    
    
