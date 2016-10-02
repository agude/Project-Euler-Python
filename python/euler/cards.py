from enum import Enum, IntEnum, unique
import operator

@unique
class CardSuit(Enum):
    """ Playing card suits. """
    clubs = 0
    diamonds = 1
    hearts = 2
    spades = 3


@unique
class CardValue(IntEnum):
    """ Playing card values. They are order able as excepted:
    2 < 3 < ...< king < ace.
    """
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    ace = 14


@unique
class PokerHandType(IntEnum):
    """ Poker hands in order of their value. """
    high_card = 0
    pair = 1
    two_pair = 2
    three_of_a_kind = 3
    straight = 4
    flush = 5
    full_house = 6
    four_of_a_kind = 7
    straight_flush = 8
    royal_flush = 9


class PlayingCard(object):
    """Represent a standard American playing card.

    Cards are comparable by value using the standard operators (<, >, <=, >=),
    which considers only the value not the suit. To compare suits, use
    card.suit == card.suit. To insure the cards are the exact same, use
    card.name == card.name.

    Attributes:
        name (str): The string used to create the card.
        suit (CardSuit): The card's suit.
        value (CardValue): The card's value.
    """

    def __init__(self, card_string):
        """ Initialize a card from a string.

        This class is constructed from a two character string of the form:
        "<VALUE><SUIT>".

        Valid values are: 2, 3, 4, 5, 6, 7, 8, 9, T, J, K, A

        Valid suits are: C, D, H, S

        Args:
            card_string (str): A string of the form "<Value><Suit>", as
                explained above.

        Raises:
            ValueError: Raised if card_string is invalid.
        """
        self.name = card_string
        self.__set_suit()
        self.__set_number()

    def __set_suit(self):
        suit_map = {
            "C": CardSuit.clubs,
            "D": CardSuit.diamonds,
            "H": CardSuit.hearts,
            "S": CardSuit.spades,
        }
        suit = self.name[1]

        try:
            self.suit = suit_map[suit]
        except KeyError:
            raise ValueError("Suit '" + suit + "' from '" + self.name + "' is invalid")

    def __set_number(self):
        value_map = {
            "2": CardValue.two,
            "3": CardValue.three,
            "4": CardValue.four,
            "5": CardValue.five,
            "6": CardValue.six,
            "7": CardValue.seven,
            "8": CardValue.eight,
            "9": CardValue.nine,
            "T": CardValue.ten,
            "J": CardValue.jack,
            "Q": CardValue.queen,
            "K": CardValue.king,
            "A": CardValue.ace,
        }
        value = self.name[0]

        try:
            self.value = value_map[value]
        except KeyError:
            raise ValueError("Value '" + value + "' from '" + self.name + "' is invalid")

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other):
        if self.__class__ is other.__class__:
            return self.name != other.name
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented


