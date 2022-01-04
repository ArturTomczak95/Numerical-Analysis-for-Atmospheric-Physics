import numpy as np


def get_init_conditions():
    f_N = [0, 37., 71., 104., 134., 161., 185., 207., 225., 239., 250.]
    h = 0.05
    return [np.array(f_N), h]


def calculate_composite_simpson_function(f_N, h):
    f_of_a = f_N[0]
    f_of_b = f_N[-1]
    listOdd = f_N[::2]      # odd/even switched due to indexing
    listEven = f_N[1::2]     # odd/even switched due to indexing
    even_sum = np.sum(listEven)
    odd_sum = np.sum(listOdd)

    return (h/3) * (f_of_a + f_of_b + 4 * even_sum + 2 * odd_sum)


def handle():
    [f_N, h] = get_init_conditions()
    simpson_sum = calculate_composite_simpson_function(f_N, h)
    print("simpson sum: %.10f" % (simpson_sum))


if __name__ == '__main__':
    print("__________started__________")
    handle()
    print("__________finished__________")