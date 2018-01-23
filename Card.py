from definitions import *



class Card:
    def __init__(self, card = "big_pot", pos=(0,0)):
        """
        @params:
        card = the image file without the *.png extension to be loaded, determines
        the class type.
        """
        self.picture = pygame.image.load(path+'\\res\\img\\cards\\'+card+".png")
        self.visible = True
        self.position = 0
        self.pos = pos
        self.name = cardname_correction(card)
        self.stats = (card_dict[self.name]["ATTACK"],
            card_dict[self.name]["DEFENSE"])


        self.make_card_surface()
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
        draw_text(self.name, (central_padding*1.5, central_padding*1.5), surf)
        draw_text("ATK: "+str(self.stats[0]), (central_padding*2, surf.get_height()*0.65), surf)
        draw_text("DEF: "+str(self.stats[1]), (central_padding*2, surf.get_height()*0.75), surf)
        self.spr_card = surf
