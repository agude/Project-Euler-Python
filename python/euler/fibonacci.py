import math
from decimal import Decimal


def fibonacci(n, memoized={0: 0, 1: 1}):
    """Returns the nth Fibonacci number.

    Recursively finds the Fibonacci numbers while memoizing all of the previous
    numbers to speed up computation.

    Args:
        n (int): The order of the Fibonacci number to calculate.
        memoized (dictionary, optional): A dictionary mapping the n to the
            corresponding Fibonacci number. This parameter is defined with the
            function so that if none is passed, all calls to the function use
            the same version of the dictionary and so avoids doing redundant
            work.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: n is not convertible to an integer.
    """
    n_int = int(n)
    if n_int not in memoized:
        memoized[n_int] = (fibonacci(n_int - 1) + fibonacci(n_int - 2))
    return memoized[n_int]


def fibonaccis(n):
    """Returns a list of the Fibonacci numbers from F0 to Fn.

    Generates the list via calls to fibonacci, and so fills the memoization
    dictionary, making further calls to either function faster (but, of course,
    trading memory usage for speed).

    Args:
        n (int): The order of the last Fibonacci number to include in the
            returned list.

    Returns:
        list: A list of Fibonacci numbers of length n + 1.

    Raises:
        ValueError: n is not convertible to an integer.
    """
    return [fibonacci(i) for i in range(n + 1)]


def fibonacci_generator(n=None):
    """Generates a generator over all Fibonacci numbers.

    This makes no use of fibonacci, and so no memoization is done. This is the
    most memory efficient way of generating Fibonacci numbers.

    Args:
        n (int, optional): The order of the last Fibonacci number to yield; if
            not provided, runs forever.

    Yields:
        int: The next Fibonacci number, starting at F0 = 0.

    Raises: ValueError if n is < 0.
    """
    # F(-1) is undefined, so we raise an error
    if n is not None and n < 0:
        raise ValueError("n is less than 0")

    elements = [0, 1]
    # If n is none, the loop will never terminate (as we intend); otherwise it
    # will stop when count is n. We start count at -1 so that we return up to
    # F(n), not F(n-1)
    count = -1 
    while n is None or count < n:
        count += 1
        new_number = elements[0] + elements[1]
        elements.append(new_number)
        yield elements.pop(0)
