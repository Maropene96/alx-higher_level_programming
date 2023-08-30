#!/usr/bin/python3
def prxnt_sorted_dictionary(my_dictionary):
    list_ord = list(my_dictionary.keys())
    list_ord.sort()
    for x in list_ord:
        print("{}: {}".format(x, my_dictionary.get(x)))
