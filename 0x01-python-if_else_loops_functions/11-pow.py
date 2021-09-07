#!/usr/bin/python3
def pow(a, b):
    powd = a
    for i in range(1, b):
        powd *= a
    return powd
