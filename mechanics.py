import math
import random
from classes import ITEMS
from utilities import clear_terminal_in_game, center_print, center_input

global random_item
# Filters out Mirror Sphere item from random drops
filtered_items = [item for item in ITEMS if item != "Mirror Sphere"]
random_item = random.choice(filtered_items)


# Class used to break combat loop when using Mirror Sphere item
class EscapeCombat(Exception):
    pass


def defeat(
    current_enemy, player_name, player_character, homescreen_callback,
    dropped_item, drop_odds, base_stats
):
    """
    Handles player & enemy defeat within combat
    """
    # Randomizes chance of item drops
    random_item_chance = random.randrange(1, 11)

    if player_character.health <= 0:
        clear_terminal_in_game(player_character, player_name)
        center_print("You have been defeated!\n")
        center_input("Press enter to return to main menu...")
        homescreen_callback()
    elif current_enemy.health <= 0:
        # Handles item drop odds upon defeating an enemy
        if random_item_chance >= drop_odds:  # 11 = 100% Chance
            center_input(f'{current_enemy.name} has been defeated!')
        else:
            center_print(f'{current_enemy.name} has been defeated!')
            item_drop(
                current_enemy, player_name, player_character,
                homescreen_callback, dropped_item, drop_odds, base_stats
            )


def item_drop(
            current_enemy, player_name, player_character, homescreen_callback,
        dropped_item, drop_odds, base_stats
        ):
    """
    Handles player choice when an enemy drops an item in combat
    """
    center_print(
        f"{current_enemy.name} has dropped an item: {dropped_item}\n"
    )
    center_print("Do you want to pick it up? (Replaces current item)")
    center_print("Yes(y) / No(n)")

    while True:
        choice = input().strip()
        if choice == "y":
            player_character.item = dropped_item
            stat_reset(player_character, base_stats)
            item_buff(player_character)
            center_print(f"You pick up the {dropped_item}")
            center_input("(Press enter to continue...)")
            clear_terminal_in_game(player_character, player_name)
            break  # Exit loop after picking up
        elif choice == "n":
            center_print(f"You left the {dropped_item} behind.")
            center_input("(Press enter to continue...)")
            clear_terminal_in_game(player_character, player_name)
            break  # Exit loop after leaving
        else:
            print(f'You can\'t do "{choice}" right now')


def death_outside_combat(player_character, player_name, homescreen, damage):
    """
    Takes player to game over screen if health reaches 0 outside of combat
    """
    player_character.health -= damage
    player_character.health = max(player_character.health, 0)

    if player_character.health == 0:
        clear_terminal_in_game(player_character, player_name)
        center_print(f"You have perished! Rest in peace {player_name}\n")
        center_input("Press enter to return to main menu...")
        homescreen()


def combat(
    current_enemy, player_character, player_name, homescreen_callback,
    dropped_item, drop_odds, base_stats
        ):
    """
    Handles the flow of combat within the game
    """
    clear_terminal_in_game(player_character, player_name)

    def combat_prompt():
        """
        Displays combat controls and enemy info
        """
        center_print(
            f"{current_enemy.name} Health: {max(current_enemy.health, 0)}hp"
        )
        center_print(f"Nature: {current_enemy.nature}\n")
        center_print("What will you do?\n")
        center_print("(l) Light Attack")
        center_print("(h) Heavy Attack")
        center_print("(i) Item")
        center_print("(r) Run\n")

    combat_prompt()

    def show_combat_details():
        clear_terminal_in_game(player_character, player_name)
        combat_prompt()

    try:
        while current_enemy.health > 0 and player_character.health > 0:

            combat_choice = input().strip()
            run_chance = random.randrange(1, 11)

            if combat_choice == "l":
                light_attack(
                    current_enemy, player_character, show_combat_details
                )

            elif combat_choice == "h":
                heavy_attack(
                    current_enemy, player_character, show_combat_details
                )

                # Handles whe player presses (i) to check item
            elif combat_choice == "i":
                check_item(player_character, current_enemy)
                center_input("(Press enter to continue...)")
                show_combat_details()

                # Handles running from combat
            elif combat_choice == "r":
                if run_chance <= 3 and current_enemy.boss is False:
                    center_input("You manage to escape!")
                    break
                elif current_enemy.boss is True:
                    center_input("You are unable to escape!")
                else:
                    center_print("Your attempt at escape was unsuccessful!")
                    player_character.health -= current_enemy.max_damage * 2
                    player_character.health = max(player_character.health, 0)
                    center_input(
                        f"The {current_enemy.name} lands a crushing blow while"
                        " you are distracted! "
                        f"(-{current_enemy.max_damage * 2}hp)"
                    )
                input()
                show_combat_details()
            else:
                show_combat_details()
                print(f'You can\'t do "{combat_choice}" right now')

        defeat(
            current_enemy, player_name, player_character,
            homescreen_callback, dropped_item, drop_odds, base_stats
        )
    except EscapeCombat:  # Handles escape when using Mirror Sphere
        center_print(
            f"You slip away while the {current_enemy.name} is blinded...")
        center_input("(Press enter to continue...)")


