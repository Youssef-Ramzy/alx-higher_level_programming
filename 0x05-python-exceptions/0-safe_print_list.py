#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for i in x:
            i += i
        print(my_list[i], end="")
        return i
    except IndexError:
        raise(IndexError)
