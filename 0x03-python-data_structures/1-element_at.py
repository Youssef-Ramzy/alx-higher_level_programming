#!/usr/bin/python3
def element_at(my_list, idx):
    n = len(my_list)
    if (idx > n):
        return (0)
    if (idx < 0):
        return (0)
    return (my_list[idx - 1])
