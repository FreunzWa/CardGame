from definitions import *
import utilities as util
import pygame
from Player import Player
from Card import Card
from CardContainer import CardContainer
import pdb

class DuelController:
    def __init__(self):
        """
        the duel controller is initialised upon every new battle
        player 1 and 2 are player objects
        """
        self.duel_phases = ["draw","main","battle","end"]
        self.phase_number = 0
        self.player_turn  = 1
        self.timer = -1

        self.player1 = Player(type = "human")
        self.player1.deck =CardContainer(size = 12)
        self.player1.hand = CardContainer(size = 3, container_type = "hand")
        self.player2 = Player(type = "cpu",  player_no = 2)
        self.player2.deck =CardContainer(size = 12, player_no = 2, container_type = "deck")
        self.player2.hand = CardContainer(size = 3, player_no = 2, container_type = "hand")
        self.duel_field = CardContainer(size=0, container_type = "field")
        self.duel_graveyard = CardContainer(size = 0, container_type = "graveyard")

        self.latency = 60


    def display(self, target_surface):
        util.draw_text("Player "+str(self.player_turn)+" : "+
        self.duel_phases[self.phase_number]+" Phase",
        (target_surface.get_width()*0.8,32), target_surface, text_color = WHITE)

    def advance_phase(self):
        self.phase_number += 1
        self.timer = -1
        if self.phase_number > len(self.duel_phases)-1:
            self.phase_number = 0
            #this reverts to the other player's turn
            self.player_turn = 3 - self.player_turn



    def activities(self):
        ##DRAW PHASE activities
        if self.timer == -1:
            self.timer = self.latency
        if self.timer >0:
            self.timer -=1


        if self.timer == 0:
            if self.phase_number == 0:
                #if draw phase.

                if self.player_turn == 1:
                    if len(self.player1.hand.contents) > hand_capacity-1 or len(self.player1.deck.contents)==0:#checking if the hand is full
                        self.advance_phase()
                    elif pygame.key.get_pressed()[pygame.K_SPACE]:
                        self.advance_phase()
                        self.player1.deck.pull_card(self.player1.hand,0)
                elif self.player_turn ==2:
                    if len(self.player2.hand.contents) > hand_capacity-1 or len(self.player2.deck.contents)==0:
                        self.advance_phase()
                    else:
                        self.advance_phase()
                        self.player2.deck.pull_card(self.player2.hand,0)

            elif self.phase_number == 1:
                #if main phase

                for card in self.duel_field.contents:
                    if card.player_no == self.player_turn:
                        self.advance_phase()

                if self.player_turn == 2 and self.phase_number ==1:
                    drawn_card = self.player2.hand.pull_card(self.duel_field, 0)
                    node = self.duel_field.surfaces[0]
                    drawn_card.pos = (node.x+node.width/2-card_dimensions[0]/2, node.y+node.height/2-card_dimensions[1]/2)

                    self.advance_phase()

            elif self.phase_number == 2:
                #if battle phase

                if len(self.duel_field.contents) < 2:
                    self.advance_phase()
                else:
                    if (self.duel_field.contents[0].stats[0] < self.duel_field.contents[1].stats[0]):
                        remove_ind = 0
                    elif  (self.duel_field.contents[0].stats[0] > self.duel_field.contents[1].stats[0]):
                        remove_ind = 1
                    else:
                        #when set to negative 1 it removes both cards, it is a draw
                        remove_ind = -1


                    for counter, card in enumerate(self.duel_field.contents):
                        if counter == remove_ind:
                            self.duel_field.pull_card(self.duel_graveyard, counter)
                        if remove_ind == -1:
                            #both cards are destroyed.
                            self.duel_field.pull_card(self.duel_graveyard, 0)
                        self.advance_phase()



                #need player input to draw.

            elif self.phase_number == 3:

                #if end phase
                self.advance_phase()
