import random
# Global Configurations
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}

def create_deck():
    """Returns a list of 52 tuples representing a standard deck: (rank, suit)"""
    deck = []
    for i in suits:
        for a in ranks:
            deck.append((a,i))
    return deck

def shuffle_deck(deck):
    """Shuffles the deck list in-place."""
    random.shuffle(deck)
    

def deal_card(deck):
    """Removes and returns the top card from the deck."""
    return deck.pop()
def calculate_score(hand):
    """
    Calculates the total value of cards in a hand.
    Requirement: If the score is over 21 and the hand contains an Ace, 
    reduce the score by 10 until the score is <= 21 or no Aces remain.
    """
    # TODO: Implement scoring logic and Ace adjustment
    hand = 0
    total = 0
    total = total + hand
    ace = 11
    if total > 21 and hand == ace:
        total = total - 10
    

def play_game():
    """Main game loop managing turns, user input, and winner logic."""
    # TODO: Implement game flow
    deck = create_deck()
    shuffle_deck(deck)
    player_hand = deal_card(deck)
    dealer_hand = deal_card(deck)
    hand = 0
    total = calculate_score(hand)
    
    
   
    while True:
        player_score = 0
        player_hand = 0
        dealer_hand = 0
        dealer_score = 0
        player_score = player_score + player_hand
        dealer_score = dealer_hand + dealer_score
        print("You have " + str(player_hand))
        print("Dealer has " + str(dealer_hand))
        choice = input("Do you want to hit or stand? ")
        if choice == "hit":
            print(player_hand.append(deal_card(deck)))
        elif choice == "stand":
            print("Your score is " + str(player_score))
            print("Dealer's turn.")
        else:
            print("Invalid input.")
        while dealer_score > 17:
            dealer_hand.append(deal_card(deck))
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
    
    
   
    
    
if __name__ == "__main__":
    play_game()
