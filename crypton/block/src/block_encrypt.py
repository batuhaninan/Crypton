import numpy as np

from crypton.utils import cryption as cryption_utils
from crypton.utils import space as space_utils
from crypton.utils import math as math_utils


def encrypt(text: str, a: np.ndarray, b: np.ndarray, space: str) -> str:
    result = []
    pairs = cryption_utils.get_pairs_of_int_two_from_text(text, space)

    for pair in pairs:
        a_times_pair = np.dot(a, pair)
        added_matrices = math_utils.add_matrices_and_flatten(a_times_pair, b)
        result_list = space_utils.convert_ints_to_char(added_matrices, space)

        result.append("".join(result_list))

    return "".join(result)
