import numpy as np
import operator
	

def get_reverse_modulus(number: int, mod: int = 26) -> int:
	result = 1

	while result % number != 0:
			result += mod

	return result // number


def modulo(number: int, mod: int = 26) -> int:
	while number < 0:
			number += mod

	return number % mod

	
def transpose(matrix):
	return np.transpose(matrix)


def det(matrix):
	return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])


def dot_product_with_multiple_matrices(matrices):
	return np.linalg.multi_dot(matrices)


def create_nested_list_from_flat_list(flat_list):
	return [[i] for i in flat_list]


def inverse_matrix(matrix):
	return [
		[matrix[1][1], -1 * matrix[0][1]],
		[-1 * matrix[1][0], matrix[0][0]]
	]

def get_inverse_matrix(matrix):
	det_of_matrix = det(matrix)

	inversed_matrix = inverse_matrix(matrix)
	
	if det_of_matrix == 1:
		return inversed_matrix

	return np.multiply(inversed_matrix, get_reverse_modulus(det_of_matrix)).tolist()

										 
def round_nested_matrix(matrix):
	return [[round(j) for j in i] for i in matrix]

	
def apply_function_and_flatten_matrices(A, B, function):
	flat_matrix = function(A,B)
	
	return [flat_matrix[0,0], flat_matrix[1,1]]


def add_matrices_and_flatten(A, B):
	return apply_function_and_flatten_matrices(A, B, np.add)


def sub_matrices(A, B):
	return A - B
	