

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

def select_character():
    # Player inputs their name
    player_name = input("Enter player name:\n")
    print(f"Welcome {player_name} \n")


    # Character options
    print("1) Fighter")
    print("2) Scholar")
    print("3) Thief")

    
    #Player selects character
    while True:
        player_character = input("Select your character (enter the number):\n")

        if player_character == '1':
            print("You chose Fighter!")
            break
        elif player_character == '2':
            print("You chose Scholar!")
            break
        elif player_character == '3':
            print("You chose Thief!")
            break
        else:
            print("Invalid choice.")

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
            print("> Invalid input. Please try again.")

homescreen()


