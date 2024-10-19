from mechanics import (
    death_outside_combat, combat, item_choice, stat_reset, random_item
)
from classes import (
    Enemy, guard, spirit, sludge_creature, beast, champion, protector, dragon
)
from utilities import clear_terminal_in_game, center_print, center_input
import random


def intro_chapter(player_character, player_name):
    """
    Intro Chapter - Called by run_game() after player chooses their character
    """
    clear_terminal_in_game(player_character, player_name)
    center_print(
        "You awaken and find yourself in an empty, dark room with stone walls."
        " You look\nup at a small window with iron bars in the far corner of "
        "the room. As your eyes\ntrace the beams of moonlight peering into "
        "the room between the bars, you notice\na thick wooden door which "
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
        "long corridor\nlined with cell blocks like the one you just left. "
        "You notice what looks to\nbe an unconscious guard clad in chainmail, "
        "laying still on the floor.\n(Press enter to continue...)\n"
    )

    center_input(
        "Not knowing what you will face, you toy with the idea of taking the "
        "chainmail\nfor yourself. (Press enter to continue...)\n"
    )

    center_print("Do you attempt to take the chainmail? Yes(y) / No(n)\n")

    while True:

        choice = input().strip()

        if choice == "y":
            if random.randrange(1, 11) >= 5:
                center_print(
                    "You manage to remove the Chainmail from the unconscious "
                    "guard without waking\nhim. (Press enter to continue...)"
                )
                player_character.item = "Chainmail"
                input()
                break
            else:
                center_input(
                    "As you attempt to remove the guard's armor he begins to "
                    "stir, suddenly springing\nto his feet with an enraged "
                    "look on his face. You attempt to reason with him,\nbut "
                    "your words fall on deaf ears. (Press enter to "
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
                "You sneak past the guard, being careful not to wake him.\n"
                "(Press enter to continue...)"
            )
            break
        else:
            center_print(f'You can\'t do "{choice}" right now')


def chapter_1b(player_character, player_name, homescreen, base_stats):
    """
    Chapter 1b - Called by run_game() when player chooses to wait in their cell
    """
    clear_terminal_in_game(player_character, player_name)
    center_input(
        "You wait in your cell, pondering how you woke up here. Suddenly, you "
        "hear a\nmetal clattering sound, followed by a loud creak and bang as "
        "your cell door\nslams open. (Press enter to continue...)\n"
    )

    center_input(
        "An enraged, dazed-looking guard, clad in chainmail stands blocking "
        "the doorway.\nYou attempt to reason with him, but your words fall on "
        "deaf ears.\n(Press enter to continue...)\n"
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
    center_input(
        "As you walk the winding hallway you find yourself following what "
        "looks to be an\nold water irrigation system. It's no longer "
        "functional due to decades worth\nof compacted sludge. "
        "(Press enter to continue...)\n"
    )

    center_print("You notice something sparkle within the mud-filled channel")
    center_print("Do you attempt to remove it?\n")
    center_print("Yes(y) / No(n)\n")

    while True:
        choice = input().strip()

        if choice == "y":
            if player_character.cunning >= 6:  # Cunning skill check
                center_print(
                    "You fish the shiny object out of the compacted sludge "
                    "without issue"
                )
                center_print("It appears to be some sort of Focusing Crystal.")

                item_choice(player_character, base_stats, "Focusing Crystal")
                break

            else:
                center_input(
                    "As you attempt to free the object, something reaches out "
                    "of the sludge and\ngrabs your hand. You pull your hand "
                    "away quickly, but lose sight of the shining\nobject. The "
                    "hand, which appears to be made of the same compacted "
                    "sludge\nfrom which it emerged, continues to rise out of "
                    "the channel. The mass of sewage\nstarts to morph into a "
                    "crude impersonation of a person.\n"
                    "(Press enter to continue...)\n"
                )

                center_print(
                    "The creature lets out a gargling roar and lunges for "
                    "you!\n"
                )

                center_print("You must defend yourself!")

                center_input("Press enter to commence combat...")

                combat(
                    sludge_creature, player_character, player_name, homescreen,
                    "Focusing Crystal", 5, base_stats
                )
                break
        elif choice == "n":
            center_print("You ignore the object and carry on walking.")
            center_input("(Press enter to continue...)")
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
        "ear,\ncatching your lobe. (You lose 1hp).\n"
        "(Press enter to continue...)\n"
    )

    death_outside_combat(player_character, player_name, homescreen, 1)
    center_input(
        "You turn around to see a hooded figure fleeing. You look at the "
        "ground in front\nof you and spot the projectile that was thrown at"
        " you.\n(Press enter to continue...)\n"
    )

    item_choice(player_character, base_stats, "Throwing Knife")


