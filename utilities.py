from definitions import *

def cardname_correction(cardname):
    """
    @function
    - takes an input cardname formatted for loading png file, like big_pot
    and reformats this into acceptable format for output. in this case, Big Pot.
    @params:
    the cardname formatted for loading png file.
    """
    corrected_name = ""
    capitalize = True
    for ind, char in enumerate(cardname):
        if capitalize:
            corrected_name = corrected_name + char.upper()
            capitalize = False
        elif char == "_":
            capitalize = True
            corrected_name = corrected_name + " "
        else:
            corrected_name = corrected_name + char

    return corrected_name

def draw_text(text, (x,y), target_surface, text_color = (0,0,0), text_size = 14):
    """
    @function
    draws a text surface containing text for displaying information to user
    @params
    string text = the text to be drawn
    int (x,y) = the location for drawing
    target_surface = the surface to be drawn on
    text_color = color of text.
    """
    text = str(text)
    game_font1 = pygame.font.Font("freesansbold.ttf", text_size)
    text_surface = game_font1.render(text, True, text_color)
    target_surface.blit(text_surface, (x,y))
