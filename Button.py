import pygame
import utilities as util
from definitions import *

class Button:
    def __init__(self,(x,y, width, height), text = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite = pygame.Surface((self.width, self.height))
        self.sprite.fill(BLACK)
        util.outline_surface(self.sprite, color = RED, width = 2)
        self.text = text


    def draw(self, target_surface):
        util.draw_text(self.sprite, (2,2), text_color = WHITE, text_size = 15)
        target_surface.blit(self.sprite, (self.x, self.y))
