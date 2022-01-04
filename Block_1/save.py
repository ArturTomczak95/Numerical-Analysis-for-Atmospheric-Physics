import numpy as np

def substract_results(result, row_no, column_no, multipy_coeficient):
    return np.copy(result[row_no]) - np.copy(result[column_no]) * multipy_coeficient


def substract_rows(constant_row, row, multipy_coeficient):
    row = np.copy(row) - np.copy(constant_row) * multipy_coeficient
    return row


def get_upper_triangle_matrix(matrix, results):
    matrix_np = np.array(matrix)
    results_np = np.array(results)
    matrix_idx = len(matrix) - 1
    matrix_idx_count = 0
    for column_no in range(matrix_idx):
        for row_no in range(matrix_idx, matrix_idx_count, -1):
            multipy_coeficient = matrix_np[row_no][column_no] / matrix_np[column_no][column_no]
            matrix_np[row_no] = substract_rows(matrix_np[column_no], matrix_np[row_no], multipy_coeficient)
            results_np[row_no] = substract_results(results_np, row_no, column_no, multipy_coeficient)
        matrix_idx_count += 1

    return matrix_np, results_np


def get_lower_triangle_matrix(matrix, results):
    matrix_np = np.array(matrix)
    results_np = np.array(results)
    matrix_idx = len(matrix) - 1
    matrix_idx_count = 0
    for column_no in range(matrix_idx, matrix_idx_count, -1):
        for row_no in range(column_no):
            multipy_coeficient = matrix_np[row_no][column_no] / matrix_np[column_no][column_no]
            matrix_np[row_no] = substract_rows(matrix_np[column_no], matrix_np[row_no], multipy_coeficient)
            results_np[row_no] = substract_results(results_np, row_no, column_no, multipy_coeficient)
        matrix_idx_count += 1

    return matrix_np, results_np


def calculate_back_substitution_phase(matrix, results):
    matrix_len = len(matrix)
    x_results = [0.0 for i in range(len(matrix))]
    for row_idx in range(matrix_len - 1,-1, -1):
        sum = 0
        for column_idx in range(matrix_len - 1, row_idx, -1):
            sum += matrix[row_idx][column_idx] * x_results[column_idx]
        x_results[row_idx] = (results[row_idx] - sum)/ matrix[row_idx][row_idx]

    return x_results
