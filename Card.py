import numpy as np
from definitions import *
import pygame
import utilities as util

class Card:
    def __init__(self,  card_id = 1, pos=(0,0)):
        """
        @params:
        card = the image file without the *.png extension to be loaded, determines
        the class type.
        """

        self.card = "big_pot" #for now this is default.
        for key in card_dict:
            if card_dict[key]["ID"] == card_id:
                self.card = key
                break

        self.picture = pygame.image.load(path+'\\res\\img\\cards\\'+self.card+".png")
        self.visible = True
        self.position = 0
        self.pos = pos
        self.color = NORMAL_MONSTER
        self.card_key = self.card
        self.name = util.cardname_correction(self.card)
        self.stats = (card_dict[self.card_key]["ATTACK"],
            card_dict[self.card_key]["DEFENSE"])
        #mouse anchor centres the drag point of the card when the card is being dragged
        self.mouse_anchor = (0,0)
        self.pickup = False
        self.is_icon = False
        self.make_card_surface()
        self.make_card_icon()
        cardList.append(self)

    def draw(self, target_surface):
        """
        @purpose:
        draws itself to the screen.
        @params:
        target_surface - the window/surface the card is to be drawn to.
        """

        target_surface.blit(self.spr_card, self.pos)


    def make_card_surface(self):
        """
        This adds the picture loaded in init to a general class environment.
        The card surface is stored in an attribute: spr_card. This card
        surface is then drawn to the screen in self.draw
        """

        surf = pygame.Surface((card_dimensions))
        surf.fill(CARD_OUTLINE)
        pygame.draw.rect(surf, NORMAL_MONSTER,(central_padding, central_padding,
            surf.get_width()-central_padding*2,
            surf.get_height()-central_padding*2))
        picture_outline = pygame.Surface((self.picture.get_width()+2,
            self.picture.get_height()+2))
        picture_outline.fill(CARD_OUTLINE)
        picture_outline.blit(self.picture,(1,1))
        surf.blit(picture_outline, (central_padding-1,surf.get_height()*1/7))
        util.draw_text(self.name, (central_padding*1.5, central_padding*1.5), surf)
        util.draw_text("ATK: "+str(self.stats[0]), (central_padding*2, surf.get_height()*0.73), surf)
        util.draw_text("DEF: "+str(self.stats[1]), (central_padding*2, surf.get_height()*0.83), surf)
        self.spr_card = surf

    def make_card_icon(self):
        """
        This generates a surface, the card's icon. This can be drawn, eg to the hand.
        """
        card_icon = pygame.Surface((card_dimensions[0]/2, card_dimensions[1]/2))
        card_icon.fill(self.color)
        pygame.draw.rect(card_icon, CARD_OUTLINE, (0,0,card_icon.get_width(), card_icon.get_height()), 1)
        #the picture
        pic = pygame.transform.scale(self.picture, (card_icon.get_width()-2, card_icon.get_height()*1/2))
        pic = util.outline_surface(pic)
        card_icon.blit(pic,(1, card_icon.get_height()/7))
        util.draw_text(self.name, (2,2), card_icon, text_size = 8)
        self.icon = card_icon

    def is_undermouse(self, surf):
        return (pygame.mouse.get_pos()[0] > self.pos[0] and pygame.mouse.get_pos()[0]<self.pos[0]+surf.get_width()) and (((pygame.mouse.get_pos()[1] > self.pos[1] and pygame.mouse.get_pos()[1]<self.pos[1]+surf.get_height()) ))


    def drag(self, mouse_occupied, surf ):

        """
        @func
        if the card's container is of type 'hand' then the card can be dragged
        to a new location.
        """

        if pygame.mouse.get_pressed()[0]:
            if self.is_undermouse(surf):
                if not self.pickup and not mouse_occupied:
                    self.pickup = True
                    mouse_occupied = True
                    self.mouse_anchor = ((pygame.mouse.get_pos()[0]-self.pos[0]),(pygame.mouse.get_pos()[1]-self.pos[1]))
        else:
            if self.pickup:
                self.pickup = False
                mouse_occupied = False


        if self.pickup:
            self.pos = ((pygame.mouse.get_pos()[0]-self.mouse_anchor[0]),(pygame.mouse.get_pos()[1]-self.mouse_anchor[1]))


        return mouse_occupied
