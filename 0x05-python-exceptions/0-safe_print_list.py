#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for i in x:
            print(my_list[1], end="")
        return i
    except IndexError:
        raise(IndexError)
