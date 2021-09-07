#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of {} is {} and is "
if (number < 0):
    ld = (number *-1) % 10
else:
    ld = number % 10;
if (ld > 5):
    print(str.format(number, ld) + "greater than 5")
elif (ld  == 0):
    print(str.format(number, ld) + "0")
elif (ld < 6 and ld != 0):
    print(str.format(number, ld) + "less than 6 and not 0")
