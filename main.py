

import pygame
import time
import pdb
from definitions import *
from Card import *
from CardContainer import *

window_resolution = (640, 480)



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

    new_deck = CardContainer(size = 40)
    player_hand = CardContainer(size = 5, container_type = "hand")

    while game_running:

        #display
        window.fill(WHITE)
        for card_container in card_container_list:
            #getting the top card from the deck
            if pygame.key.get_pressed()[pygame.K_SPACE] and card_container.container_type == "deck":
                card_container.draw_card(player_hand)

            #drawing visible cards
            if card_container.container_type == "hand":
                for card in card_container.contents:
                    card.draw(window)
                    mouse_occupied = card.drag(mouse_occupied)





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
