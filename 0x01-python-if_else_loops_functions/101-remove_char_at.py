#!/usr/bin/python3
def remove_char_at(str, n):
    t = ""
    for i in range(len(str)):
        if i != n:
            t = t + str[i]
    return (t)
