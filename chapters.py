from mechanics import *
from classes import *
from utilities import *
import random


def intro_chapter(player_character, player_name):
    """
    Intro Chapter - Called by run_game() after player chooses their character
    """
    clear_terminal_in_game(player_character, player_name)
    center_print(
        "You awaken and find yourself in a empty, dark room with stone walls. "
        "You look up \nto a small window with iron bars in the far corner of "
        "the room. As your eyes \ntrace the beams of moonlight peering into "
        "the room between the bars, you notice\na thick wooden door which "
        "appears to be open ajar.\n"
    )

    center_print("Do you wait(w) or try to open the door(o)?\n")


def chapter_1a(player_character, player_name, homescreen, base_stats):
    """
    Chapter 1a - Called by run_game() when player chooses to leave their cell
    """
    clear_terminal_in_game(player_character, player_name)
    center_print(
        "You push the door, which opens with a loud creak. You emerge in a "
        "long corridor \nlined with cell blocks like the one you just left. "
        "You notice what looks to be an \nunconscious guard clad in chainmail, "
        "laying still on the floor.\n"
    )

    center_print(
        "Not knowing what you will face, you toy with the idea of taking the "
        "chainmail for\nyourself\n"
    )

    while True:

        choice = input("Do you attempt to take the chainmail? Yes(y) / No(n)\n")

        if choice == "y":
            if random.randrange(1,11) >= 5:
                center_print(
                    "You manage to remove the Chainmail from the unconcious "
                    "guard without waking him"
                )
                player_character.item = "Chainmail"
                input()
                break
            else:
                center_print(
                    "As you attempt to remove the guards armor he begins to "
                    "stir, suddenly springing to his \nfeet with an enraged "
                    "look on his face. You attempt to reason with him, but your"
                    " words \nfall on deaf ears\n"
                )

                center_print("You must defend yourself!")

                center_input("Press enter to commence combat...")

                combat(
                    guard, player_character, player_name, homescreen, 
                "Chainmail", 11, base_stats
                )
                break
        elif choice == "n":
            center_print(
                "You sneak past the guard, being carful not to wake him"
            )
            break
        else:
            center_print(f'You can\'t do "{choice}" right now')


def chapter_1b(player_character, player_name, homescreen, base_stats):
    """
    Chapter 1b - Called by run_game() when player chooses to wait in their cell
    """
    clear_terminal_in_game(player_character, player_name)
    center_print(
        "You wait in your cell, pondering how you woke up here. Suddenly, you "
        "hear a metal \nclattering sound, followed by a loud creak and bang as "
        "your cell door slams open \n"
    )
        
    center_print(
        "An enraged, dazed looking guard, clad in chainmail stands blocking "
        "the doorway. You \nattempt to reason with him, but your words fall on "
        "deaf ears\n"
    )

    center_print("You must defend yourself!")

    center_input("Press enter to commence combat...")

    combat(
        guard, player_character, player_name, homescreen, "Spiked Gloves", 11, 
        base_stats
    )


def chapter_2a(player_character, player_name, homescreen, base_stats):
    """
    Chapter 2a - Called by run_game() when player chooses to go left at the 
                 fork in the road
    """
    clear_terminal_in_game(player_character, player_name)
    center_print(
        "As you walk the winding hallway you find yourself following what looks"
        "to be an\nold water irrigation system. It's no longer functional due"
        "to decades\nworth of compacted sludge.\n"
    )
            
    center_print("You notice something sparkle within the mud filled channel")
    center_print("Do you attempt to remove it?\n")

    while True:
        center_print("Yes(y) / No(n)\n")
        choice = input()

        if choice == "y":
            if player_character.cunning >= 6: # Cunning skill check
                center_print(
                    "You fish the shiny object out of the compacted sludge "
                    "without issue"
                )
                center_print("It appears to be some sort of Focusing Crystal.")
                
                item_choice(player_character, base_stats, "Focusing Crystal")
                break

            else:     
                center_print(
                    "As you attempt to free the object, something reaches out "
                    "of the sludge and grabs your \nhand. You pull your hand "
                    "away quickly, but lose sight of the shining object. The "
                    "hand,\n which appears to be made of the same compacted "
                    "sludge from which it emerged, continues \n to rise out of "
                    "the channel. The mass of sewage starts to morph into a "
                    "crude \nimpersonation of a person.\n"
                )

                center_print(
                    "The creature lets out a gargling roar and lunges for you!"
                )

                center_print("You must defend yourself!")

                center_input("Press enter to commence combat...")

                combat(
                    sludge_creature, player_character, player_name, homescreen, 
                    "Focusing Crystal", 5, base_stats
                )
                break
        elif choice == "n":
            center_print("You ignore the object and carry on walking")
            break
        else:
            center_print(f'You can\'t do "{choice}" right now')


