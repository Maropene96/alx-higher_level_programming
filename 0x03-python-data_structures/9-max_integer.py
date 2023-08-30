#!/usr/bin/python3
def max_integer(my_list=[]):
    num_of_items = len(my_list)

    if num_of_items == 0:
        return (None)

    max_int = my_list[0]

    for i in range(1, num_of_items):
        if my_list[i] > max_int:
            max_int = my_list[i]

    return (max_int)
