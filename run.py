from classes import *
from mechanics import *
import math
from utilities import clear_terminal, clear_terminal_in_game, blank_lines

def select_name():
    """
    Prompts player to choose their name
    """
    global player_name  # Declare player_name as a global variable
    clear_terminal()
    # Player inputs their name
    while True:
        player_name = input("Enter player name:\n").strip()

        if len(player_name) == 0:  # Checks if input is empty
            print("Character name must contain at least 1 character.\n")

        elif len(player_name) > 15:  # Check for names longer than 15 characters
            print("Character name cannot be more than 15 characters long.\n")

        else:
            clear_terminal()
            print(f"Welcome {player_name} \n")
            break
    
    select_character()
    return player_name
    
def select_character():
    """
    Prompts player to select a character
    """
    # Character options
    for index, character in enumerate(characters, start=1): # Iterate through characters list and index number
        print(f"{index}) {character.name} (Might: {character.might} | Wisdom: {character.wisdom} | Cunning: {character.cunning})")
   
   # Prompts player to select character
    while True:
        global player_character
        try:
            choice = int(input("\nEnter the number of your chosen character: "))
            if 1 <= choice <= len(characters):
                player_character = characters[choice - 1]
                print(f"\nYou have selected: {player_character.name}")
                break
            else:
                print(f"Please enter a number between 1 and {len(characters)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    reset_stats(player_character)
    print(player_character.description())

    input("\nPress any button to start your journey...")
    run_game()

def run_game():

    def decision(a, b, chapter_a, chapter_b):
        while True:
            player_choice = input()
            if player_choice == str(a):
                chapter_a()
                break
            elif player_choice == str(b):
                chapter_b()
                break
            else:
                choice_1 = input("You can't do that right now!")

    intro_chapter()

    decision("o", "w", chapter_1a, chapter_1b)

    clear_terminal_in_game(player_character, player_name)
    print("As you approch what looks like the end of the cell block you are met with a fork in the road.\n")
    print("Do you turn left(l) or right (r)?\n")

    decision("l", "r", chapter_2a, chapter_2b)

    clear_terminal_in_game(player_character, player_name)
    print("You find yourself in the middle landing of a winding staircase.\n")
    print("Do you go up(u) or down (d)?\n")

    decision("u", "d", chapter_3a, chapter_3b)
    clear_terminal_in_game(player_character, player_name)


def intro_chapter():
    clear_terminal_in_game(player_character, player_name)
    print("You awaken and find yourself in a empty, dark room with stone walls. \n\
You look up to a small window with iron bars in the far corner of the room. \n\
As your eyes trace the beams of moonlight peering into the room between the bars, \n\
you notice a thick wooden door which appears to be open ajar.\n")

    print("Do you wait(w) or try to open the door(o)?\n")

def chapter_1a():
    clear_terminal_in_game(player_character, player_name)
    print("You push the door, which opens with a loud creak. You emerge in a long corridor\n\
lined with cell blocks line the one you just left. You notice what looks \n\
to be an unconscious guard clad in chainmail laying still on the floor.\n")

    print("Not knowing what you will face, you toy with the idea of taking the chainmail\n\
for yourself\n")

    while True:

        choice = input("Do you attempt to take the chainmail? Yes(y) / No(n)\n")

        if choice == "y":
            if random.randrange(1,11) >= 5:
                print("You manage to remove the Chainmail from the unconcious guard without disturbing him")
                player_character.item = "Chainmail"
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

def chapter_1b():
    clear_terminal_in_game(player_character, player_name)
    print("You wait in your cell, pondering how you woke up here. Suddenly, you \n\
hear a metal clattering sound, followed by a loud creak and bang as your cell door \n\
slams open\n")
    
    print("An enraged, dazed looking guard, clad in chainmail stands blocking the doorway. \n\
You attempt to reason with him, but your words fall on deaf ears\n")

    print("You must defend yourself!")

    input("Press any key to commence combat...")

    combat(guard, player_character, player_name, homescreen, "Chainmail", 10)

def chapter_2a():
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


def chapter_2b():
    clear_terminal_in_game(player_character, player_name)
    print("Walking down a narrow corridor you feel something whistle past your ear, catching your lobe. (You lose 1hp) \n\
You turn around to see a hooded figure fleeing. You look at the ground in front of you and spot the projectile that was thrown at you.")
    player_character.health -= 1
    print("\nDo you pick up the Throwing Knife? ")

    item_choice(player_character, "Throwing Knife")

def chapter_3a():
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
                print(f"The mass of goo constricts tightly. You hear the {player_character.item} in your pocket break.")
                print("The goo tosses you aside and slithers back to the empty wooden frame in the middle of the room.\n")
                print("As the amorphous silver blob mounts itself onto the frame you here a faint whisper, as if carried on the wind... \n")
                print('"Those with greed in their hearts should be punished... This was your first and only warning."')
                player_character.item = "None"
                player_character.health -= 5
                input("You loose 5hp and your item was destroyed.")
                break
        elif choice == "n":
            print("You resist the urge to touch the mirror and continue to stare at it for another moment before moving on.\n")
            print("You have the strangest feeling you saw something getting closer...\n")
            player_character.mirror = True
            input()
            break
        else:
            print("You can't do that right now")

def chapter_3b():
    clear_terminal_in_game(player_character, player_name)

def chapter_4a():
    clear_terminal_in_game(player_character, player_name)

def chapter_4b():
    clear_terminal_in_game(player_character, player_name)

def chapter_5a():
    clear_terminal_in_game(player_character, player_name)

def chapter_5b():
    clear_terminal_in_game(player_character, player_name)

def boss_a():
    clear_terminal_in_game(player_character, player_name)

def boss_b():
    clear_terminal_in_game(player_character, player_name)

def boss_c():
    clear_terminal_in_game(player_character, player_name)

def reset_stats(player_character):
    player_character.health = 20
    player_character.item = "None"
    player_character.mirror = False

def display_instructions_screen():
    """
    Displays instructions screen
    """
    clear_terminal()
    while True:
        print("How to play\n")
        print("Play Game (p)")
        print("Back to main menu (h)")
        player_choice = input()

        if player_choice == "h":
            homescreen()
            break
        elif player_choice == "p":
            select_name()
            break
        else:
            print("> Invalid input. Please try again.")
    
def homescreen():
    """
    Displays homescreen when program is run
    """
    clear_terminal()
    while True:
        print("Dark Castle lite\n")
        print("Play Game (p)")
        print("Instructions (i)")
        player_choice = input()
        
        if player_choice == "i":
            display_instructions_screen()
            break
        elif player_choice == "p":
            select_name()
            break
        else:
            player_choice = input("Invalid input. Please try again.")
            clear_terminal()
            homescreen()
            
homescreen()