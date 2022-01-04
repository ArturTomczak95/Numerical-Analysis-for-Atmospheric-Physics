import numpy as np
from core.gaussPivot import gaussPivot


def calculcate_matrix_inverse(matrix):
    matrix_len = len(matrix)
    identity_matrix = np.identity(matrix_len)
    tranposed_identyity = np.transpose(identity_matrix)
    inversed_matrix = []
    for column in tranposed_identyity:
        inverse_column = gaussPivot(np.copy(matrix), column)
        inversed_matrix.append(inverse_column)

    return np.array(inversed_matrix)


def handle(matrix):
    inverse_matrix = calculcate_matrix_inverse(matrix)
    print("Matrix inverse:")
    print(inverse_matrix)


if __name__ == '__main__':
    print("__________started__________")
    A = np.array([[2., -1., 0],
         [-1., 2. ,-1.],
         [0, -1. ,2.]])
    handle(A)
    print("__________finished__________")
