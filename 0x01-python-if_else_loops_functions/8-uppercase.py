#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if (i != len(str) - 1):
            if (96 < ord(str[i]) < 123):
                print(chr(ord(str[i]) - 32), end='')
            else:
                print(str[i], end='')
        else:
            if (96 < ord(str[i]) < 123):
                print(chr(ord(str[i]) - 32))
            else:
                print(str[i])
