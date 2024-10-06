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
    print("Select your character (enter the number):\n")
    print("1) Fighter (Might: 3 / Wisdom: 1 / Cunning: 2)")
    print("2) Scholar (Might: 1 / Wisdom: 3 / Cunning: 2)")
    print("3) Thief   (Might: 2 / Wisdom: 1 / Cunning: 3)\n")

    #Player selects character
    while True:
        character_selection = input()
        global player_character

        if character_selection == '1':
            print("You chose Fighter!")
            player_character = fighter
            break
        elif character_selection == '2':
            print("You chose Scholar!")
            player_character = scholar
            break
        elif character_selection == '3':
            print("You chose Thief!")
            player_character = thief
            break
        else:
            print("Invalid choice.")

    print(player_character.description())
    input("\n Press any button to start your journey...")
    run_game()

def run_game():

    global player_health 
    player_health = 20

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

    clear_terminal_in_game(player_health, player_character, player_name)
    print("As you approch what looks like the end of the cell block you are met with a fork in the road.\n")
    print("Do you turn left(l) or right (r)?\n")

    decision("l", "r", chapter_2a, chapter_2b)


def intro_chapter():
    clear_terminal_in_game(player_health, player_character, player_name)
    print("You awaken and find yourself in a empty, dark room with stone walls. \n\
You look up to a small window with iron bars in the far corner of the room. \n\
As your eyes trace the beams of moonlight peering into the room between the bars, \n\
you notice a thick wooden door which appears to be open ajar.\n")

    print("Do you wait(w) or try to open the door(o)?\n")

def chapter_1a():
    clear_terminal_in_game(player_health, player_character, player_name)
    print("You push the door, which opens with a loud creak. You emerge in a long corridor\n\
lined with cell blocks line the one you just left. You notice what looks \n\
to be an unconscious guard clad in chainmail laying still on the floor.\n")

    print("Not knowing what you will face, you toy with the idea of taking the chainmail\n\
for yourself\n")

    while True:

        take_item = input("Do you attempt to take the chainmail? Yes(y) / No(n)\n")

        if take_item == "y":
            if random.randrange(1,11) >= 5:
                print("You manage to remove the Chainmail from the unconcious guard without disturbing him")
                player_character.item = "Chainmail"
                break
            else:
                print("As you attempt to remove the guards armor he begins to stir, suddenly springing to his feet \n\
with an enraged look on his face. You attempt to reason with him, but your words fall on deaf ears\n")

                print("You must defend yourself!")

                input("Press any key to commence combat...")

                combat(guard, player_character, player_health, player_name, homescreen, "Chainmail", 10)
                break
        elif take_item == "n":
            print("You sneak past the guard, being carful not to wake him")
            break
        else:
            print("You can't do that right now")

def chapter_1b():
    clear_terminal_in_game(player_health, player_character, player_name)
    print("You wait in your cell, pondering how you woke up here. Suddenly, you \n\
hear a metal clattering sound, followed by a loud creak and bang as your cell door \n\
slams open\n")
    
    print("An enraged, dazed looking guard, clad in chainmail stands blocking the doorway. \n\
You attempt to reason with him, but your words fall on deaf ears\n")

    print("You must defend yourself!")

    input("Press any key to commence combat...")

    combat(guard, player_character, player_health, player_name, homescreen, "Chainmail", 10)

def chapter_2a():
    clear_terminal_in_game(player_health, player_character, player_name)
    print("As you walk the winding hallway you find yourself following what looks to be an old water irrigation \n\
system. It's no longer functional due to decades worth of compacted sludge.")
    print("You notice something sparkle within the mud filled channel")
    print("Do you attempt to remove it?\n")

    while True:
        take_item = input("Yes(y) / No(n)\n")

        if take_item == "y":
            if random.randrange(1,5) * player_character.cunning >= 6: # Cunning skill check
                print("You fish the shiny object out of the compacted sludge without issue")
                print("It appears to be some sort of Focusing Crystal. Do you wish to keep it?")
                while True:
                    choice = input("Yes(y) / No(n) (Replaces current item)")
                    if choice == "y":
                        player_character.item = "Focusing Crystal"
                        break  # Exit loop after picking up
                    elif choice == "n":
                        print("You left the item behind.")
                        break  # Exit loop after leaving
                    else:
                        print("You can't do that right now")
            else:
                print("As you attempt to free the object, something reaches out of the sludge and grabs your hand.\n\
You pull your hand away quickly, but lose sight of the shining object. The hand, which appears to be made\n\
of the same compacted sludge from which it emerged, continues to rise out of the channel. The mass of sewage\n\
starts to morph into an crude impersonation of a person.\n")

                print("The creature lets out a gargling roar and lunges for you!")

                print("You must defend yourself!")

                input("Press any key to commence combat...")

                combat(sludge_creature, player_character, player_health, player_name, homescreen, "Focusing Crystal", 5)
                break
        elif take_item == "n":
            print("You ignore the object and carry on walking")
            break
        else:
            print("You can't do that right now")


def chapter_2b():
    clear_terminal_in_game(player_health, player_character, player_name)

def chapter_3a():
    clear_terminal_in_game(player_health, player_character, player_name)

def chapter_3b():
    clear_terminal_in_game(player_health, player_character, player_name)

def chapter_4a():
    clear_terminal_in_game(player_health, player_character, player_name)

def chapter_4b():
    clear_terminal_in_game(player_health, player_character, player_name)

def chapter_5a():
    clear_terminal_in_game(player_health, player_character, player_name)

def chapter_5b():
    clear_terminal_in_game(player_health, player_character, player_name)

def boss_a():
    clear_terminal_in_game(player_health, player_character, player_name)

def boss_b():
    clear_terminal_in_game(player_health, player_character, player_name)

def boss_c():
    clear_terminal_in_game(player_health, player_character, player_name)


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