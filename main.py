

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

window_resolution = (720, 640)







game_running = True


if __name__ == "__main__":

    start_time = time.time()
    pygame.init()
    print "Display Initialising . . ."
    print "Simulation start."
    window = pygame.display.set_mode(window_resolution)
    #starts a new duel.
    """
    initialises a new duel
    creates all of the card containers necessary for a duel
    """
    #Starting values
    duel_field = CardContainer(size=0, container_type = "field")

    duel_graveyard = CardContainer(size = 0, container_type = "graveyard")

    player1 = Player(type = "human")
    player1.deck =CardContainer(size = 40)
    player1.hand = CardContainer(size = 5, container_type = "hand")
    player2 = Player(type = "cpu", deck=CardContainer(size = 40), player_no = 2)
    player2.deck =CardContainer(size = 40)
    player2.hand = CardContainer(size = 5, player_no = 2, container_type = "hand")

    duel_controller = DuelController(player1, player2)



    pygame.display.set_caption("Ruler of Card Battles")
    clock = pygame.time.Clock()
    while game_running:
        clock.tick(60)
        #display
        window.fill(BACKGROUND)
        util.draw_text("Indev 0.4", (window.get_width()-120,4), window)
        duel_controller.display(window)
        for card_container in card_container_list:
            card_container.display(window)


            #drawing visible cards
            if card_container.container_type == "hand":

                for counter, card in enumerate(card_container.contents):
                    initial_mouse_occupied = mouse_occupied
                    mouse_occupied = card.drag(mouse_occupied, card.icon)
                    if card.pickup == True:
                        card.draw(window)
                    if initial_mouse_occupied and not mouse_occupied:
                        for node in duel_field.surfaces:
                            if util.mouse_in_region((node.x ,node.y, node.width, node.height)):
                                card_container.pull_card(duel_field, ind = counter)
                                card.pos = (node.x+node.width/2-card_dimensions[0]/2, node.y+node.height/2-card_dimensions[1]/2)
                                break
                        break

            if card_container.container_type == "field":
                for counter, card in enumerate(card_container.contents):
                    card.draw(window)
                    initial_mouse_occupied = mouse_occupied
                    mouse_occupied = card.drag(mouse_occupied, card.icon)
                    if not initial_mouse_occupied and mouse_occupied:
                        card_container.pull_card(duel_graveyard, ind = counter)
                        mouse_occupied = False

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
