import abc
import collections
import random
import unittest

class Card:
    def __init__(self, number, color, suit, folded=False):
        self.number = number
        self.color = color
        self.suit = suit
        self.folded = folded

    def fold(self):
        self.fold = not self.fold

    def __str__(self):
        return f'{self.__class__.__name__}, num: {self.number}, suit: {self.suit}, color: {self.color}'

class FaceCard(Card): pass
class NumberCard(Card): pass
class GhostCard(Card):
    def __init__(self, number=-1, color='Black', suit='Ghost', folded=False):
        self.number = -1
        self.color = 'Black'
        self.suit = 'Ghost'
        self.folded = folded

class DeckOfCards(abc.ABC):
    def __init__(self, size):
        self.size = size
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    @abc.abstractmethod
    def new_deck(self, factory):
        """
        Create a new deck of cards. Supply a factory to create new deck.
        """

class HouseDeck(DeckOfCards):
    def __init__(self, size=54):
        super().__init__(size=54)

    def new_deck(self, factory):
        self.cards = []
        for suit in ['diamond', 'heart', 'spade', 'club']:
            for i in range(1, 14):
                self.cards.append(factory.add_card(i, suit))
        self.cards.extend([GhostCard() for i in range(2)])
        self.shuffle()

class BlackJackDeck(DeckOfCards):
    def __init__(self, size=5):
        super().__init__(size=5)

    def new_deck(self, house: HouseDeck):
        self.cards = [house.draw() for i in range(self.size)]

class CardFactory(abc.ABC):
    def __init__(self):
        self.COLOR_CONFIG = collections.defaultdict(lambda x: 'BLACK')
        self.COLOR_CONFIG['diamond'] = 'RED'
        self.COLOR_CONFIG['heart'] = 'RED'
        self.COLOR_CONFIG['spade'] = 'BLACK'
        self.COLOR_CONFIG['club'] = 'BLACK'

    @abc.abstractmethod
    def add_card(self, number, suit):
        """
        Add a new card based on the info provided.
        """

class HouseCardFactory(CardFactory):
    def add_card(self, number, suit):
        if number in [11, 12, 13]:
            card = Card(number, self.COLOR_CONFIG[suit], suit)
        elif 1 <= number <= 10:
            card = NumberCard(number, self.COLOR_CONFIG[suit], suit)
        elif number == -1:
            card = GhostCard()
        else:
            raise ValueError(f'Card number {number} not supported')

        return card

class Test(unittest.TestCase):
    def test_house_deck(self):
        doc = HouseDeck()
        doc.new_deck(HouseCardFactory())
        assert len(doc.cards) == 54

    def test_blackjack_deck(self):
        doc = HouseDeck()
        doc.new_deck(HouseCardFactory())
        bj = BlackJackDeck()
        bj.new_deck(doc)
        assert len(bj.cards) == 5
