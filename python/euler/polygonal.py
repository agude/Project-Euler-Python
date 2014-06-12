import math


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
    print(test_number)
    return (test_number > 0 and int(test_number) == test_number)


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
