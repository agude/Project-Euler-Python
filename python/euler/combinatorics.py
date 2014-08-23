import math
try:
    import euler.countable as countable
except ImportError:
    import countable


def n_choose_k(n, k):
    """ Return the binomial coefficient for n choose k.

    The binomial coefficient is defined as:

        n choose k = n! / (k!(n-k)!)

    For a number of objects n, which k choices allowed, this function reports
    the number of ways to make the selection if order is disregarded.

    Args:
        n (int): A positive integer indicating the possible number of items to
            select.
        k (int): A positive integer indicating the number of items selected.

    Returns:
        int: The result of n choose k.

    Raises:
        ValueError: if n or k are not non-negative integers.
    """
    # Check that n and k are allowed
    if not countable.is_nonnegative_integer(n):
        raise ValueError("n is a not a non-negative integer")
    if not countable.is_nonnegative_integer(k):
        raise ValueError("k is a not a non-negative integer")
    # Compute and return
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
