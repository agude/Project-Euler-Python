import collections
import itertools
import math
import numpy
try:
    import euler.countable as countable
except ImportError:
    import countable
try:
    import euler.converter as converter
except ImportError:
    import converter


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


def circular_primes(number, prime_list=None):
    """Returns a list of all the circular primes associated with number if
    there are any, otherwise returns [].

    This function uses is_prime unless prime_list is provided, in which case it
    assumes that all possible primes it might need are in that list.

    Args:
        number (int): Number to check if it is part of a circular prime ring.
        prime_list (list, optional): If None, this function uses the (slow)
            is_prime function to test primality, otherwise it uses "test_number
            in prime_list", which is hopefully very fast (something like a set
            that does very fast 'in' checking is recommended).

    Returns:
        set: A set of the primes if number is part of a circular prime ring,
            otherwise returns [].

    Raises:
        TypeError: If prime_list is not None and does not support "in".
    """
    circular_primes = set([])
    # The input number must be prime
    if prime_list is None:
        if not is_prime(number):
            return []
    elif number not in prime_list:
        return []
    circular_primes.add(number)
    # We now rotate the prime once for every digit to check all possible
    # rotations (less one, since we have already checked the current number
    prime_digits = collections.deque(converter.int_to_tuple(number))
    for _ in range(len(prime_digits) - 1):
        prime_digits.rotate()
        new_number = converter.iterable_to_int(prime_digits)
        if prime_list is None:
            if not is_prime(new_number):
                return []
        elif new_number not in prime_list:
            return []
        circular_primes.add(new_number)
    return circular_primes


def is_truncatable_prime(number, right_truncate=False):
    """Returns true if number is a truncatable prime.

    A prime is left-truncatable if it is prime and if, when digits are removed
    from the left, all subsequent numbers are all prime. A right-truncatable
    prime is the same, but with digits removed from the right.

    By default, numbers are truncated from the left, and so the function checks
    if a number if a left-truncatable prime.

    Args:
        number (int): the number to test
        right_truncate (bool, False): truncate from the right instead of the
            left

    Returns:
        bool: true if the number is a truncatable prime, False otherwise

    Raises:
        ValueError: If number is not integral
        AttributeError: If number doesn't support number.is_integer()
    """
    if not is_prime(number):
        return False
    # Truncate the number until we have removed all the digits. If it is prime
    # at all stages return True, otherwise return False.
    while True:
        # Truncate the primes from the left or right as desired
        if right_truncate:
            number = converter.right_truncate(number)
        else:
            number = converter.left_truncate(number)
        # None is returned when there are no more digits to remove
        if number is None:
            break
        if not is_prime(number):
            return False

    # Passed all of the tests
    return True


def is_right_truncatable_prime(number):
    """Returns true if number is a right-truncatable prime.

    A prime is right-truncatable if it is prime and if, when digits are removed
    from the right, all subsequent numbers are all prime.

    This is a simple wrapper around is_truncatable_prime. The source is:
        is_truncatable_prime(number, right_truncate=True):

    Args:
        number (int): the number to test

    Returns:
        bool: true if the number is a right-truncatable prime, False otherwise

    Raises:
        ValueError: If number is not integral
        AttributeError: If number doesn't support number.is_integer()
    """
    return is_truncatable_prime(number, right_truncate=True)


def is_left_truncatable_prime(number):
    """Returns true if number is a left-truncatable prime.

    A prime is left-truncatable if it is prime and if, when digits are removed
    from the left, all subsequent numbers are all prime.

    This is a simple wrapper around is_truncatable_prime. The source is:
        is_truncatable_prime(number, left_truncate=False):

    Args:
        number (int): the number to test

    Returns:
        bool: true if the number is a left-truncatable prime, False otherwise

    Raises:
        ValueError: If number is not integral
        AttributeError: If number doesn't support number.is_integer()
    """
    return is_truncatable_prime(number, right_truncate=False)


def is_two_sided_prime(number):
    """Returns true if number is a two-sided prime, that is if it is both left
    and right-truncatable.

    A prime is left-truncatable if it is prime and if, when digits are removed
    from the left, all subsequent numbers are all prime. A right-truncatable
    prime is the same, but with digits removed from the right.

    This is a simple wrapper around is_left_truncatable_prime and
    is_right_truncatable_prime.

    Args:
        number (int): the number to test

    Returns:
        bool: true if the number is a two-sided prime, False otherwise

    Raises:
        ValueError: If number is not integral
        AttributeError: If number doesn't support number.is_integer()
    """
    return (is_right_truncatable_prime(number)
            and is_left_truncatable_prime(number))
