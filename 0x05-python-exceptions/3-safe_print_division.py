#!/usr/bin/python3
""" Safe division - checking for Division by zero """


def safe_print_division(a, b):
    q = 0
    try:
        q = a / b
    except ZeroDivisionError:
        q = None
    finally:
        print('Inside result: {}'.format(q))
        return q
