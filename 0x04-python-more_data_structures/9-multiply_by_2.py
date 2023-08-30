#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict = a_dictionary.copy()
    list_keys = list(dict.keys())
    for i in list_keys:
        dict[i] *= 2
    return (dict)
