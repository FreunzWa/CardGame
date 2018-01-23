
from definitions import *


class CardContainer:
    def __init__(self, size = 0, container_type = "deck"):
        """
        initialises a new card container_type
        the 'top' card is considered to be index 0
        """
        self.container_type = container_type
        self.contents = np.zeros(size,)

    def shuffle(self):
        """
        @func:
        randomises the order of the contents of the card container
        @param:
        none
        """
        self.contents = np.random.shuffle(self.contents)

    def draw_card(self):
        """
        @func
        especially used when the container is of type deck. removes the first
        element from the container, and returns the card object.
        """
        drawn_card = self.contents[0]
        self.contents = self.contents[1:]
        return drawn_card

    
