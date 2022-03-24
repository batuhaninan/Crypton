from typing import List, Callable

import numpy as np


def get_reverse_modulus(number: int, mod: int = 26) -> int:
    result = 1

    while result % number != 0:
        result += mod

    return result // number


def modulo(number: int, mod: int = 26) -> int:
    while number < 0:
        number += mod

    return number % mod


def det(matrix: np.ndarray) -> int:
    return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])


def dot_product_with_multiple_matrices(matrices: List[np.ndarray]) -> np.ndarray:
    return np.linalg.multi_dot(matrices)


def create_nested_list_from_flat_list(flat_list: List[int]) -> List[List[int]]:
    return [[i] for i in flat_list]


def inverse_matrix(matrix: np.ndarray) -> List:
    return [[matrix[1][1], -1 * matrix[0][1]], [-1 * matrix[1][0], matrix[0][0]]]


def get_inverse_matrix(matrix: np.ndarray) -> List:
    det_of_matrix = det(matrix)

    inversed_matrix = inverse_matrix(matrix)

    if det_of_matrix == 1:
        return inversed_matrix

    multiplied_matrices = np.multiply(
        inversed_matrix, get_reverse_modulus(det_of_matrix)
    )

    return multiplied_matrices.tolist()


def apply_function_and_flatten_matrices(
    a: np.ndarray, b: np.ndarray, function: Callable
) -> List[int]:
    flat_matrix = function(a, b)

    return [flat_matrix[0, 0], flat_matrix[1, 1]]


def add_matrices_and_flatten(a: np.ndarray, b: np.ndarray) -> List[int]:
    return apply_function_and_flatten_matrices(a, b, np.add)


def sub_matrices(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a - b
