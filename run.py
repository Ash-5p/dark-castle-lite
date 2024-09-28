

def display_instructions_screen():
    while True:
        print("How to play")
        print("Play Game - p")
        print("Back to main menu - h")
        player_choice = input()

        if player_choice == "h":
            homescreen()
            break
        elif player_choice == "p":
            # start_game()
            print("> Start Game")
            break
        else:
            print("> Invalid input. Please try again.")


def homescreen():
    """
    Display homescreen when program is run
    """
    while True:
        print("Dark Castle lite")
        print("Play Game - p")
        print("Instructions - i")
        player_choice = input()
        
        if player_choice == "i":
            display_instructions_screen()
            break
        elif player_choice == "p":
            # start_game()
            print("> Start Game")
            break
        else:
            print("> Invalid input. Please try again.")

homescreen()


