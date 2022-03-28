from crypton.utils.math import modulo
from functools import partial
from crypton.utils.space import get_index_of_char
from typing import Callable, List


def apply_func_to_char(c: int, f: Callable, mod: int = 26) -> int:
    """Applies function to given char in int form, takes the modulus with given mod and returns the result

    :param c: Char in int form
    :type c: int

    :param f: Function to apply
    :type f: Function

    :param mod: Modulus space
    :type mod: int

    :return: Function applied character
    :rtype: int
    """
    result = f(c)

    return modulo(result, mod)


def encrypt_decrypt_helper(
    plain_text: str, a: int, b: int, f: Callable, space: str
) -> str:
    """Because of the similarity between encrypt & decrypt operations, this function applies the given function f and
    does affine encryption

    :param plain_text: Text we want to encrypt/decrypt
    :type plain_text: str


    :param a: An integer that corresponds to the A parameter in affine cypher
    :type a: int


    :param b: An integer that corresponds to the B parameter in affine cypher
    :type b: int


    :param f: Function to apply, this parameter decides if we're going to encrypt or decrypt
    :type f: Function


    :param space: Target space
    :type space: str

    :return: Encrypted/decrypted text
    :rtype: str
    """
    encrypt_func = partial(apply_func_to_char, f=f(a, b), mod=len(space))

    text_as_list_of_ints = list(
        map(partial(get_index_of_char, space=space), plain_text)
    )

    result_as_list_of_ints = list(map(encrypt_func, text_as_list_of_ints))

    result_as_list_of_strs = list(map(lambda x: space[x], result_as_list_of_ints))

    return "".join(result_as_list_of_strs)


def get_pairs_of_int_two_from_text(text: str, space: str) -> List[List[int]]:
    """Creates pairs of two from the given text

    :param text: Text we want to create pairs from
    :type text: str

    :param space: Target space
    :type space: str

    :return: Pairs of two in list form
    :rtype: List(List(int))
    """
    return [
        [space.index(text[i]), space.index(text[i + 1])]
        for i in range(0, len(text) - 1, 2)
    ]
