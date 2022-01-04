import numpy as np
from math import factorial
import matplotlib.pyplot as plt


def func(x, y):
    F = np.zeros(3)
    F[0] = y[1]
    F[1] = -0.5*(y[0]**2 + 1) - y[0]
    F[2] = (-0.5*(y[0]**2 + 1))**(-1) * 2 * F[1] - F[1]
    return F


def get_init_conditions():
    x0 = 0
    y0 = [1, 0]
    h = 0.01
    return [x0, y0, h]


def run_tay3(F, x, y, h):
    T0 = h*F(x, y)[0]
    T1 = (h**2 / factorial(2)) * F(x, y)[1]
    T2 = (h**3 / factorial(3)) * F(x, y)[2]
    return T0 + T1 + T2


def error(F, x, y, h):
    return h**3 / (factorial(3 + 1)) * (F(x + h, y)[2] - F(x , y)[2])


def integrate(F, x, y, h):
    return y + run_tay3(F, x, y, h) + error(F, x, y, h)


def handle():
    [x0, y0, h] = get_init_conditions()
    y = integrate(func, x0, y0, h)
    print("f(0.1) estimated: %.10f" % y[0])
    plt.plot([0], [1], marker='o', color="blue", label="y(0) 1st")
    plt.plot([0.1], [y[0]], marker='o', color="red", label="y_est 1st")
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    print("__________started__________")
    handle()
    print("__________finished__________")
