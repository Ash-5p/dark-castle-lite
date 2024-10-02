from classes import *
from chapters import *
from utilities import clear_terminal, blank_lines, return_home

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
    while True:
        player_name = input("Enter player name:\n")

        if len(player_name) <= 15:
            clear_terminal()
            print(f"Welcome {player_name} \n")
            break
        
        #Doesn't work
        elif len(player_name) == 0:
            print("Character name must contain at least 1 character.\n")

        else:
            print("Character name cannot be more than 15 characters long.\n")
    
    # Character options
    print("Select your character (enter the number):\n")
    print("1) Fighter (Might: 3 / Wisdom: 1 / Cunning: 2)")
    print("2) Scholar (Might: 1 / Wisdom: 3 / Cunning: 2)")
    print("3) Thief   (Might: 2 / Wisdom: 1 / Cunning: 3)\n")

    #Player selects character
    while True:
        character_selection = input()

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
    player_health = 20
    intro_chapter()

    player_choice = input()
    while True:
        if player_choice == "o":
            chapter_1a()
            break
        elif player_choice == "w":
            chapter_1b()
            break
        else:
            choice_1 = input("You can't do that right now!")

    
    
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
            select_character()
            break
        else:
            player_choice = input("Invalid input. Please try again.")
            clear_terminal()
            homescreen()
            
homescreen()


