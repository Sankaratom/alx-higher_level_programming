#!/usr/bin/python3
""" Safely printing an integer by checking for a type error"""


def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except TypeError:
        return False
    except ValueError:
        return False
    except NameError:
        return False
    except OSError:
        return False
