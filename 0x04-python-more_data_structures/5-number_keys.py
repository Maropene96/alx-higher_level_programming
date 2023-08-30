#!/usr/bin/python3
def number_keys(my_dictionary):
    number = 0
    list_keys = list(my_dictionary.keys())

    for x in list_keys:
        number += 1

    return (number)
