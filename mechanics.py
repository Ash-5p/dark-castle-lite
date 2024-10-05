import math
import random
from classes import ITEMS
from utilities import clear_terminal_in_game, clear_terminal

def defeat(current_enemy, player_health, player_name, player_character, homescreen_callback, dropped_item, drop_odds):
    """
    Handles player & enemy defeat
    """
    random_item = random.choice(ITEMS) # Chooses random item from ITEMS list
    random_item_chance = random.randrange(1,11) # Randomizes chance of item drops

    if player_health == 0:
        clear_terminal_in_game(player_health, player_character, player_name)
        print("You have been defeated!")
        input("Press any button to return to main menu...")
        homescreen_callback()
    elif current_enemy.health == 0:
        if random_item_chance >= drop_odds: # 10 = 100% Chance
            print(f'{current_enemy.name} has been defeated!')
        else:
            print(f'{current_enemy.name} has been defeated!')
            print(f"{current_enemy.name} has dropped an item: {dropped_item}\n")
            print("Do you want to pick it up? (Replaces current item)")
            print("Yes(y) / No(n)")

            while True:
                choice = input()
                if choice == "y":
                    player_character.item = dropped_item
                    clear_terminal_in_game(player_health, player_character, player_name)
                    break  # Exit loop after picking up
                elif choice == "n":
                    print("You left the item behind.")
                    clear_terminal_in_game(player_health, player_character, player_name)
                    break  # Exit loop after leaving
                else:
                    print("You can't do that right now")


def combat(current_enemy, player_character, player_health, player_name, homescreen_callback, dropped_item, drop_odds):
    """
    Handles the flow of combat within the game
    """
    clear_terminal_in_game(player_health, player_character, player_name)

    def combat_prompt():
        print(f'{current_enemy.name} Health: {max(current_enemy.health, 0)}hp')
        print("What will you do?\n")
        print("(l) Light Attack")
        print("(h) Heavy Attack")
        print("(r) Run\n") 

    combat_prompt()

    item_buff(player_character, current_enemy)

    def show_combat_details():
        clear_terminal_in_game(player_health, player_character, player_name)    
        combat_prompt()
    
    while current_enemy.health > 0 and player_health > 0:
        
        combat_choice = input()
        run_chance = random.randrange(1,11)
        light_attack = attack(current_enemy, player_character, player_health, 9, 2)
        heavy_attack = attack(current_enemy, player_character, player_health, 5, 3)

        if combat_choice == "l":
            # Handle damage and hit chande of light attack
            player_health = light_attack
            input()
            show_combat_details()
        elif combat_choice == "h":
            # Handle damage and hit chande of heavy attack
            player_health = heavy_attack
            input()
            show_combat_details()
        elif combat_choice == "r":
            if run_chance <= 4:
                print("You manage to escape!") 
                break
            else:
                print("Your attempt at escape was unsuccessful!") 
                player_health -= current_enemy.damage * 2
            input()
            show_combat_details()
        else:
            show_combat_details()
            print("You can't do that right now")

    defeat(current_enemy, player_health, player_name, player_character, homescreen_callback, dropped_item, drop_odds)

def attack(current_enemy, player_character, player_health, accuracy, damage_mult):
    """
    Handles damage dealt and hit chance for light attack
    """
    hit_chance = random.randrange(1, 11)  # Only calculate once per attack
    enemy_hit_chance = random.randrange(1, 11)  # Enemy hit chance calculated once per turn
    
    if current_enemy.nature == "Might":
        if hit_chance < accuracy:  # Attack lands if hit_chance < 9
            current_enemy.health -= player_character.wisdom * damage_mult 
            current_enemy.health = max(current_enemy.health, 0)  # Prevent health from dropping below 0
        else:
            print("Your attack missed!")
        if enemy_hit_chance < 8:  # Enemy attack logic
            player_health -= math.ceil(current_enemy.damage / player_character.wisdom) 
            player_health = max(player_health, 0) # Prevent health from dropping below 0
        else: 
            print("You dodged the enemy's attack!")
        
    elif current_enemy.nature == "Wisdom":
        if hit_chance < accuracy:
            current_enemy.health -= player_character.cunning * damage_mult
            current_enemy.health = max(current_enemy.health, 0)  # Prevent health from dropping below 0
        else:
            print("Your attack missed!")
        if enemy_hit_chance < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.cunning)
            player_health = max(player_health, 0) # Prevent health from dropping below 0
        else: 
            print("You dodged the enemy's attack!")
        
    else:
        if hit_chance < accuracy:
            current_enemy.health -= player_character.might * damage_mult
            current_enemy.health = max(current_enemy.health, 0)  # Prevent health from dropping below 0
        else:
            print("Your attack missed!")
        if enemy_hit_chance < 8:
            player_health -= math.ceil(current_enemy.damage / player_character.might)
            player_health = max(player_health, 0) # Prevent health from dropping below 0
        else: 
            print("You dodged the enemy's attack!")

    return player_health  # Return updated player_health

def item_buff(player_character, current_enemy):
    if player_character.item == "Chainmail":
        current_enemy.damage -= 1
    elif player_character.item == "Spiked Gloves":
        player_character.might += 1
    elif player_character.item == "Hooded Cloak":
        player_character.cunning += 1
    elif player_character.item == "Lexicon":
        player_character.wisdom += 1
    elif player_character.item == "Focusing Crystal":
        accuracy += 1