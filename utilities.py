"""
This module contains utility functions.
"""
import os
import sys

def clear_terminal():
    """
    Clears the terminal
    """
    # Suggested in stackoverflow. (see Credits section in README)
    print("\033c")

def clear_terminal_in_game(player_character, player_name):
    """
    Clears the terminal and displays player's health and item
    """
    print("\033c")
    print(f"Name: {player_name} | Class: {player_character.name} | Health: {player_character.health}hp | Item: {player_character.item} | {player_character.description()}")
    print("________________________________________________________________________________")


def blank_lines(num_lines, line_type="print_line"):
    """
    Adds specific number of blank lines for styling.
    Parameters: num_lines (number of blank lines), line type

    "line_type" accepts "print_line", "inline", and after_line"
    as arguments.
    "print_line" (default): - if this is inside print();
    "inline": - if this is concatenated in a string but not at the end;
    "after_line": - if this is concatenated at end of a string.

    Returns: number of blank lines that can be printed in the terminal
    """
    if line_type == "print_line":
        num_lines -= 1
    elif line_type == "inline":
        num_lines += 1
    elif line_type == "after_line":
        num_lines += 0

    return "\n" * num_lines