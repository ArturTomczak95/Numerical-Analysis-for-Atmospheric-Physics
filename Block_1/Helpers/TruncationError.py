from Block_1.Helpers.StepsCoodrindate import FiveStepsCoordinate, FiveStepsCoordinateForward, FiveStepsCoordinateBackward


class TruncationDerivativesCentered:
    @staticmethod
    def calculate_truncation_third_derivative(y: FiveStepsCoordinate, step):
        nominator = y.x_plus_2h - 2 * y.x_plus_h + 2 * y.x_minus_h - y.x_minus_2h
        denominator = 2 * step ** 3

        return nominator / denominator

    @staticmethod
    def calculate_truncation_forth_derivative(y: FiveStepsCoordinate, step):
        # f(x+2h) - 4f(x + h) + 6f(x) - 4f(x-h) + f(x-2h)
        nominator = y.x_plus_2h - 4 * y.x_plus_h + 6 * y.x - 4 * y.x_minus_h + y.x_minus_2h
        denominator = step ** 4  # (h^4)

        return nominator / denominator


class TruncationDerivativesForward:
    @staticmethod
    def calculate_truncation_second_derivative(y: FiveStepsCoordinateForward, step):
        nominator = y.x - 2 * y.x_plus_h + y.x_plus_2h
        denominator = step ** 2

        return nominator / denominator

    @staticmethod
    def calculate_truncation_third_derivative(y: FiveStepsCoordinateForward, step):
        # -f(x) + 3f(x+h) -3f(x+2h) + f(x + 3h)
        nominator = - y.x + 3 * y.x_plus_h - 3 * y.x_plus_2h + y.x_plus_3h
        denominator = step ** 3 # (h^3)

        return nominator / denominator

    @staticmethod
    def calculate_truncation_forth_derivative(y: FiveStepsCoordinateForward, step):
        # f(x) - 4f(x+h) + 6f(x+2h) - 4f(x+3h) + f(x+4h)
        nominator = y.x - 4 * y.x_plus_h + 6 * y.x_plus_2h - 4 * y.x_plus_3h + y.x_plus_4h
        denominator = step ** 4  # (h^4)

        return nominator / denominator


class TruncationDerivativesBackward:
    @staticmethod
    def calculate_truncation_second_derivative(y: FiveStepsCoordinateBackward, step):
        nominator = y.x - 2 * y.x_minus_h + y.x_minus_2h
        denominator = step ** 2

        return nominator / denominator

    @staticmethod
    def calculate_truncation_third_derivative(y: FiveStepsCoordinateBackward, step):
        # f(x) - 3f(x-h) + 3f(x-2h) - f(x-3h)
        nominator = - y.x - 3 * y.x_minus_h + 3 * y.x_minus_2h - y.x_minus_3h
        denominator = step ** 3 # (h^3)

        return nominator / denominator

    @staticmethod
    def calculate_truncation_forth_derivative(y: FiveStepsCoordinateBackward, step):
        # f(x) - 4f(x-h) + 6f(x-2h) - 4f(x-3h) + f(x-4h)
        nominator = y.x - 4 * y.x_minus_h + 6 * y.x_minus_2h - 4 * y.x_minus_3h + y.x_minus_4h
        denominator = step ** 4  # (h^4)

        return nominator / denominator
