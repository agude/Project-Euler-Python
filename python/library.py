from numpy import array, bool, nonzero, ones, int64
from math import ceil, sqrt, floor, log
from itertools import count, islice

##########
# Primes #
##########


def PrimeSieve(num):
    """ Return an array of primes below num.

    Keyword arguments:
        num  -- find primes below this number
    """
    # An array of bools to test using their index
    is_prime = ones(num, dtype=bool)
    is_prime[0] = is_prime[1] = False  # 0,1 not prime
    for i in range(2, int(ceil(sqrt(num)))):
        if is_prime[i]:  # False if already proven to be not prime
            # Starting at i*i : until the end of the array : increment by i
            # We can start at i*i because lower multiples have already been removed
            is_prime[i * i:num + 1:i] = False
    # Return the index values of True, that is primes
    return array(nonzero(is_prime)[0], dtype=int64)


def Primes():
    """ Return an iterator over prime numbers. """
    not_primes = {}
    yield 2  # Only even prime, put in by hand
    for i in islice(count(0), 3, None, 2):
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


def PrimeFactors(number):
    """ Return an array of prime factors.  """
    # We only need to test up to the square root of the number
    BOUND = ceil(sqrt(number))
    PRIMES = PrimeSieve(BOUND)

    # We divide through by primes until we reach 1, repeating with each prime
    # until it no longer divides through evenly.
    factors = []
    for prime in PRIMES:
        while number % prime == 0:
            number = number / prime
            factors.append(prime)
            if number <= 1:
                return factors

    return number  # Failed, it is prime


def PrimeTest(number, PRIMES=None):
    """ Return True if number is prime, False otherwise.

    If provided a list of primes, we use that to check (this is faster is many
    checks are needed), otherwise we test by checking all numbers up to the
    square root.

    Keyword arguments:
        number  -- test number for primeness
        PRIMRES -- an object that supports the 'in' operator, if None we
        instead test the number by brute force
    """
    if PRIMES is None:
        # 0,1, negative numbers, and floats are not prime
        if number < 2 or int(number) != float(number):
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
            r = floor(sqrt(number))
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
    else:
        return number in PRIMES

#######################
# Palindromic Numbers #
#######################


def Palindromic(number):
    """ Returns True if num is palindromic, False otherwise. A palindromic
    number reads the same backwards as forwards.

    Keyword arguments:
    number -- test if number is palindromic
    """
    number = str(number)
    return number == number[::-1]  # [::-1] reverses a list
