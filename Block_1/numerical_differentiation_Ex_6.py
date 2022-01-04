from block_1_methods import NumericalMethods, Helpers
from Helpers.PlotData import PlotData
from Helpers.StepsCoodrindate import FiveStepsCoordinate, FiveStepsCoordinateBackward, FiveStepsCoordinateForward
from math import factorial


class FirstCentral:
    @staticmethod
    def calculate_3_points_central_second_derivative(y, step):
        nominator = y.x_plus_h - 2 * y.x + y.x_minus_h
        denominator = step ** 2  # (h^2)

        return nominator / denominator

    @staticmethod
    def calculate_second_derivative(five_steps, step):
        derivative = FirstCentral.calculate_3_points_central_second_derivative(five_steps, step)
        error_part = Helpers.calculate_truncation_forth_derivative_central(five_steps, step)

        return derivative - (step ** 2 / 6) * error_part

    @staticmethod
    def get_first_central_derivatives(plot_data: PlotData, step):
        five_steps = FiveStepsCoordinate(plot_data)
        first_derivative = NumericalMethods.calculate_first_central_first_derivative(five_steps.get_y_coordinates(),
                                                                                     step)
        second_derivative = FirstCentral.calculate_second_derivative(five_steps, step)

        return [first_derivative, second_derivative]


class FirstBackward:
    @staticmethod
    def calculate_backward_first_derivative(y: FiveStepsCoordinateBackward, step):
        nominator = y.x - y.x_minus_h
        denominator = step

        return nominator / denominator

    @staticmethod
    def calculate_first_derivative(derivative_func, five_steps: FiveStepsCoordinateBackward, step):
        derivative = derivative_func
        second_derivative = Helpers.calculate_truncation_second_derivative_backward(five_steps, step)
        third_derivative = Helpers.calculate_truncation_third_derivative_backward(five_steps, step)
        forth_derivative = Helpers.calculate_truncation_forth_derivative_backward(five_steps, step)

        return derivative - (step / 2) * second_derivative - (step ** 2 / 6) * third_derivative - (step ** 3 / factorial(4)) * forth_derivative

    @staticmethod
    def calculate_backward_second_derivative(y: FiveStepsCoordinateBackward, step):
        nominator = y.x - 2 * y.x_minus_h + y.x_minus_2h
        denominator = step ** 2

        return nominator / denominator

    @staticmethod
    def calculate_second_derivative(derivative_func, five_steps: FiveStepsCoordinateBackward, step):
        derivative = derivative_func
        third_derivative = Helpers.calculate_truncation_forth_derivative_backward(five_steps, step)
        forth_derivative = Helpers.calculate_truncation_forth_derivative_backward(five_steps, step)

        return derivative - (step ** 2 / 6) * third_derivative - (step ** 3 / factorial(4)) * forth_derivative

    @staticmethod
    def get_first_backward_finite_differences(plot_data: PlotData, step):
        five_steps = FiveStepsCoordinateBackward(plot_data)
        first_derivative_func = FirstBackward.calculate_backward_first_derivative(five_steps, step)
        first_derivative = FirstBackward.calculate_first_derivative(first_derivative_func, five_steps, step)

        second_derivative_func = FirstBackward.calculate_backward_second_derivative(five_steps, step)
        second_derivative = FirstBackward.calculate_second_derivative(second_derivative_func, five_steps, step)

        return [first_derivative, second_derivative]


