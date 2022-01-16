import numpy as np
from core3.householder import householder, computeP
from core3.eigenvals3 import eigenvals3
from core3.inversePower3 import inversePower3
from block_3_methods import SymmetricMatrixEigenvalue


def calculate_eigenvalues(np_A_matrix, diagonal_a_0, diagonal_a_1):
    matrix_size = len(np_A_matrix)
    P = computeP(np_A_matrix.copy())
    eigenvalues = eigenvals3(diagonal_a_0, diagonal_a_1, matrix_size)
    print("eigenvalues: \n", np.transpose(eigenvalues))
    print()

    return eigenvalues


def calculate_eigenvectors(diagonal_a_0, diagonal_a_1, eigenvalues):
    eigenvectors = []
    for eigenvalue in eigenvalues:
        [_, eigenvector] = inversePower3(diagonal_a_0, diagonal_a_1, eigenvalue)
        eigenvectors.append(eigenvector.tolist())
    print("eigenvectors: \n", np.array(eigenvectors))
    print()

    return eigenvectors


def handle(A_matrix):
    np_A_matrix = np.array(A_matrix)
    [diagonal_a_0, diagonal_a_1] = householder(np_A_matrix.copy())
    eigenvalues = calculate_eigenvalues(np_A_matrix, diagonal_a_0, diagonal_a_1)
    eigenvectors = calculate_eigenvectors(diagonal_a_0, diagonal_a_1, eigenvalues)
    SymmetricMatrixEigenvalue.check_accuracy(A_matrix, eigenvalues, eigenvectors)


if __name__ == '__main__':
    print("__________started__________")
    A = [[7., -4., 3., -2., 1., 0.],
         [-4., 8., -4., 3., -2., 1.],
         [3., -4., 9., -4., 3., -2.],
         [-2., 3., -4., 10., -4., 3.],
         [1., -2., 3., -4., 11., -4.],
         [0., 1., -2., 3., -4., 12.]]
    handle(A)
    print("__________finished__________")