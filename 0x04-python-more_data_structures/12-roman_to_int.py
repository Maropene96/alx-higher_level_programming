#!/usr/bin/python3
def to_subtracttract(list_number):
    to_subtract = 0
    maximum_list = max(list_number)

    for x in list_number:
        if maximum_list > x:
            to_subtract += x

    return (maximum_list - to_subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_n.keys())

    number = 0
    last_roman = 0
    list_number = [0]

    for ch in roman_string:
        for r_number in list_keys:
            if r_number == ch:
                if roman_n.get(ch) <= last_roman:
                    number += to_subtracttract(list_number)
                    list_number = [roman_n.get(ch)]
                else:
                    list_number.append(roman_n.get(ch))

                last_roman = roman_n.get(ch)

    number += to_subtracttract(list_number)

    return (number)
