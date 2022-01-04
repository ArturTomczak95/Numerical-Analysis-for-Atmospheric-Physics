from numpy import array
import matplotlib.pyplot as plt
from core2 import run_kut4


def func(x, y):
    return x**2 - 4*y


def get_init_conditions():
    x0 = 0
    y0 = 1
    xStop = 1
    h = 0.1
    return [x0, y0, xStop, h]


def run_kut2(F,x,y,h):
    K0 = h*F(x,y)
    K1 = h*F(x + h/2.0, y + K0/2.0)
    return K1

def integrate(F,x,y,xStop,h):
    X = []; Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut2(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
    return array(X),array(Y)


def handle():
    [x0, y0, xStop, h] = get_init_conditions()
    [kut_2_set_x, kut_2_set_y] = integrate(func, x0, y0, xStop, h)
    [kut_4_set_x, kut_4_set_y] = run_kut4.integrate(func, x0, y0, xStop, h)
    plt.plot(kut_2_set_x, kut_2_set_y, marker='o', color="blue", label="kut_2 y est")
    plt.plot(kut_4_set_x, kut_4_set_y, marker='o', color="red", label="kut_4 y est")
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    print("__________started__________")
    handle()
    print("__________finished__________")
