import numpy as np
import sympy as sp
from Helpers.PlotData import PlotData
from core.polyFit import stdDev
from block_1_methods import NumericalMethods, LinearAlgebraicMethods, Helpers

x_symbol = sp.Symbol('x')


def get_lowest_st_dev_coefs(plot_data, x_data):
    global x_symbol
    std_dev = np.Inf
    coefs = []
    for i in range(1, 20):
        [matrix, results] = NumericalMethods.least_squares_k_degree(plot_data.x_coordinates, plot_data.y_coordinates, i)
        coefs = LinearAlgebraicMethods.gauss_decomposition(matrix, results)
        std_dev_bufor = stdDev(coefs, plot_data.x_coordinates, plot_data.y_coordinates)
        if std_dev_bufor < std_dev:
            std_dev = std_dev_bufor
        else:
            break
    return coefs


def handle(matrix, x_data):
    plot_data = PlotData(matrix)
    coefs = get_lowest_st_dev_coefs(plot_data, x_data)
    polynomial = NumericalMethods.get_least_squares_polynomial(coefs, x_symbol)
    Helpers.calculate_derivatives(polynomial, 0, x_symbol, second_derivative=False)
    print()
    Helpers.calculate_derivatives(polynomial, 1, x_symbol, second_derivative=False)


if __name__ == '__main__':
    print("__________started__________")
    matrixA = [[0., .0919],
               [.2, .1667],
               [.4, .4065],
               [.6, .5094],
               [.8, .7676],
               [1.0, .7925],
               [1.2, .9332],
               [1.4, 1.0253],
               [1.6, 1.0778],
               [1.8, 1.0657],
               [2., .9187]]  # [[x,y], [x, y],...]
    handle(matrixA, 1)
    print("__________finished__________")