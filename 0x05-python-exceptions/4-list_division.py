#!/usr/bin/python3
""" Dividing elements of a list with elements of another list"""


def list_division(my_list_1, my_list_2, list_length):
    div = [None] * list_length
    for i in range(list_length):
        try:
            div[i] = my_list_1[i] / my_list_2[i]
        except IndexError:
            div[i] = 0
            print("out of range")
        except ZeroDivisionError:
            div[i] = 0
            print("division by 0")
        except TypeError:
            div[i] = 0
            print("wrong type")
        finally:
            continue
    return div
