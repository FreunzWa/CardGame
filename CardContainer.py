
from definitions import *
from Card import *

class CardContainer:
    def __init__(self, size = 0, container_type = "deck", player_no = 1):
        """
        initialises a new card container_type
        the 'top' card is considered to be index 0
        """
        self.player_no = player_no
        self.container_type = container_type
        self.id_values = np.random.randint(1,11,(size,))
        self.contents = np.ndarray([0,])
        self.bounds = pygame.Surface((0,0))
        for i in self.id_values:
            new_card = Card(card_id = i)
            self.contents = np.append(self.contents, new_card)

        print "New card container created of type '%s' with contents: " %(container_type.upper())
        print self.id_values
        card_container_list.append(self)


    def display(self, target_surface):
        """
        The container is drawn to the screen for interactivity.
        @params:
        target_surface - the screen or surface for the container to be drawn
        to
        """
        padding = 4
        if self.container_type == "deck":
            card_back = pygame.Surface((card_dimensions))
            card_back.fill(CARD_OUTLINE)
            pygame.draw.rect(card_back, CARD_BACK, (1,1,card_back.get_width()-2,card_back.get_height()-2))

            for card_bunch in range(0,len(self.contents)//2):
                #draws the deck in the appropriate position depending on player
                max_deck_height =(60)//2*2

                if self.player_no == 1:
                    target_surface.blit(card_back, (target_surface.get_width()
                    -card_dimensions[0]-padding, target_surface.get_height()
                    -card_dimensions[1]-padding-card_bunch*2 ))
                else:
                    target_surface.blit(card_back,(padding, padding+max_deck_height-card_bunch*2))


        for card_num, card in enumerate(self.contents):
            if self.container_type == "hand":
                card.pos = ((padding*3+card.icon.get_width()*1.2*card_num+0.5*card_dimensions[0], target_surface.get_height()-padding*3-card.icon.get_height()))
                target_surface.blit(card.icon, (card.pos) )
                card.is_icon = True
                if card.is_undermouse(card.icon) == True:
                    target_surface.blit(card.spr_card, (card.pos[0]-card.icon.get_width()/2, card.pos[1]-card.spr_card.get_height()-padding))
            else:
                card.is_icon = False



    def shuffle(self):
        """
        @func:
        randomises the order of the contents of the card container
        @param:
        none
        """
        self.contents = np.random.shuffle(self.contents)

    def pull_card(self, target_container, ind = 0):
        """
        @func
        especially used when the container is of type deck. removes the first
        element from the container, and returns the card object.
        """
        if len(self.contents) > 0:
            pdb.set_trace()
            drawn_card = self.contents[ind]
            self.contents = np.delete(self.contents, ind)
            target_container.contents = np.append(target_container.contents, drawn_card)
            print target_container.contents
        else:
            raise ValueError("There are no more cards left in deck!")
