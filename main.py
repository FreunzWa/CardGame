

import pygame
import time
import pdb
from definitions import *
from Card import *
from CardContainer import *

window_resolution = (720, 640)



game_running = True


if __name__ == "__main__":

    start_time = time.time()
    pygame.init()
    print "Display Initialising . . ."
    print "Simulation start."
    window = pygame.display.set_mode(window_resolution)
    trialcard = Card()
    trialcard = Card(card_id = 1)
    trialcard = Card(card_id = 1)


    player_deck = CardContainer(size = 40)
    enemy_deck = CardContainer(size = 40, player_no = 2)
    player_hand = CardContainer(size = 5, container_type = "hand")
    field = CardContainer(size=0, container_type = "field")

    while game_running:

        #display
        window.fill(WHITE)

        for card_container in card_container_list:
            card_container.display(window)
            #getting the top card from the deck
            if pygame.key.get_pressed()[pygame.K_SPACE] and card_container.container_type == "deck":
                if card_container.player_no == 1:
                    card_container.pull_card(player_hand)

            #drawing visible cards
            if card_container.container_type == "hand":
                initial_mouse_occupied = mouse_occupied
                for counter, card in enumerate(card_container.contents):
                    mouse_occupied = card.drag(mouse_occupied, card.icon)
                    if card.pickup == True:
                        card.draw(window)
                    if initial_mouse_occupied and not mouse_occupied:
                        if card.pos[1] < 270:
                            print card.pos[1]
                            card_container.pull_card(field)

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
