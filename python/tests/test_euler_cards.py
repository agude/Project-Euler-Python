#!/usr/bin/env python

import pytest
from itertools import product, combinations, combinations_with_replacement
import euler.cards as eu


@pytest.fixture(scope="function")
def playing_cards():
    # All 52 playing cards from lowest value to highest
    cards = [
        ["2H", "2D", "2C", "2S"],
        ["3H", "3D", "3C", "3S"],
        ["4H", "4D", "4C", "4S"],
        ["5H", "5D", "5C", "5S"],
        ["6H", "6D", "6C", "6S"],
        ["7H", "7D", "7C", "7S"],
        ["8H", "8D", "8C", "8S"],
        ["9H", "9D", "9C", "9S"],
        ["TH", "TD", "TC", "TS"],
        ["JH", "JD", "JC", "JS"],
        ["QH", "QD", "QC", "QS"],
        ["KH", "KD", "KC", "KS"],
        ["AH", "AD", "AC", "AS"],
    ]

    # Create playing cards
    for i in range(len(cards)):
        for j in range(len(cards[i])):
            cards[i][j] = eu.PlayingCard(cards[i][j])

    return cards


def test_PlayingCard(playing_cards):
    # Get the all combinations of cards, including self-self pairs
    values = range(len(playing_cards))
    suits = range(len(playing_cards[0]))
    card_positions = product(values, suits)
    for (value0, suit0), (value1, suit1) in combinations_with_replacement(card_positions, 2):
        # Get the cards
        card0 = playing_cards[value0][suit0]
        card1 = playing_cards[value1][suit1]

        # card1 is always equal to or greater in value than card0
        assert card1 >= card0
        assert card0 <= card1

        # If the suites are the same
        same_suit = (suit0 == suit1)
        if same_suit:
            assert card0.suit == card1.suit
        else:
            assert card0.suit != card1.suit

        # If the values are the same
        same_value = (value0 == value1)
        if same_value:
            assert card0 == card1
        else:
            assert card0 != card1
            assert card0 < card1
            assert card1 > card0

        # If the cards are the same
        if same_suit and same_value:
            assert card0.name == card1.name
        else:
            assert card0.name != card1.name


def test_invalid_cards():
    for card in ["KZ", "ZC", "ZZ"]:
        with pytest.raises(ValueError):
            eu.PlayingCard(card)


@pytest.fixture(scope="function")
def poker_hands():
    # These hands are order from best to worst
    pairs = [
        [("TH", "JH", "QH", "KH", "AH"), eu.PokerHandType.royal_flush],
        [("4C", "5C", "6C", "7C", "8C"), eu.PokerHandType.straight_flush],
        [("2C", "KS", "KD", "KH", "KC"), eu.PokerHandType.four_of_a_kind],
        [("5C", "5S", "QH", "QD", "QC"), eu.PokerHandType.full_house],
        [("2C", "4C", "6C", "8C", "TC"), eu.PokerHandType.flush],
        [("4H", "5C", "6S", "7D", "8H"), eu.PokerHandType.straight],
        [("2H", "3S", "JC", "JH", "JD"), eu.PokerHandType.three_of_a_kind],
        [("3C", "3H", "5C", "5D", "7S"), eu.PokerHandType.two_pair],
        [("2H", "5D", "6C", "6H", "8D"), eu.PokerHandType.pair],
        [("2C", "4D", "6H", "8S", "AD"), eu.PokerHandType.high_card],
    ]

    for i in range(len(pairs)):
        pairs[i][0] = eu.PokerHand((eu.PlayingCard(card) for card in pairs[i][0]))

    return pairs


def test_PokerHand_type(poker_hands):
    for hand, hand_type in poker_hands:
        assert hand.hand_type is hand_type


def test_PokerHand_ordering(poker_hands):
    for hand0, hand1 in combinations(poker_hands, 2):
        # Check that a hand is equal to itself
        for hand in (hand0, hand1):
            assert hand == hand
            assert hand >= hand
            assert hand <= hand

        # Check that orders are correct (hand 0 is always better than hand1)
        assert hand0 > hand1
        assert hand0 >= hand1
        assert hand1 < hand0
        assert hand1 <= hand0
        assert hand0 != hand1
