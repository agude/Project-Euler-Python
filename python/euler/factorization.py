import bisect
import math
from typing import List
try:
    import euler.countable as countable
except ImportError:
    import countable


def proper_factors(number: int) -> List[int]:
    """ Returns a list of the proper factors of a number.

    The proper factors of a number are all numbers that divide it evenly,
    except for itself (although 1 is included).

    Args:
        number (int): The number to factorize.

    Returns:
        list: A sorted list of all the proper factors of the number.
    elif number <= 0:

    Raises:
        TypeError: number is not convertible to a float (for sqrt), of if
            number is not a non-negative integer.
    """
    # Check that our input is legal
    if not countable.is_positive_integer(number):
        raise TypeError("can not factorize non-positive integers")
    # If the number is 1, then it has no proper divisors
    elif number == 1:
        return []
    # Otherwise all numbers are divisible by 1
    factors = [1]
    # Try all divisors up to the square root of the number, add those
    bound = int(math.floor(math.sqrt(number)))
    for i in range(2, bound + 1):
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


def factors(number: int) -> List[int]:
    """ Returns a list of the factors of a number.

    The factors of a number are all numbers that divide it evenly, including
    itself.

    Args:
        number (int): The number to factorize.

    Returns:
        list: A sorted list of all the proper factors of the number.

    Raises:
        TypeError: number is not convertible to a float (for sqrt), of if
            number is not a non-negative integer.
    """
    return proper_factors(number) + [number]


def number_of_proper_factors(number: int) -> int:
    """ Returns the number of proper factors of a number.

    The proper factors of a number are all numbers that divide it evenly,
    except for itself (although 1 is included).

    This is equivilent to len(proper_factors(number)).

    Args:
        number (int): The number to compute the number of factors for.

    Returns:
        int: The number of factors.

    Raises:
        TypeError: number is not convertible to a float (for sqrt), of if
            number is not a non-negative integer.
    """
    return len(proper_factors(number))


def number_of_factors(number: int) -> int:
    """ Returns the number of factors of a number.

    The factors of a number are all numbers that divide it evenly, including
    itself.

    This is equivilent to len(factors(number)).

    Args:
        number (int): The number to compute the number of factors for.

    Returns:
        int: The number of factors.

    Raises:
        TypeError: number is not convertible to a float (for sqrt), of if
            number is not a non-negative integer.
    """
    return len(factors(number))
