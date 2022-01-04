import numpy as np


def get_row_norm(row, row_no):
    row_sum = 0
    for value in row[row_no]:
        row_sum += abs(value)
    return row_sum


def get_matrix_norm(matrix):
    row_max_sum = 0
    for row_no in range(0, len(matrix)):
        row_sum = get_row_norm(matrix, row_no)
        if row_sum > row_max_sum:
            row_max_sum = row_sum
    return row_max_sum


def calculate_infinity_norm_condition_number(matrix):
    matrix_norm = get_matrix_norm(matrix)
    inverse_matrix = np.linalg.inv(matrix)
    inverse_matrix_norm = get_matrix_norm(inverse_matrix)
    return matrix_norm * inverse_matrix_norm


def calculate_1_norm_condition_number(matrix):
    matrix_transposed = np.transpose(matrix)
    return calculate_infinity_norm_condition_number(matrix_transposed)


def calculate_condition_number(matrix, norm):
    if norm == "1":
        condition_number = calculate_1_norm_condition_number(matrix)
    elif norm == "inf":
        condition_number = calculate_infinity_norm_condition_number(matrix)
    else:
        print("no valid norm given")
        return

    print("%s matrix CN = %.10f:" % (matrix, condition_number))


def handle():
    norm_input = input("Norm (1/inf)?")
    exercise_5_matrix = [[-3, 5, 7], [2, 6, 4], [0, 2, 8]]
    exercise_1_matrix = [[2, -3, -1], [3, 2, -5], [2, 4, -1]]
    calculate_condition_number(exercise_5_matrix, norm_input)
    calculate_condition_number(exercise_1_matrix, norm_input)


if __name__ == '__main__':
    handle()
