#!/usr/bin/python3

"""
Appends text to a file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends text to a file and returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
