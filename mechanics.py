import math
import random
from classes import ITEMS
from utilities import *

global random_item
random_item = random.choice(list(ITEMS.keys()))

class EscapeCombat(Exception):
    pass

def defeat(
    current_enemy, player_name, player_character, homescreen_callback, 
    dropped_item, drop_odds, base_stats
):
    """
    Handles player & enemy defeat
    """
    # Randomizes chance of item drops
    random_item_chance = random.randrange(1,11)
    

    if player_character.health <= 0:
        clear_terminal_in_game(player_character, player_name)
        center_print("You have been defeated!\n")
        center_input("Press any button to return to main menu...")
        homescreen_callback()
    elif current_enemy.health <= 0:
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
                    stat_reset(player_character, base_stats)
                    item_buff(player_character)
                    clear_terminal_in_game(player_character, player_name)
                    break  # Exit loop after picking up
                elif choice == "n":
                    print(f"You left the {dropped_item} behind.")
                    clear_terminal_in_game(player_character, player_name)
                    break  # Exit loop after leaving
                else:
                    print(f'You can\'t do "{choice}" right now')


def combat(
    current_enemy, player_character, player_name, homescreen_callback, 
    dropped_item, drop_odds, base_stats
    ):
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
    
    try:
        while current_enemy.health > 0 and player_character.health > 0:
            
            combat_choice = input()
            run_chance = random.randrange(1,11)  

            if combat_choice == "l":
                # Handle damage and hit chande of light attack
                player_character.health = attack(
                    current_enemy, player_character, 9, 1.5
                )
                input()
                show_combat_details()

            elif combat_choice == "h":
                # Handle damage and hit chande of heavy attack
                player_character.health = attack(
                    current_enemy, player_character, 5, 3
                )
                input()
                show_combat_details()

                # Handles whe player presses (i) to check item
            elif combat_choice == "i":
                check_item(player_character, current_enemy)
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
                    player_character.health = max(player_character.health, 0)
                    input(
                        f"The {current_enemy.name} lands a crushing blow while "
                        "you are distracted! "
                        f"(-{current_enemy.max_damage * 2}hp)"
                    )
                input()
                show_combat_details()
            else:
                show_combat_details()
                print(f'You can\'t do "{combat_choice}" right now')

        defeat(current_enemy, player_name, player_character, 
            homescreen_callback, dropped_item, drop_odds, base_stats
        )
    except EscapeCombat:
        center_input("You successfully escaped the combat!")


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
        damage_dealt_formula = math.ceil(
            player_resistant_stat * damage_mult * random.uniform(0.8, 1.2)
        )

        if hit_chance < accuracy:  # Attack lands if hit_chance < accuracy
            current_enemy.health -= damage_dealt_formula
            # Prevent health from dropping below 0
            current_enemy.health = max(current_enemy.health, 0)
            print(f"Your attack lands! (-{damage_dealt_formula}hp)")
        else:
            print("Your attack missed!")

        if enemy_hit_chance < 8:  # Enemy attack logic
            # Damaged recieved is determined by resistant stat
            player_character.health -= damage_taken_formula
            # Prevent health from dropping below 0
            player_character.health = max(player_character.health, 0)
            print(
                f"You get hit by the {current_enemy.name}! "
                f"(-{damage_taken_formula}hp)"
            )
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


def check_item(player_character, current_enemy):
    """
    Handles item command during combat
    """
    item = player_character.item.strip()

    if player_character.item == "Apple" or player_character.item == "Throwing Knife" or player_character.item == "Mirror Sphere":
        if item in ITEMS:
            print(f"{item} - {ITEMS[item]}")
            while True:
                print(f"Do you want to use the {item}?")
                choice = input("Yes(y) / No(n)")
                if choice == "y":
                    print(f"You used the {item}")
                    if player_character.item == "Throwing Knife":
                        current_enemy.health -= 15
                    elif player_character.item == "Apple":
                        player_character.health += 30
                    elif player_character.item == "Mirror Sphere":
                        if current_enemy.boss == False:
                            input(
                                "You throw the Mirror Sphere on the ground, "
                                "causing it to explode in a dazzling light!\n"
                                f"You slip away while the {current_enemy.name} "
                                "is blinded..."
                            )
                            player_character.item = "None"
                            raise EscapeCombat
                        else:
                            player_character.health += 60
                            player_character.might *= 2
                            player_character.wisdom *= 2
                            player_character.cunning *= 2

                            input(
                                "The Mirror Sphere starts to glow in your hand"
                                "until it bursts in a dazzling light!\n When "
                                "the light dims the sphere is gone... But you "
                                "feel twice as strong!"
                            )

                    player_character.item = "None"
                    break
                elif choice == "n":
                    print(f"You put the {item} away")
                    break
                else:
                    print(f'You can\'t do "{choice}" right now!')
        else:
            print("Unknown item")
    elif player_character.item == "None":
        print("You don't currently have an item!")
    else:
        if item in ITEMS:
            print(f"{item} - {ITEMS[item]}")
        else:
            print("Unknown item")


def item_choice(player_character, base_stats, item):
    """
    Handles player choice when picking up an item
    """
    center_print(f"Do you pick up the {item}?\n")
    center_print("Yes(y) / No(n) (Replaces current item)")
    choice = input()
    if choice == "y":
        player_character.item = item
        stat_reset(player_character, base_stats)
        item_buff(player_character)
        print(f"You pick up the {item}")
        
    elif choice == "n":
        print(f"You left the {item} behind.")
        
    else:
        print(f'You can\'t do "{choice}" right now')

############### Not yet functional ######################
def item_buff(player_character):

    if player_character.item == "Spiked Gloves":
        player_character.might += 3
    elif player_character.item == "Hooded Cloak":
        player_character.cunning += 3
    elif player_character.item == "Lexicon":
        player_character.wisdom += 3


def stat_reset(player_character, base_stats):
    """
    Resets charater Might, Wisdom & Cunning Stats
    """
    player_character.wisdom = base_stats.wisdom
    player_character.might = base_stats.might
    player_character.cunning = base_stats.cunning

# enemy_damage = current_enemy.get_random_damage()
# if player_character.item == "Chainmail":
#     enemy_damage -= 2
# elif player_character.item == "Focusing Crystal":
#     accuracy += 1
            