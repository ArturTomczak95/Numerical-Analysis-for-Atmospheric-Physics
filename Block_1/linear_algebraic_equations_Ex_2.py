import numpy as np
from math import sqrt


def calculate_sum_for_equals(matrix, row_idx, column_idx):
    matrix_len_idx = len(matrix)
    sum = 0
    for k in range(0, matrix_len_idx - 1):
        sum += matrix[row_idx][k] * matrix[column_idx][k]

    return sum


def calculate_sum_for_not_equals(matrix, row_idx, column_idx):
    matrix_len_idx = len(matrix)
    sum = 0
    for k in range(0, matrix_len_idx - 2):
        sum += matrix[row_idx][k] * matrix[column_idx][k]

    return sum


def cholesky(matrix):
    matrix_len = len(matrix)
    lower_triangular_matrix = [[0.0] * matrix_len for i in range(matrix_len)]

    for row_idx in range(matrix_len):
        for column_idx in range(row_idx+1):
            if row_idx == 0 & column_idx == 0:
                lower_triangular_matrix[row_idx][column_idx] = sqrt(matrix[row_idx][column_idx])
            elif row_idx == column_idx:
                lower_triangular_matrix[row_idx][column_idx] = sqrt(matrix[row_idx][column_idx] - calculate_sum_for_equals(lower_triangular_matrix, row_idx, column_idx))
            elif column_idx == 0:
                lower_triangular_matrix[row_idx][column_idx] = matrix[row_idx][column_idx] / lower_triangular_matrix[0][0]
            else:
                lower_triangular_matrix[row_idx][column_idx] = ((matrix[row_idx][column_idx] - calculate_sum_for_not_equals(lower_triangular_matrix, row_idx, column_idx)) / lower_triangular_matrix[column_idx][column_idx])

    return lower_triangular_matrix

def cholesky_decomposition(matrix, results):
    # Ax = b
    # L * U * x = b
    # U^T * U * x = b => U * x = b
    # U^T * y = b
    # y = (U^T)^-1 * b
    # U * x = y
    # x = U^-1 * y
    lower_triangle_matrix = np.array(cholesky(matrix))
    upper_triangle_matrix = np.transpose(np.copy(lower_triangle_matrix))  # L = U^T
    lower_inverse_matrix = np.linalg.inv(lower_triangle_matrix)  # L^-1 = (U^T)^-1
    y_vector = np.matmul(lower_inverse_matrix, np.copy(results))  # y = (U^T)^-1 * b
    upper_inverse_matrix = np.linalg.inv(np.copy(upper_triangle_matrix))  # U^-1
    x_vector = np.matmul(upper_inverse_matrix, np.copy(y_vector))  # x = U^-1 * y
    print("x vector")
    print(x_vector)
    print("check")
    print(np.matmul(np.array(matrix), x_vector))


def handle(matrix, results):
    print("# Cholesky decomposition")
    cholesky_decomposition(matrix, results)


if __name__ == '__main__':
    np.set_printoptions(formatter={'float_kind':"{:.16f}".format})
    matrix_input = [
        [1., 1., 1.],
        [1., 2., 2.],
        [1., 2., 3.]
    ]  # A = A^T
    matrix_results = [1., 1.5, 3.]
    handle(matrix_input, matrix_results)
