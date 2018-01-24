

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

    new_field = CardContainer(size=0, container_type = "field")
    player_deck = CardContainer(size = 40)
    enemy_deck = CardContainer(size = 40, player_no = 2)
    player_hand = CardContainer(size = 5, container_type = "hand")
    enemy_hand = CardContainer(size = 5, player_no = 2, container_type = "hand")

    pygame.display.set_caption("Ruler of Card Battles")
    #the objects that will be used in teh game are defined here.
    game_field = new_field
    game_graveyard = CardContainer(size = 0, container_type = "graveyard")
    clock = pygame.time.Clock()
    while game_running:
        clock.tick(60)
        #display
        window.fill(BACKGROUND)
        draw_text("Indev 0.4", (window.get_width()-120,4), window)
        for card_container in card_container_list:
            card_container.display(window)
            #getting the top card from the deck
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and card_container.container_type == "deck":
                        if card_container.player_no == 1:
                            card_container.pull_card(player_hand)

            #drawing visible cards
            if card_container.container_type == "hand":

                for counter, card in enumerate(card_container.contents):
                    initial_mouse_occupied = mouse_occupied
                    mouse_occupied = card.drag(mouse_occupied, card.icon)
                    if card.pickup == True:
                        card.draw(window)
                    if initial_mouse_occupied and not mouse_occupied:
                        for node in game_field.surfaces:
                            if mouse_in_region((node.x ,node.y, node.width, node.height)):
                                card_container.pull_card(game_field, ind = counter)
                                card.pos = (node.x+node.width/2-card_dimensions[0]/2, node.y+node.height/2-card_dimensions[1]/2)
                                break
                        break

            if card_container.container_type == "field":
                for counter, card in enumerate(card_container.contents):
                    card.draw(window)
                    initial_mouse_occupied = mouse_occupied
                    mouse_occupied = card.drag(mouse_occupied, card.icon)
                    if not initial_mouse_occupied and mouse_occupied:
                        card_container.pull_card(game_graveyard, ind = counter)
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
