#!/usr/bin/python3
""" Safely printing an integer by checking for a type error"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("Value Error")
        return False
