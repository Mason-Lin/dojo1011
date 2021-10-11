class PokerGame:
    def __init__(self, player1, cards1, player2, cards2):
        self.cards1 = self.parse_card_number(cards1)
        self.player1 = player1
        self.cards2 =  self.parse_card_number(cards2)
        self.player2 = player2

    def parse_card_number(self, cards):
        splited = cards.split(" ")
        first_char =[i[0] for i in splited]
        mapping = {
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        numbers = [mapping[i] for i in first_char]
        return numbers

    def result(self):
        for card in self.cards1:

