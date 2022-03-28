import numpy as np

from crypton.utils import cryption as cryption_utils
from crypton.utils import space as space_utils
from crypton.utils import math as math_utils


__all__ = [
	"encrypt"
]


def encrypt(plain_text: str, a: np.ndarray, b: np.ndarray, space: str) -> str:
	"""Encrypts the given text with given a, b and space

	:param plain_text: Text you want to encrypt
	:type plain_text: str

	:param a: An integer that corresponds to the A parameter in block cypher
	:type a: np.ndarray

	:param b: An integer that corresponds to the B parameter in block cypher
	:type b: np.ndarray

	:param space: Target space
	:type space: str

	:return: Encrypted text in string form
	:rtype: str
	"""
	result = []
	pairs = cryption_utils.get_pairs_of_int_two_from_text(plain_text, space)

	for pair in pairs:
		a_times_pair = np.dot(a, pair)
		added_matrices = math_utils.add_matrices_and_flatten(a_times_pair, b)
		result_list = space_utils.convert_ints_to_char(added_matrices, space)

		result.append("".join(result_list))

	return "".join(result)
