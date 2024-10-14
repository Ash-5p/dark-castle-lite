"""
This module contains utility functions.
"""
import os
import sys
from art import HTP


def center_print(text):
    print(f"{text : ^80}")


def center_input(text):
    input(f"{text : ^80}")


def clear_terminal():
    """
    Clears the terminal
    """
    # Suggested in stackoverflow. (see Credits section in README)
    print("\033c")


def clear_terminal_in_game(player_character, player_name):
    """
    Clears the terminal while keeping character information visible
    """
    player_info = (
        f"Name: {player_name} | Class: {player_character.name} | "
        f"{player_character.description()}\n"
    )
    health_item = (
        f"Health: {player_character.health}hp | Item: {player_character.item}"
    )

    clear_terminal()
    center_print(player_info)
    center_print(health_item)
    center_print(
        "_____________________________________________________________________"
        "___________\n")


def clear_terminal_instructions():
    clear_terminal()
    center_print(HTP)
    center_print("Play Game (p) | Back to main menu (h)")
    center_print(
        "Page 1 (1) | Page 2 (2) | Page 3 (3) | Page 4 (4) | Page 5 (5)"
    )
    center_print(
        "_____________________________________________________________________"
        "___________\n")
