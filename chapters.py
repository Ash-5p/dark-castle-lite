from run import *
from utilities import clear_terminal, blank_lines, return_home

def intro_chapter():
    clear_terminal()
    print("You awaken and find yourself in a empty, dark room with stone walls. \n\
You look up to a small window with iron bars in the far corner of the room. \n\
As your eyes trace the beams of moonlight peering into the room between the bars, \n\
you notice a thick wooden door which appears to be open ajar.\n")

    print("Do you wait(w) or try to open the door(o)?\n")

def chapter_1a():
    clear_terminal()
    print("You push the door, which opens with a loud creak. You emerge in a long corridor\n\
lined with cell blocks line the one you just left. You notice what looks \n\
to be an unconscious guard clad in chainmail laying still on the floor.\n")

    print("Not knowing what you will face, you toy with the idea of taking the chainmail\n\
        for yourself")

    input("Do you attempt to take the chainmail? Yes(y) / No(n)")



def chapter_1b():
    clear_terminal()
    print("You wait in your cell, pondering how you woke up here. Suddenly, you \n\
hear a metal clattering sound, followed by a loud creak and bang as your cell door \n\
slams open\n")
    
    print("An enraged, dazed looking guard, clad in chainmail stands blocking the doorway. \n\
You attempt to reason with him, but your words fall on deaf ears\n")

    print("You must defend yourself!")

    input("Press any key to commence combat...")