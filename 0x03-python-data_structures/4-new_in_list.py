#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    num_of_items = len(my_list)

    new_list = my_list[:]

    if 0 <= idx < num_of_items:
        new_list[idx] = element

    return (new_list)
