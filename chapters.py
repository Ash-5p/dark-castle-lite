
from mechanics import *
from classes import *
from utilities import *
import random


def intro_chapter(player_character, player_name):
    """
    Intro Chapter - Called by run_game() after player chooses their character
    """
    clear_terminal_in_game(player_character, player_name)
    center_print(("You awaken and find yourself in a empty, dark room with stone walls.You look up \n" 
            "to a small window with iron bars in the far corner of the room. As your eyes \n"
            "trace the beams of moonlight peering into the room between the bars, you notice\n"
            "a thick wooden door which appears to be open ajar.\n"))

    center_print("Do you wait(w) or try to open the door(o)?\n")

def chapter_1a(player_character, player_name, homescreen):
    """
    Chapter 1a - Called by run_game() when player chooses to leave their cell
    """
    clear_terminal_in_game(player_character, player_name)
    center_print(("You push the door, which opens with a loud creak. You emerge in a long corridor \n"
            "lined with cell blocks like the one you just left. You notice what looks to be an \n "
            "unconscious guard clad in chainmail, laying still on the floor.\n"))

    center_print(("Not knowing what you will face, you toy with the idea of taking the chainmail for\n"
            "yourself\n"))

    while True:

        choice = input("Do you attempt to take the chainmail? Yes(y) / No(n)\n")

        if choice == "y":
            if random.randrange(1,11) >= 5:
                center_print("You manage to remove the Chainmail from the unconcious guard without waking him")
                player_character.item = "Chainmail"
                input()
                break
            else:
                center_print(("As you attempt to remove the guards armor he begins to stir, suddenly springing to his \n" 
                        "feet with an enraged look on his face. You attempt to reason with him, but your words \n"
                        "fall on deaf ears\n"))

                center_print("You must defend yourself!")

                input("Press any key to commence combat...")

                combat(guard, player_character, player_name, homescreen, "Chainmail", 11)
                break
        elif choice == "n":
            center_print("You sneak past the guard, being carful not to wake him")
            break
        else:
            center_print("You can't do that right now")

def chapter_1b(player_character, player_name, homescreen):
    """
    Chapter 1b - Called by run_game() when player chooses to wait in their cell
    """
    clear_terminal_in_game(player_character, player_name)
    center_print(("You wait in your cell, pondering how you woke up here. Suddenly, you hear a metal \n"
            "clattering sound, followed by a loud creak and bang as your cell door slams open \n"))
        
    center_print(("An enraged, dazed looking guard, clad in chainmail stands blocking the doorway. You \n"
            "attempt to reason with him, but your words fall on deaf ears\n"))

    center_print("You must defend yourself!")

    input("Press any key to commence combat...")

    combat(guard, player_character, player_name, homescreen, "Chainmail", 11)

def chapter_2a(player_character, player_name, homescreen):
    """
    Chapter 2a - Called by run_game() when player chooses to go left at the fork in the road
    """
    clear_terminal_in_game(player_character, player_name)
    center_print(("As you walk the winding hallway you find yourself following what looks to be an old water \n"
            "irrigation system. It's no longer functional due to decades worth of compacted sludge.\n"))
            
    center_print("You notice something sparkle within the mud filled channel")
    center_print("Do you attempt to remove it?\n")

    while True:
        choice = input("Yes(y) / No(n)\n")

        if choice == "y":
            if player_character.cunning >= 6: # Cunning skill check
                center_print("You fish the shiny object out of the compacted sludge without issue")
                center_print("It appears to be some sort of Focusing Crystal. Do you wish to keep it?")
                
                item_choice(player_character, "Focusing Crystal")
                break

            else:     
                center_print(("As you attempt to free the object, something reaches out of the sludge and grabs your \n"
                        "hand. You pull your hand away quickly, but lose sight of the shining object. The hand,\n"
                        "which appears to be made of the same compacted sludge from which it emerged, continues \n"
                        "to rise out of the channel. The mass of sewage starts to morph into a crude \n"
                        "impersonation of a person.\n"))

                center_print("The creature lets out a gargling roar and lunges for you!")

                center_print("You must defend yourself!")

                input("Press any key to commence combat...")

                combat(sludge_creature, player_character, player_name, homescreen, "Focusing Crystal", 5)
                break
        elif choice == "n":
            center_print("You ignore the object and carry on walking")
            break
        else:
            center_print("You can't do that right now")


