from definitions import *




class Card:
    def __init__(self, card = "big_pot"):
        """
        @params:
        card = the image file without the *.png extension to be loaded, determines
        the class type.
        """
        self.picture = pygame.image.load(path+'\\res\\img\\cards\\'+card+".png")
        self.visible = True
        self.position = 0

        cardList.append(self)
    def draw(self, target_surface):
        """
        @purpose:
        draws itself to the screen.
        @params:
        target_surface - the window/surface the card is to be drawn to.
        """
        target_surface.blit(self.picture, (0,0))
