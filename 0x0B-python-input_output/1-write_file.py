#!/usr/bin/python3
"""Write file"""


def write_file(filename="UTF8", text=""):
    '''Write file'''
    with open(filename + ".txt", "w") as file:
        return file.write(text)
