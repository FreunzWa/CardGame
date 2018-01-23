import pygame
import os
from utilities import *
from  CardDatabase import *
import numpy as np
import pdb
#colors
WHITE = (255,255,255)
BLACK = (0,0,0)


CARD_OUTLINE = BLACK
NORMAL_MONSTER = (244,177,38)
CARD_BACK = (200,0,0)
#dir
path = os.path.dirname(os.path.abspath(__file__))


#objects Lists
cardList = []
card_container_list = []

#card sizes
card_dimensions = (127, 192)
central_padding = 5

#fonts




#mouse
mouse_occupied = False
