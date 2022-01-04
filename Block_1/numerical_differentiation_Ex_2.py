import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from Helpers.PlotData import PlotData

x_symbol = sp.Symbol('x')


def calculate_lagrange_polynomial(x_coordinates, y_coordinates, x):
    interpolants = []
    matrix_len = len(x_coordinates)
    for current_y_inx in range(matrix_len):  # y
        y_point = y_coordinates[current_y_inx]
        x_multiplication_nominator = 1
        x_multiplication_denominator = 1
        for current_x_inx in range(matrix_len):  # x
            if current_y_inx != current_x_inx:
                x_n = x_coordinates[current_x_inx]
                x_main = x_coordinates[current_y_inx]
                x_multiplication_nominator *= x - x_n
                x_multiplication_denominator *= x_main - x_n
        interpolants.append(y_point * (x_multiplication_nominator / x_multiplication_denominator))

    return sum(interpolants)


def get_lagrange_polynomial(plot_data):
    global x_symbol
    lagrange_polynomial = calculate_lagrange_polynomial(plot_data.x_coordinates, plot_data.y_coordinates, x_symbol)
    return lagrange_polynomial


def get_lagrange_func(lagrange_polynomial):
    global x_symbol
    return sp.lambdify(x_symbol, lagrange_polynomial, modules=['numpy'])


def arrange_plot_samples(plot_data):
    delta = 0.025
    return np.arange(min(plot_data.x_coordinates) - abs(500),
                     max(plot_data.x_coordinates) + abs(500), delta).tolist()


def show_data(plot_data, lagrange_func):
    x_samples = arrange_plot_samples(plot_data)
    y_array = []
    for x_sample in x_samples:
        y_array.append(lagrange_func(x_sample))
    y_unknown = lagrange_func(plot_data.x_data)
    plt.scatter(plot_data.x_data, y_unknown, color='red')
    plt.scatter(plot_data.x_coordinates, plot_data.y_coordinates, color='blue', marker='o')
    plt.plot(x_samples, y_array, color='green', linestyle='dashed', markerfacecolor='blue', markersize=12)
    plt.show()


def calculate_derivatives(lagrange_polynomial, x_data):
    global x_symbol
    lagrange_func = get_lagrange_func(lagrange_polynomial)
    first_derivative = sp.diff(lagrange_polynomial, x_symbol)
    first_derivative_func = sp.lambdify(x_symbol, first_derivative, modules=['numpy'])
    second_derivative = sp.diff(first_derivative, x_symbol)
    second_derivative_func = sp.lambdify(x_symbol, second_derivative, modules=['numpy'])
    print("lagrange polynomial: ", sp.simplify(lagrange_polynomial))
    print("y value of x=%d: %.10f" % (x_data, lagrange_func(x_data)))
    print("first derivative: ", sp.simplify(first_derivative))
    print("first derivative of %.10f: %.10f" % (x_data, first_derivative_func(x_data)))
    print("second derivative: %.10f" % (sp.simplify(second_derivative)))
    print("second derivative of %d: %.10f" % (x_data, second_derivative_func(x_data)))


def handle(matrix, x_data):
    plot_data = PlotData(matrix, int(x_data))
    lagrange_polynomial = get_lagrange_polynomial(plot_data)
    lagrange_func = get_lagrange_func(lagrange_polynomial)
    show_data(plot_data, lagrange_func)
    calculate_derivatives(lagrange_polynomial, x_data)


if __name__ == '__main__':
    x_data_inputted = input("x? ")
    matrixA = [[0, 7], [2, 11], [3, 28]]  # [[x,y], [x, y],...]
    # matrixA = np.array([[0.84, 0.431711], [0.92, 0.398519], [1.00, 0.367879], [1.08, 0.339596], [1.16, 0.313486]])  # [[x,y], [x, y],...]
    handle(matrixA, int(x_data_inputted))