def chapter_3a(player_character, player_name, homescreen, base_stats):
    """
    Chapter 3a - Called by run_game() when player chooses to go up the
                 staircase
    """
    clear_terminal_in_game(player_character, player_name)

    center_input(
        "You enter a large circular room. The only light source is a beam of "
        "moonlight\nwhich shines through a large well-like hole in the center "
        "of the ceiling,\nilluminating a single mirror in the middle of the "
        "room.\n(Press enter to continue...)\n"
    )

    center_input(
        "You approach the mirror to inspect it more closely, and notice that "
        "the surface\nof the mirror looks to be moving around like a viscous "
        "liquid. You are taken\nback by a sudden realization that you appear "
        "to have no reflection!\n(Press enter to continue...)\n"
    )

    center_print(
        "Though startled, you feel compelled to touch the mirror's surface.\n"
    )
    center_print("Do you touch the mirror?\n")
    center_print("Yes(y) / No(n)\n")

    while True:
        choice = input()

        if choice == "y":
            clear_terminal_in_game(player_character, player_name)

            center_input(
                "As your finger comes into contact with the mirror, the "
                "surface breaks like\nwater and begins to wrap itself around "
                "your arm in a slithering, tentacle-like\nfashion. Before you "
                "can even attempt to struggle, you are enveloped in a living\n"
                "silver goo. (Press enter to continue...)\n"
            )

            center_input(
                "Unable to see or move, you feel that this is the end...\n"
                "(Press enter to continue...)\n"
            )

            if player_character.item == "None":

                center_input(
                    "When suddenly the goo loosens it's grip on you and begins"
                    " to melt away, as if\ndissolving. When all the goo has "
                    "dissipated, you are left facing the blank\nwooden frame "
                    "where the mirror once attached itself.\n"
                    "(Press enter to continue...)\n"
                )

                center_print(
                    "You notice a small iridescent sphere sitting on the "
                    "ground.\n"
                )

                center_print(
                    "There is a faint whisper, as if carried on"
                    " the wind...\n"
                )
                center_input("(Press enter to continue...)\n")

                center_print('"Those abscent of greed are rewarded..."')
                center_print("(Mirror Sphere acquired!)\n")
                center_input("(Press enter to continue...)")
                player_character.item = "Mirror Sphere"
                break
            else:
                clear_terminal_in_game(player_character, player_name)

                center_input(
                    "The mass of goo constricts tightly. You hear the "
                    f"{player_character.item}\nin your pocket break. The goo "
                    "tosses you aside and slithers back to the\nempty wooden "
                    "frame in the middle of the room. As the amorphous silver "
                    "blob\nmounts itself onto the frame you here a faint "
                    "whisper, as if carried on\nthe wind... "
                    "(Press enter to continue...)\n"
                )

                center_input(
                    '"No aid shall be given to those with greed in '
                    'their hearts... This was your\nfirst and only warning." '
                    '(Press enter to continue...)\n'
                )
                player_character.item = "None"
                center_print("You loose 5hp and your item was destroyed.\n")
                center_input("(Press enter to continue...)")
                death_outside_combat(
                    player_character, player_name, homescreen, 5
                )
                break

        elif choice == "n":
            clear_terminal_in_game(player_character, player_name)
            center_input(
                "You resist the urge to touch the mirror and continue to stare"
                " at it for another\nmoment before moving on. "
                "(Press enter to continue...)\n"
            )
            center_input(
                "You have the strangest feeling you saw something "
                "getting closer...\n(Press enter to continue...)\n"
            )
            player_character.mirror = True
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
        "Walking down the winding staircase you begin to feel uneasy. Suddenly"
        " a dark,\nghostly apparition materializes in front of you and begins "
        "to speak in a\ndistorted, otherworldly tone...\n"
    )

    center_print('"ThOsE wHo EnTEr My DoMaIn ShAlL kNoW FEAR!!!"\n')
    center_input("(Press enter to continue...)\n")

    center_print(
        "The spirit rises into the air ominously, then swoops down "
        "toward you!\n"
    )

    center_print("You must defend yourself!\n")

    center_input("Press enter to commence combat...")

    combat(
        spirit, player_character, player_name, homescreen, random_item, 8,
        base_stats
    )


