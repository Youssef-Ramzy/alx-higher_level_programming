#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    if n is 0:
        return 0, None
    return n, sentence[0]
