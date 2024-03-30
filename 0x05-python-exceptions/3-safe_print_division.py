#!/usr/bin/python3
def safe_print_division(a, b):
    c = None
    try:
        c = a / b
    except ZeroDivisionError:
        return c
    finally:
        if c is None:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(c))
        return c
