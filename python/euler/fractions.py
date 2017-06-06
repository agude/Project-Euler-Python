try:
    import euler.countable as countable
except ImportError:
    import countable


def cycle_length_prime(number):
    """ Return the length of cycle of repeating digits of 1/number,
    where number is prime.

    This function uses the fact that, for certain primes, the length is equal
    to p where ((10 ** p) - 1) % number == 0.

    It will return incorrect results for non-prime numbers!

    Args:
        number (int): The number to use to calculate the length of the cycle of
            repeating digits in 1/number.

    Returns:
        int: The length of the cycle of repeating digits.

    Raises:
        ValueError: number is <= 0, or a non-integer, or is not convertible to
        a float.
    """
    # Test that number is valid
    if not countable.is_positive_integer(number):
        raise ValueError("input is not a positive integer")
    # Otherwise test the number
    d = 1
    while True:
        power = 10 ** d
        if (power - 1) % number == 0:
            return d
        d += 1
        if d == number:
            return 0
