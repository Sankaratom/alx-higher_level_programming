#!/usr/bin/python3
""" Safely printing an integer by checking for a type error"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        print("Type Error")
        return False
    except ValueError:
        print("Value Error")
        return False
    except NameError:
        print("Name Error")
        return False
    except FloatingPointError:
        print("Floating point Error")
        return False

