#!/usr/bin/python3
def complex_delete(my_dictionary, value):
    list_keys = list(my_dictionary.keys())

    for value_dictionary in list_keys:
        if value == my_dictionary.get(value_dictionary):
            del my_dictionary[value_dictionary]

    return (my_dictionary)
