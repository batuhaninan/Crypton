from typing import Callable
from crypton.utils.cryption import encrypt_decrypt_helper

__all__ = [
	"encrypt"
]


def encrypt(plain_text: str, a: int, b: int, space: str) -> str:
	"""Encrypts the given text with given a, b and space

	:param plain_text: Text you want to encrypt
	:type plain_text: str

	:param a: An integer that corresponds to the A parameter in affine cypher
	:type a: int

	:param b: An integer that corresponds to the B parameter in affine cypher
	:type b: int

	:param space: Target space
	:type space: str

	:return: Encrypted text in string form
	:rtype: str
	"""
	return encrypt_decrypt_helper(plain_text, a, b, get_encrypt_function, space)


def get_encrypt_function(a: int, b: int) -> Callable[[int], int]:
	"""Returns a function that does the encrytion process

	:param a: An integer that corresponds to the A parameter in affine cypher
	:type a: int

	:param b: An integer that corresponds to the B parameter in affine cypher
	:type b: int

	:return: Encryption function
	:rtype: Function
	"""
	def inner(x: int) -> int:
		return (a * x) + b

	return inner
