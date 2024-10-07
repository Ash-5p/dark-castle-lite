import math
import random
from classes import ITEMS
from utilities import *

global ranom_item
random_item = random.choice(list(ITEMS.keys()))


def defeat(current_enemy, player_name, player_character, homescreen_callback, dropped_item, drop_odds):
    """
    Handles player & enemy defeat
    """
    # Randomizes chance of item drops
    random_item_chance = random.randrange(1,11)
    

    if player_character.health == 0:
        clear_terminal_in_game(player_character, player_name)
        center_print("You have been defeated!\n")
        center_input("Press any button to return to main menu...")
        homescreen_callback()
    elif current_enemy.health == 0:
        if random_item_chance >= drop_odds: # 11 = 100% Chance
            input(f'{current_enemy.name} has been defeated!')
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
                    print(f"You left the {dropped_item} behind.")
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
            player_character.health = attack(current_enemy, player_character, 9, 1.5)
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
            if run_chance <= 3 and current_enemy.boss == False:
                input("You manage to escape!") 
                break
            elif current_enemy.boss == True:
                input("You are unable to escape!")
            else:
                print("Your attempt at escape was unsuccessful!") 
                player_character.health -= current_enemy.max_damage * 2
                input(f"The {current_enemy.name} lands a crushing blow while you are distracted! (-{current_enemy.max_damage * 2}hp)")
            input()
            show_combat_details()
        else:
            show_combat_details()
            print("You can't do that right now")

    defeat(current_enemy, player_name, player_character, homescreen_callback, dropped_item, drop_odds)


def attack(current_enemy, player_character, accuracy, damage_mult):
    """
    Handles damage dealt and hit chance for attack type
    """
    hit_chance = random.randrange(1, 11)  # Only calculate once per attack
    enemy_hit_chance = random.randrange(1, 11)  # Enemy hit chance calculated once per turn
    enemy_damage = current_enemy.get_random_damage()


    def nature_weakness_calculation(player_resistant_stat):
        """
        Function to handle enemy & player nature weaknesses & resistances 
        (Might > Cunning > Wisdom > Might)
        """
        # Damage Formulas
        enemy_damage_mult = 1 + (2.5 / player_resistant_stat)
        damage_taken_formula = math.ceil(enemy_damage * enemy_damage_mult)
        damage_dealt_formula = math.ceil(player_resistant_stat * damage_mult * random.uniform(0.8, 1.2))

        if hit_chance < accuracy:  # Attack lands if hit_chance < accuracy
            current_enemy.health -= damage_dealt_formula
            current_enemy.health = max(current_enemy.health, 0)  # Prevent health from dropping below 0
            print(f"Your attack lands! (-{damage_dealt_formula}hp)")
        else:
            print("Your attack missed!")

        if enemy_hit_chance < 8:  # Enemy attack logic
            player_character.health -= damage_taken_formula # Damaged recieved is determined by resistant stat
            player_character.health = max(player_character.health, 0) # Prevent health from dropping below 0
            print(f"You get hit by the {current_enemy.name}! (-{damage_taken_formula}hp)")
            print("Press enter to continue...")
        else: 
            print("You dodged the enemy's attack!")
            print("Press enter to continue...")

    if current_enemy.nature == "Might": # Wisdom > Might
        nature_weakness_calculation(player_character.wisdom)

    elif current_enemy.nature == "Wisdom": # Cunning > Wisdom
        nature_weakness_calculation(player_character.cunning)

    else: # Might > Cunning
        nature_weakness_calculation(player_character.might)
   
    return player_character.health  # Return updated player_character.health


def check_item(player_character):
    """
    Handles item command during combat
    """
    item = player_character.item.strip()

    if player_character.item == "Apple" or player_character.item == "Throwing Knife" or player_character.item == "Mirror Film":
        if item in ITEMS:
            print(f"{item} - {ITEMS[item]}")
            while True:
                print(f"Do you want to use the {item}?")
                choice = input("Yes(y) / No(n)")
                if choice == "y":
                    print(f"You used the {item}")
                    player_character.item = "None"
                    break
                elif choice == "n":
                    print(f"You put the {item} away")
                    break
                else:
                    print("You can't do that right now!")
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
    center_print("Yes(y) / No(n) (Replaces current item)")
    choice = input()
    if choice == "y":
        player_character.item = item
        print(f"You pick up the {item}")
        
    elif choice == "n":
        print(f"You left the {item} behind.")
        
    else:
        print("You can't do that right now")

############### Not yet functional ######################
def item_buff(player_character, current_enemy):
    while True:
        enemy_damage = current_enemy.get_random_damage()
        if player_character.item == "Chainmail":
            enemy_damage -= 1
        elif player_character.item == "Spiked Gloves":
            player_character.might += 1
        elif player_character.item == "Hooded Cloak":
            player_character.cunning += 1
        elif player_character.item == "Lexicon":
            player_character.wisdom += 1
        elif player_character.item == "Focusing Crystal":
            accuracy += 1
            