

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
            # display_instructions_screen()
            print("> Go to instructions screen")
            break
        elif player_choice == "p":
            # start_game()
            print("> Go to homescreen")
            break
        else:
            print("> Invalid input. Please try again.")

homescreen()