import numpy as np
from core.LUdecomp import *
from save import get_upper_triangle_matrix, calculate_back_substitution_phase, get_lower_triangle_matrix


def gauss_decomposition(matrix_A, matrix_b):
    matrix, results = get_upper_triangle_matrix(matrix_A, matrix_b)
    x = calculate_back_substitution_phase(matrix, results)
    return x


def doolittle_decomposition(matrix_A, matrix_b):
    a = np.array(matrix_A)
    b = np.array(matrix_b)
    a = LUdecomp(a)
    x = LUsolve(a, b)
    return x


def gauss_jordan_method(matrix_A, matrix_b):
    matrix, results = get_upper_triangle_matrix(matrix_A, matrix_b)
    matrix_rev, results_rev = get_lower_triangle_matrix(matrix, results)
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
    # A = [[2.0, -3.0, -1.0],
    #      [3.0, 2.0, -5.0],
    #      [2.0, 4.0, -1.0]]
    # b = [3.0, -9.0, -5.0]
    # A = [[3.50, 2.77, -1.80, 2.68],
    #      [-0.76, 1.80, 3.44, -0.09],
    #      [0.27, 5.07, 1.71, 5.45],
    #      [6.90, 1.61, 2.68, 1.71]]
    # b = [[7.31, 5.30, 4.23, -1.89], [4.54 ,2.74, 1.55, 1.64],[ 13.85, 1.88, 11.55, 3.42], [8.78, 7.17, 6.10, 4.39]]
    A = [[2., -1., 0.], [-1., 2., -1.], [0., -1., 2.]]
    b = [[100., 100., 100.]]
    handle(A, b)
