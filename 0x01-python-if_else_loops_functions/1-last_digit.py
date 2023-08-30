#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = 0

if number >= 0:
    l_digit = number % 10
else:
    l_digit = (-number % 10) * -1

print(f"Last digit of {number} is {l_digit}")

if l_digit == 0:
    print(" and is 0")
elif l_digit > 5 and l_digit % 10 != 0:
    print(" is greater than 5")
else:
    print(" and is less than 6 and not 0")
