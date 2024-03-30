#!/usr/bin/python3
def safe_print_division(a, b):
    c = None
    try:
        c = a/b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {:.1f}".format(c))
