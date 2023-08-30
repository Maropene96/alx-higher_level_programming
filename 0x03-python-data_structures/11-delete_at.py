#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    num_of_items = len(my_list)
    if idx < 0 or idx >= num_of_items:
        return (my_list)
    del my_list[idx]
    return (my_list)
