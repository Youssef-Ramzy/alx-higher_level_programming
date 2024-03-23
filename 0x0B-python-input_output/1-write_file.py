#!/usr/bin/python3
"""Write file"""


def write_file(filename="UTF8.txt", text=""):
    """Write file"""
    with open(filename, 'w') as file:
        return file.write(text)
