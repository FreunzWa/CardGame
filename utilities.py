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
            corrected_name.append(char.upper())
            capitalize = False
        elif char == "_":
            capitalize = True
        else:
            corrected_name.append(char)
