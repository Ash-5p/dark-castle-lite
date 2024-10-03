import math

def combat(current_enemy, player_character, player_health):
    """
    Handles the combat mechanics within the game
    """
    print("What will you do?\n")
    print("Attack(a)")
    print("Run(r)\n")

    print(player_health, current_enemy.health) 

    combat_choice = input()

    while current_enemy.health > 0:
        if combat_choice == "a":
            if current_enemy.nature == "Might":
                current_enemy.health -= player_character.wisdom * 2
                player_health -= math.ceil(current_enemy.damage / player_character.wisdom)
            elif current_enemy.nature == "Wisdom":
                current_enemy.health -= player_character.cunning * 2
                player_health -= math.ceil(current_enemy.damage / player_character.cunning)
            else:
                current_enemy.health -= player_character.might * 2
                player_health -= math.ceil(current_enemy.damage / player_character.might)
        print(player_health, current_enemy.health)