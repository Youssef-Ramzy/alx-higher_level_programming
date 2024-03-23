#!/usr/bin/python3
"""Read file"""
def read_file(filename="UTF8.txt"):
    """Read file"""
    with open(filename, 'r') as file:
        print(file.read(), end="")