def chapter_2b(player_character, player_name, homescreen, base_stats):
    """
    Chapter 2b - Called by run_game() when player chooses to go right at the 
                 fork in the road
    """
    clear_terminal_in_game(player_character, player_name)
          
    center_print(
        "Walking down a narrow corridor you feel something whistle past your "
        "ear, catching your\nlobe. (You lose 1hp). You turn around to see a "
        "hooded figure fleeing. You look at the\nground in front of you and "
        "spot the projectile that was thrown at you.\n"
    )

    player_character.health -= 1

    item_choice(player_character, base_stats, "Throwing Knife")


def chapter_3a(player_character, player_name, homescreen, base_stats):
    """
    Chapter 3a - Called by run_game() when player chooses to go up the staircase
    """
    clear_terminal_in_game(player_character, player_name)
          
    center_print(
        "You enter a large circular room. The only light source is a beam of "
        "moonlight which\nshines through a large well-like hole in the center "
        "of the ceiling, illuminating a \nsingle mirror in the middle of the "
        "room.\n"
    )
    
    center_print(
        "You approach the mirror to inspect it more closely, and notice that "
        "the surface of the\nmirror looks to be moving around like a viscous "
        "liquid. You are taken back by sudden\nrealization that you appear to "
        "have no reflection!\n"
    )

    center_print(
        "Though startled, you feel compelled to touch the mirrors surface\n"
    )
    center_print("Do you touch the mirror?\n")

    while True:
        choice = input("Yes(y) / No(n)\n")

        if choice == "y":
            clear_terminal_in_game(player_character, player_name)
                    
            center_print(
                "As your finger comes into contact with the mirror, the surface"
                " breaks like water \nand begins to wrap intself around your "
                "arm in a slithering, tentacle-like fashion.\nBefore you can "
                "even attempt to struggle, you are enveloped in a living "
                "silver goo.\n"
            )

            center_print(
                "Unable to see or move, you feel that this is the end..."
            )
            input()

            if player_character.item == "None":
                      
                center_print(
                    "When suddenly the goo loosens it's grip on you and begins "
                    "to melt away, as if dissolving.\nWhen all the goo has "
                    "dissipated, you are left facing the blank wooden frame "
                    "where the\nmirror once attached itself.\n"
                )

                center_print(
                    "You notice small iridescent sphere sitting on the "
                    "ground.\n"
                )

                center_print(
                    "You here a hear a faint whisper, as if carried on"
                    " the wind...\n"
                )
                input()

                center_print('"Those abscent of greed are rewarded..."')
                player_character.item = "Mirror Sphere"
                input()
                break
            else:
                clear_terminal_in_game(player_character, player_name)
                        
                center_print(
                    "The mass of goo constricts tightly. You hear the "
                    f"{player_character.item} in your\npocket break. The goo "
                    "tosses you aside and slithers back to the empty wooden\n"
                    "frame in the middle of the room. As the amorphous silver "
                    "blob mounts itself onto\nthe frame you here a faint "
                    "whisper, as if carried on the wind...\n"
                )

                center_print(
                    '"No aid shall be given to those with greed in '
                    'their hearts... This was your first and only warning."'
                )
                player_character.item = "None"
                player_character.health -= 5
                input("You loose 5hp and your item was destroyed.")
                break

        elif choice == "n":
            clear_terminal_in_game(player_character, player_name)
            center_print(
                "You resist the urge to touch the mirror and continue to stare "
                "at it for another\nmoment before moving on.\n"
            )
            center_print(
                "You have the strangest feeling you saw something "
                "getting closer...\n"
            )
            player_character.mirror = True
            input()
            break
        else:
            center_print(f'You can\'t do "{choice}" right now')


def chapter_3b(player_character, player_name, homescreen, base_stats):
    """
    Chapter 3b - Called by run_game() when player chooses to go down the 
                 staircase
    """
    clear_terminal_in_game(player_character, player_name)
           
    center_print(
        "Walking down the winding staircase you begin to feel uneasy. Suddenly "
        "a dark,\nghostly apparition appears meterializes infront of you and "
        "begins to speak \nin a distorted, otherworldly tone...\n"
    )

    center_input('"ThOsE wHo EnTEr My DoMaIn ShAlL kNoW FEAR!!!"\n')

    center_print(
        "The spirit rises into the air ominously, then swoops down "
        "toward you!\n"
    )

    center_print("You must defend yourself!\n")

    center_input("Press enter to commence combat...")
    
    combat(
        spirit, player_character, player_name, homescreen, "Lexicon", 6, 
        base_stats
    )


