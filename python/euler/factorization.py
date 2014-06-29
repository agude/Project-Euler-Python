import bisect
import math


def proper_factors(number):
    """ Returns a list of the proper factors of a number.

    The proper factors of a number are all numbers that divide it evenly,
    except for itself (although 1 is included).

    Args:
        number (int): The number to factorize.

    Returns:
        list: A sorted list of all the proper factors of the number.

    Raises:
        TypeError: number is not convertible to a float (for sqrt).
    """
    bound = int(math.floor(math.sqrt(number)))
    # All numbers are divisible by 1
    if number == 1:
        return []
    factors = [1]
    # Try all divisors up to the square root of the number, add those
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


def factors(number):
    """ Returns a list of the factors of a number.

    The factors of a number are all numbers that divide it evenly, including
    itself.

    Args:
        number (int): The number to factorize.

    Returns:
        list: A sorted list of all the proper factors of the number.

    Raises:
        TypeError: number is not convertible to a float (for sqrt).
    """
    return proper_factors(number) + [number]


def number_of_proper_factors(number):
    """ Returns the number of proper factors of a number.

    The proper factors of a number are all numbers that divide it evenly,
    except for itself (although 1 is included).

    This is equivilent to len(proper_factors(number)).

    Args:
        number (int): The number to compute the number of factors for.

    Returns:
        int: The number of factors.

    Raises:
        TypeError: number is not convertible to a float (for sqrt).
    """
    return len(proper_factors(number))


def number_of_factors(number):
    """ Returns the number of factors of a number.

    The factors of a number are all numbers that divide it evenly, including
    itself.

    This is equivilent to len(factors(number)).

    Args:
        number (int): The number to compute the number of factors for.

    Returns:
        int: The number of factors.

    Raises:
        TypeError: number is not convertible to a float (for sqrt).
    """
    return len(factors(number))
