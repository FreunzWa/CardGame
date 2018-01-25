

import pygame
import time
import pdb

from definitions import *
import utilities as util
from Card import Card
from CardContainer import CardContainer
from DuelController import DuelController
from Button import Button
from Player import Player
from GameMaster import GameMaster



game_running = True


if __name__ == "__main__":

    start_time = time.time()
    pygame.init()
    print "Display Initialising . . ."
    print "Simulation start."

    #starts a new duel.
    """
    initialises a new duel
    creates all of the card containers necessary for a duel
    """
    #Starting values


    #defines the master controller, with it the window dimensiosns
    master = GameMaster((720,640))
    control = DuelController(master)
    pygame.display.set_caption("Ruler of Card Battles")
    clock = pygame.time.Clock()



    while game_running:
        clock.tick(60)
        if master.game_freeze == False:
            control.activities()

        #display
        master.window.fill(BACKGROUND)
        util.draw_text("Indev 0.7", (master.window.get_width()-120,4), master.window, text_color = WHITE)
        control.display(master.window)
        for card_container in card_container_list:
            card_container.display(master.window)


            #drawing visible cards
            if card_container.container_type == "hand" and control.phase_number== 1:

                for counter, card in enumerate(card_container.contents):
                    initial_mouse_occupied = mouse_occupied
                    mouse_occupied = card.drag(mouse_occupied, card.icon)
                    if card.pickup == True:
                        card.draw(master.window)
                    if initial_mouse_occupied and not mouse_occupied:
                        for node in control.duel_field.surfaces:
                            if util.mouse_in_region((node.x ,node.y, node.width, node.height)):
                                #checking if you are putting the card in one of the field spots
                                control.advance_phase()
                                card_container.pull_card(control.duel_field, ind = counter)
                                card.pos = (node.x+node.width/2-card_dimensions[0]/2, node.y+node.height/2-card_dimensions[1]/2)
                                break
                        break

            if card_container.container_type == "field":
                for counter, card in enumerate(card_container.contents):
                    card.draw(master.window)
                    initial_mouse_occupied = mouse_occupied
                    mouse_occupied = card.drag(mouse_occupied, card.icon)
                    if not initial_mouse_occupied and mouse_occupied:
                        card_container.pull_card(control.duel_graveyard, ind = counter)
                        mouse_occupied = False

        master.activities()

        pygame.display.flip()
        #ending the game
        for event in pygame.event.get():
            if event == pygame.QUIT:
                game_running = False

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            game_running = False


print "Simulation end."
print "Simulation ran for %0.2f seconds." %(time.time()-start_time)
pygame.quit()