class PokerHand(object):
    """Represent a hand in poker.

    The various python operators are used to compare the values of hands as
    follows:
        A  >  B: True if A beats B.
        A  <  B: True if A loses to B.
        A  >= B: True if A beats or ties B.
        A  >= B: True if A loses to or ties B.
        A  =  B: True if A ties B.

    Attributes:
        cards (list of PlayingCards): A list of 5 PlayingCard objects.
        value_count (dictionary): A dictionary mapping CardValue to number
            those cards in the hand. CardValues with 0 cards in the hand
            are left out of the dictionary.
            Example for five full of kings: {5: 3, 13: 2}
        hand_type (PokerHandType): The type of hand (pair, flush, etc.).
    """

    def __init__(self, cards):
        """ Initialize a hand from a list of 5 PlayingCard objects.

        Args:
            cards (list of PlayingCards): A list of 5 PlayingCard objects.

        Raises:
            ValueError: Raised if cards is invalid.
        """
        self.cards = tuple(sorted(cards))
        self.__tie_breakers = [0, 0]

        # Determine how many cards of each value exist
        self.value_count = {}
        for card in self.cards:
            value = int(card.value)
            try:
                self.value_count[value] += 1
            except KeyError:
                self.value_count[value] = 1

        # Set the hand type
        self.__set_hand_type()

    def __set_hand_type(self):
        # Is a Flush?
        is_flush = True
        first_suit = self.cards[0].suit
        for card in self.cards[1:]:
                is_flush &= (card.suit == first_suit)

        # Is a Straight?
        is_straight = True
        last_value = self.cards[0].value
        for card in self.cards[1:]:
            if last_value + 1 != card.value:
                is_straight = False
                break
            last_value = card.value

        # Is a royal flush, a straight flush, or just a straight or flush?
        if is_straight and is_flush:
            if self.cards[-1].value == CardValue.ace:
                self.hand_type = PokerHandType.royal_flush
                #print("Royal Flush!", self.cards)
                return
            else:
                self.hand_type = PokerHandType.straight_flush
                #print("Straight Flush", self.cards)
                return
        elif is_straight:
            self.hand_type = PokerHandType.straight
            #print("Straight", self.cards)
            return
        elif is_flush:
            self.hand_type = PokerHandType.flush
            #print("Flush", self.cards)
            return

        # Count the types of card matches we have
        quads = 0
        trips = 0
        pairs = 0
        for value in self.value_count.values():
            if value == 4:
                quads += 1
            elif value == 3:
                trips += 1
            elif value == 2:
                pairs += 1

        # Four of a kind
        if quads:
            self.hand_type = PokerHandType.four_of_a_kind
            self.__set_four_of_a_king_tie_breakers()
            #print("Four of a kind", self.cards)
        # Full House
        elif pairs and trips:
            self.hand_type = PokerHandType.full_house
            self.__set_full_house_tie_breakers()
            #print("Full house", self.cards)
        # Three of a kind
        elif trips:
            self.hand_type = PokerHandType.three_of_a_kind
            self.__set_three_of_a_kind_tie_breakers()
            #print("Three of a kind", self.cards)
        # Two pair
        elif pairs == 2:
            self.hand_type = PokerHandType.two_pair
            self.__set_two_pair_tie_breakers()
            #print("Two pair", self.cards)
        # Pair
        elif pairs:
            self.hand_type = PokerHandType.pair
            self.__set_pair_tie_breakers()
            #print("Pair", self.cards)
        # Nothing, only a high card
        else:
            self.hand_type = PokerHandType.high_card

    def __set_four_of_a_king_tie_breakers(self):
        for card_value, count in self.value_count.items():
            if count == 4:
                self.__tie_breakers[0] = card_value
                return

    def __set_full_house_tie_breakers(self):
        for card_value, count in self.value_count.items():
            if count == 3:
                self.__tie_breakers[0] = card_value
            elif count == 2:
                self.__tie_breakers[1] = card_value

    def __set_three_of_a_kind_tie_breakers(self):
        for card_value, count in self.value_count.items():
            if count == 3:
                self.__tie_breakers[0] = card_value

    def __set_two_pair_tie_breakers(self):
        for card_value, count in self.value_count.items():
            if count == 2:
                if not self.__tie_breakers[0]:
                    self.__tie_breakers[0] = card_value
                else:
                    self.__tie_breakers[1] = card_value
        self.__tie_breakers.sort(reverse=True)

    def __set_pair_tie_breakers(self):
        for card_value, count in self.value_count.items():
            if count == 2:
                self.__tie_breakers[0] = card_value
                return

    def __compare_cards(self, op, other):
        # Compare card values from high to low
        for i in reversed(range(len(self.cards))):
            us = self.cards[i]
            them = other.cards[i]
            # Unless we have an "equality accepting" operator, cards of the
            # same value have no use to us in breaking ties
            if us.value == them.value and (op is operator.gt or op is operator.lt):
                continue
            else:
                return op(us, them)
        # We have an equality accepting operator, and all have returned equal
        return True

    def __repr__(self):
        return self.cards.__repr__()

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            if self.hand_type == other.hand_type:
                if self.__tie_breakers[0] != other.__tie_breakers[0]:
                    return self.__tie_breakers[0] < other.__tie_breakers[0]
                elif self.__tie_breakers[1] != other.__tie_breakers[1]:
                    return self.__tie_breakers[1] < other.__tie_breakers[1]
                else:
                    return self.__compare_cards(operator.lt, other)
            else:
                return self.hand_type < other.hand_type
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            if self.hand_type == other.hand_type:
                if self.__tie_breakers[0] != other.__tie_breakers[0]:
                    return self.__tie_breakers[0] <= other.__tie_breakers[0]
                elif self.__tie_breakers[1] != other.__tie_breakers[1]:
                    return self.__tie_breakers[1] <= other.__tie_breakers[1]
                else:
                    return self.__compare_cards(operator.le, other)
            else:
                return self.hand_type <= other.hand_type
        return NotImplemented

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.hand_type == other.hand_type
        return NotImplemented

    def __ne__(self, other):
        if self.__class__ is other.__class__:
            return self.hand_type != other.hand_type
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            if self.hand_type == other.hand_type:
                if self.__tie_breakers[0] != other.__tie_breakers[0]:
                    return self.__tie_breakers[0] > other.__tie_breakers[0]
                elif self.__tie_breakers[1] != other.__tie_breakers[1]:
                    return self.__tie_breakers[1] > other.__tie_breakers[1]
                else:
                    return self.__compare_cards(operator.gt, other)
            else:
                return self.hand_type > other.hand_type
        return NotImplemented

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            if self.hand_type == other.hand_type:
                if self.__tie_breakers[0] != other.__tie_breakers[0]:
                    return self.__tie_breakers[0] >= other.__tie_breakers[0]
                elif self.__tie_breakers[1] != other.__tie_breakers[1]:
                    return self.__tie_breakers[1] >= other.__tie_breakers[1]
                else:
                    return self.__compare_cards(operator.ge, other)
            else:
                return self.hand_type >= other.hand_type
        return NotImplemented
