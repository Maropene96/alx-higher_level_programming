#!/usr/bin/python3
def multiple_returns(sentence):
    num_of_ch = len(sentence)

    if (num_of_ch == 0):
        new_tuple = (num_of_ch, None)
    else:
        new_tuple = (num_of_ch, sentence[0])

    return (new_tuple)
