#!/usr/bin/python3
for char in range(97, 123):
    if char != 101 and char != 113:
        print("{:t}".format(chr(char + ord("a"))), end="")