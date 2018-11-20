from typing import SupportsFloat


def is_integer(number: SupportsFloat) -> bool:
    """Determine if a number is an integer.

    Args:
        number: The number to test.

    Returns:
        bool: True if number is an integer, False otherwise.

    Raises:
        AttributeError: If number doesn't support number.is_integer()
    """
    return float(number).is_integer()


def is_nonnegative_integer(number) -> bool:
    """Determine if a number is an integer and not negative.

    Args:
        number: The number to test.

    Returns:
        bool: True if number is an integer and not negative, False otherwise.

    Raises:
        AttributeError: If number doesn't support number.is_integer()
    """
    return (number >= 0 and is_integer(number))


def is_positive_integer(number) -> bool:
    """Determine if a number is an integer and greater than 0.

    Args:
        number: The number to test.

    Returns:
        bool: True if number is an integer and greater than 0, False otherwise.

    Raises:
        AttributeError: If number doesn't support number.is_integer()
    """
    return (number >= 1 and is_integer(number))


def is_nonpositive_integer(number) -> bool:
    """Determine if a number is an integer and not positive.

    Args:
        number: The number to test.

    Returns:
        bool: True if number is an integer and not positive, False otherwise.

    Raises:
        AttributeError: If number doesn't support number.is_integer()
    """
    return (number <= 0 and is_integer(number))


def is_negative_integer(number) -> bool:
    """Determine if a number is an integer and less than 0.

    Args:
        number: The number to test.

    Returns:
        bool: True if number is an integer and less than 0, False otherwise.

    Raises:
        AttributeError: If number doesn't support number.is_integer()
    """
    return (number <= -1 and is_integer(number))
