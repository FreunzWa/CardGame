from definitions import *
import utilities as util

class DuelController:
    def __init__(self, player1, player2):
        """
        the duel controller is initialised upon every new battle
        player 1 and 2 are player objects
        """
        self.duel_phases = ["draw","main","battle","end"]
        self.phase_number = 0
        self.player_turn  = 1
        self.timer = -1

    def display(self, target_surface):
        util.draw_text("Player "+str(self.player_turn)+" : "+
        self.duel_phases[self.phase_number]+" Phase",
        (target_surface.get_width()*0.8,32), target_surface)

    def advance_phase(self):
        self.phase_number += 1
        if self.phase_number > len(self.duel_phases)-1:
            self.phase_number = 0
            #this reverts to the other player's turn
            self.player_turn = 3 - self.player_turn

    def timer(self, latency, timer):
        """
        function: sets the timer variable to latency, this then counts down
        until it reaches 0.
        """
        if timer == -1:
            timer = latency
        else:
            if timer >0:
                timer -=1


    def activities(self):
        ##DRAW PHASE activities
        timer(60,timer)
        if timer == 0:
            if phase_number == 0:
                if player_turn == 1:
                    pass
                else:
                    pass
                #need player input to draw.