def chapter_4a(player_character, player_name, homescreen, base_stats):
    """
    Chapter 4a - Called by run_game() when player chooses to go through the
                 door
    """
    clear_terminal_in_game(player_character, player_name)

    center_input(
        "You enter a dimly lit, long, rectangular room when the door behind "
        "you suddenly\nslams shut. Ahead you see the shadowed outline of a "
        "large brutish creature\nmoving a large carved slab in front of the "
        "door ahead.\n(Press enter to continue...)\n"
    )

    center_input(
        "Realizing that your only exit is about to be blocked, you attempt to "
        "run the\nlength of the room before the door can be sealed...\n"
        "(Press enter to continue...)\n"
    )

    # Outcome determined by players cunning stat
    if player_character.cunning >= 9:
        center_input(
            "You dash across the room, nimbly avoiding the jutting-up peices "
            "of cobblestone\nfloor. You manage to slip through the remaining "
            "gap in the door at the last\nsecond. (Press enter to continue...)"
            "\n"
        )
        center_input(
            "You breathe a sigh of relief for a moment, before the sudden "
            "realization hits\nyou... You are now in the room with whatever "
            "brutish abomination just sealed\nthe door!\n"
            "(Press enter to continue...)\n"
        )
        center_input(
            "The beast lets out a snarl and bears its teeth. It stoops into a"
            " crouch\nready to pounce on its prey before lunging towards you!"
            "(Press enter to continue...)\n"
        )
        center_print("You must defend yourself!\n")

        center_input("Press enter to commence combat...")

        combat(
            beast, player_character, player_name, homescreen, random_item, 7,
            base_stats
        )

    else:  # If cunning check is failed
        center_input(
            "You dash across the room, trying to avoid the jutting-up peices "
            "of cobblestone\non the floor, but in your panic you trip and "
            "fall, foiling your chances of\nreaching the door in time. "
            "(Press enter to continue...)\n"
        )
        center_input(
            "As the door seals shut the room is left pitch black until "
            "suddenly, the sconces\nlining the room ignite as if by magic. "
            "There is a brief silence before you\nhear a rumbling coming from"
            " above. (Press enter to continue...)\n"
        )
        center_input(
            "You look upwards to see a ceiling covered in jagged metal spikes,"
            " slowly\ndecending towards you. (Press enter to continue...)\n"
        )
        center_print("There isn't much time! What do you do?!\n")
        center_print(
            "Attempt to move the slab(m). Look for another way out(w)\n"
        )

        while True:

            def chapter_4a_death():
                """
                Handles game over if player fails all skill checks on
                chapter 4a
                """
                center_print("The jagged ceiling looms too close to escape.\n")
                center_print("Your demise is certain...")
                center_input("(Press enter to continue...)\n")
                center_print("Game Over\n")
                center_input("Press enter to return to the homescreen...")
                homescreen()

            choice = input().strip()
            if choice == "m":  # Might Check
                if player_character.might >= 9:
                    center_input(
                        "You force your weight against the huge slab blocking "
                        "your path. Years of\nhoning your strength pays off as"
                        " you force the slab aside as if it were made\nof "
                        "paper. (Press enter to continue...)\n"
                    )
                    center_input(
                        "As you walk through the door you see the beast-like "
                        "humanoid who sealed the\ndoor. Intimidated by your "
                        "feat of strength it stares at you with a\nfearful "
                        "expression before fleeing. You notice it drops "
                        "something...\n(Press enter to continue...)\n"
                    )
                    item_choice(player_character, base_stats, random_item)
                    break
                else:
                    center_input(
                        "You attempt to move the huge slab blocking your path "
                        "but to no avail. It is\nsimply too heavy.\n"
                        "(Press enter to continue...)\n"
                    )

                    chapter_4a_death()

            elif choice == "w":  # Wisdom check
                if player_character.wisdom >= 9:
                    center_input(
                        "You methodically look for any levers or switches "
                        "that may lead to an escape.\nYour methodical "
                        "approach pays off! As you pull one of the fire "
                        "sconces\non the wall, a hidden passage opens up and "
                        "you slip away.\n(Press enter to continue...)\n"
                    )
                    break
                else:
                    center_input(
                        "You frantically search for a button or switch to help"
                        " you escape but to no\navail. "
                        "(Press enter to continue...)\n"
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
        "You step through the narrow passageway, the walls around you feel as "
        "if they\nare closing in. The air is damp and heavy, making it hard to"
        " breathe.\n(Press enter to continue...)\n"
    )
    center_input(
        "The only light comes from faintly glowing moss lining the cracks in "
        "the stone\nwalls. (Press enter to continue...)\n"
    )
    center_input(
        "Suddenly, the ground beneath you gives way, and you tumble down a "
        "hidden chute,\nsliding into the darkness! "
        "(Press enter to continue...)\n"
    )
    if player_character.cunning >= 6:  # Cunning check for avoiding damage
        center_input(
            "With quick reflexes, you manage to control your fall, avoiding "
            "any serious\ninjury as you land at the bottom. "
            "(Press enter to continue...)\n"
        )
    else:
        center_input(
            "You crash to the ground painfully, your body aching from the "
            "impact.\n(Press enter to continue...)\n"
        )
        # Deduct health for failing the skill check
        center_print("You lose 5hp.")
        center_input("(Press enter to continue...)\n")
        death_outside_combat(player_character, player_name, homescreen, 5)


