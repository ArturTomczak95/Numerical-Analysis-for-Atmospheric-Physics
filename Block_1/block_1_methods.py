import linear_algebraic_equations_Ex_1
import linear_algebraic_equations_Ex_2
import linear_algebraic_equations_Ex_4
import linear_algebraic_equations_Ex_5
import numerical_differentiation_Ex_1
import numerical_differentiation_Ex_2
import numerical_differentiation_Ex_4
from Helpers.Derevatives import DerivativesFromPolynomial
from Helpers.TruncationError import TruncationDerivativesCentered, TruncationDerivativesBackward, TruncationDerivativesForward
from Helpers.StepsCoodrindate import FiveStepsCoordinate, FiveStepsCoordinateBackward, FiveStepsCoordinateForward


class LinearAlgebraicMethods:
    @staticmethod
    def gauss_decomposition(matrix, results):
        return linear_algebraic_equations_Ex_1.gauss_decomposition(matrix, results)

    @staticmethod
    def doolittle_decomposition(matrix, results):
        return linear_algebraic_equations_Ex_1.doolittle_decomposition(matrix, results)

    @staticmethod
    def gauss_jordan_method(matrix, results):
        return linear_algebraic_equations_Ex_1.gauss_jordan_method(matrix, results)

    @staticmethod
    def cholesky_decomposition(matrix, results):
        return linear_algebraic_equations_Ex_2.cholesky_decomposition(matrix, results)

    @staticmethod
    def calculcate_matrix_inverse(matrix):
        return linear_algebraic_equations_Ex_4.calculcate_matrix_inverse(matrix)

    @staticmethod
    def calculate_1_norm_condition_number(matrix):
        return linear_algebraic_equations_Ex_5.calculate_1_norm_condition_number(matrix)

    @staticmethod
    def calculate_infinity_norm_condition_number(matrix):
        return linear_algebraic_equations_Ex_5.calculate_infinity_norm_condition_number(matrix)


class NumericalMethods:
    @staticmethod
    def calculate_first_central_first_derivative(y_coordinates, step):
        return numerical_differentiation_Ex_1.calculate_first_central_first_derivative(y_coordinates, step)

    @staticmethod
    def get_lagrange_polynomial(plot_data):
        return numerical_differentiation_Ex_2.get_lagrange_polynomial(plot_data)

    @staticmethod
    def least_squares_k_degree(x_coordinates, y_coordinates, degree):
        return numerical_differentiation_Ex_4.least_squares(x_coordinates, y_coordinates, degree)

    @staticmethod
    def get_least_squares_polynomial(coefficients, symbol_x):
        return numerical_differentiation_Ex_4.get_least_squares_polynomial(coefficients, symbol_x)


class Helpers:
    @staticmethod
    def calculate_derivatives(polynomial, x_data, symbol_x, second_derivative=True):
        return DerivativesFromPolynomial.calculate_derivatives(polynomial, x_data, symbol_x, second_derivative)

    @staticmethod
    def get_func(polynomial, x_symbol):
        return DerivativesFromPolynomial.get_func(polynomial, x_symbol)

    @staticmethod
    def calculate_truncation_third_derivative_central(five_steps: FiveStepsCoordinate, step):
        return TruncationDerivativesCentered.calculate_truncation_third_derivative(five_steps, step)

    @staticmethod
    def calculate_truncation_forth_derivative_central(five_steps: FiveStepsCoordinate, step):
        return TruncationDerivativesCentered.calculate_truncation_forth_derivative(five_steps, step)

    @staticmethod
    def calculate_truncation_second_derivative_backward(five_steps: FiveStepsCoordinateBackward, step):
        return TruncationDerivativesBackward.calculate_truncation_second_derivative(five_steps, step)

    @staticmethod
    def calculate_truncation_third_derivative_backward(five_steps: FiveStepsCoordinateBackward, step):
        return TruncationDerivativesBackward.calculate_truncation_third_derivative(five_steps, step)

    @staticmethod
    def calculate_truncation_forth_derivative_backward(five_steps: FiveStepsCoordinateBackward, step):
        return TruncationDerivativesBackward.calculate_truncation_forth_derivative(five_steps, step)

    @staticmethod
    def calculate_truncation_second_derivative_forward(five_steps: FiveStepsCoordinateForward, step):
        return TruncationDerivativesForward.calculate_truncation_second_derivative(five_steps, step)

    @staticmethod
    def calculate_truncation_third_derivative_forward(five_steps: FiveStepsCoordinateForward, step):
        return TruncationDerivativesForward.calculate_truncation_third_derivative(five_steps, step)

    @staticmethod
    def calculate_truncation_forth_derivative_forward(five_steps: FiveStepsCoordinateForward, step):
        return TruncationDerivativesForward.calculate_truncation_forth_derivative(five_steps, step)
