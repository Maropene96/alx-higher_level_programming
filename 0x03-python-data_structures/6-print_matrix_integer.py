#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for line in range(len(matrix[i])):
            if line != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][line]), end='')
        print()
