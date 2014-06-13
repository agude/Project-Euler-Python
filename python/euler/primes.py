import itertools
import math
import numpy
try:
    import euler.countable as countable
except ImportError:
    import countable


def prime_sieve(max_number):
    """Returns a (numpy) array of all prime numbers less than max_number.

    This function uses a sieve of Eratosthenes, and hence needs to store at
    least as many numbers in memory as max_number.

    Args:
        max_number (int): The largest number to test up to.

    Returns:
        array: A numpy array of prime numbers.

    Raises:
        TypeError: max_number is not convertible to an integer.
    """
    # An array of bools, we use the index to store if a number is prime or not
    is_prime = numpy.ones(max_number, dtype=numpy.bool)
    is_prime[0] = is_prime[1] = False  # 0,1 not prime
    for i in range(2, int(math.ceil(math.sqrt(max_number)))):
        if is_prime[i]:  # False if already proven to be not prime
            # Starting at i*i : until the end of the array : increment by i
            # We can start at i*i because lower multiples have already been
            # removed
            is_prime[i * i:max_number + 1:i] = False
    # Return the index values of True, that is primes
    return numpy.array(numpy.nonzero(is_prime)[0], dtype=numpy.int64)


def primes():
    """Returns an iterator over all prime numbers.

    Yields:
        int: The next prime number.
    """
    not_primes = {}
    yield 2  # Only even prime, put in by hand
    for i in itertools.islice(itertools.count(0), 3, None, 2):
        # If i is already in not_primes, remove and return it, otherwise return
        # None
        j = not_primes.pop(i, None)
        if j is None:
            yield i
            not_primes[i * i] = i
        else:
            k = i + j
            # If k will be knocked out by a smaller multiple, we ignore it and
            # continue
            while k in not_primes or not k % 2:
                k += j
            not_primes[k] = j


def prime_factors(number):
    """Returns a list of numbers containing all the prime factors of number.

    This function uses a sieve of Eratosthenes, and hence needs to store at
    least as many numbers as sqrt(number).

    Args:
        number (int): The number to find the prime factors of.

    Returns:
        array: A numpy array of prime numbers.

    Raises:
        TypeError: number doesn't support sqrt().
    """
    # We only need to test up to the square root of the number
    bound = math.ceil(math.sqrt(number))
    primes = prime_sieve(bound)

    # We divide through by primes until we reach 1, repeating with each prime
    # until it no longer divides through evenly.
    factors = []
    for prime in primes:
        while number % prime == 0:
            number = number / prime
            factors.append(prime)
            if number <= 1:
                return factors

    return number  # Failed, it is prime


def is_prime(number):
    """Returns True if number is prime, else false.

    This function uses a deterministic, brute-force prime test.

    Args:
        number (int): Test if this number is prime.

    Returns:
        bool: True if number is prime, else False.

    Raises:
        ValueError: If number doesn't support int(number).
    """
    # 0,1, negative numbers, and floats are not prime
    if number < 2 or not countable.is_integer(number):
        return False
    # 2, 3 are prime, others already excluded
    elif number < 4:
        return True
    # Even numbers are not prime
    elif not number % 2:
        return False
    # We have now excluded 4, 6, 8, so under 9 is prime
    elif number < 9:
        return True
    # 3 is prime, numbers divided by three are not
    elif not number % 3:
        return False
    # We now use the fact that primes are 6n+-1
    else:
        r = math.floor(math.sqrt(number))
        f = 5
        while f <= r:
            if not number % f:
                return False
            elif not number % (f + 2):
                return False
            else:
                f += 6
        else:
            return True
