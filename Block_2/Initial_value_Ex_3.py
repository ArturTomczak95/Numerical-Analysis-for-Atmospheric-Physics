from core2 import run_kut4, run_kut5
import numpy as np
import matplotlib.pyplot as plt


def func(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -4.75 * y[0] - 10*y[1]
    return F


def get_init_conditions():
    x0 = 0
    y0 = [-9, 0]
    xStop = 3
    h = np.logspace(start=np.log10(0.1),stop=np.log10(1.0), num=1000)**2
    return [x0, y0, xStop, h]


def calculate_estimated_x_y():
    [x0, y0, xStop, h] = get_init_conditions()
    sets_x = []
    sets_y = []
    for idx, step in enumerate(h):
        if idx % 100 == 0:
            print("{%s} sets: %i/%i" % (calculate_estimated_x_y.__name__, idx, len(h)), end="\r")
        [x, y] = run_kut4.integrate(func, x0, y0, xStop, step)
        sets_x.append(x)
        sets_y.append(y)

    return sets_x, sets_y


def plot(x_calculated, y_calculated, color, label):
    plt.plot(x_calculated, y_calculated, color=color, linestyle='dashed', markerfacecolor=color, markersize=12,
             label=label)


def calculate_estimated_solution():
    [set_x, set_y] = calculate_estimated_x_y()
    idx = 0
    plot(set_x[idx], set_y[idx][:,1], color="blue", label="y' 1st")
    plot(set_x[idx], set_y[idx][:,0], color="red", label="y_est 1st")

    return [set_x, set_y]


def exact_func(x):
    return -9.5 * np.exp(-x/2) + 0.5*np.exp(-(9.5 * x)/2)


def get_exact_x_y_values(x, y, xStop, h):
    X = []
    Y = []
    X.append(x)
    Y.append(exact_func(x))
    while x < xStop:
        h = min(h,xStop - x)
        y = exact_func(x)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)


def calculate_exact_solution():
    [x0, y0, xStop, _] = get_init_conditions()
    [x, y] = get_exact_x_y_values(x0, y0, xStop, 0.001)
    plot(x, y, color="green", label="y_exp")
    return x, y


def show_plot():
    plt.legend(loc='best')
    plt.show()


def plot_errors(errors, h):
    plot(h, errors, color="red", label="errors")
    plt.yscale('log')
    show_plot()


def calculate_errors(y_est_sets, y_exp, h):
    errors = []
    for i in range(0, len(y_est_sets)):
        error = abs(y_exp[-1] - y_est_sets[i][:,1][-1])
        errors.append(error)

    plot_errors(errors, h)
    return errors


def get_h_min_for_y_of_3(h, errors):
    min_err_idx = np.argmin(errors)
    step = h[min_err_idx]
    print("{%s} \t\t min error for f(3): %f, step index: %i, step: %f" % (get_h_min_for_y_of_3.__name__,
                                                                     min(errors), min_err_idx, step))


def get_h_boundary(h, errors):
    error_acceptance_level = 0.05
    boundary_h_idx = 0
    for i in range(0, len(errors) - 1):
        err_ratio = (errors[i] - errors[i + 1]) / errors[i]

        if abs(err_ratio) > error_acceptance_level:
            boundary_h_idx = i
            break

    print("{%s} \t\t\t boundary step index: %i, step: %f" % (get_h_boundary.__name__, boundary_h_idx, h[boundary_h_idx]))


def calculate_optimal_step(x_exp, y_exp, x_est, y_est, h):
    error_index = 0
    smallest_error = np.infty

    z = np.polyfit(x_exp, y_exp, 3)
    f = np.poly1d(z)
    y_expected = []
    for x_val in x_exp:
        y_expected.append(f(x_val))
    for i in range(0, len(y_est)):
        if i % 50 == 0:
            print("{%s} sets: %i/%i" % (calculate_optimal_step.__name__, i, len(y_est)), end="\r")
        z = np.polyfit(x_est[i], y_est[i][:,0], 3)
        f = np.poly1d(z)
        y_estimated = []
        for x_val in x_exp:
            y_estimated.append(f(x_val))
        error = np.absolute(np.array(y_expected) - np.array(y_estimated))
        error_sum = np.sum(error)
        if error_sum < smallest_error:
            smallest_error = error_sum
            error_index = i

    plot(x_est[error_index], y_est[error_index][:,1], color="blue", label="y' 1st")
    plot(x_est[error_index], y_est[error_index][:,0], color="red", label="y_est 1st")
    plot(x_exp, y_exp, color="green", label="y_exp")
    show_plot()
    print("{%s} \t smallest error: %f, err idx: %i, step: %f" % (calculate_optimal_step.__name__, smallest_error,
                                                               error_index, h[error_index]))


def get_y_of_3_from_runKut5():
    [x0, y0, xStop, h] = get_init_conditions()
    sets_x = []
    sets_y = []
    for idx, step in enumerate(h):
        if idx % 100 == 0:
            print("{%s} sets: %i/%i" % (get_y_of_3_from_runKut5.__name__, idx, len(h)), end="\r")
        [x, y] = run_kut5.integrate(func, x0, y0, xStop, step)
        sets_x.append(x)
        sets_y.append(y)

    idx = 0
    calculate_exact_solution()
    plot(sets_x[idx], sets_y[idx][:,1], color="blue", label="y' 1st")
    plot(sets_x[idx], sets_y[idx][:,0], color="red", label="y_est 1st")
    show_plot()

    return sets_x, sets_y


def handle():
    [_, _, _, h] = get_init_conditions()

    [x_est, y_est] = calculate_estimated_solution()
    [x_exp, y_exp] = calculate_exact_solution()
    show_plot()

    kut4_errors = calculate_errors(y_est, y_exp, h)

    get_h_min_for_y_of_3(h, kut4_errors)
    get_h_boundary(h, kut4_errors)
    calculate_optimal_step(x_exp, y_exp, x_est, y_est, h)

    [_, y5_est] = get_y_of_3_from_runKut5()
    kut5_errors = calculate_errors(y5_est, y_exp, h)
    get_h_min_for_y_of_3(h, kut5_errors)


if __name__ == '__main__':
    print("__________started__________")
    handle()
    print("__________finished__________")
