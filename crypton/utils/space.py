def convert_int_to_space_index(i: int, space: str) -> str:
    return space[i]


def convert_space_index_to_int(i: str, space: str) -> int:
    return space.index(i)
