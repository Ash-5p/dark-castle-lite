from characters import *
from utilities import clear_terminal, blank_lines, return_home

def display_instructions_screen():
    """
    Displays instructions screen
    """
    while True:
        print("How to play")
        print("Play Game (p)")
        print("Back to main menu (h)")
        player_choice = input()

        if player_choice == "h":
            homescreen()
            break
        elif player_choice == "p":
            select_character()
            break
        else:
            print("> Invalid input. Please try again.")

player_character = {}
def select_character():
    """
    Prompts player to choose their name and select a character
    """
    clear_terminal()
    # Player inputs their name
    player_name = input("Enter player name:\n")
    print(f"Welcome {player_name} \n")


    # Character options
    print("1) Fighter (Might - 3 / Wisdom - 1 / Cunning - 2)")
    print("2) Scholar (Might - 1 / Wisdom - 3 / Cunning - 2)")
    print("3) Thief (Might - 2 / Wisdom - 1 / Cunning - 3)\n")

    #Player selects character
    while True:
        character_selection = input("Select your character (enter the number):\n")

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

    print(player_character)

def homescreen():
    """
    Displays homescreen when program is run
    """
    while True:
        print("Dark Castle lite\n")
        print("Play Game (p)")
        print("Instructions (i)")
        player_choice = input()
        
        if player_choice == "i":
            display_instructions_screen()
            break
        elif player_choice == "p":
            select_character()
            break
        else:
            player_choice = input("Invalid input. Please try again.")
            clear_terminal()
            homescreen()
            
homescreen()


