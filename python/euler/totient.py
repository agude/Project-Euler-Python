import fractions
import numpy
try:
    import euler.primes as primes
except ImportError:
    import primes


def eulers_totient(number: int) -> int:
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


def totient_sieve(max_number: int):
    """Returns a (numpy) array of all values of Euler's totient function,
    phi(n), for all values from 0 to the specified number.

    This function uses a sieve approach which allows it to find primes as it
    goes. Once it has the primes it can move through the sieve and build up
    larger valued solutions by taking advantage of the fact that, for a number
    n, with prime factorization:

        n = p1^k1 * p2^k2 * ... * pm^km

    Euler's totient function is:

        phi(n) = (p1^(k1 - 1)) (p1 - 1) * ... * (pm^(km - 1)) (pm - 1)

    Args:
        max_number (int): The largest number to test up to.

    returns:
        array: a numpy array of values with array[i] corresponding to phi(i).
    """
    # We set the type of ints stored in the array based on the size of the
    # input to try to save some space
    numpy_type = numpy.uint32
    if max_number <= 65535:  # 2**16 - 1
        numpy_type = numpy.uint16

    # An array of the totients, with totient_array[n] = phi(n).
    totient_array = numpy.ones(max_number + 1, dtype=numpy_type)
    totient_array[0] = 0

    # Now sieve numbers
    for number in range(2, max_number + 1):
        # As we proceed through the sieve, the only numbers that are not the
        # product of previous primes are prime themselves, and so primes are
        # the only number that will have a value of 1 when we reach them.
        if totient_array[number] == 1:
            prime = number
            for number_to_update in range(prime, max_number + 1, prime):
                # All numbers that contain the prime at least once get
                # multiplied by (prime - 1)
                totient_array[number_to_update] *= prime - 1
                # Numbers that contain additional powers of the prime are
                # multiplied by the prime for each additional power.
                quotient = number_to_update / prime
                while not quotient % prime:
                    totient_array[number_to_update] *= prime
                    quotient /= prime

    return totient_array
