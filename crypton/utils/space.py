import numpy as np

from crypton.utils import math
from typing import List


def get_char_at_index(index: int, space: str) -> str:
    """Returns the char at the given index in the given space

    :param index: Index of the char
    :type index: int

    :param space: Target space
    :type space: str

    :return: Character at the index in the space
    :rtype: str
    """
    return space[index]


def get_index_of_char(character: str, space: str) -> int:
    """Returns the index of the character in the given space

    :param character: Character we want to get the index of
    :type character: str

    :param space: str
    :type space: Target space

    :return: Index of the character
    :rtype: int
    """
    return space.index(character)


def convert_ints_to_char(array: List[int], space: str) -> List[str]:
    """Converts list of integer indices to list of characters

    :param array: List of integers
    :type array: List(int)

    :param space: Target space
    :type space: str

    :return: List of characters
    :rtype: List(str)
    """
    space_length = len(space)
    return [
        get_char_at_index(math.modulo(i, space_length), space) for i in array
    ]


def convert_nested_ints_to_char(array: np.ndarray, space: str) -> List[str]:
    """Calls the :func:`crypton.utils.space.convert_ints_to_char` function repeatedly on every element of the list

    :param array: Nested list of integers
    :type array: np.ndarray

    :param space: Target space
    :type space: str

    :return: List of strings
    :rtype: List(str)
    """
    return [
        "".join(
            convert_ints_to_char(i, space)
        )
        for i in array
    ]
