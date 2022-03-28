from string import ascii_lowercase
from typing import Callable, Tuple

from crypton.affine import encrypt, decrypt
from functools import partial


__all__ = [
	"get_cryption_functions"
]


def create_partial_encrypt(a: int = 3, b: int = 5, space: str = ascii_lowercase) -> Callable:
	return partial(encrypt, a=a, b=b, space=space)


def create_partial_decrypt(a: int = 3, b: int = 5, space: str = ascii_lowercase) -> Callable:
	return partial(decrypt, a=a, b=b, space=space)


def get_cryption_functions(*args, **kwargs) -> Tuple[Callable, Callable]:
	_encrypt = create_partial_encrypt(*args, **kwargs)
	_decrypt = create_partial_decrypt(*args, **kwargs)

	return _encrypt, _decrypt

