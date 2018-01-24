from definitions import *
from utilities import *

class DuelController:
    def __init__(self):

        self.duel_phases = ["draw","main","battle","end"]
        self.phase_number = 0
        self.player_turn  = 1

    def display(self, target_surface):
        draw_text("Player "+str(self.player_turn)+" : "+
        self.duel_phases[self.phase_number]+" Phase",
        (target_surface.get_width()*0.8,32), target_surface)

    def advance_phase(self):
        self.phase_number += 1
        if self.phase_number > len(self.duel_phases)-1:
            self.phase_number = 0
            #this reverts to the other player's turn
            self.player_turn = 3 - self.player_turn
