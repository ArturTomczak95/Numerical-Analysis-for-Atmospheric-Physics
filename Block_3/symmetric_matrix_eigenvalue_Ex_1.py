import numpy as np

from core3.jacobi import jacobi


def calculate_jacobi(A_matrix):
    np_arr = np.array(A_matrix)
    [eigenvalues, eigenvectors] = jacobi(np_arr)
    print("eigenvalues: \n", eigenvalues)
    print()
    print("eigenvectors: \n", eigenvectors)
    print()

    return eigenvalues, eigenvectors


def compare_results(A_matrix, eigenvalues, eigenvectors):
    matrix_size = len(A_matrix)
    np_A_matrix = np.array(A_matrix)
    eigenvectors = np.array(eigenvectors)

    # result_matrix = np.zeros(shape=(matrix_size, matrix_size))
    print("check if: Av = λv")
    for i in range(0, matrix_size):
        # Av = λv
        eigenvalue = eigenvalues[i]
        eigenvector = eigenvectors[:, i]
        left_side = np.matmul(np_A_matrix, eigenvector)
        right_side = eigenvalue * eigenvector
        print("%s = %s" % (left_side, right_side))
    print()


def calculate_determinants(A_matrix, eigenvalues):
    # det(A - λI) = 0
    matrix_size = len(A_matrix)
    identity_matrix = np.identity(matrix_size)
    lambda_times_identity = np.matmul(np.array(eigenvalues), np.array(identity_matrix))
    matrix_to_calculate = np.subtract(A_matrix, lambda_times_identity)
    determinant = np.linalg.det(matrix_to_calculate)
    print("check if: det(A - λI) = 0")
    print("det(A - λI) =", determinant)

    fulfill_sentence = "Eigenvalue problem equation is %s fulfilled"
    fulfilled_sentence = ""
    if determinant != 0:
        fulfilled_sentence = " NOT"

    print(fulfill_sentence % fulfilled_sentence)


def check_accuracy(A_matrix, eigenvalues, eigenvectors):
    compare_results(A_matrix, eigenvalues, eigenvectors)
    calculate_determinants(A_matrix, eigenvalues)


def handle(A_matrix):
    [eigenvalues, eigenvectors] = calculate_jacobi(A_matrix)
    check_accuracy(A_matrix, eigenvalues, eigenvectors)


if __name__ == '__main__':
    print("__________started__________")
    np.set_printoptions(precision=10)
    A = [[4., -2., 1., -1.],
         [-2., 4., -2., 1.],
         [1., -2., 4., -2.],
         [-1., 1., -2., 4.]]
    handle(A)
    print("__________finished__________")
