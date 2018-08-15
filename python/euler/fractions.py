from typing import Callable, Dict
try:
    import euler.countable as countable
except ImportError:
    import countable


def cycle_length_prime(number: int) -> int:
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
    d:int = 1
    while True:
        power: int = 10 ** d
        if (power - 1) % number == 0:
            return d
        d += 1
        if d == number:
            return 0


class ContinuedFraction:
    """A class to compute the convergents of a continued fraction.

    Continued fractions are written in the form:

        [a_{0}; a_{1}, a_{2}, ...] = a_{0} + 1/(a_{1} + 1/(a_{2} + ... ))
    """

    def __init__(self, a0: int, an: Callable[[int], int]) -> None:
        """Set up the continued fraction.

        Args:
            a0 (int): The value of the coefficient a0.
            an (int -> int): A function that takes an integer, n, and returns the
                coefficient an.
        """
        # The coefficients of the fraction
        self.a0: int = a0
        self.an: Callable[[int], int] = an

        # The numerator and denominator terms
        self.denominator_terms: Dict[int, int] = {-2: 1, -1: 0}
        self.numerator_terms: Dict[int, int] = {-2: 0, -1: 1}

    def nth_convergent_numerator(self, n: int) -> int:
        """Return the numerator of the nth convergent of a continued fraction.

        Args:
            n (int): The nth convergent to calculate.
            terms (dict: int -> int): A dictionary mapping the n to the nth
                convergent for numerators.

        Returns:
            int: The numerator of the nth convergent.

        Raises:
            ValueError: number is < -2, or a non-integer.
        """
        return self.__nth_convergent_helper(n, self.numerator_terms)

    def nth_convergent_denominator(self, n: int) -> int:
        """Return the denominator of the nth convergent of a continued fraction.

        Args:
            n (int): The nth convergent to calculate.
            terms (dict: int -> int): A dictionary mapping the n to the nth
                convergent for denominators.

        Returns:
            int: The denominator of the nth convergent.

        Raises:
            ValueError: number is < -2, or a non-integer.
        """
        return self.__nth_convergent_helper(n, self.denominator_terms)

    def __nth_convergent_helper(self, n: int, terms: Dict[int, int]) -> int:
        """Helps to computer either the denominator or numerator of the nth
        convergent of a continued fraction.

        Continued fractions are written in the form:

            [a_{0}; a_{1}, a_{2}, ...] = a_{0} + 1/(a_{1} + 1/(a_{2} + ... ))

        Then the nth numerator/denominator is:

            k_{n} = a_{n} * k_{n-1} + k_{n-2}


        For the denominator, we start with: k_{-1} = 0 and k_{-2} = 1.

        For the numerator, we start with:   k_{-1} = 1 and k_{-2} = 0.

        Args:
            n (int): The nth convergent to calculate.
            terms (dict: int -> int): A dictionary mapping the n to the nth
                convergent for either denominators or numerators.

        Returns:
            int: The denominator or numerator of the nth convergent.

        Raises:
            ValueError: number is < -2, or a non-integer.
        """
        # Negative numbers are not defined, except to define n=0
        if n < -2:
            raise ValueError("n is less than -2")

        if n not in terms:
            term_1: int = self.__nth_convergent_helper(n-1, terms)
            term_2: int = self.__nth_convergent_helper(n-2, terms)

            a: int = self.an(n) if n else self.a0
            terms[n] = a * term_1 + term_2

        return terms[n]
