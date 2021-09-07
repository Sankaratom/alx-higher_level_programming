#!/usr/bin/python3
def pow(a, b):
    powd = a
    if (b > 0):
        for i in range(1, b):
            powd *= a
        return powd
    elif (b = 0):
        return 1
    else:
        for i in range(1, -1 * b):
            powd *= a
        return 1 / powd
