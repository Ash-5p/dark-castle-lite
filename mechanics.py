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

    def show_combat_details():
        clear_terminal_in_game(player_health, player_character)    
        print(f'Enemy Health: {current_enemy.health}hp')
        combat_prompt()
    
    combat_choice = input()

    while current_enemy.health > 0:

        if combat_choice == "l":
            player_health = light_attack(current_enemy, player_character, player_health)
            input()
            show_combat_details()
        elif combat_choice == "h":
            player_health = heavy_attack(current_enemy, player_character, player_health)
            input()
            show_combat_details()
        else:
            show_combat_details()
            print("Invalid Choice")
            input()

def light_attack(current_enemy, player_character, player_health):
    """
    Handles damage dealt and hit chance for light attack
    """
    hit_chance = random.randrange(1, 11)  # Only calculate once per attack
    enemy_hit_chance = random.randrange(1, 11)  # Enemy hit chance calculated once per turn
    
    if current_enemy.nature == "Might":
        if hit_chance < 9:  # Attack lands if hit_chance < 9
            current_enemy.health -= player_character.wisdom * 2 
        else:
            print("Your attack missed!")
        if enemy_hit_chance < 8:  # Enemy attack logic
            player_health -= math.ceil(current_enemy.damage / player_character.wisdom) 
        else: 
            print("You dodged the enemy's attack!")
        
    elif current_enemy.nature == "Wisdom":
        if hit_chance < 9:
            current_enemy.health -= player_character.cunning * 2
        else:
            print("Your attack missed!")
        if enemy_hit_chance < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.cunning)
        else: 
            print("You dodged the enemy's attack!")
        
    else:
        if hit_chance < 9:
            current_enemy.health -= player_character.might * 2
        else:
            print("Your attack missed!")
        if enemy_hit_chance < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.might)
        else: 
            print("You dodged the enemy's attack!")

    return player_health  # Return updated player_health

def heavy_attack(current_enemy, player_character, player_health):
    """
    Handles damage dealt and hit chance for heavy attack
    """
    hit_chance = random.randrange(1, 11)  # Only calculate once per attack
    enemy_hit_chance = random.randrange(1, 11)  # Enemy hit chance calculated once per turn
    
    if current_enemy.nature == "Might":
        if hit_chance < 5:  # More difficult to land a heavy attack
            current_enemy.health -= player_character.wisdom * 3 
        else:
            print("Your attack missed!")
        if enemy_hit_chance < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.wisdom) 
        else: 
            print("You dodged the enemy's attack!")
    
    elif current_enemy.nature == "Wisdom":
        if hit_chance < 9:
            current_enemy.health -= player_character.cunning * 3
        else:
            print("Your attack missed!")
        if enemy_hit_chance < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.cunning)
        else: 
            print("You dodged the enemy's attack!")

    else:
        if hit_chance < 9:
            current_enemy.health -= player_character.might * 3
        else:
            print("Your attack missed!")
        if enemy_hit_chance < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.might)
        else: 
            print("You dodged the enemy's attack!")

    return player_health  # Return updated player_health
