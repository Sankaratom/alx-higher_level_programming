#!/usr/bin/python3
""" Printing only integers from a list of various types """


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        var = my_list[i]
        try:
            print("{:d}".format(var), end="")
            count += 1
        except ValueError:
            continue
    print()
    return count
