import numpy as np
from Helpers.PlotData import PlotData

def calculate_3_points_central_first_derivative(y_coordinates, step):
    nominator = y_coordinates[-1] - y_coordinates[0]
    denominator = 2 * step

    return nominator / denominator


def calculate_5_points_central_third_derivative(y_coordinates, step):
    nominator = y_coordinates[-1] - 2 * y_coordinates[-2] + 2 * y_coordinates[1] - y_coordinates[0]
    denominator = 2 * step ** 3

    return nominator / denominator


def calculate_first_central_first_derivative(y_coordinates, step):
    derivative = calculate_3_points_central_first_derivative(y_coordinates[1:-1], step)
    error_part = calculate_5_points_central_third_derivative(y_coordinates, step)

    return derivative - (step ** 2 / 6) * error_part


def handle(matrix):
    [x_coordinates, y_coordinates] = PlotData.get_xy_coordinates(matrix)
    step = x_coordinates[1] - x_coordinates[0]

    first_derivative = calculate_first_central_first_derivative(y_coordinates, step)
    print("First derivative of 1.00: %.10f" % first_derivative)


if __name__ == '__main__':
    print("__________started__________")
    matrixA = np.array([[0.84, 0.431711], [0.92, 0.398519], [1.00, 0.367879], [1.08, 0.339596], [1.16, 0.313486]])  # [[x,y], [x, y],...]
    handle(matrixA)
    print("__________finished__________")
