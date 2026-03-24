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
    list = []
    for i in suits:
        for a in ranks:
            list.append(i,a)
    return list

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
    total = total + hand
    ace = 11
    if total > 21 and hand == ace:
        total = total - 10
    
    

def show_hand(player_name, hand, hide_first_card=False):
    """Prints the formatted hand and current score for the user."""
    # TODO: Print cards. If hide_first_card is True, obscure the first card.
    print(player_name + hand)
    print("Your score is: " + total_score)

def play_game():
    """Main game loop managing turns, user input, and winner logic."""
    # TODO: Implement game flow
    deck = create_deck()
    shuffle_deck(deck)
    deal_one = deal_card(deck)
    deal_two = deal_card(deck)
    total = calculate_score(hand)
    show_hand(player_name, hand, hide_first_card=False)
    
   
   
   
    while true:
        user_choice = input("Do you want to hit or stand")
        if user_choice == "hit" or "Hit":
            return
        elif user_choice == "stand" or "Stand":
            return
        else:
            print("invalid input")
    if total == 21:
        print("winner")



if __name__ == "__main__":
    play_game()
    
