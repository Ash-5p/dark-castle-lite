import math
import random
from utilities import clear_terminal_in_game

def combat(current_enemy, player_character, player_health):
    """
    Handles the flow of combat within the game
    """
    clear_terminal_in_game(player_health, player_character)

    def combat_prompt():
        print("What will you do?\n")
        print("Light Attack(l)")
        print("Heavy Attack(h)")
        print("Run(r)\n") 

    combat_prompt()
    
    global combat_choice
    combat_choice = input()

    while current_enemy.health > 0:
        if combat_choice == "l":
            light_attack(current_enemy, player_character, player_health)
        elif combat_choice == "h":
            heavy_attack(current_enemy, player_character, player_health)
        else:
            input("Invalid Choice")
            
        clear_terminal_in_game(player_health, player_character)    
        print(f'Enemy Health: {current_enemy.health}hp')
        combat_prompt()

def light_attack(current_enemy, player_character, player_health):
    """
    Handles damage dealt and hit chance for light attack
    """
    if current_enemy.nature == "Might":
        if random.randrange(1,11,) < 9:
            current_enemy.health -= player_character.wisdom * 2 
        else:
            print("Your attack missed!")
        if random.randrange(1,11,) < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.wisdom) 
        else: 
            print("You dodged the enemies attack!")
        input()
        
    elif current_enemy.nature == "Wisdom":
        if random.randrange(1,11,) < 9:
            current_enemy.health -= player_character.cunning * 2
        else:
            print("Your attack missed!")

        if random.randrange(1,11,) < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.cunning)
        else: 
            print("You dodged the enemies attack!")
        input()
        
    else:
        if random.randrange(1,11,) < 9:
            current_enemy.health -= player_character.might * 2
        else:
            print("Your attack missed!")
        if random.randrange(1,11,) < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.might)
        else: 
            print("You dodged the enemies attack!")
        input()




def heavy_attack(current_enemy, player_character, player_health):
    """
    Handles damage dealt and hit chance for heavy attack
    """
    if current_enemy.nature == "Might":
        if random.randrange(1,11,) < 5:
            current_enemy.health -= player_character.wisdom * 3 
        else:
            print("Your attack missed!")
        if random.randrange(1,11,) < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.wisdom) 
        else: 
            print("You dodged the enemies attack!")
        input()
        
    elif current_enemy.nature == "Wisdom":
        if random.randrange(1,11,) < 9:
            current_enemy.health -= player_character.cunning * 3
        else:
            print("Your attack missed!")

        if random.randrange(1,11,) < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.cunning)
        else: 
            print("You dodged the enemies attack!")
        input()
        
    else:
        if random.randrange(1,11,) < 9:
            current_enemy.health -= player_character.might * 3
        else:
            print("Your attack missed!")
        if random.randrange(1,11,) < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.might)
        else: 
            print("You dodged the enemies attack!")
        input()
        