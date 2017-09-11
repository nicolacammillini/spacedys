"""Test for deck management"""

from spacedyspoker import Suit, Value, describe_card, get_deck, shuffle_deck


def test_deck_size():
    """Check deck is made up of 52 cards"""
    deck = get_deck()
    assert len(deck) == 52


def test_deck_thirteen_hearts():
    """Check hearts are 13"""
    counter = {Suit.HEARTS: 0, Suit.SPADES: 0, Suit.CLUBS: 0, Suit.DIAMONDS: 0}
    deck = get_deck()
    for card in deck:
        value, suit = card
        counter[suit] += 1

    assert value in Value
    assert counter[Suit.HEARTS] == 13


def test_deck_thirteen_clubs():
    """Check clubs are 13"""
    counter = {Suit.HEARTS: 0, Suit.SPADES: 0, Suit.CLUBS: 0, Suit.DIAMONDS: 0}
    deck = get_deck()
    for card in deck:
        value, suit = card
        counter[suit] += 1

    assert value in Value
    assert counter[Suit.CLUBS] == 13


def test_deck_thirteen_diamonds():
    """Check diamonds are 13"""
    counter = {Suit.HEARTS: 0, Suit.SPADES: 0, Suit.CLUBS: 0, Suit.DIAMONDS: 0}
    deck = get_deck()
    for card in deck:
        value, suit = card
        counter[suit] += 1

    assert value in Value
    assert counter[Suit.DIAMONDS] == 13


def test_deck_thirteen_spades():
    """Check spades are 13"""
    counter = {Suit.HEARTS: 0, Suit.SPADES: 0, Suit.CLUBS: 0, Suit.DIAMONDS: 0}
    deck = get_deck()
    for card in deck:
        value, suit = card
        counter[suit] += 1

    assert value in Value
    assert counter[Suit.SPADES] == 13


def test_shuffled_deck():
    """Check deck is different after shuffle"""
    deck = get_deck()
    sorted_deck = deck.copy()
    shuffle_deck(deck)

    assert deck != sorted_deck


def test_description_ace_o_hearts():
    """Check description of ace of hearts is correct"""
    card = (Value.ACE, Suit.HEARTS)
    description = describe_card(card)
    assert description == "Ace of Hearts"


def test_description_queen_o_spades():
    """Check description of queen of spades is correct"""
    card = (Value.QUEEN, Suit.SPADES)
    description = describe_card(card)
    assert description == "Queen of Spades"


def test_description_ten_o_diamonds():
    """Check description of ten of diamonds is correct"""
    card = (Value.TEN, Suit.DIAMONDS)
    description = describe_card(card)
    assert description == "Ten of Diamonds"
