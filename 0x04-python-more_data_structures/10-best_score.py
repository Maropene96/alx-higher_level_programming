#!/usr/bin/python3
def best_score(my_dictionary):
    if not my_dictionary:
        return (None)

    return (max(my_dictionary, key=my_dictionary.get))
