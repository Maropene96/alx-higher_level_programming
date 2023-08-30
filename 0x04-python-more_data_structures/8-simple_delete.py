#!/usr/bin/python3
def eight_simple_delete(my_dictionary, key=""):
    if my_dictionary.get(key) is not None:
        del my_dictionary[key]
    return (my_dictionary)
