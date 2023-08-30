#!/usr/bin/python3
def uppercase(str):
    for t in range(len(str)):
        if ord(str[t]) >= 97 and ord(str[t]) < 123:
            number = 32
        else:
            number = 0
        print("{:c}".format(ord(str[t]) - number), end='')
    print()
