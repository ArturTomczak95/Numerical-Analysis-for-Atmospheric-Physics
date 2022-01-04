import sympy as sp
from Helpers.PlotData import PlotData
from block_1_methods import Helpers

x_symbol = sp.Symbol('x')


def get_gradient_base(xi, xj, yi, yj):
    nominator = yj - yi
    denominator = xj - xi

    return nominator / denominator


def calculate_coeficients(plot_data):
    x_coord = plot_data.x_coordinates
    y_coord = plot_data.y_coordinates

    a = []
    for i in range(0 , plot_data.elements_count() - 1):
        a_i = []
        if i == 0:
            for j in range(i, plot_data.elements_count() - 1):
                    a_j = (y_coord[j + 1] - y_coord[j]) / (x_coord[j + 1] - x_coord[j])
                    a_i.append(a_j)
        else:
            for j in range(0, len(a[i - 1]) - 1):
                a_j = (a[i - 1][j + 1] - a[i - 1][j]) / (x_coord[j + i + 1] - x_coord[j])
                a_i.append(a_j)
        a.append(a_i)

    coefs = []
    coefs.append(y_coord[0])
    for list in a:
        coefs.append(list[0])

    return coefs


def get_polynomial(x_coord, coefs, x):
    polynomial = 0
    for i in range(0, len(x_coord)):
        x_calcualtions = 1
        for j in range(0, i):
            x_calcualtions = x_calcualtions * (x - x_coord[j])
        polynomial = polynomial + coefs[i] * x_calcualtions
    return polynomial


def get_newton_polynomial(plot_data):
    global x_symbol
    coefs = calculate_coeficients(plot_data)
    polynomial = get_polynomial(plot_data.x_coordinates, coefs, x_symbol)

    return  polynomial


def get_newton_func(newton_polynomial):
    global x_symbol
    return sp.lambdify(x_symbol, newton_polynomial, modules=['numpy'])


def handle(matrix, x_data):
    global x_symbol
    plot_data = PlotData(matrix, x_data)
    newton_polynomial = get_newton_polynomial(plot_data)
    Helpers.calculate_derivatives(newton_polynomial, x_data, x_symbol)


if __name__ == '__main__':
    print("__________started__________")
    # x_data_inputted = input("x? ")
    x_data_inputted = 1
    matrixA = [[0, 7], [2, 11], [3, 28]]  # [[x,y], [x, y],...]
    # matrixA = [[-5., -2.], [-1., 6.], [0, 1.], [2., 3.]]  # [[x,y], [x, y],...]
    # matrixA = np.array([[0.84, 0.431711], [0.92, 0.398519], [1.00, 0.367879], [1.08, 0.339596], [1.16, 0.313486]])  # [[x,y], [x, y],...]
    handle(matrixA, int(x_data_inputted))
    print("__________finished__________")