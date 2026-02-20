Black Jack Game

# -----------------------------
# Card setup (tuple = immutable)
# -----------------------------
CARD_VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('♠', '♥', '♦', '♣')


# -----------------------------
# Functions
# -----------------------------
def create_deck():
    deck = [(value, suit) for value in CARD_VALUES for suit in SUITS]
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)


def deal_card(deck):
    return deck.pop()


def calculate_total(hand):
    total = 0
    aces = 0

    for card, suit in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            total += 11
            aces += 1
        else:
            total += int(card)

    # Ace logic (11 → 1 if bust)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total


def show_hand(hand, owner):
    print(f"{owner}'s hand:", hand, "| Total:", calculate_total(hand))


# -----------------------------
# Main Game Logic
# -----------------------------
def main_game():
    deck = create_deck()
    shuffle_deck(deck)

    player_hand = []
    dealer_hand = []

    # Alternating initial deal (player first)
    player_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))
    player_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))

    print("\n--- Initial Deal ---")
    show_hand(player_hand, "Player")
    print("Dealer's hand:", [dealer_hand[0], 'Hidden'])

    # -----------------------------
    # Player Turn
    # -----------------------------
    while True:
        if calculate_total(player_hand) > 21:
            print("Player busts! Dealer wins.")
            return

        choice = input("Hit or Stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deal_card(deck))
            show_hand(player_hand, "Player")
        else:
            break

    # -----------------------------
    # Dealer Turn
    # -----------------------------
    print("\n--- Dealer's Turn ---")
    show_hand(dealer_hand, "Dealer")

    while cal