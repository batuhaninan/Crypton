from string import ascii_lowercase
from typing import Callable, Tuple

from crypton.affine import encrypt, decrypt
from functools import partial


__all__ = [
	"get_cryption_functions"
]


def create_partial_encrypt(a: int = 3, b: int = 5, space: str = ascii_lowercase) -> Callable:
	"""Creates a partial encrypt function with given a, b, and space

	:param a: An integer that corresponds to the A parameter in affine cypher
	:type a: int

	:param b: An integer that corresponds to the B parameter in affine cypher
	:type b: int

	:param space: Target space
	:type space: str

	:return: Partial encrypt function
	:rtype: Function
	"""
	return partial(encrypt, a=a, b=b, space=space)


def create_partial_decrypt(a: int = 3, b: int = 5, space: str = ascii_lowercase) -> Callable:
	"""Creates a partial decrypt function with given a, b, and space

	:param a: An integer that corresponds to the A parameter in affine cypher
	:type a: int

	:param b: An integer that corresponds to the B parameter in affine cypher
	:type b: int

	:param space: Target space
	:type space: str

	:return: Partial decrypt function
	:rtype: Function
	"""
	return partial(decrypt, a=a, b=b, space=space)


def get_cryption_functions(*args, **kwargs) -> Tuple[Callable, Callable]:
	"""Returns encrypt and decrypt functions with the same a, b, and space

	:param args: Arguments
	:param kwargs: Keyword Arguments
	:return: Encrypt and Decrypt functions
	:rtype: (Function, Function)
	"""
	_encrypt = create_partial_encrypt(*args, **kwargs)
	_decrypt = create_partial_decrypt(*args, **kwargs)

	return _encrypt, _decrypt

