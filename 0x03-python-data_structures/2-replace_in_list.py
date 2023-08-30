#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    num_of_items = len(my_list)
    if idx > num_of_items - 1:
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
