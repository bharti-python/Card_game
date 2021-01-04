import pytest
from Card_Game.Card import Card, Rank, Suite


def test_card_init():
	oneCard = Card(Suite.Spades, "Ace")
	assert oneCard.suite == Suite.Spades, "Wrong Suite error."
	assert oneCard.rank.name == "Ace", "Wrong Rank error."

def test_card_print():
    oneCard = Card(Suite.Diamonds, "King")
    assert str(oneCard) == "(Diamonds King)", "Wrong Card string format."

def test_card_lt():
    oneCard = Card(Suite.Spades, "Ace")
    anotherCard = Card(Suite.Diamonds, "King")
    assert (oneCard < anotherCard) == True, "Card less than (<) operator failed."

def test_card_le():
    oneCard = Card(Suite.Spades, "Ace")
    anotherCard = Card(Suite.Diamonds, "King")
    assert (oneCard <= anotherCard) == True, "Card less than equal to (<=) operator failed."


def test_card_eq():
    oneCard = Card(Suite.Spades, "Ace")
    anotherCard = Card(Suite.Diamonds, "King")
    assert (oneCard == anotherCard) == False, "Card equal to (==) operator failed."

def test_card_getValue():
    oneCard = Card(Suite.Spades, "Ace")
    assert oneCard.getValue() == 14, "Card getValue function failed."


def test_suite_list():
	assert len(list(Suite)) == 4, "Length of Suites is incorrect."

def test_rank_list():
	assert len(list(Rank)) == 13, "Length of Ranks is incorrect."
