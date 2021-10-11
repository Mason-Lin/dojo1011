"""
    https://codingdojo.org/kata/PokerHands/
"""
from pocker_hands import PokerGame


def test_compare_highcard():
    game = PokerGame(
        player1="Black",
        cards1="2H 3D 5S 9C KD",
        player2="White",
        cards2="2C 3H 4S 8C AH",
    )
    assert game.result() == "White wins. - with high card: A"

def test_parse_card_number():
    game = PokerGame(
        player1="Black",
        cards1="2H 3D 5S 9C KD",
        player2="White",
        cards2="2C 3H 4S 8C AH",
    )
    assert game.parse_card_number("2H 3D 5S 9C KD") == [{'number': 2, 'suit': 'H'}, {'number': 3, 'suit': 'D'}, {'number': 5, 'suit': 'S'}, {'number': 9, 'suit': 'C'}, {'number': 13, 'suit': 'D'}]
