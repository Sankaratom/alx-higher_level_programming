#!/usr/bin/python3
def pow(a, b):
    powd = a
    for i in range(0, b):
        powd *= a
    return powd
