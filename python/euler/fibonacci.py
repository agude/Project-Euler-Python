from typing import Generator
import math
import decimal
from typing import Dict, List


def fibonacci(n: int, memoized: Dict[int, int]={0: 0, 1: 1}) -> int:
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
        ValueError: n is not convertible to an integer or n < 0.
    """
    # F(-1) is undefined, so we raise an error
    if n < 0:
        raise ValueError("n is less than 0")

    n_int = int(n)
    if n_int not in memoized:
        memoized[n_int] = (fibonacci(n_int - 1) + fibonacci(n_int - 2))
    return memoized[n_int]


def fibonaccis(n: int) -> List[int]:
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
        ValueError: n is not convertible to an integer or n < 0.
    """
    # F(-1) is undefined, so we raise an error
    if n < 0:
        raise ValueError("n is less than 0")

    return [fibonacci(i) for i in range(n + 1)]


def fibonacci_generator(n: int=None, mod: int=None) -> Generator[int, None, None]:
    """Generates a generator over all Fibonacci numbers.

    This makes no use of fibonacci, and so no memoization is done. This is the
    most memory efficient way of generating Fibonacci numbers.

    Args:
        n (int, optional): The order of the last Fibonacci number to yield; if
            not provided, runs forever.
        mod (int, optional): Mod the numbers with mod. If None, then the full
            number is returned.

    Yields:
        int: The next Fibonacci number, starting at F0 = 0.

    Raises: ValueError if n is < 0, or if mod is < 1.
    """
    # F(-1) is undefined, so we raise an error
    if n is not None and n < 0:
        raise ValueError("n is less than 0")
    if mod is not None and mod < 1:
        raise ValueError("mod is less than 1")

    elements = [0, 1]
    # If n is none, the loop will never terminate (as we intend); otherwise it
    # will stop when count is n. We start count at -1 so that we return up to
    # F(n), not F(n-1)
    count = -1
    while n is None or count < n:
        count += 1
        new_number = elements[0] + elements[1]
        if mod is not None:
            new_number %= mod
        elements.append(new_number)
        yield elements.pop(0)


def fibonacci_binet(n: int, suppress_exception: bool=False) -> int:
    """Returns the nth Fibonacci number using Binet's closed form solution.

    The closed form solution is of the form:

        phi = (1 + sqrt(5)) / 2
        psi = (1 - sqrt(5)) / 2

        F_n = (phi^n - psi^n) / sqrt(5)

    In practice, we ignore the psi term as it vanishes for large n, and is
    always smaller than 0.5, so the rounding done to return an integer
    correctly compensates for it in all cases.

    Although this solution is quick to calculate, it loses accuracy due to
    floating point imprecision after n~70.

    Args:
        n (int): The order of the Fibonacci number to calculate.
        suppress_exception (bool): Allow n > 70 without throwing an exception.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: n is not convertible to an integer or n < 0.
        ArithmeticError: n > 70, at which point the function fails to compute
            the correct answer. This exception can be turned off with the
            suppress_exception argument.
    """
    # F(-1) is undefined, so we raise an error
    if n < 0:
        raise ValueError("n is less than 0")
    # Floating point error gives us the wrong answer after n = 70
    if not suppress_exception and n > 70:
        raise ArithmeticError("results are inaccurate for n greater than 70")

    s5 = decimal.Decimal(math.sqrt(5))
    phi = decimal.Decimal((1 + s5) / 2)
    ans = (phi ** n) / s5
    return int(round(ans))
