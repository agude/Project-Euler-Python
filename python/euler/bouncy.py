from enum import Enum
try:
    import euler.converter as converter
except ImportError:
    import converter
try:
    import euler.countable as countable
except ImportError:
    import countable


class NumberSlope(Enum):
    """ Enumerates the three possible number slopes. """
    decreasing = -1
    bouncy = 0
    increasing = 1


def check_number_slope(number):
    """ A general function to check if a number is a decreasing number, an
    increasing number, or neither (called "bouncy").

    A number is decreasing if its digits, read left-to-right, are always
    smaller than or equal to the digits that preceded them.  A number is
    increasing if its digits, read left-to-right, are always larger than or
    equal to the digits that preceded them. If it is neither, it is called
    "bouncy".

    Args:
        number (int): The number to test.

    Returns:
        NumberSlope: An element of the NumberSlope Enum, with -1 meaning
            decreasing, 1 meaning increasing, and 0 meaning neither.

    Raises:
        ValueError: If number is < 0, or not an integer.
    """
    if not countable.is_positive_integer(number):
        raise ValueError("input is not an integer")
    # We make a two lists out of the digits and sort them. If the results are
    # the same, then the number is increasing.
    first_list = list(converter.int_to_tuple(number))
    second_list = list(converter.int_to_tuple(number))
    second_list.sort()
    if first_list == second_list:
        return NumberSlope.increasing

    # For decreasing numbers, we need to also reverse the list so that the
    # largest digits are on the left
    second_list.reverse()
    if first_list == second_list:
        return NumberSlope.decreasing

    return NumberSlope.bouncy


def is_decreasing(number):
    """ Returns True if a number is decreasing, False otherwise.

    A number is decreasing if its digits, read left-to-right, are always
    smaller than or equal to the digits that preceded them.

    Args:
        number (int): The number to test.

    Returns:
        bool: True if the number is decreasing, False otherwise.

    Raises:
        ValueError: If number is < 0, or not an integer.
    """
    return check_number_slope(number) == NumberSlope.decreasing


def is_increasing(number):
    """ Returns True if a number is increasing, False otherwise.

    A number is increasing if its digits, read left-to-right, are always
    larger than or equal to the digits that preceded them.

    Args:
        number (int): The number to test.

    Returns:
        bool: True if the number is increasing, False otherwise.

    Raises:
        ValueError: If number is < 0, or not an integer.
    """
    return check_number_slope(number) == NumberSlope.increasing


def is_bouncy(number):
    """ Returns True if a number is bouncy, False otherwise.

    A number is bouncy if its digits, read left-to-right, are not always larger
    than or equal to the digits that preceded them and not always smaller than
    or equal to  the digits that preceded them. That is, the number is neither
    an increasing number nor a decreasing number.

    Args:
        number (int): The number to test.

    Returns:
        bool: True if the number is bouncy, False otherwise.

    Raises:
        ValueError: If number is < 0, or not an integer.
    """
    # Must be false for numbers less than 3 digits
    if 0 <= number < 100:
        return False
    # Otherwise, check if it is not increasing and not decreasing
    return check_number_slope(number) == NumberSlope.bouncy
