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
