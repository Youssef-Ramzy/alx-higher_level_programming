#!/usr/bin/python3
def print_last_digit(number):
    digit = abs(number) % 10
    print(digit, end='')
    return digit
r = print_last_digit(-98)
print(r)