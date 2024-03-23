#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    with open(filename + ".txt", "w") as file:
        return file.write(text)
