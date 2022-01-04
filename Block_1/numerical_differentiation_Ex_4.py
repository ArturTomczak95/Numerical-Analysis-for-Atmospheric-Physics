import sympy as sp
import numpy as np
from Helpers.PlotData import PlotData

x_symbol = sp.Symbol('x')


def calculate_two_arrays_sum(array_a, array_b):
    a = np.array(array_a)
    b = np.array(array_b)
    arr_mul = np.matmul(a, b)

    return np.sum(arr_mul)


def calculate_array_sum(array, degree):
    arr = np.array(array)
    arr_to_degree = arr ** degree

    return np.sum(arr_to_degree)


def least_squares(x_coordinates, y_coordinates, degree):
    n = degree + 1
    A = np.zeros(shape=(n, n))
    A[0][0] = len(x_coordinates)
    j_start = 1
    for i in range(0, n):
        for j in range(j_start, n):
            sum_degree = i + j
            A[i][j] = calculate_array_sum(x_coordinates, sum_degree)
        j_start = 0

    b = np.zeros(shape=(n))
    b[0] = sum(y_coordinates)
    for i in range(1, n):
        x_arr = np.array(x_coordinates)
        x_to_degree = x_arr ** i
        b[i] = calculate_two_arrays_sum(x_to_degree, y_coordinates)

    return A, b


def get_least_squares_polynomial(coefs, symbol_x):
    formula = coefs[0]
    for i in range(1, len(coefs)):
        formula = formula + coefs[i] * symbol_x ** i

    return formula


def least_squares_linear(plot_data, x_data):
    from block_1_methods import LinearAlgebraicMethods, Helpers
    global x_symbol

    print()
    print("Least squares linear")
    [A, b] = least_squares(plot_data.get_x_coordinates(), plot_data.get_y_coordinates(), degree=1)
    coefficients = LinearAlgebraicMethods.gauss_decomposition(A, b)
    polynomial = get_least_squares_polynomial(coefficients, x_symbol)
    Helpers.calculate_derivatives(polynomial, x_data, x_symbol)


def least_squares_quadratic(plot_data, x_data):
    from block_1_methods import LinearAlgebraicMethods, Helpers
    global x_symbol

    print()
    print("Least squares quadratic")
    [A, b] = least_squares(plot_data.get_x_coordinates(), plot_data.get_y_coordinates(), degree=2)
    coefficients = LinearAlgebraicMethods.gauss_decomposition(A, b)
    polynomial = get_least_squares_polynomial(coefficients, x_symbol)
    Helpers.calculate_derivatives(polynomial, x_data, x_symbol)


def handle(matrix, x_data):
    plot_data = PlotData(matrix)
    least_squares_linear(plot_data, x_data)
    least_squares_quadratic(plot_data, x_data)


if __name__ == '__main__':
    print("__________started__________")
    matrixA = [[0, 7], [2, 11], [3, 28]]  # [[x,y], [x, y],...]
    handle(matrixA, 1)
    print("__________finished__________")