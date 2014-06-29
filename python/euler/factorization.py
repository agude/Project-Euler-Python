import bisect
import math
import numpy


def factors(number):
    """ Returns a list of the factors of a number.

    Args:
        number (int): The number to factorize.

    Returns:
        list: A sorted list of all the factors of the number.

    Raises:
        TypeError: number is not convertible to a float (for sqrt).
    """
    bound = int(math.floor(math.sqrt(number)))
    factors = []
    # Try all divisors up to the square root of the number, add those
    for i in range(1, bound + 1):
        if not number % i:
            fact1 = i
            fact2 = number / i
            # We use bisect to keep the factor list sorted
            if fact1 == fact2:
                bisect.insort(factors, i)
            else:
                bisect.insort(factors, i)
                bisect.insort(factors, number // i)

    return factors


def number_of_factors(number):
    """ Returns the number of factors of a number.

    This is equivilent to len(factors(number)).

    Args:
        number (int): The number to compute the number of factors for.

    Returns:
        int: The number of factors.

    Raises:
        TypeError: number is not convertible to a float (for sqrt).
    """
    return len(factors(number))
