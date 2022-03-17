def get_reverse_modulus(number: int, mod: int = 26) -> int:
    result = 1

    while result % number != 0:
        result += mod

    return result // number


def modulo(number: int, mod: int = 26) -> int:
    while number < 0:
        number += mod

    return number % mod