def chapter_5a(player_character, player_name, homescreen, base_stats):
    clear_terminal_in_game(player_character, player_name)
    center_input(
        "You enter a throne room. You scan the room and see three doors. "
        "Each door is\nlabeled with a golden plaque. "
        "(Press enter to continue...)\n"
    )
    center_print('To your left is a door labled "Armory"(a)')
    center_print('To your right is a door labeled "Library"(l)')
    center_print('Ahead is a door labled "Treasury"(t).\n')
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
        " you spot\na familiar looking mirror (Press enter to continue...)\n"
    )
    center_input(
        "As you get closer, you notice that this time you can see your "
        "reflection. You\nstop a few paces short of the mirror and look at "
        " your reflection for a moment\nwhen suddenly...! "
        "(Press enter to continue...)\n"
    )
    center_input(
        "Your reflection start to walk forward on its own! As it reaches the "
        "surface of\nthe mirror it passes through causing ripples as if "
        "emerging from water.\n(Press enter to continue...)\n"
    )
    center_input(
        "The being stops inches from your face and stares at you with a "
        "sinister grin.\nEvery detail of the sinister being is identical to "
        "you, apart from its souless\nwhite eyes, devoid of any features! "
        "(Press enter to continue...)\n"
    )
    center_input(
        "Without warning it lets out an inhuman scream and goes into a violent"
        " frenzy!\n(Press enter to continue...)\n"
    )
    center_print("You must defend yourself!\n")

    center_input("Press enter to commence combat...")

    def determine_clone_nature(player_character):
        """
        Determines Mirror Clone's nature based on player character class
        """

        return (
            "Might" if player_character.name == "Fighter" else
            "Wisdom" if player_character.name == "Scholar" else "Cunning"
        )

    clone_nature = determine_clone_nature(player_character)

    # Mirror clone enemy listed within chapter
    mirror_clone = Enemy(
        f"Mirror {player_name}", player_character.health, clone_nature, 6, 9,
        False
    )

    # Calls fight with mirror clone enemey
    combat(
        mirror_clone, player_character, player_name, homescreen,
        "Mirror Sphere", 11, base_stats
    )

    clear_terminal_in_game(player_character, player_name)

    center_input(
        "As you deliver the final blow to the clone, it shatters as if made "
        "of glass!\nThe mirror behind it also shatters, leaving a blank "
        " wooden frame standing the\nhallway. (Press enter to continue...)\n"
    )
    center_input(
        "You walk past the frame and continue down the hallway\n"
        "(Press enter to continue...)\n"
    )

    chapter_5a(player_character, player_name, homescreen, base_stats)


