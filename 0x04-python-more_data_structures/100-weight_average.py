#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    denominator = 0

    for tuple in my_list:
        number += tuple[0] * tuple[1]
        denominator += tuple[1]

    return (number / denominator)
