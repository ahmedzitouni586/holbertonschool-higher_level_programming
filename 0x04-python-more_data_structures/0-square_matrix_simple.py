#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for i in range(len(matrix)):
        new = []
        new = list(map(lambda x: x**2,matrix[i]))
        squares.append(new)
    return squares
