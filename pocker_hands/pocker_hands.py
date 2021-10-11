class PokerGame:
    def __init__(self, player1, cards1, player2, cards2):
        self.cards1 = self.parse_card_number(cards1)
        self.player1 = player1
        self.cards2 =  self.parse_card_number(cards2)
        self.player2 = player2

    def parse_card_number(self, cards):
        splited = cards.split(" ")
        first_char =[i[:-1] for i in splited]
        suit = [i[-1] for i in splited]
        mapping = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        numbers = [{ 'number': mapping[i], 'suit': j } for i, j in zip(first_char, suit)]
        return numbers

    def result(self):
        raise NotImplemented

