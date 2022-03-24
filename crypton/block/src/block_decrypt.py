import numpy as np

from crypton.utils import cryption as cryption_utils
from crypton.utils import space as space_utils
from crypton.utils import math as math_utils


def decrypt(text: str, a: np.ndarray, b: np.ndarray, space: str) -> str:
    result = []

    t = math_utils.get_inverse_matrix(a)
    pairs = cryption_utils.get_pairs_of_int_two_from_text(text, space)

    for pair in pairs:
        c = math_utils.create_nested_list_from_flat_list(pair)
        subtracted_matrix = math_utils.sub_matrices(c, b)
        dot_product = math_utils.dot_product_with_multiple_matrices(
            [t, np.array(subtracted_matrix)]
        )
        result_list = space_utils.convert_nested_ints_to_char(dot_product, space)

        result.append("".join(result_list))

    return "".join(result)
