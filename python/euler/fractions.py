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


def continued_fraction_numerator(n, a0, an, memoized={-2: 0, -1: 1}):
    """Return the numerator of the nth convergent of a continued fraction.

    Continued fractions are written in the form:

        [a0; a1, a2, a3, ...] = a0 + 1/(a1 + 1/(a2 + 1/(a3 + ... )))

    Then the nth numerator is:

        h_{n} = a_{n} * h_{n-1} + h_{n-2}

    With h_{-1} = 1 and h_{-2} = 0.

    Args:
        n (int): The nth convergent to calculate.
        a0 (int): The value of the coefficient a0.
        an (int -> int): A function that takes an integer, n, and returns the
            coefficient an.
        memoized (dict: int -> int): A dictionary mapping the n to the nth
            convergent numerator.

    Returns:
        int: The numerator of the nth convergent.

    Raises:
        ValueError: number is < -2, or a non-integer.
    """
    # Negative numbers are not defined, except to define n=0
    if n < -2:
        raise ValueError("n is less than -2")

    if n not in memoized:
        term_1 = continued_fraction_numerator(n-1, a0, an)
        term_2 = continued_fraction_numerator(n-2, a0, an)

        a = an(n) if n else a0
        memoized[n] = a * term_1 + term_2

    return memoized[n]


def continued_fraction_denominator(n, a0, an, memoized={-2: 1, -1: 0}):
    """Return the denominator of the nth convergent of a continued fraction.

    Continued fractions are written in the form:

        [a0; a1, a2, a3, ...] = a0 + 1/(a1 + 1/(a2 + 1/(a3 + ... )))

    Then the nth denominator is:

        k_{n} = a_{n} * k_{n-1} + k_{n-2}

    With h_{-1} = 0 and h_{-2} = 1.

    Args:
        n (int): The nth convergent to calculate.
        a0 (int): The value of the coefficient a0.
        an (int -> int): A function that takes an integer, n, and returns the
            coefficient an.
        memoized (dict: int -> int): A dictionary mapping the n to the nth
            convergent denominator.

    Returns:
        int: The denominator of the nth convergent.

    Raises:
        ValueError: number is < -2, or a non-integer.
    """
    # Negative numbers are not defined, except to define n=0
    if n < -2:
        raise ValueError("n is less than -2")

    if n not in memoized:
        term_1 = continued_fraction_denominator(n-1, a0, an)
        term_2 = continued_fraction_denominator(n-2, a0, an)

        a = an(n) if n else a0
        memoized[n] = a * term_1 + term_2

    return memoized[n]
