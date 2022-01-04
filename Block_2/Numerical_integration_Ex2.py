from core2 import trapezoid as tr
import math
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return math.sqrt(x) * math.sin(math.sin(x))


def get_init_conditions():
    x0 = 0
    y0 = 1
    xStop = 1
    h = 0.1
    return [x0, y0, xStop, h]


def calculate_trapezoid():
    diff = math.inf
    trapezoid_prev_val = tr.trapezoid(func, 0, math.pi, 0, 1)
    trapezoid_val = 0
    i = 2
    while diff > 10**(-6):
        trapezoid_val = tr.trapezoid(func, 0, math.pi, trapezoid_prev_val, i)
        diff = trapezoid_val - trapezoid_prev_val
        trapezoid_prev_val = trapezoid_val
        i += 1

    print("trapezoid k final value: %i" % i)
    return [trapezoid_val, i]


def calculate_function(iterations):
    y_vals = []
    x_vals = np.linspace(0, math.pi, iterations)
    for x in x_vals:
        y_vals.append(func(x))

    return [x_vals, y_vals]


def draw_func(i):
    [x_vals, y_vals] = calculate_function(10000)
    [x_vals_trap, y_vals_trap] = calculate_function(i)

    plt.plot(x_vals, y_vals, color="red")
    plt.fill_between(x_vals_trap, y_vals_trap, color="blue")
    plt.show()


def handle():
    [trapezoid_val, iterations] = calculate_trapezoid()
    print("calculated area: ", trapezoid_val)
    draw_func(iterations)

if __name__ == '__main__':
    print("__________started__________")
    handle()
    print("__________finished__________")