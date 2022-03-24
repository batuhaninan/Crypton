from typing import Callable
from crypton.utils.cryption import encrypt_decrypt_helper
from crypton.utils.math import get_reverse_modulus


def decrypt(plain_text: str, a: int, b: int, space: str) -> str:

    return encrypt_decrypt_helper(plain_text, a, b, get_decrypt_function, space)


def get_decrypt_function(a: int, b: int) -> Callable[[int], int]:
    def inner(x: int) -> int:
        return get_reverse_modulus(a) * (x - b)

    return inner
