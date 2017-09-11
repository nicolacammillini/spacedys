"""Constants and functions for playing poker"""

from random import shuffle

from enum import Enum


class Suit(Enum):
    """SUITS_DESCRIPTION enum"""
    HEARTS = 1
    CLUBS = 2
    DIAMONDS = 3
    SPADES = 4


class Value(Enum):
    """VALUES_DESCRIPTION enum"""
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


_VALUES_DESCRIPTION = {
    Value.ACE: 'Ace',
    Value.TWO: 'Two',
    Value.THREE: 'Three',
    Value.FOUR: 'Four',
    Value.FIVE: 'Five',
    Value.SIX: 'Six',
    Value.SEVEN: 'Seven',
    Value.EIGHT: 'Eight',
    Value.NINE: 'Nine',
    Value.TEN: 'Ten',
    Value.JACK: 'Jack',
    Value.QUEEN: 'Queen',
    Value.KING: 'King'
}

_SUITS_DESCRIPTION = {
    Suit.HEARTS: 'Hearts',
    Suit.CLUBS: 'Clubs',
    Suit.DIAMONDS: 'Diamonds',
    Suit.SPADES: 'Spades'
}


def get_deck():
    """Creates a sorted deck of cards"""
    deck = []
    for suit in Suit:
        for value in Value:
            deck.append((value, suit))

    return deck


def shuffle_deck(deck):
    """Shuffle deck list implementation"""
    shuffle(deck)


def describe_card(card):
    """String description of a card"""
    value, suit = card
    value_description = _VALUES_DESCRIPTION[value]
    suit_description = _SUITS_DESCRIPTION[suit]

    description = "{} of {}".format(value_description, suit_description)

    return description
