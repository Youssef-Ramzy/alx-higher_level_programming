#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in my_list:
        n = 0
        new_list = None
        if (i % 2) == 0:
            new_list[n] = True
            n = n+1
        new_list[n] = False
        n = n+1
    return new_list
