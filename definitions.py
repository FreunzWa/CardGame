import pygame
import os
from utilities import *
from  CardDatabase import *
#colors
WHITE = (255,255,255)
BLACK = (0,0,0)

CARD_OUTLINE = BLACK
NORMAL_MONSTER = (244,177,38)

#dir
path = os.path.dirname(os.path.abspath(__file__))


#objects Lists
cardList = []


#card sizes
card_dimensions = (127, 192)
central_padding = 5

#fonts
