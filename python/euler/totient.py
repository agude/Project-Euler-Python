import fractions
try:
    import euler.primes as primes
except ImportError:
    import primes


def eulers_totient(number):
    """Returns the Euler's totient (also known as the Euler's Phi) of a number.

    For a number n, euler's totient is the number of numbers of value < n which
    are coprime to n. A number m is coprime to n if gcd(n, m) = 1.

    Args:
        number (int): The number to calculate the totient of.

    Returns:
        int: The totient.

    Raises:
        TypeError: if number doesn't support sqrt().
    """
    # We get the unique prime factors of the number
    factors = set(primes.prime_factors(number))
    # We use the formula: Phi(n) = n Product(1-1/p), where p are the prime
    # factors of n
    answer = number
    for factor in factors:
        answer *= (1 - fractions.Fraction(1, factor))
    # The answer must be an integer
    return int(answer)
