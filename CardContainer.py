
from definitions import *
from Card import *

class CardContainer:
    def __init__(self, size = 0, container_type = "deck"):
        """
        initialises a new card container_type
        the 'top' card is considered to be index 0
        """

        self.container_type = container_type
        self.id_values = np.random.randint(1,11,(size,))
        self.contents = np.ndarray([0,])
        for i in self.id_values:
            new_card = Card(card_id = i)
            self.contents = np.append(self.contents, new_card)

        print "New card container created of type '%s' with contents: " %(container_type.upper())
        print self.id_values
        print self.contents
        card_container_list.append(self)

    def shuffle(self):
        """
        @func:
        randomises the order of the contents of the card container
        @param:
        none
        """
        self.contents = np.random.shuffle(self.contents)

    def draw_card(self, target_container):
        """
        @func
        especially used when the container is of type deck. removes the first
        element from the container, and returns the card object.
        """
        if len(self.contents) > 0:
            drawn_card = self.contents[0]
            self.contents =  self.contents[1:]
            target_container.contents = np.append(target_container.contents, drawn_card)
            print target_container.contents
        else:
            raise ValueError("There are no more cards left in deck!")
