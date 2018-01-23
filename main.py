

import pygame
import time
import pdb
from definitions import *
from Card import *


window_resolution = (640, 480)



game_running = True


if __name__ == "__main__":

    start_time = time.time()
    pygame.init()
    print "Display Initialising . . ."
    print "Simulation start."
    window = pygame.display.set_mode(window_resolution)
    trialcard = Card()
    trialcard = Card(card = "fish_man", pos=(300,0))
    while game_running:

        #display
        window.fill(WHITE)
        for card in cardList:
            card.draw(window)



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
