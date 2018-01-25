import numpy as np
from definitions import *
from Button import Button
from Card import Card
import utilities as util
import pygame

class CardContainer:
    def __init__(self, size = 0, container_type = "deck", player_no = 1, contents = None):
        """
        initialises a new card container_type
        the 'top' card is considered to be index 0
        """
        self.player_no = player_no
        self.container_type = container_type
        if contents == None:
            self.id_values = np.random.randint(1,12,(size,))
        else:
            self.id_values = contents

        #Field initialisation
        if self.container_type == "field":
            #self.field, when the container is a field it has an associated field shape
            self.field = [2,1]
            self.surfaces = np.zeros([0,])
            self.node_width = card_dimensions[0]*1.1
            self.node_height = card_dimensions[1]*1.1
            for i in range(0,self.field[1]):
                for j in range(0,self.field[0]):
                    new_button = Button((0,0,self.node_width, self.node_height))
                    self.surfaces = np.append(self.surfaces, new_button)
            self.contents = np.ndarray([0,])
        else:
            self.contents = np.ndarray([0,])

        for i in self.id_values:
            new_card = Card(card_id = i, container_type = self.container_type, player_no=player_no )
            self.contents = np.append(self.contents, new_card)
        self.pos = (0,0)

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
        ##HAND
        if self.container_type != "field":
            for card_num, card in enumerate(self.contents):
                if self.container_type == "hand" and card.pickup == False:
                    if self.player_no ==1:
                        card.pos = ((padding*3+card.icon.get_width()*1.2*card_num+0.5*card_dimensions[0], target_surface.get_height()-padding*3-card.icon.get_height()))
                        target_surface.blit(card.icon, (card.pos) )
                        if card.is_undermouse(card.icon) == True:
                            target_surface.blit(card.spr_card, (card.pos[0]-card.icon.get_width()/2, card.pos[1]-card.spr_card.get_height()*0.4-padding))

                    else:
                        card.pos = ((padding*18+card.icon.get_width()*1.2*card_num+0.5*card_dimensions[0], padding*3))
                        card.icon.fill(CARD_BACK)
                        target_surface.blit(util.outline_surface(card.icon), (card.pos) )
                    card.is_icon = True

                else:
                    card.is_icon = False
        ##FIELD
        if self.container_type == "field":

            if self.surfaces[0].x == 0 and self.surfaces[1].x == 0:
                #checks the first surface to see if not centred properly (ie it's still at the default position)
                field_drawx = target_surface.get_width()/2-self.field[1]*self.node_width*1.1/2
                field_drawy = target_surface.get_height()/2-self.field[0]*self.node_height*1.1/2
                for counter, surface in enumerate(self.surfaces):
                    surface.x = field_drawx + (counter%self.field[1])*self.node_width*1.1
                    surface.y = field_drawy + (counter%self.field[0])*self.node_height*1.1

            #this draws the surface list
            for surface in self.surfaces:
                pygame.draw.rect(target_surface, DARK_BROWN, (surface.x, surface.y, surface.width, surface.height))
        ##FIELD
        if self.container_type == "deck":
            scale = 1
            card_back = pygame.Surface((card_dimensions[0]*scale, card_dimensions[1]*scale))
            card_back.fill(CARD_OUTLINE)
            pygame.draw.rect(card_back, CARD_BACK, (1,1,card_back.get_width()*scale-2,card_back.get_height()*scale-2))

            for card_bunch in range(0,(len(self.contents)+1)//2):
                #draws the deck in the appropriate position depending on player
                max_deck_height =(60)//2*2

                if self.player_no == 1:
                    target_surface.blit(card_back, (target_surface.get_width()
                    -card_dimensions[0]*scale-padding, target_surface.get_height()
                    -card_dimensions[1]*scale-padding-card_bunch*2 ))
                else:
                    target_surface.blit(card_back,(padding, padding+max_deck_height-card_bunch*2))



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
            drawn_card = self.contents[ind]
            drawn_card.container = target_container
            self.contents = np.delete(self.contents, ind)
            target_container.contents = np.append(target_container.contents, drawn_card)
            return drawn_card
        else:
            raise ValueError("There are no more cards left in deck!")
