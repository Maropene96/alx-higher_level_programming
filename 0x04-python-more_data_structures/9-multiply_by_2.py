#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary_new = a_dictionary.copy()
    list_keys = list(dictionary_new.keys())

    for i in list_keys:
        dictionary_new[i] *= 2

    return (dictionary_new)
