from run import *

def combat(enemy_health, enemy_type, enemy_stat, enemy_damage):
    """
    Handles the combat mechanics within the game
    """
    print("What will you do?\n")
    print("Attack(a)")
    print("Run(r)\n")

    combat_choice = input()

    while enemy_health > 0:
        if combat_choice == "a":
            if enemy_stat == might:
                enemy_health -= player_character.wisdom * 2
                player_health -= math.ceil(enemy_damage / player_character.wisdom)
            elif enemy_stat == wisdom:
                enemy_health -= player_character.cunning * 2
                player_health -= math.ceil(enemy_damage / player_character.cunning)
            else:
                enemy_health -= player_character.might * 2
                player_health -= math.ceil(enemy_damage / player_character.might)