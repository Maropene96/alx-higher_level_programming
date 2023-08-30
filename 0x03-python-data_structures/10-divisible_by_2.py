#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divis_vals = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divis_vals.append(True)
        else:
            divis_vals.append(False)

    return (divis_vals)
