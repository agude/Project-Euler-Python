#####################

from numpy import array, bool, nonzero, ones, int64
from math import ceil, sqrt

def get_primes(num):
    """ Return an array of primes below num.

    Keyword arguments:
        num  -- find primes below this number

    """
    isPrime = ones(num,dtype=bool) # An array of bools to test using their index
    isPrime[0] = isPrime[1] = False # 0,1 not prime
    for i in xrange(2,int(ceil(sqrt(num)))):
        if isPrime[i]: # False if already proven not prime
            # Starting at i*i : until the end of the array : increment by i
            # You can start at i*i because lower multiples have already been removed
            isPrime[i*i:num+1:i] = False

    return array(nonzero(isPrime)[0],dtype=int64) # Return the index values of True, that is primes

#####################

from itertools import count,islice

def prime_iter():
    """ Return an iterator over prime numbers. """
    not_primes = {}
    yield 2 # Only even prime, put in by hand
    for i in islice(count(0),3,None,2):
        j = not_primes.pop(i, None) # If i is already in not_primes, remove and return it, otherwise return None
        if j is None:
            yield i
            not_primes[i*i] = i
        else:
            k = i+j
            while k in not_primes or not k%2: #If k will be knocked out by a smaller multiple, we ignore it and continue
                k += j
            not_primes[k] = j

#####################

from math import sqrt, floor

def isPrime(num):
    """ Return True if number is prime, False otherwise.

    Keyword arguments:
        num  -- test num for primeness

    """
    if num < 2 or int(num) != float(num): # 0,1, negative numbers, and floats are not prime
        return False
    elif num < 4:
        return True # 2,3 are prime, others already excluded
    elif not num%2:
        return False
    elif num < 9: # We have now excluded 4,6,8
        return True
    elif not num%3:
        return False
    else: # we now use the fact that primes are 6n+-1
        r = floor(sqrt(num))
        f = 5
        while f <= r:
            if not num%f:
                return False
            elif not num%(f+2):
                return False
            else:
                f += 6
        else:
            return True

#####################

def is_palindromic(num):
    """ Returns True if num is palindromic, False otherwise.

    Keyword arguments:
    num  -- test if num is palindromic

    """
    num = str(num)

    for i in xrange(len(num) / 2):
        if num[i] != num[-(i+1)]:
            return False

    return True