def attack(current_enemy, player_character, accuracy, damage_mult):
    """
    Handles attack logic such as accuracy and damage calculations based on
    player stats, enemy nature, and player item.
    Use to create new attacks & control their accuracy & damage output with a
    single line.
    """
    # Only calculate once per attack
    hit_chance = random.randrange(1, 11)
    # Enemy hit chance calculated once per turn
    enemy_hit_chance = random.randrange(1, 11)
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
            center_print(f"Your attack lands! (-{damage_dealt_formula}hp)")
        else:
            center_print("Your attack missed!")

        if enemy_hit_chance < 8:  # Enemy attack logic
            # Damaged recieved is determined by resistant stat
            if player_character.item == "Chainmail":
                # Damage reduction buff from Chainmal item
                player_character.health -= (damage_taken_formula - 2)
            else:
                player_character.health -= damage_taken_formula
            # Prevent health from dropping below 0
            player_character.health = max(player_character.health, 0)
            center_print(
                f"You get hit by the {current_enemy.name}! "
                f"(-{damage_taken_formula}hp)"
            )
            center_print("(Press enter to continue...)")
        else:
            center_print("You dodged the enemy's attack!")
            center_print("(Press enter to continue...)")

    if current_enemy.nature == "Might":  # Wisdom > Might
        nature_weakness_calculation(player_character.wisdom)

    elif current_enemy.nature == "Wisdom":  # Cunning > Wisdom
        nature_weakness_calculation(player_character.cunning)

    else:  # Might > Cunning
        nature_weakness_calculation(player_character.might)

    return player_character.health  # Return updated player_character.health


def light_attack(current_enemy, player_character, show_combat_details):
    """
    Handles damage & accuracy of light attacks
    """
    if player_character.item == "Focusing Crystal":
        # Handle damage and hit chande of light attack with
        # Focusing Crystal item.
        player_character.health = attack(
            current_enemy, player_character, 11, 1.5
        )
        input()
        show_combat_details()
    else:
        # Handle damage and hit chance of light attack
        player_character.health = attack(
            current_enemy, player_character, 10, 1.5
        )
        input()
        show_combat_details()


def heavy_attack(current_enemy, player_character, show_combat_details):
    """
    Handles damage & accuracy of heavy attacks
    """
    if player_character.item == "Focusing Crystal":
        player_character.health = attack(
            current_enemy, player_character, 7, 3
        )
        input()
        show_combat_details()
    else:
        # Handle damage and hit chance of heavy attack
        player_character.health = attack(
            current_enemy, player_character, 6, 3
        )
        input()
        show_combat_details()


def check_item(player_character, current_enemy):
    """
    Handles item command during combat
    """
    item = player_character.item.strip()

    if (
        player_character.item == "Apple" or player_character.item
        == "Throwing Knife" or player_character.item == "Mirror Sphere"
    ):
        if item in ITEMS:
            center_print(f"{item} - {ITEMS[item]}")
            center_print(f"Do you want to use the {item}?")
            center_print("Yes(y) / No(n)\n")
            while True:
                choice = input().strip()
                if choice == "y":
                    center_print(f"You used the {item}\n")
                    if player_character.item == "Throwing Knife":
                        current_enemy.health -= 15
                        center_print("Enemy Health (-15hp)")
                    elif player_character.item == "Apple":
                        player_character.health += 30
                        center_print("Player Health (+30hp)")
                    elif player_character.item == "Mirror Sphere":
                        if current_enemy.boss is False:
                            center_print(
                                "You throw the Mirror Sphere on the ground, "
                                "causing it to explode in a dazzling\nlight!\n"
                            )
                            player_character.item = "None"
                            raise EscapeCombat
                        else:
                            player_character.health += 60
                            player_character.might *= 2
                            player_character.wisdom *= 2
                            player_character.cunning *= 2

                            center_input(
                                "The Mirror Sphere starts to glow in your hand"
                                " until it bursts in a dazzling\nlight! When "
                                "the light dims the sphere is gone... But you "
                                "feel twice as strong!\n"
                            )

                    player_character.item = "None"
                    break
                elif choice == "n":
                    center_print(f"You put the {item} away")
                    break
                else:
                    center_print(f'You can\'t do "{choice}" right now!')
        else:
            center_print("Unknown item")
    elif player_character.item == "None":
        center_print("You don't currently have an item!")
    else:
        if item in ITEMS:
            center_print(f"{item} - {ITEMS[item]}")
        else:
            center_print("Unknown item")


def item_choice(player_character, base_stats, item):
    """
    Handles player choice when picking up an item
    """
    center_print(f"Do you pick up the {item}?\n")
    center_print("Yes(y) / No(n) (Replaces current item)")
    while True:
        choice = input().strip()
        if choice == "y":
            player_character.item = item
            stat_reset(player_character, base_stats)
            item_buff(player_character)
            center_input(f"You pick up the {item}")
            break

        elif choice == "n":
            center_input(f"You left the {item} behind.")
            break

        else:
            center_print(f'You can\'t do "{choice}" right now')


def item_buff(player_character):
    """
    Handles stat buffs from Spiked Gloves, Hooded Clock & Lexicon items
    """

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
