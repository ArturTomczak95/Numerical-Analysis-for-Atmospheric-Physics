import numpy as np
from core.LUdecomp import *
from Block_1.Helpers.Decomposition import MatrixDecomposition


def gauss_decomposition(matrix_A, matrix_b):
    matrix, results = MatrixDecomposition.get_upper_triangle_matrix(matrix_A, matrix_b)
    x = MatrixDecomposition.calculate_back_substitution_phase(matrix, results)
    return x


def doolittle_decomposition(matrix_A, matrix_b):
    a = np.array(matrix_A)
    b = np.array(matrix_b)
    a = LUdecomp(a)
    x = LUsolve(a, b)
    return x


def gauss_jordan_method(matrix_A, matrix_b):
    matrix, results = MatrixDecomposition.get_upper_triangle_matrix(matrix_A, matrix_b)
    matrix_rev, results_rev = MatrixDecomposition.get_lower_triangle_matrix(matrix, results)
    x = []
    for i in range(len(results_rev)):
        x.append(results_rev[i] / matrix_rev[i][i])
    return x


def print_results(x, matrix_A):
    print("xT", np.matrix(x))
    print("check A*x: ", np.matmul(np.array(matrix_A), x))


def handle(matrix_A, matrix_b):
    print("# Gauss decomposition")
    print()
    gauss = gauss_decomposition(matrix_A, matrix_b)
    print_results(gauss, matrix_A)
    print("# Doolittle decomposition")
    print()
    doolittle = doolittle_decomposition(matrix_A, matrix_b)
    print_results(doolittle, matrix_A)
    print()
    print("# Gauss-Jordan decomposition")
    gauss_jordan = gauss_jordan_method(matrix_A, matrix_b)
    print_results(gauss_jordan, matrix_A)


if __name__ == '__main__':
    np.set_printoptions(formatter={'float_kind':"{:.10f}".format})
    A = [[2.0, -3.0, -1.0],
         [3.0, 2.0, -5.0],
         [2.0, 4.0, -1.0]]
    b = [3.0, -9.0, -5.0]
    handle(A, b)
