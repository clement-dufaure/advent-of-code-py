import math


def ppmc(a: int, b: int) -> int:
    return (a * b) // math.gcd(a, b)


def ppmc_de_liste(nombres: list[int]) -> int:
    if len(nombres) == 2:
        return ppmc(nombres[0], nombres[1])
    else:
        return ppmc(nombres[0], ppmc_de_liste(nombres[1:]))
