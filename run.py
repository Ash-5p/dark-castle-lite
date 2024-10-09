import math
import copy
from classes import *
from mechanics import *
from chapters import *
from utilities import *
from art import *


def select_name():
    """
    Prompts player to choose their name
    """
    global player_name  # Declare player_name as a global variable
    clear_terminal()
    # Player inputs their name
    while True:
        center_print("Enter player name:\n")
        player_name = input().strip()

        if len(player_name) == 0:  # Checks if input is empty
            center_print("Character name must contain at least 1 character.\n")
            input()
            clear_terminal()
            select_name()

        # Check for names longer than 15 characters
        elif len(player_name) > 15:
            center_print(
                "Character name cannot be more than 15 characters long.")
            input()
            clear_terminal()
            select_name()

        else:
            clear_terminal()
            center_print(f"Welcome {player_name} \n")
            break

    select_character()
    return player_name


def select_character():
    """
    Prompts player to select a character
    """
    # Character options
    # Iterate through characters list and index number
    for index, character in enumerate(characters, start=1):
        center_print(
            f"{index}) {character.name} (Might: {character.might}"
            f"| Wisdom: {character.wisdom} | Cunning: {character.cunning})"
        )
    center_print("Enter the number of your chosen character:")
    # Prompts player to select character
    while True:
        global player_character
        # Remembers starting Might, Wisdom & Cunning to return stats to normal
        # where required
        global base_stats
        try:
            choice = int(input())
            if 1 <= choice <= len(characters):
                player_character = characters[choice - 1]
                base_stats = copy.deepcopy(characters[choice - 1])
                center_print(f"You have selected: {player_character.name}")
                break
            else:
                center_print(
                    f"Please enter a number between 1 and {len(characters)}."
                )
        except ValueError:
            center_print("Invalid input. Please enter a number.")

    reset_stats(player_character)

    center_input("Press enter button to start your journey...")
    run_game()


def run_game():
    """
    Main function for handling the flow of the game between chapter functions.
    Player decisions determine which chapter functions are called.
    """

    def decision(a, b, chapter_a, chapter_b):
        """
        Template function for presenting player with decision
        """
        while True:
            player_choice = input()
            if player_choice == str(a):
                chapter_a(player_character, player_name, homescreen, base_stats)
                break
            elif player_choice == str(b):
                chapter_b(player_character, player_name, homescreen, base_stats)
                break
            else:
                choice_1 = input("You can't do that right now!")

    # Intro Chapter
    intro_chapter(player_character, player_name)

    # Chapter 1
    decision("o", "w", chapter_1a, chapter_1b)
    clear_terminal_in_game(player_character, player_name)

    # Chapter 2
    center_print(
        "As you approch what looks like the end of the cell block you are met\n"
        "with a fork \n in the road.\n"
    )
    center_print("Do you turn left(l) or right (r)?\n")

    decision("l", "r", chapter_2a, chapter_2b)
    clear_terminal_in_game(player_character, player_name)

    # Chapter 3
    center_print(
        "You find yourself in the middle landing of a winding staircase.\n"
    )
    center_print("Do you go up(u) or down (d)?\n")

    decision("u", "d", chapter_3a, chapter_3b)
    clear_terminal_in_game(player_character, player_name)

    # Chapter 4
    center_print(
        "You finally reach the end of a seemingly endless corridor, where"
        "you are met \n with a large metal door and a narrow passageway on"
        "your right\n"
    )

    center_print(
        "Do you go through the door(d) or follow the passageway(p)?\n"
    )

    decision("d", "p", chapter_4a, chapter_4b)
    clear_terminal_in_game(player_character, player_name)

    # Chapter 5
    # Calls chapter 5a if player_character.mirror == True
    mirror = player_character.mirror
    if mirror == True:
        chapter_5a(player_character, player_name, homescreen, base_stats)
    else:
        chapter_5b(player_character, player_name, homescreen, base_stats)

    # clone_nature = player_character.return_highest_stat()
    # mirror_clone = Enemy(f"Mirror {player_name}", 20, clone_nature, random.randrange(3,6), True)  # noqa

    ending_chapter(player_character, player_name, homescreen)

def reset_stats(player_character):
    player_character.health = 60
    player_character.item = "None"
    player_character.mirror = False


def display_instructions_screen():
    """
    Displays instructions screen
    """
    clear_terminal()
    while True:
        center_print("How to play\n")
        center_print("Play Game (p)")
        center_print("Back to main menu (h)")
        player_choice = input()

        if player_choice == "h":
            homescreen()
            break
        elif player_choice == "p":
            select_name()
            break
        else:
            center_print("> Invalid input. Please try again.")


def homescreen():
    """
    Displays homescreen when program is run
    """
    clear_terminal()
    while True:
        center_print(LOGO)
        center_print(CASTLE)
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
