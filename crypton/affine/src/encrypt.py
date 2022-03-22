from typing import Callable, Sequence
from crypton.utils.cryption import encrypt_decrypt_helper


def encrypt(plain_text: str, a: int, b: int, space: Sequence) -> str:

    return encrypt_decrypt_helper(plain_text, a, b, get_encrypt_function, space)


def get_encrypt_function(a: int, b: int) -> Callable[[int], int]:
    def inner(x: int) -> int:
        return (a * x) + b

    return inner
