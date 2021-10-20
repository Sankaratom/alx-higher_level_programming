#!/usr/bin/python3
""" Prints a list safely by handling a possible out of bounds index """


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
