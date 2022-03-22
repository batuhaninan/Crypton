import numpy as np

from crypton.utils import math
from typing import List, Sequence


def convert_int_to_space_index(index: int, space: Sequence) -> str:
    return space[index]


def convert_space_index_to_int(character: str, space: Sequence) -> int:
    return space.index(character)


def convert_ints_to_char(array: List, space: Sequence) -> List:
    space_length = len(space)
    return [
        convert_int_to_space_index(math.modulo(i, space_length), space) for i in array
    ]


def convert_nested_ints_to_char(array: np.ndarray, space: Sequence) -> List:
    space_length = len(space)
    return [
        "".join(
            [convert_int_to_space_index(math.modulo(j, space_length), space) for j in i]
        )
        for i in array
    ]
