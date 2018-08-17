from enum import Enum
import euler.converter as converter
import euler.countable as countable


class NumberSlope(Enum):
    """ Enumerates the four possible number slopes. """
    decreasing = -1
    bouncy = 0
    increasing = 1
    both = 2


def check_number_slope(number: int) -> NumberSlope:
    """ A general function to check if a number is a decreasing number, an
    increasing number, both, or neither (called "bouncy").

    A number is decreasing if its digits, read left-to-right, are always
    smaller than or equal to the digits that preceded them.  A number is
    increasing if its digits, read left-to-right, are always larger than or
    equal to the digits that preceded them. If it is neither, it is called
    "bouncy".

    Args:
        number (int): The number to test.

    Returns:
        NumberSlope: An element of the NumberSlope Enum, with -1 meaning
            decreasing, 1 meaning increasing, 2 meaning both, and 0 meaning
            neither.

    Raises:
        ValueError: If number is < 0, or not an integer.
    """
    # Only defined for integers
    if not countable.is_positive_integer(number):
        raise ValueError("input is not an integer")
    number_tuple = converter.int_to_tuple(number)

    # Check through the number from left-to-right and keep track if it can be a
    # decreasing or increasing number.
    decreasing = True
    increasing = True
    for i in range(len(number_tuple) - 1):
        # Check if increasing
        if increasing and not number_tuple[i] <= number_tuple[i+1]:
            increasing = False
        # Check if decreasing
        if decreasing and not number_tuple[i] >= number_tuple[i+1]:
            decreasing = False
        # If we have already shown it is neither, it must be bouncy
        if not decreasing and not increasing:
            return NumberSlope.bouncy

    # At this point it is either decrease XOR decreasing
    if increasing and decreasing:
        return NumberSlope.both
    elif increasing:
        return NumberSlope.increasing
    else:
        return NumberSlope.decreasing


def is_decreasing(number: int) -> bool:
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
    result = check_number_slope(number)
    return result == NumberSlope.decreasing or result == NumberSlope.both


def is_increasing(number: int) -> bool:
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
    result = check_number_slope(number)
    return result == NumberSlope.increasing or result == NumberSlope.both


def is_bouncy(number: int) -> bool:
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