class FirstForward:
    @staticmethod
    def calculate_forward_first_derivative(y: FiveStepsCoordinateForward, step):
        nominator = y.x_plus_h - y.x
        denominator = step

        return nominator / denominator

    @staticmethod
    def calculate_first_derivative(derivative_func, five_steps: FiveStepsCoordinateForward, step):
        derivative = derivative_func
        second_derivative = Helpers.calculate_truncation_second_derivative_forward(five_steps, step)
        third_derivative = Helpers.calculate_truncation_forth_derivative_forward(five_steps, step)
        forth_derivative = Helpers.calculate_truncation_forth_derivative_forward(five_steps, step)

        return derivative - (step / 2) * second_derivative - (step ** 2 / 6) * third_derivative - (step ** 3 / factorial(4)) * forth_derivative

    @staticmethod
    def calculate_forward_second_derivative(y: FiveStepsCoordinateForward, step):
        nominator = y.x - 2 * y.x_plus_h + y.x_plus_2h
        denominator = step ** 2

        return nominator / denominator

    @staticmethod
    def calculate_second_derivative(derivative_func, five_steps: FiveStepsCoordinateForward, step):
        derivative = derivative_func
        third_derivative = Helpers.calculate_truncation_forth_derivative_forward(five_steps, step)
        forth_derivative = Helpers.calculate_truncation_forth_derivative_forward(five_steps, step)

        return derivative - (step ** 2 / 6) * third_derivative - (step ** 3 / factorial(4)) * forth_derivative

    @staticmethod
    def get_first_forward_derivatives(plot_data: PlotData, step):
        five_steps = FiveStepsCoordinateForward(plot_data)

        first_derivative_func = FirstForward.calculate_forward_first_derivative(five_steps, step)
        first_derivative = FirstForward.calculate_first_derivative(first_derivative_func, five_steps, step)

        second_derivative_func = FirstForward.calculate_forward_second_derivative(five_steps, step)
        second_derivative = FirstForward.calculate_second_derivative(second_derivative_func, five_steps, step)

        return [first_derivative, second_derivative]


class SecondBackward:
    @staticmethod
    def calculate_first_derivative(y: FiveStepsCoordinateBackward, step):
        nominator = 3 * y.x - 4 * y.x_minus_h - y.x_minus_2h
        denominator = 2 * step

        return nominator / denominator

    @staticmethod
    def calculate_second_derivative(y: FiveStepsCoordinateBackward, step):
        nominator = 2 * y.x - 5 * y.x_minus_h + 4 * y.x_minus_2h - y.x_minus_3h
        denominator = step ** 2

        return nominator / denominator

    @staticmethod
    def get_second_backward_derivatives(plot_data, step):
        five_steps = FiveStepsCoordinateBackward(plot_data)

        first_derivative = SecondBackward.calculate_first_derivative(five_steps, step)
        second_derivative = SecondBackward.calculate_second_derivative(five_steps, step)

        return [first_derivative, second_derivative]


class SecondForward:
    @staticmethod
    def calculate_first_derivative(y: FiveStepsCoordinateForward, step):
        nominator = - 3 * y.x + 4 * y.x_plus_h - y.x_plus_2h
        denominator = 2 * step

        return nominator / denominator

    @staticmethod
    def calculate_second_derivative(y: FiveStepsCoordinateForward, step):
        nominator = 2 * y.x - 5 * y.x_plus_h + 4 * y.x_plus_2h - y.x_plus_3h
        denominator = step ** 2

        return nominator / denominator

    @staticmethod
    def get_second_forward_derivatives(plot_data, step):
        five_steps = FiveStepsCoordinateForward(plot_data)

        first_derivative = SecondForward.calculate_first_derivative(five_steps, step)
        second_derivative = SecondForward.calculate_second_derivative(five_steps, step)

        return [first_derivative, second_derivative]


def calculate_step(x_coordinates):
    return x_coordinates[1] - x_coordinates[0]


def handle(matrix):
    plot_data = PlotData(matrix)
    step = calculate_step(plot_data.get_x_coordinates())

    first_central_derivatives = FirstCentral.get_first_central_derivatives(plot_data, step)
    first_backward_derivatives = FirstBackward.get_first_backward_finite_differences(plot_data, step)
    first_forward_derivatives = FirstForward.get_first_forward_derivatives(plot_data, step)

    second_forward_derivatives = SecondBackward.get_second_backward_derivatives(plot_data, step)
    second_backward_derivatives = SecondForward.get_second_forward_derivatives(plot_data, step)

    print("[f'(x), f''(x)]")
    print("first finite difference approximation")
    print("forward, \t x = 1.00", first_central_derivatives)
    print("backward, \t x = 1.16", first_backward_derivatives)
    print("forward, \t x = 0.84", first_forward_derivatives)
    print()
    print("second finite difference approximation")
    print("backward, \t x = 1.16", second_backward_derivatives)
    print("second, \t x = 0.84", second_forward_derivatives)


if __name__ == '__main__':
    print("__________started__________")
    matrixA = [[.84, .431711],
               [.92, .398519],
               [1., .367879],
               [1.08, .339596],
               [1.16, .313486]]  # [[x,y], [x, y],...]
    handle(matrixA)
    print("__________finished__________")