def chapter_2b(player_character, player_name, homescreen):
    """
    Chapter 2b - Called by run_game() when player chooses to go right at the fork in the road
    """
    clear_terminal_in_game(player_character, player_name)
          
    center_print(("Walking down a narrow corridor you feel something whistle past your ear, catching your\n" 
            "lobe. (You lose 1hp). You turn around to see a hooded figure fleeing. You look at the\n"
            "ground in front of you and spot the projectile that was thrown at you.\n"))

    player_character.health -= 1
    center_print("\nDo you pick up the Throwing Knife? ")

    item_choice(player_character, "Throwing Knife")

def chapter_3a(player_character, player_name, homescreen):
    """
    Chapter 3a - Called by run_game() when player chooses to go up the staircase
    """
    clear_terminal_in_game(player_character, player_name)
          
    center_print(("You enter a large circular room. The only light source is a beam of moonlight which\n"
            "shines through a large well-like hole in the center of the ceiling, illuminating a \n"
            "single mirror in the middle of the room.\n"))
    
    center_print(("You approach the mirror to inspect it more closely, and notice that the surface of the\n"
            "mirror looks to be moving around like a viscous liquid. You are taken back by sudden\n"
            "realization that you appear to have no reflection!\n"))

    center_print("Though startled, you feel compelled to touch the mirrors surface\n")
    center_print("Do you touch the mirror?\n")

    while True:
        choice = input("Yes(y) / No(n)\n")

        if choice == "y":
            clear_terminal_in_game(player_character, player_name)
                    
            center_print(("As your finger comes into contact with the mirror, the surface breaks like water \n"
                    "and begins to wrap intself around your arm in a slithering, tentacle-like fashion. \n"
                    "Before you can even attempt to struggle, you are enveloped in a living silver goo.\n"))

            center_print("Unable to see or move, you feel that this is the end...")
            input()

            if player_character.item == "None":
                      
                center_print(("When suddenly the goo loosens it's grip on you and begins to melt away, as if dissolving.\n"
                        "When all the goo has dissipated, you are left facing the blank wooden frame where the \n"
                        "mirror once attached itself.\n"))

                center_print("You notice your skin is now coated in a film of iridescent sheen.\n")

                center_print("You here a hear a faint whisper, as if carried on the wind... \n")
                input()

                center_print('"Those abscent of greed are rewarded..."')
                player_character.item = "Mirror Film"
                input()
                break
            else:
                clear_terminal_in_game(player_character, player_name)
                        
                center_print((f"The mass of goo constricts tightly. You hear the {player_character.item} in your \n"
                        "pocket break. The goo tosses you aside and slithers back to the empty wooden \n"
                        "frame in the middle of the room. As the amorphous silver blob mounts itself onto \n"
                        "the frame you here a faint whisper, as if carried on the wind...\n")) 

                center_print('"Those with greed in their hearts should be punished... This was your first and only warning."')
                player_character.item = "None"
                player_character.health -= 5
                input("You loose 5hp and your item was destroyed.")
                break

        elif choice == "n":
            clear_terminal_in_game(player_character, player_name)
            center_print(("You resist the urge to touch the mirror and continue to stare at it for another\n"
                    "moment before moving on.\n"))
            center_print("You have the strangest feeling you saw something getting closer...\n")
            player_character.mirror = True
            input()
            break
        else:
            center_print("You can't do that right now")

def chapter_3b(player_character, player_name, homescreen):
    """
    Chapter 3b - Called by run_game() when player chooses to go down the staircase
    """
    clear_terminal_in_game(player_character, player_name)
           
    center_print(("Walking down the winding staircase you begin to feel uneasy. Suddenly a dark,\n"
            "ghostly apparition appears meterializes infront of you and begins to speak \n" 
            "in a distorted, otherworldly tone...\n"))

    input('"ThOsE wHo EnTEr My DoMaIn ShAlL kNoW FEAR!!!"\n')

    center_print("The spirit rises into the air ominously, then swoops down toward you!\n")

    center_print("You must defend yourself!\n")

    input("Press any key to commence combat...")
    
    combat(spirit, player_character, player_name, homescreen, "Lexicon", 6)

