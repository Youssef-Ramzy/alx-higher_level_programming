#!/usr/bin/python3
"""Add item"""
import sys
import os.path
import json


def add_item(filename="add_item.json", *args):
    """Add item"""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            obj = json.load(file)
    else:
        obj = []
    obj.extend(args)
    with open(filename, "w") as file:
        json.dump(obj, file)
