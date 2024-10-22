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

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suit_values = {'C': 1, 'D': 2, 'H': 3, 'S': 4}  # Clubs < Diamonds < Hearts < Spades

# Function to get card rank (value + suit)
def get_card_rank(card):
    value = card[:-1]  # Extract card value
    suit = card[-1]    # Extract card suit
    return (card_values[value], suit_values[suit])

# Initialize points dictionary
points = defaultdict(int)

# Each player plays their strongest card (5 rounds)
for round_num in range(5):
    # Track the highest card and its owner
    highest_card = None
    round_winner = None

    for player, hand in hands.items():
        # Get the current card
        card = hand[round_num]
        card_rank = get_card_rank(card)

        # Determine if this card beats the highest card seen so far
        if highest_card is None or card_rank > highest_card:
            highest_card = card_rank
            round_winner = player

    # Award a point to the winner of this round
    points[round_winner] += 1