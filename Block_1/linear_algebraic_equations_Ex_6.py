import numpy as np
from core.gaussPivot import gaussPivot
from block_1_methods import LinearAlgebraicMethods


def handle(matrix, b):
    x = gaussPivot(matrix, b)
    condition_number = LinearAlgebraicMethods.calculate_1_norm_condition_number(matrix)
    matrix_determinant = np.linalg.det(matrix)
    print("Gauss-Jordan method result:")
    print(x)
    print("1 norm condition number:", condition_number)
    print("Matrix determinant:", matrix_determinant)


if __name__ == '__main__':
    print("__________started__________")
    A = np.array([[2., -1., 0],
                  [-1., 2. ,-1.],
                  [0, -1. ,2.]])
    b = [100]
    handle(A, b)
    print("__________finished__________")