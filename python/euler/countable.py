def is_integer(number): 
    """Determine if a number is an integer.

    Args:
        number: The number to test.

    Returns:
        bool: True if number is an integer, False otherwise.

    Raises:
        AttributeError: If number doesn't support number.is_integer()
    """
    return number.is_integer()


def is_nonnegative_integer(number):
    """Determine if a number is an integer and not negative.

    Args:
        number: The number to test.

    Returns:
        bool: True if number is an integer and not negative, False otherwise.

    Raises:
        AttributeError: If number doesn't support number.is_integer()
    """
    return (number >= 0 && is_integer(number))


def is_positive_integer(number):
    """Determine if a number is an integer and greater than 0.

    Args:
        number: The number to test.

    Returns:
        bool: True if number is an integer and greater than 0, False otherwise.

    Raises:
        AttributeError: If number doesn't support number.is_integer()
    """
    return (number >= 1 && is_integer(number))


def is_nonpositive_integer(number):
    """Determine if a number is an integer and not positive.

    Args:
        number: The number to test.

    Returns:
        bool: True if number is an integer and not positive, False otherwise.

    Raises:
        AttributeError: If number doesn't support number.is_integer()
    """
    return (number <= 0 && is_integer(number))


def is_negative_integer(number):
    """Determine if a number is an integer and less than 0.

    Args:
        number: The number to test.

    Returns:
        bool: True if number is an integer and less than 0, False otherwise.

    Raises:
        AttributeError: If number doesn't support number.is_integer()
    """
    return (number <= -1 && is_integer(number))
