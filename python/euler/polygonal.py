import math
try:
    import euler.countable as countable
except ImportError:
    import countable


def polygonals(multiplier, divisor, offset, stop=None, start=1):
    """ A generator for generic polygonal numbers.

    This generator uses the following formula:

        n * ((multiplier * n) + offset) // divisor

    Where n is an integer greater than or equal to 0, and multiplier, offset,
    and divisor are numbers. By properly setting the constants multiplier,
    offset, and divisor various polygonal number sequences are generated. These
    constants are correctly set by the various wrapping functions (triangulars,
    etc.).

    Args:
        multiplier (int): The multiplier used in the general formula.
        divisor (int): The divisor used in the general formula.
        offset (int): The offset used in the general formula.
        stop (int, None): Stop when n exceeds this number
        start (int, 1): Start with n equal to this number

    Yields:
        int: The next polygonal number.

    Raises:
        ValueError: If stop or start are not integers greater than or equal to
            zero.
    """
    # Test the input values
    if stop is not None and not countable.is_nonnegative_integer(stop):
        raise ValueError("stop must be a nonnegative integer")
    if not countable.is_nonnegative_integer(start):
        raise ValueError("start must be a nonnegative integer")

    # Set up the run condition
    run_forever = False
    if stop is None:
        run_forever = True

    # Loop over triangular numbers
    n = start
    while run_forever or n <= stop:
        yield n * ((multiplier * n) + offset) // divisor
        n += 1


def triangulars(stop=None, start=1):
    """Returns an iterator over all triangular numbers.

    Computes all triangular numbers from n = 1 to infinity by default, although
    the starting and stopping values of n can be adjusted with the arguments.

    Args:
        stop (int, None): Stop when n exceeds this number
        start (int, 1): Start with n equal to this number

    Yields:
        int: The next triangular number.
    """
    return polygonals(1, 2, 1, stop, start)


def pentagonals(stop=None, start=1):
    """Returns an iterator over all pentagonal numbers.

    Computes all pentagonal numbers from n = 1 to infinity by default, although
    the starting and stopping values of n can be adjusted with the arguments.

    Args:
        stop (int, None): Stop when n exceeds this number
        start (int, 1): Start with n equal to this number

    Yields:
        int: The next pentagonal number.
    """
    return polygonals(3, 2, -1, stop, start)


def hexagonals(stop=None, start=1):
    """Returns an iterator over all hexagonal numbers.

    Computes all hexagonal numbers from n = 1 to infinity by default, although
    the starting and stopping values of n can be adjusted with the arguments.

    Args:
        stop (int, None): Stop when n exceeds this number
        start (int, 1): Start with n equal to this number

    Yields:
        int: The next hexagonal number.
    """
    return polygonals(2, 1, -1, stop, start)


def is_polygonal(number, multiplier, divisor):
    """Determine if a number is a specific type of polygonal number.

    This functions uses the formula:

    P = (sqrt(multiplier * number + 1) + 1) / divisor

    If P is an integer and > 0, then the test number is the specific type of
    polygonal, otherwise it is not.

    This function is completely general, but requires the user to specify the
    constants themselves. Using the wrapping functions in this module
    (is_hexagonal, etc.) is recommended as these set the constants correctly
    for the specific type of polygonal number.

    Args:
        number (int): The number to test.
        multiplier (int): The multiplier used in the general formula.
        divisor (int): The divisor used in the general formula.

    Returns:
        bool: True if number is polygonal, False otherwise.

    Raises:
        TypeError: If number and multiplier do not support +, *, or sqrt(), or
        if divisor does not support / .
    """
    test_number = (math.sqrt(multiplier * number + 1) + 1) / divisor
    return (test_number > 0 and countable.is_integer(test_number))


def is_triangular(number):
    """Determine if a number triangular.

    Args:
        number (int): The number to test.

    Returns:
        bool: True if number is polygonal, False otherwise.

    Raises:
        TypeError: If number does not support +, *, or sqrt().
    """
    return is_polygonal(number, 8, 2)


def is_pentagonal(number):
    """Determine if a number pentagonal.

    Args:
        number (int): The number to test.

    Returns:
        bool: True if number is polygonal, False otherwise.

    Raises:
        TypeError: If number does not support +, *, or sqrt().
    """
    return is_polygonal(number, 24, 6)


def is_hexagonal(number):
    """Determine if a number hexagonal.

    Args:
        number (int): The number to test.

    Returns:
        bool: True if number is polygonal, False otherwise.

    Raises:
        TypeError: If number does not support +, *, or sqrt().
    """
    return is_polygonal(number, 8, 4)
