import math
import random
from classes import ITEMS
from utilities import clear_terminal_in_game, clear_terminal

def defeat(current_enemy, player_name, player_character, homescreen_callback, dropped_item, drop_odds):
    """
    Handles player & enemy defeat
    """
    random_item_chance = random.randrange(1,11) # Randomizes chance of item drops

    if player_character.health == 0:
        clear_terminal_in_game(player_character, player_name)
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
                    clear_terminal_in_game(player_character, player_name)
                    break  # Exit loop after picking up
                elif choice == "n":
                    print("You left the item behind.")
                    clear_terminal_in_game(player_character, player_name)
                    break  # Exit loop after leaving
                else:
                    print("You can't do that right now")


def combat(current_enemy, player_character, player_name, homescreen_callback, dropped_item, drop_odds):
    """
    Handles the flow of combat within the game
    """
    clear_terminal_in_game(player_character, player_name)

    def combat_prompt():
        print(f'{current_enemy.name} Health: {max(current_enemy.health, 0)}hp')
        print("What will you do?\n")
        print("(l) Light Attack")
        print("(h) Heavy Attack")
        print("(i) Item")
        print("(r) Run\n") 

    combat_prompt()

    def show_combat_details():
        clear_terminal_in_game(player_character, player_name)    
        combat_prompt()
    
    while current_enemy.health > 0 and player_character.health > 0:
        
        combat_choice = input()
        run_chance = random.randrange(1,11)  

        if combat_choice == "l":
            # Handle damage and hit chande of light attack
            player_character.health = attack(current_enemy, player_character, 9, 2)
            input()
            show_combat_details()

        elif combat_choice == "h":
            # Handle damage and hit chande of heavy attack
            player_character.health = attack(current_enemy, player_character, 5, 3)
            input()
            show_combat_details()

            # Handles whe player presses (i) to check item
        elif combat_choice == "i":
            check_item(player_character)
            input()
            show_combat_details()

            # Handles running from combat
        elif combat_choice == "r":
            if run_chance <= 4:
                print("You manage to escape!") 
                break
            else:
                print("Your attempt at escape was unsuccessful!") 
                player_character.health -= current_enemy.damage * 2
                input(f"The {current_enemy.name} lands a crushing blow while you are distracted! (-{current_enemy.damage * 2}hp)")
            input()
            show_combat_details()
        else:
            show_combat_details()
            print("You can't do that right now")

    defeat(current_enemy, player_name, player_character, homescreen_callback, dropped_item, drop_odds)

def attack(current_enemy, player_character, accuracy, damage_mult):
    """
    Handles damage dealt and hit chance for light attack
    """
    hit_chance = random.randrange(1, 11)  # Only calculate once per attack
    enemy_hit_chance = random.randrange(1, 11)  # Enemy hit chance calculated once per turn
    
    if current_enemy.nature == "Might":
        if hit_chance < accuracy:  # Attack lands if hit_chance < accuracy
            current_enemy.health -= player_character.wisdom * damage_mult 
            current_enemy.health = max(current_enemy.health, 0)  # Prevent health from dropping below 0
            input(f"Your attack lands! (-{player_character.wisdom * damage_mult}hp)")
        else:
            print("Your attack missed!")

        if enemy_hit_chance < 8:  # Enemy attack logic
            player_character.health -= math.ceil(current_enemy.damage / player_character.wisdom) 
            player_character.health = max(player_character.health, 0) # Prevent health from dropping below 0
            input(f"You get hit by the {current_enemy.name}! (-{math.ceil(current_enemy.damage / player_character.wisdom)}hp)")
        else: 
            print("You dodged the enemy's attack!")
        
    elif current_enemy.nature == "Wisdom":
        if hit_chance < accuracy: # Attack lands if hit_chance < accuracy
            current_enemy.health -= player_character.cunning * damage_mult
            current_enemy.health = max(current_enemy.health, 0)  # Prevent health from dropping below 0
            input(f"Your attack lands! -{player_character.cunning * damage_mult}hp")
        else:
            print("Your attack missed!")
        if enemy_hit_chance < 8:
            player_character.health -= math.ceil(current_enemy.damage / player_character.cunning)
            player_character.health = max(player_character.health, 0) # Prevent health from dropping below 0
            input(f"You get hit by the {current_enemy.name}! (-{math.ceil(current_enemy.damage / player_character.cunning)}hp)")
        else: 
            print("You dodged the enemy's attack!")
        
    else:
        if hit_chance < accuracy: # Attack lands if hit_chance < accuracy
            current_enemy.health -= player_character.might * damage_mult
            current_enemy.health = max(current_enemy.health, 0)  # Prevent health from dropping below 0
            input(f"Your attack lands! -{player_character.might * damage_mult}hp")
        else:
            print("Your attack missed!")
        if enemy_hit_chance < 8:
            player_character.health -= math.ceil(current_enemy.damage / player_character.might)
            player_character.health = max(player_character.health, 0) # Prevent health from dropping below 0
            input(f"You get hit by the {current_enemy.name}! (-{math.ceil(current_enemy.damage / player_character.might)}hp)")
        else: 
            print("You dodged the enemy's attack!")

    return player_character.health  # Return updated player_character.health

def check_item(player_character):
    """
    Handles item command during combat
    """
    item = player_character.item.strip()

    if player_character.item == "Apple" or player_character.item == "Throwing Knife":
        if item in ITEMS:
            print(f"{item} - {ITEMS[item]}")
        else:
            print("Unknown item")
    elif player_character.item == "None":
        print("You don't currently have an item!")
    else:
        if item in ITEMS:
            print(f"{item} - {ITEMS[item]}")
        else:
            print("Unknown item")

def item_choice(player_character, item):
    """
    Handles player choice when picking up an item
    """
    choice = input("Yes(y) / No(n) (Replaces current item)")
    if choice == "y":
        player_character.item = item
        print(f"You pick up the {item}")
        
    elif choice == "n":
        print(f"You left the {item} behind.")
        
    else:
        print("You can't do that right now")

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