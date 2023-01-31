#!/usr/bin.python3
"""matrix division"""


def matrix_division(matrix, div):
    """Divide all elements of a matrix

    Args:
        matrix (list): A list of lists of ints or floats
        div (int/float): divisor for the elements in matrix

        Raises:
            TypeError: for non numbers different row sizez
            ZeroDivisionError: if div is 0
            Returns: new matrix with results
    """

    for row in matrix:
        for item in row:
            if (not isinstance(item, int) or not isinstance(item, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if (len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if (not isinstance(div, int) or not isinstance(div, float)):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
