#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters
    written.

    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
