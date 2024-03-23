#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="UTF8.txt", text=""):
    """Append to a file"""
    with open(filename, 'a') as file:
        return file.write(text)
