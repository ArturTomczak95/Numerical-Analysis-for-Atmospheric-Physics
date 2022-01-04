import sympy as sp


class DerivativesFromPolynomial:
    @staticmethod
    def get_func(polynomial, symbol_x):
        return sp.lambdify(symbol_x, polynomial, modules=['numpy'])

    @staticmethod
    def calculate_derivatives(polynomial, x_data, symbol_x, second_derivative=True):
        lagrange_func = DerivativesFromPolynomial.get_func(polynomial, symbol_x)
        first_derivative = sp.diff(polynomial, symbol_x)
        first_derivative_func = sp.lambdify(symbol_x, first_derivative, modules=['numpy'])

        print("f(x): ", sp.simplify(polynomial))
        print("f(x=%d) = %.10f" % (x_data, lagrange_func(x_data)))
        print("f'(x): ", sp.simplify(first_derivative))
        print("f'(%.10f) = %.10f" % (x_data, first_derivative_func(x_data)))

        if second_derivative:
            second_derivative = sp.diff(first_derivative, symbol_x)
            second_derivative_func = sp.lambdify(symbol_x, second_derivative, modules=['numpy'])
            print("f''(x) = %.10f" % (sp.simplify(second_derivative)))
            print("f''(%.10f) = %.10f" % (x_data, second_derivative_func(x_data)))
