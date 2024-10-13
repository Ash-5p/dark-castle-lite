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
            center_print(
                "Character name must contain at least 1 character."
            )
            center_print("Press enter, then please try again.")
            input()
            clear_terminal()
            select_name()

        # Check for names longer than 15 characters
        elif len(player_name) > 15:
            center_print(
                "Character name cannot be more than 15 characters long."
            )
            center_print("Press enter, then please try again.")
            input()
            clear_terminal()
            select_name()

        # Check for non-alphanumeric characters
        elif not player_name.isalnum():
            center_print(
                "Character name can only contain letters and numbers."
            )
            center_print("Press enter, then please try again.")
            input()
            clear_terminal()
            continue  # Re-prompt the user

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
            f"| Wisdom: {character.wisdom} | Cunning: {character.cunning})\n"
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
                center_print(f"You have selected: {player_character.name}\n")
                break
            else:
                center_print(
                    f"Please enter a number between 1 and {len(characters)}."
                )
        except ValueError:
            center_print(
                "Invalid input. Please enter a number."
            )

    player_character = base_stats

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
            choice = input().strip()
            if choice == str(a):
                chapter_a(
                    player_character, player_name, homescreen, base_stats
                )
                break
            elif choice == str(b):
                chapter_b(
                    player_character, player_name, homescreen, base_stats
                )
                break
            else:
                center_print(f'You can\'t do "{choice}" right now!')

    # Intro Chapter
    intro_chapter(player_character, player_name)

    # Chapter 1
    decision("o", "w", chapter_1a, chapter_1b)
    clear_terminal_in_game(player_character, player_name)

    # Chapter 2
    center_print(
        "As you approch what looks like the end of the cell block you are "
        "met with a fork in the road.\n"
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
    if mirror is False:
        chapter_5a(player_character, player_name, homescreen, base_stats)
    else:
        chapter_5b(player_character, player_name, homescreen, base_stats)

    ending_chapter(player_character, player_name, homescreen, base_stats)
    homescreen()


def display_instructions_screen():
    """
    Displays instructions screen
    """
    def page_1():
            clear_terminal_instructions()
            print("G̲E̲T̲T̲I̲N̲G̲ S̲T̲A̲R̲T̲E̲D̲\n")
            print(
                "Choose your name and select a character from one of the "
                "3 available choices:\nFighter / Scholar / Thief. "
                "Each character starts with 60hp and no item.\n"
            )

            print("C̲H̲A̲R̲A̲C̲T̲E̲R̲ N̲A̲T̲U̲R̲E̲S̲\n")

            center_print(
                "There are 3 natures within the game: Might / Wisdom / "
                "Cunning. These natures\ndetermine how much damage is done in "
                "combat, as well as the outcome of some\nof the scenarios you "
                " will face.\n"
            )

            center_print("Fighter - (Might: 9| Wisdom: 6 | Cunning: 3)")
            center_print("Scholar - (Might: 3| Wisdom: 9 | Cunning: 6)")
            center_print(" Thief   - (Might: 6| Wisdom: 3 | Cunning: 9)\n")

            print("Page 1 of 5")


    def page_2():
        clear_terminal_instructions()
        print("C̲O̲M̲B̲A̲T̲\n")
        print(
            "Some decisions will result in combat. During combat you will be "
            "presented with\nthe following options (shown below):\n"
        )
        print("Enemy Health: 50hp      <--  Current Enemy's Health")
        print("Nature: Might           <--  Current Enemy's Nature")
        print("What will you do?\n")
        print("(l) Light Attack        <--  Perform a Light Attack")
        print("(h) Heavy Attack        <--  Perform a Heavy Attack")
        print("(i) Item                <--  View/Use Current Item")
        print("(r) Run                 <--  Attempt to Run from Combat\n") 

        center_print("Futher explaination on page 3... ")

        print("Page 2 of 5")


    def page_3():
        clear_terminal_instructions()
        print("C̲O̲M̲B̲A̲T̲ C̲O̲N̲T̲.\n")
        
        print(
            "𝗘𝗻𝗲𝗺𝘆 𝗡𝗮𝘁𝘂𝗿𝗲 - Determines which of the players stats are "
        "used in damage\n               calculation.\n"
        )
        print("𝗟𝗶𝗴𝗵𝘁 𝗔𝘁𝘁𝗮𝗰𝗸 - Deals moderate damage. 90%\ hit chance.\n")
        print("𝗛𝗲𝗮𝘃𝘆 𝗔𝘁𝘁𝗮𝗰𝗸 - Deals high damage. 50%\ hit chance.\n")
        print(
            "       𝗜𝘁𝗲𝗺  - Displays the description of current item, "
            "and also prompts\n               "
            "player to use item if consumable.\n"
        )
        print(
            "        𝗥𝘂𝗻  - Attempt to run from combat. "
        "Failed attempt results in health\n               penalty. "
        "(Enemy will not drop item on successful run attempt.)\n"
        )

        print("Page 3 of 5")


    def page_4():
        clear_terminal_instructions()
        print("I̲T̲E̲M̲S̲\n")
        
        print(
            "Items will sometimes be aquired through certain scenarios "
            "throughout the game.\nMost defeated enemies will have a chance of "
            "dropping an item. You will always\nbe prompted with a yes or no "
            "choice before an item is added to your inventory.\nOnly one item "
            "can be held at one time, so picking up a new one will replace\n"
            "your current item.\n"
        )

        print(
            "Some items have passive effects while being held. Others have to "
            "be used during\ncombat (consumable items).\n")

        print(
            'To view the description of your current item, choose the "Item" '
            'option in\ncombat. If the item is consumable, you will be '
            'prompted to use the item.\n\n')

        print("Page 4 of 5")

    def page_5():
        clear_terminal_instructions()
        print("N̲A̲T̲U̲R̲E̲ M̲A̲T̲C̲H̲-̲U̲P̲S̲\n")
        
        print(
            "Each nature has a corrisponding nature that it is strong "
            "against and one\nit is weak against:\n"
        )

        center_print("Might > Cunning > Wisdom > Might\n\n")

        print(
            "When fighting an enemy, the stat that is strong against the "
            "enemy's nature\nwill be the one used in damage calculations. "
            "For example, when fighting an\nenemy with the Might nature, the "
            "players Wisdom stat will be use to determine\nboth damage dealt, "
            "and damage taken.\n\n\n"
        )

        print("Page 5 of 5")


    page_1()
    current_page = 1 # Used to save current page upon clear_terminal()

    while True:      
        
        choice = input().strip()

        if choice == "h":
            homescreen()
            break
        elif choice == "p":
            select_name()
            break
        elif choice == "1":
            page_1()
            current_page = 1
        elif choice == "2":
            page_2()
            current_page = 2
        elif choice == "3":
            page_3() 
            current_page = 3
        elif choice == "4":
            page_4() 
            current_page = 4
        elif choice == "5":
            page_5() 
            current_page = 5
        else:
            print(current_page)
            center_input(
                f'"{choice}" is an invalid input. Press enter, then '
                'please try again.'
            )
            (  # Makes clear_terminal_instructions() show current page
                page_1() if current_page == 1 else page_2() 
                if current_page == 2 else page_3() if current_page == 3 else 
                page_4() if current_page == 4 else page_5()
            )


def homescreen():
    """
    Displays homescreen when program is run
    """
    clear_terminal()
    while True:
        center_print(LOGO)
        center_print(CASTLE)
        choice = input().strip()
        if choice == "i":
            display_instructions_screen()
            break
        elif choice == "p":
            select_name()
            break
        else:
            center_input(
                f'"{choice}" is an invalid input. Press enter, then '
                'please try again.'
            )
            clear_terminal()
            homescreen()


if __name__ == "__main__":
    # initialise the application
    homescreen()
