
from mechanics import *
from classes import *
from utilities import clear_terminal_in_game
import random


def intro_chapter(player_character, player_name):
    clear_terminal_in_game(player_character, player_name)
    print("You awaken and find yourself in a empty, dark room with stone walls. \n\
You look up to a small window with iron bars in the far corner of the room.\n\
As your eyes trace the beams of moonlight peering into the room between the\n\
bars, you notice a thick wooden door which appears to be open ajar.\n")

    print("Do you wait(w) or try to open the door(o)?\n")

def chapter_1a(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)
    print("You push the door, which opens with a loud creak. You emerge in a long corridor\n\
lined with cell blocks like the one you just left. You notice what looks \n\
to be an unconscious guard clad in chainmail, laying still on the floor.\n")

    print("Not knowing what you will face, you toy with the idea of taking the chainmail\n\
for yourself\n")

    while True:

        choice = input("Do you attempt to take the chainmail? Yes(y) / No(n)\n")

        if choice == "y":
            if random.randrange(1,11) >= 5:
                print("You manage to remove the Chainmail from the unconcious guard without disturbing him")
                player_character.item = "Chainmail"
                input()
                break
            else:
                print("As you attempt to remove the guards armor he begins to stir, suddenly springing to his feet \n\
with an enraged look on his face. You attempt to reason with him, but your words fall on deaf ears\n")

                print("You must defend yourself!")

                input("Press any key to commence combat...")

                combat(guard, player_character, player_name, homescreen, "Chainmail", 11)
                break
        elif choice == "n":
            print("You sneak past the guard, being carful not to wake him")
            break
        else:
            print("You can't do that right now")

def chapter_1b(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)
    print("You wait in your cell, pondering how you woke up here. Suddenly, you \n\
hear a metal clattering sound, followed by a loud creak and bang as your cell door \n\
slams open\n")
    
    print("An enraged, dazed looking guard, clad in chainmail stands blocking the doorway. \n\
You attempt to reason with him, but your words fall on deaf ears\n")

    print("You must defend yourself!")

    input("Press any key to commence combat...")

    combat(guard, player_character, player_name, homescreen, "Chainmail", 11)

def chapter_2a(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)
    print("As you walk the winding hallway you find yourself following what looks to be an old water irrigation \n\
system. It's no longer functional due to decades worth of compacted sludge.")
    print("You notice something sparkle within the mud filled channel")
    print("Do you attempt to remove it?\n")

    while True:
        choice = input("Yes(y) / No(n)\n")

        if choice == "y":
            if random.randrange(1,5) * player_character.cunning >= 6: # Cunning skill check
                print("You fish the shiny object out of the compacted sludge without issue")
                print("It appears to be some sort of Focusing Crystal. Do you wish to keep it?")
                
                item_choice(player_character, "Focusing Crystal")
                break

            else:
                print("As you attempt to free the object, something reaches out of the sludge and grabs your hand.\n\
You pull your hand away quickly, but lose sight of the shining object. The hand, which appears to be made\n\
of the same compacted sludge from which it emerged, continues to rise out of the channel. The mass of sewage\n\
starts to morph into an crude impersonation of a person.\n")

                print("The creature lets out a gargling roar and lunges for you!")

                print("You must defend yourself!")

                input("Press any key to commence combat...")

                combat(sludge_creature, player_character, player_name, homescreen, "Focusing Crystal", 5)
                break
        elif choice == "n":
            print("You ignore the object and carry on walking")
            break
        else:
            print("You can't do that right now")


def chapter_2b(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)
    print("Walking down a narrow corridor you feel something whistle past your ear, catching your lobe. (You lose 1hp) \n\
You turn around to see a hooded figure fleeing. You look at the ground in front of you and spot the projectile that was thrown at you.")
    player_character.health -= 1
    print("\nDo you pick up the Throwing Knife? ")

    item_choice(player_character, "Throwing Knife")

def chapter_3a(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)
    print("You enter a large circular room. The only light source is a beam of moonlight which shines through a large\n\
well-like hole in the center of the ceiling, illuminating a single mirror in the middle of the room.\n")
    print("You approach the mirror to inspect it more closely, and notice that the surface of the mirror looks to be moving\n\
around like a viscous liquid. You are taken back by sudden realization that you appear to have no reflection!\n")
    print("Though startled, you feel compelled to touch the mirrors surface\n")
    print("Do you touch the mirror?\n")

    while True:
        choice = input("Yes(y) / No(n)\n")

        if choice == "y":
            clear_terminal_in_game(player_character, player_name)
            print("As your finger comes into contact with the mirror, the surface breaks like water and begins to wrap intself\n\
around your arm in a slithering, tentacle-like fashion. Before you can even attempt to struggle, you are enveloped in\n\
a living silver goo.\n")
            print("Unable to see or move, you feel that this is the end...")
            input()
            if player_character.item == "None":
                print("When suddenly the goo loosens it's grip on you and begins to melt away, as if dissolving. When all the goo has\n\
dissipated, you are left facing the blank wooden frame where the mirror once attached itself.\n")
                print("You notice your skin is now coated in a film of iridescent sheen.\n")
                print("You here a hear a faint whisper, as if carried on the wind... \n")
                input()
                print('"Those abscent of greed are rewarded..."')
                player_character.item = "Mirror Film"
                input()
                break
            else:
                clear_terminal_in_game(player_character, player_name)
                print(f"The mass of goo constricts tightly. You hear the {player_character.item} in your pocket break.")
                print("The goo tosses you aside and slithers back to the empty wooden frame in the middle of the room.\n")
                print("As the amorphous silver blob mounts itself onto the frame you here a faint whisper, as if carried on the wind... \n")
                print('"Those with greed in their hearts should be punished... This was your first and only warning."')
                player_character.item = "None"
                player_character.health -= 5
                input("You loose 5hp and your item was destroyed.")
                break
        elif choice == "n":
            clear_terminal_in_game(player_character, player_name)
            print("You resist the urge to touch the mirror and continue to stare at it for another moment before moving on.\n")
            print("You have the strangest feeling you saw something getting closer...\n")
            player_character.mirror = True
            input()
            break
        else:
            print("You can't do that right now")

def chapter_3b(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)
    print("Walking down the winding staircase you begin to feel uneasy. Suddenly a dark, ghostly apparition appears meterializes\n\
infront of you and begins to speak in a distorted, otherworldly tone...")
    input('"ThOsE wHo EnTEr My DoMaIn ShAlL kNoW FEAR!!!"')
    print("The spirit rises into the air ominously, then swoops toward down you!")

    print("You must defend yourself!")

    input("Press any key to commence combat...")
    
    combat(spirit, player_character, player_name, homescreen, "Lexicon", 5)

def chapter_4a(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)

def chapter_4b(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)

def chapter_5a(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)

def chapter_5b(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)
    print("You fall")

def boss_a(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)

def boss_b(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)

def boss_c(player_character, player_name, homescreen):
    clear_terminal_in_game(player_character, player_name)