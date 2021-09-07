#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if (96 < ord(str[i]) < 123):
            str = str.replace(str[i], chr(ord(str[i]) - 32))
    print(str)