def boss_a(player_character, player_name, homescreen, base_stats):
    clear_terminal_in_game(player_character, player_name)
    center_input(
        "You enter the armory, which is brimming with an assortment of tools "
        "all capable\nof ensuring a swift and bloody end to the wielders "
        "enemies.\n(Press enter to continue...)\n"
    )
    center_input(
        "Your attention is drawn to a suit of armor in the center of the room "
        "which is\nholding an extravagant sliver blade. You reach out to grab "
        "the sword.\n(Press enter to continue...)\n"
    )
    center_input(
        "Suddenly you are forced to jump back as the suit of armor springs to "
        "life, and\nswings the sword at you, narrowly missing your chest. In a"
        " fenzy, the suit of\narmor charges at you! "
        "(Press enter to continue...)\n"
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
        "bursting with\nancient texts of knowledge lost to time "
        "(Press enter to continue...)\n"
    )
    center_input(
        "As you approach the center of the room you spot a pedestal sitting a "
        "large,\nexquisite looking book, bound in leather, with an intricate "
        "symbol on the front.\n(Press enter to continue...)\n"
    )
    center_input(
        "As you reach out to open the first page you catch a moving shadow in "
        "the corner\nof your eye, darting from one bookshelf to another!\n"
        "(Press enter to continue...)\n"
    )
    center_input(
        "Thinking it must have been a trick of the light you carry on opening "
        "the book,\nwhen you catch another shadow moving again. Only this "
        "time, much closer.\n(Press enter to continue...)\n"
    )
    center_input(
        "This time you keep your eyes fixed where you saw the movement, while "
        "proceeding\nto open the book, when suddenly, the shadow emerges from "
        "between the\nbookshelves and lunges at you! "
        "(Press enter to continue...)\n"
    )
    center_input(
        "It lands on top of you, forcing you onto the ground. The creature "
        "is wrapped\nin a tattered brown robe with a large hood which covers "
        "its face. Its hands are\ndark grey, with long bony fingers. "
        "(Press enter to continue...)\n"
    )
    center_input(
        "As you wrestle the creature off you with a well-placed kick. Its "
        "hood flicks\nback over its head, revealing a grotesque pale face with"
        " sunken eyes, and a mass\nof tentacles where a mouth would usually "
        "sit! (Press enter to continue...)\n"
    )
    center_input(
        "The creature roars with an almost reptilian-sounding gargle, and "
        "begins to\ncharge at you again! (Press enter to continue...)\n"
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
        "There looks to\nbe enough to buy a large country! "
        "(Press enter to continue...)\n"
    )
    center_input(
        "You walk between the large piles of treasure, running your hand over "
        "the coins,\nlistening to them clink against each other. As you walk"
        "around one pile of gold,\nyou see a large open chest in front of an "
        "impossibly large mountain of gold\ncoins. "
        "(Press enter to continue...)\n"
    )
    center_input(
        "You approach the chest, and looking inside you see a magnificent "
        "diamond the\nsize of your head! (Press enter to continue...)\n"
    )
    center_input(
        "As you reach into the chest to pick up the diamond, the mountain of "
        "gold coins\nin front of you begins to shift causing coins to spill "
        "down the sides of the\npile. (Press enter to continue...)\n"
    )
    center_input(
        "Suddenly a ginormous scaley head bursts out of the pile of gold, "
        "followed by a\nlong neck and two enormous wings! "
        "(Press enter to continue...)\n"
    )
    center_input(
        "The creature roars and spouts scorching flames into the air before "
        "swinging a\nlarge tail towards you! (Press enter to continue...)\n"
    )
    center_print("You must defend yourself!\n")

    center_input("Press enter to commence combat...")

    combat(
        dragon, player_character, player_name, homescreen, "None", 0,
        base_stats
    )


def ending_chapter(player_character, player_name, homescreen, base_stats):

    stat_reset(player_character, base_stats)  # Resets any stat buffs
    clear_terminal_in_game(player_character, player_name)

    center_input(
        "As you lay the final, decisive blow on the enemy there is a blinding "
        "flash of\nlight! (Press enter to continue...)\n"
    )
    center_input(
        "When your vision clears you find yourself standing on a hill, "
        "overlooking a\ndecrepid looking castle. "
        "(Press enter to continue...)\n"
    )
    center_input(
        "Where many have perished, you have survived... Congratulations "
        f"{player_name}, you have\nescaped the dark castle! "
        "(Press enter to continue...)"
    )
