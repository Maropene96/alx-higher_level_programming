#!/usr/bin/python3
def multiply_by_two(my_dictionary):
    new_dictionary = my_dictionary.copy()
    list_keys = list( new_dictionary.keys())

    for x in list_keys:
         new_dictionary[x] *= 2

    return ( new_dictionary)
