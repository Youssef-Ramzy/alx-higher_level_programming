#!/usr/bin/python3
"""Add item"""
import sys
load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

def main():
    """Main function"""
    args = sys.argv[1:]
    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(args)
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
