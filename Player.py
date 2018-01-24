

class Player:
    def __init__(self, type = "human", deck = None, player_no = 1):
        """
        Player object.
        player objects have an associated type, and a deck array. the deck array
        is used to create the new deck.
        """
        self.type = type
        self.deck = deck

    def cpu_play_card(self):
        if self.type == "cpu":
            return random.choose(self.hand)
