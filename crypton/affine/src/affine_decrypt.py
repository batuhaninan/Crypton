from typing import Callable
from crypton.utils.cryption import encrypt_decrypt_helper
from crypton.utils.math import get_reverse_modulus

__all__ = [
	"decrypt"
]


def decrypt(plain_text: str, a: int, b: int, space: str) -> str:
	"""Decrypts the given text with given a, b and space

	:param plain_text: Text you want to decrypt
	:type plain_text: str

	:param a: An integer that corresponds to the A parameter in affine cypher
	:type a: int

	:param b: An integer that corresponds to the B parameter in affine cypher
	:type b: int

	:param space: Target space
	:type space: str

	:return: Decrypted text in string form
	:rtype: str
	"""
	return encrypt_decrypt_helper(plain_text, a, b, get_decrypt_function, space)


def get_decrypt_function(a: int, b: int) -> Callable[[int], int]:
	"""Returns a function that does the decrytion process

	:param a: An integer that corresponds to the A parameter in affine cypher
	:type a: int

	:param b: An integer that corresponds to the B parameter in affine cypher
	:type b: int

	:return: Decryption function
	:rtype: Function
	"""
	def inner(x: int) -> int:
		return get_reverse_modulus(a) * (x - b)

	return inner
