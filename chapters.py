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
        "You look up to a small window with iron bars in the far corner of "
        "the room. As your eyes trace the beams of moonlight peering into "
        "the room between the bars, you notice a thick wooden door which "
        "appears to be open ajar.\n"
    )

    center_print("Do you wait(w) or try to open the door(o)?\n")


def chapter_1a(player_character, player_name, homescreen, base_stats):
    """
    Chapter 1a - Called by run_game() when player chooses to leave their cell
    """
    clear_terminal_in_game(player_character, player_name)
    center_input(
        "You push the door, which opens with a loud creak. You emerge in a "
        "long corridor \nlined with cell blocks like the one you just left. "
        "You notice what looks to be an \nunconscious guard clad in chainmail, "
        "laying still on the floor. (press enter to continue...)\n"
    )

    center_input(
        "Not knowing what you will face, you toy with the idea of taking the "
        "chainmail for yourself. (press enter to continue...)\n"
    )

    center_print("Do you attempt to take the chainmail? Yes(y) / No(n)\n")

    while True:

        choice = input().strip()

        if choice == "y":
            if random.randrange(1,11) >= 5:
                center_print(
                    "You manage to remove the Chainmail from the unconcious "
                    "guard without waking him. (press enter to continue...)"
                )
                player_character.item = "Chainmail"
                input()
                break
            else:
                center_input(
                    "As you attempt to remove the guards armor he begins to "
                    "stir, suddenly springing to his feet with an enraged "
                    "look on his face. You attempt to reason with him, but "
                    "your words fall on deaf ears. (press enter to "
                    "continue...)\n"
                )

                center_print("You must defend yourself!")

                center_input("Press enter to commence combat...")

                combat(
                    guard, player_character, player_name, homescreen, 
                "Chainmail", 11, base_stats
                )
                break
        elif choice == "n":
            center_input(
                "You sneak past the guard, being carful not to wake him. "
                "(press enter to continue...)"
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
        guard, player_character, player_name, homescreen, "Chainmail", 11, 
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
        choice = input().strip()

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
          
    center_input(
        "Walking down a narrow corridor you feel something whistle past your "
        "ear, catching your\nlobe. (You lose 1hp). "
        "(press enter to continue...)\n" 
    )
            
    death_outside_combat(player_character, player_name, homescreen, 1)
    center_input(
        "You turn around to see a hooded figure fleeing. You look at the "
        "ground in front of you and spot the projectile that was thrown at"
        " you. (press enter to continue...)\n"
)
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
                input("You loose 5hp and your item was destroyed.")
                death_outside_combat(
                    player_character, player_name, homescreen, 5
                )
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
    if player_character.cunning >= 9:
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


            choice = input().strip()
            if choice == "m": # Might Check
                if player_character.might >= 9:
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
                if player_character.wisdom >= 9:
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

    center_input(
    "You step through the narrow passageway, the walls around you feel as if"
    " they are closing in. The air is damp and heavy, making it hard to "
    "breathe. (press enter to continue...)\n"
    )
    center_input(
        "The only light comes from faintly glowing moss lining the cracks in "
        "the stone walls. (press enter to continue...)\n"
    )
    center_input(
        "Suddenly, the ground beneath you gives way, and you tumble down a "
        "hidden chute, sliding into the darkness! "
        "(press enter to continue...)\n"
    )
    if player_character.cunning >= 6:  # Cunning check for avoiding damage
        center_input(
            "With quick reflexes, you manage to control your fall, avoiding any"
            " serious injury as you land at the bottom."
            "(press enter to continue...)\n"
        )
    else:
        center_input(
            "You crash to the ground painfully, your body aching from the "
            "impact.\n"
        )
        # Deduct health for failing the skill check
        center_input(f"You lose 5hp.\n")
        death_outside_combat(player_character, player_name, homescreen, 5)



def chapter_5a(player_character, player_name, homescreen, base_stats):
    clear_terminal_in_game(player_character, player_name)
    center_input(
        "You enter an throne room. You scan the room and see three doors. Each "
        "door is labeled with a golden plaque. (press enter to continue...)\n"
    )
    center_input(
        'To your left is a door labled "Armory"(a), to your right is a door '
        'labeled "Library"(l), and ahead is one labled "Treasury"(t).'
        '(press enter to continue...)\n'
    )
    center_print("Which room do you enter?\n")
    while True:
        choice = input().strip()
        if choice == "a":
            boss_a(player_character, player_name, homescreen, base_stats)
            break
        elif choice == "l":
            boss_b(player_character, player_name, homescreen, base_stats)
            break
        elif choice == "t":
            boss_c(player_character, player_name, homescreen, base_stats)
            break
        else:
            center_print(f'You can\'t do "{choice}" right now!')

def chapter_5b(player_character, player_name, homescreen, base_stats):
    clear_terminal_in_game(player_character, player_name)
    center_input(
        "You walk down a narrow hallway leading to a throne room. Halfway down"
        " you stop familiar looking mirror (press enter to continue...)\n"
    )
    center_input(
        "As you get closer, you notice that this time you can see your "
        "reflection. You stop a few paces short of the mirror and look at your "
        "reflection for a moment when suddenly...! (press enter to continue...)"
        "\n"
    )
    center_input(
        "Your reflection start to walk forward on its own! As it reaches the "
        "surface of the mirror it passes through causing ripples as if "
        "emerging from water. (press enter to continue...)\n"
    )
    center_input(
        "The being, stops inches from your face and stares at you with a "
        "sinister grin. Every detail of the sinister being is identical to "
        "you, apart from its souless white eyes, devoid of any features!"
        "(press enter to continue...)\n"
    )
    center_input(
        "Without warning it lets out an inhuman scream and goes into a violent "
        " frenzy! (press enter to continue...)\n"
    )
    center_print("You must defend yourself!\n")

    center_input("Press enter to commence combat...")
    
    # Mirror clone enemy listed within chapter
    clone_nature = player_character.return_highest_stat()
    mirror_clone = Enemy(
        f"Mirror {player_name}", player_character.health, clone_nature, 6, 9, 
        True
    )

    # Calls fight with mirror clone enemey
    combat(
        mirror_clone, player_character, player_name, homescreen, 
        "Mirror Sphere", 11, base_stats
    )

    clear_terminal_in_game(player_character, player_name)

    center_input(
        "As you deliver the final blow to the clone, it shatters as if made of "
        "glass! The mirror behind it also shatters, leaving a blank wooden "
        "frame standing the hallway. (press enter to continue...)\n"
    )
    center_input(
        "You walk past the frame and continue down the hallway "
        "(press enter to continue...)\n"
    )

    chapter_5a(player_character, player_name, homescreen, base_stats)


def boss_a(player_character, player_name, homescreen, base_stats):
    clear_terminal_in_game(player_character, player_name)
    center_input(
        "You enter the armory, which is brimming with an assortment of tools "
        "all capable of ensuring a swift and bloody end to the wielders "
        "enemies. (press enter to continue...)\n" 
    )
    center_input(
        "Your attention is drawn to a suit of armor in the center of the room "
        "which is holding an extravagant sliver blade. You reach out to grab "
        "the sword. (press enter to continue...)\n" 
    )
    center_input(
        "Suddenly you are forced to jump back as the suit of armor springs to "
        "life, and swings the sword at you, narrowly missing your chest. In a "
        "fenzy the suit of armor charges at you! (press enter to continue...)\n" 
    )
    center_print("You must defend yourself!\n")

    center_input("Press enter to commence combat...")
        
    combat(
        champion, player_character, player_name, homescreen, "None", 0,
        base_stats
    )


def boss_b(player_character, player_name, homescreen, base_stats):
    clear_terminal_in_game(player_character, player_name)

    center_input(
        "You enter a library of seemingly endless rows of bookshelves, all "
        "bursting with ancient texts of knowledge lost to time "
        "(press enter to continue...)\n" 
    )
    center_input(
        "As you approch the center of the room you spot a pedestal sitting a "
        "large, exquisite looking book, bound in leather, with an intricate "
        "symbol on the front. (press enter to continue...)\n" 
    )
    center_input(
        "As you reach out to open the first page you catch a moving shadow in "
        "the corner of your eye, darting from one bookshelf to another!"
        "(press enter to continue...)\n" 
    )
    center_input(
        "Thinking it must have been a trick of the light you carry on opening "
        "the book, when you catch another shadow moving again. Only this time "
        "much closer. (press enter to continue...)\n" 
    )
    center_input(
        "This time you keep your eyes fixed where you saw the movement, while "
        "proceeding to open the book, when suddenly, the shadow emerges from "
        "between the bookshelve and lunges at you! "
        "(press enter to continue...)\n" 
    )
    center_input(
        "It lands on stop of you, forcing you onto the ground. The creature is "
        "wrapped in a tattered brown robe with a large hood which covers its "
        "face. Its hands are dark grey, with long boney fingers "
        "(press enter to continue...)\n"
    )
    center_input(
        "As you wrestle the creature off you with a well placed kick. Its hood "
        "Flicks back over its head, revealing a grotesque pale face with "
        "sunken eyes, and a mass of tentacles where a mouth would usually sit!"
        "(press enter to continue...)\n"
    )
    center_input(
        "The creature roars with an almost reptilian sounding gargle, and "
        "begins to charge at you again! (press enter to continue...)\n"
    )
    center_print("You must defend yourself!\n")

    center_input("Press enter to commence combat...")
        
    combat(
        protector, player_character, player_name, homescreen, "None", 0,
        base_stats
    )


def boss_c(player_character, player_name, homescreen, base_stats):
    clear_terminal_in_game(player_character, player_name)

    center_input(
        "You enter a room full of mountains of gold, silver and jewels. "
        "There looks to be enough to buy a large country!"
        "(press enter to continue...)\n" 
    )
    center_input(
        "You walk beteen the large piles of treasure, running your hand over "
        "the coins, listening to them clink against each other. As you walk"
        "around one pile of gold, you see a large open chest in front of an "
        "impossibly large mountain of gold coins."
        "(press enter to continue...)\n" 
    )
    center_input(
        "You approch the chest, and looking inside you see a magnificent "
        "diamond, the size of your head! (press enter to continue...)\n" 
    )
    center_input(
        "As you reach into the chest to pick up the diamond, the mountain of "
        "gold coins in front of you begins to shift causing coins to spill "
        "down the sides of the pile (press enter to continue...)\n" 
    )
    center_input(
        "Suddenly a ginormous scaley head bursts out of the pile of gold, "
        "followed by a long neck and two enormous wings! "
        "(press enter to continue...)\n" 
    )
    center_input(
        "The creature roars and spouts scorching flames into the air before "
        "swinging a large tail towards you! (press enter to continue...)\n" 
    )
    center_print("You must defend yourself!\n")

    center_input("Press enter to commence combat...")
        
    combat(
        dragon, player_character, player_name, homescreen, "None", 0,
        base_stats
    )


def ending_chapter(player_character, player_name, homescreen, base_stats):

    stat_reset(player_character, base_stats) # Resets any stat buffs
    clear_terminal_in_game(player_character, player_name)

    center_input(
        "As you lay the final, decisive blow on the enemy there is a blinding"
        "flash of light! (press enter to continue...)\n" 
    )
    center_input(
        "When your vision clears you find yourself standing on a hill, "
        "overlooking a decrepid looking castle. (press enter to continue...)\n"
    )
    center_input(
        "Where many have perished, you have survived... Congratulations "
        f"{player_name}, you have escaped the dark castle. "
        "(press enter to continue...)"
    )