def chapter_4a(player_character, player_name, homescreen, base_stats):
    """
    Chapter 4a - Called by run_game() when player chooses to go through the door
    """
    clear_terminal_in_game(player_character, player_name)
           
    center_print(
        "You enter a dimly lit, long, rectangular room when the door behind you"
        " suddenly \nslams shut. Ahead you see the shadowed outline of a large "
        "brutish creature \nmoving a large carved slab in front of the door "
        "ahead.\n"
    )
    input()

    center_print(
        "Realizing that your only exit is about to be blocked, you attmpt to "
        "run the\nlength of the room before the door can be sealed... \n"
    )
    input()
    
    # Will be determined by a formula (cunning_check)
    if player_character.cunning == 9:
        center_print(
            "You dash accross the room, nimbly avoiding the jutting up peices "
            "of cobblestone\nfloor. You manage to slip through the remaining "
            "gap in the door at the last\nsecond \n"
        )
        input()
        center_print(
            "You breath a sigh of relief for a moment, before the sudden "
            "realization hits\nyou... You are now in the room with whatever "
            "brutish abomination just\nsealed the door!\n"
        )
        input()
        center_print(
            "The beast lets out a snarl and bears it's teeth. It stoops into a "
            "crouch\nready to pounce on it's prey before lunging towards you!"
        )
        input()
        center_print("You must defend yourself!\n")

        center_input("Press enter to commence combat...")
        
        combat(
            beast, player_character, player_name, homescreen, random_item, 7,
            base_stats
        )

    else:
        center_print(
            "You dash accross the room, trying to avoid the jutting up peices "
            "of cobblestone\non the floor, but in your panic you trip and fall,"
            " foiling your chances of \nreaching the door in time.\n"
        )
        input()
        center_print(
            "As the door seals shut the room is left pitch black until suddenly"
            " the sconces\nlining the room ignite, as if by magic. There is a "
            "brief silence before you \nhear a rumbling coming from above.\n"
        )
        input()
        center_print(
            "You look upwards to see a ceiling covered in jagged metal spikes, "
            "slowly\ndecending towards you.\n"
        )
        input()
        center_print("There in't much time! What do you do?!\n")
        center_print(
            "Attempt to move the slab(m). Look for another way out(w)\n"
        )

        while True:


            def chapter_4a_death():
                """
                Handles game over if player fails all skill checks on chapter 4a
                """
                center_print("The jagged ceiling looms too close to escape.\n")
                center_input("Your demise is certain...\n")
                center_print("Game Over\n")
                center_input("Press any button to return to the homescreen")
                homescreen()


            choice = input()
            if choice == "m": # Might Check
                if player_character.might == 9:
                    center_input(
                        "You force your weight against the huge slab blocking "
                        "your path. Years of\nhoning your strength pays off as "
                        "you force the slab aside as if it were\nmade of paper."
                    )
                    center_input(
                        "As you walk through the door you see the beast like "
                        "humanoid who sealed\nthe door. Intimidated by your "
                        "feat of strength it stares at you with a\nfearful "
                        "expression before fleeing. You notice it drops "
                        "something..."
                    )
                    item_choice(player_character, base_stats, random_item)
                    break
                else:
                    center_print(
                        "You attempt to move the huge slab blocking you path" 
                        "but to no avail.\nIt is simply too heavy.\n"
                    )
                    input()

                    chapter_4a_death()
                    
            elif choice == "w": # Wisdom check
                if player_character.wisdom == 9:
                    center_input(
                        "You methodically look for any levers or switches that "
                        "may lead to an\nescape. Your methodical approche pays "
                        "off! As you pull one of the fire\nsconces on the wall," 
                        " a hidden passage opens up and you slip away."
                    )
                    break
                else:
                    center_print(
                        "You frantically search for a button or switch to help "
                        "you escape but to\nno avail.\n"
                    )
                    chapter_4a_death()
            else:
                center_print(f'You can\'t do "{choice}" right now')
                

def chapter_4b(player_character, player_name, homescreen, base_stats):
    """
    Chapter 4b - Called by run_game() when player chooses to go through the 
                 passageway
    """
    clear_terminal_in_game(player_character, player_name)


def chapter_5a(player_character, player_name, homescreen, base_stats):
    clear_terminal_in_game(player_character, player_name)
    center_print("You enter a chamber")

def chapter_5b(player_character, player_name, homescreen, base_stats):
    clear_terminal_in_game(player_character, player_name)
    center_print("You fall")


def boss_a(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)


def boss_b(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)


def boss_c(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)
