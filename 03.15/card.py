# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
# The Deck class should have a deal method to deal a single card from the deckAfter a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
import random
from typing import List,Optional

class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value
        
    def display_card(self) -> str:
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []
        suits: List[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values: List[str] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for value in values:
                card_dict = {"suit": suit, "value": value}
                card = Card(card_dict)
                self.cards.append(card)
                
    def shuffle(self) -> None:
        random.shuffle(self.cards)
        
    def deal(self) -> Optional[Card]:
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()


deck = Deck()
deck.shuffle()
for i in range(5):
    card = deck.deal()
    if card is not None:
        print(f"Card {i+1}: {card.value} of {card.suit}")
    else:
        print("There are no more cards left in the deck.")