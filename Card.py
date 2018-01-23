from definitions import *




class Card:
    def __init__(self, card = "big_pot"):
        self.picture = pygame.image.load(path+'\\res\\img\\cards\\'+card+".png")
        self.visible = True
        self.position = 0

        cardList.append(self)
    def draw(self, target_surface):
        target_surface.blit(self.picture, (0,0))