def chapter_4a(player_character, player_name, homescreen):
    """
    Chapter 4a - Called by run_game() when player chooses to go through the door
    """
    clear_terminal_in_game(player_character, player_name)
           
    center_print(("You enter a dimly lit, long, rectangular room when the door behind you suddenly \n"
            "slams shut. Ahead you see the shadowed outline of a large brutish creature \n"
            "moving a large carved slab in front of the door ahead.\n"))
    input()

    center_print(("Realizing that your only eixt is about to be blocked, you attmpt to run the\n"
            "length of the room before the door can be sealed... \n"))
    input()
    
    # Will be determined by a formula (cunning_check)
    if player_character.cunning == 9:
        center_print(("You dash accross the room, nimbly avoiding the jutting up peices of cobblestone\n"
                "floor. You manage to slip through the remaining gap in the door at the last\n"
                "second \n"))
        input()
        center_print(("You breath a sigh of relief for a moment, before the sudden realization hits\n"
                        "you... You are now in the room with whatever brutish abomination just\n"
                        "sealed the door!\n"))
        input()
        center_print(("The beast lets out a snarl and bears it's teeth. It stoops into a crouch\n"
                "ready to pounce on it's prey before lunging towards you!"))
        input()
        center_print("You must defend yourself!\n")

        input("Press any key to commence combat...")
        
        combat(beast, player_character, player_name, homescreen, random_item, 7)

    else:
        center_print(("You dash accross the room, trying to avoid the jutting up peices of cobblestone\n"
                "on the floor, but in your panic you trip and fall, foiling your chances of \n"
                "reaching the door in time.\n"))
        input()
        center_print(("As the door seals shut the room is left pitch black until suddenly the sconces\n"
                      "lining the room ignite, as if by magic. There is a brief silence before you \n"
                      "hear a rumbling coming from above.\n"))
        input()
        center_print(("You look upwards to see a ceiling covered in jagged metal spikes, slowly\n"
                      "decending towards you.\n"))
        input()
        center_print("There in't much time! What do you do?!\n")

        while True:
            choice = input("Attempt to move the slab(m). Look for another way out(w)")
            if choice == "m": # Might Check
                if player_character.might == 9:
                                  #############################################################################
                    center_print(("You force your weight against the huge slab blocking you path. Years of\n"
                                  "honing your strength pays off as you force the slab aside as if it were\n"
                                  "made of paper"))
                    break
                else:
                    center_print(("You attempt to move the huge slab blocking you path but to no avail.\n"
                                  "It is simply too heavy.\n"))
                    input()
                    center_print(("The jagged ceiling looms too close to escape...\n"
                                  "Your demise is certain.\n"))
                    center_print("Game Over\n")
                    center_input("Press any button to return to the homescreen")
                    homescreen()
                    
            elif choice == "w": # Wisdom check
                if player_character.wisdom == 9:
                                  #############################################################################
                    center_print(("You methodically look for any levers or switches that may lead to an\n"
                                  "escape. Your methodical approche pays off! As you pull one of the fire\n"
                                  "sconces on the wall, a hidden passage opens up."))
                    break
                else:
                    center_print(("You frantically search for a button or switch to help you escape but to\n"
                                  "no avail.\n"))
                    input()
                    center_print(("The jagged ceiling looms too close to escape...\n"
                                  "Your demise is certain.\n"))
                    center_print("Game Over\n")
                    center_input("Press any button to return to the homescreen")
                    homescreen()
            else:
                center_print("You can't do that right now!")
                

                    



def chapter_4b(player_character, player_name, homescreen):
    """
    Chapter 4b - Called by run_game() when player chooses to go through the passageway
    """
    clear_terminal_in_game(player_character, player_name)

def chapter_5a(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)

def chapter_5b(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)
    center_print("You fall")

def boss_a(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)

def boss_b(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)

def boss_c(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)