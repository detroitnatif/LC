from collections import defaultdict

hands = {
    "John": ["AD", "QS", "3H", "5H", "KC"],
    "Clara": ["10H", "6D", "JS", "AS", "2C"],
    "Jane": ["9C", "7D", "3S", "4C", "8S"],
    "Bob": ["7S", "2H", "AH", "KD", "6C"],
}

# Work out which player wins the game
#
# Rules:
# 1. A card consists of its value and suit
# 2. Ace is the highest value, followed by King, Queen, Jack, 10, 9, ... down to 2
# 3. When the value of the card is the same, spades is the most valuable suit, then hearts, diamonds and clubs in that order
# 4. Each round, every player plays their strongest card, the winner of that round gets a point
# 5. The player with the most points wins the game
#
# Output: {"John": 1, "Clara": 2, "Jane": 1, "Bob": 1}
def f(card, suit):
    d = {"A": 1, "K": 2, "Q": 3, "J": 4, "10": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}
    suits = {"S": 4, "H": 3, "D": 2, "C": 1}
    return d[card] + suits[suit]


def compute_scores(hands):
    
    # for p, h in hands.items():
        # h.sort(key=f(p, h))
    
        # some sort to get all hands in order
    hands = {
        "John": ["AD", "QS"],
        "Clara": ["10H", "6D"],
        "Jane": ["9C", "7D"],
        "Bob": ["7S", "2H"],
    }
    
    out = {}
    for i in hands.keys():
        out[i] = 0
        
    for players in hands.keys():
        
        for player in players:
            
            print(hands[player][0])
            

            
            
            
            
        
        
    # TODO
    pass

print(compute_scores(hands))