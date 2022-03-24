from crypton.utils.math import modulo
from functools import partial
from crypton.utils.space import convert_space_index_to_int
from typing import Callable, List


def apply_func_to_char(c: int, f: Callable, mod: int = 26) -> int:
    result = f(c)

    return modulo(result, mod)


def encrypt_decrypt_helper(
    plain_text: str, a: int, b: int, f: Callable, space: str
) -> str:

    encrypt_func = partial(apply_func_to_char, f=f(a, b), mod=len(space))

    text_as_list_of_ints = list(
        map(partial(convert_space_index_to_int, space=space), plain_text)
    )

    result_as_list_of_ints = list(map(encrypt_func, text_as_list_of_ints))

    result_as_list_of_strs = list(map(lambda x: space[x], result_as_list_of_ints))

    return "".join(result_as_list_of_strs)


def get_pairs_of_int_two_from_text(text: str, space: str) -> List[List[int]]:
    return [
        [space.index(text[i]), space.index(text[i + 1])]
        for i in range(0, len(text) - 1, 2)
    ]
