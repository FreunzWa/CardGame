import os
from CardDatabase import *
import pygame
#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
DARK_BROWN = (92,60,17)
RED = (255,0,0)

BACKGROUND = (122,90,47)
CARD_OUTLINE = BLACK
NORMAL_MONSTER = (244,177,38)
CARD_BACK = (200,0,0)
#dir
path = os.path.dirname(os.path.abspath(__file__))


#objects Lists
cardList = []
card_container_list = []

#card sizes
card_dimensions = (127, 160)
central_padding = 5

#display
fullscreen = 1




#mouse
mouse_occupied = False

#game rules
hand_capacity = 4


#input
input_RETURN = pygame.K_RETURN
input_SPACE = pygame.K_SPACE

#rarities
