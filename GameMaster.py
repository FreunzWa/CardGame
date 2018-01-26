from definitions import *
import utilities as util
import pygame
from Player import Player
import time
from Card import Card
import numpy as np
import random
from CardContainer import CardContainer
from CardDatabase import *
import pdb
class GameMaster:
    def __init__(self, (window_width, window_height)):
        """
        a game master instance is created at the start of the game. it controls
        switching in between scenes, and stores variables which must be kept
        track of for the entire game, like the player trunk and decks.
        it also contains methods for displaying information to the player,
        like messages.
        """
        self.display_text = []
        self.text_scroll_position = 0
        self.game_freeze = False

        release_mode = False

        if release_mode == True:
            pygame.mixer.init()
            pygame.mixer.music.load(path+"\\res\\bgm\\bgm01.mp3")
            pygame.mixer.music.play(loops = -1)
            self.window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
        else:
            self.window = pygame.display.set_mode((window_width, window_height))
        self.trunk = CardContainer(size = 0, container_type = "trunk")

        self.menu_tree = {
            "main menu": ["deck builder", "campaign mode", "options"],
        }
        self.possible_scenes = ["main menu", "deck builder", "campaign mode",
        "options","duel","get card"]
        self.current_scene = "duel"

    def activities(self):
        self.message_display(self.display_text)

        if self.current_scene == "get card":
            if self.game_freeze== False:
                bonus_card_ind = random.randint(0,len(card_dict)+1)
                for key in card_dict:
                    if card_dict[key]["ID"] == bonus_card_ind:
                        self.display_text = ["You got a " + util.cardname_correction(key)+"!"]
                        new_card = Card(card_id = bonus_card_ind, container_type = "trunk", player_no=1 )
                        self.trunk.contents = np.append(self.trunk.contents,new_card)
                        self.scene_goto("duel")
                        break


    def scene_goto(self, scene):
        """
        checks if the scene which is being switched to is an available scene,
        otherwise it raises an Error.
        """
        if scene in self.possible_scenes:
            self.current_scene = scene
        else:
            raise ValueError("Error! Trying to go to a non-existing scene!")

    def message_display(self, text, location = "bottom"):

        #defines the rectangular surface
        """
        params:
        text = takes a list of strings, that are cycle through upon user input.
        """

        if len(self.display_text) == 0:
            return 0
        self.game_freeze = True
        border_width = 2
        message_proportion = 0.2
        surf_message = pygame.Surface((self.window.get_width(), self.window.get_height()*(message_proportion)))
        surf_message.fill(BLACK)
        util.outline_surface(surf_message, RED, border_width)
        #the triangle prompting to advance

        if int(time.time()*2 % 2) ==0:
            triangle_color = WHITE
        else:
            triangle_color = BLACK
        pygame.draw.polygon(surf_message, triangle_color,
        ((surf_message.get_width()-22,surf_message.get_height()-22),
        (surf_message.get_width()-6,surf_message.get_height()-22),
        (surf_message.get_width()-14,surf_message.get_height()-6)))


        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key == input_SPACE:
                self.text_scroll_position += 1
                if self.text_scroll_position == len(text):
                    self.text_scroll_position = 0
                    self.game_freeze = False
                    self.display_text = []
                    return 0
        if location == "bottom":
            util.draw_text(text[self.text_scroll_position], (border_width*2, border_width*2),surf_message, WHITE, text_size = 20)
            self.window.blit(surf_message, (0,self.window.get_height()*(1-message_proportion)))
