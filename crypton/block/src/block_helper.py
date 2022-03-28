from typing import Callable, Tuple
import numpy as np
from crypton.block import encrypt, decrypt
from functools import partial


__all__ = [
	"get_cryption_functions"
]


def create_partial_encrypt(a: np.ndarray, b: np.ndarray, space: str) -> Callable:
	return partial(encrypt, a=a, b=b, space=space)


def create_partial_decrypt(a: np.ndarray, b: np.ndarray, space: str) -> Callable:
	return partial(decrypt, a=a, b=b, space=space)


def get_cryption_functions(*args, **kwargs) -> Tuple[Callable, Callable]:
	_encrypt = create_partial_encrypt(*args, **kwargs)
	_decrypt = create_partial_decrypt(*args, **kwargs)

	return _encrypt, _decrypt

