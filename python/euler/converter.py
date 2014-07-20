try:
    import euler.countable as countable
except ImportError:
    import countable


def iterable_to_int(input_tuple):
    """Returns an integer from an ordered iterable, with the first item in the
    iterable taking the most significant digit's place, and so on.

    For example: (1, 2, 3) -> 123

    Note that it only support numbers >= 0.

    Args:
        input_tuple (ordered iterable): An order iterable of the digits of an
            integer in order from most to least significant digit.

    Returns:
        int: The number represented by the tuple.

    Raises:
        TypeError: If input_tuple does not support reversed().
    """
    # Using a string is faster than looping over the tuple and adding numbers
    str_tuple = (str(i) for i in input_tuple)
    return int(''.join(str_tuple))


def int_to_tuple(number):
    """Takes an integer and returns a tuple of the digits in order.

    For example: 123 -> (1, 2, 3)

    Note that it only support numbers >= 0.

    Args:
        number (int): An integer to turn into a tuple.

    Returns:
        tuple: The tuple representation of the input number.

    Raises:
        ValueError: If number is < 0.
    """
    if number < 0:
        raise ValueError("Input less than 0")
    # Using a string might not be as clean as some sort of division and modulo
    # loop, but using the string is much faster for large numbers
    return tuple([int(i) for i in str(number)])


def truncate(number, right_truncate=False):
    """Truncate an integer and return the smaller integer.

    It will truncate from the left side by default, right side truncate is
    supported with the optional argument.

    Negative numbers are kept negative.

    Args:
        number (int): the number to truncate
        right_truncate (bool, False): truncate from the right instead of the
            left

    Returns:
        int: the result of truncation, or None if the number is truncated to
            nothing

    Raises:
        ValueError: If number is none integral
        AttributeError: If number doesn't support number.is_integer()
    """
    # Only integers are supported
    if not countable.is_integer:
        raise ValueError("Input is non-integral")
    # For negative numbers, we remember that they are negative and strip the
    # sign
    is_negative = number < 0
    number = abs(number)

    # Convert to a string and strip the correct element
    str_number = str(number)
    if right_truncate:
        truncated_str = str_number[:-1]
    else:
        truncated_str = str_number[1:]
    # An empty string means we truncated the number away, so return None
    if not truncated_str:
        return None
    # Convert to int, restore the sign if needed, and return
    truncated_number = int(truncated_str)
    if is_negative:
        truncated_number *= -1

    return truncated_number


def right_truncate(number):
    """Truncate an integer from the right and return the smaller integer.

    This is a simple wrapper around truncate. The source is simply:
        return truncate(number, right_truncate=True)

    Args:
        number (int): the number to truncate

    Returns:
        int: the result of truncation, or None if the number is truncated to
            nothing

    Raises:
        ValueError: If number is none integral
        AttributeError: If number doesn't support number.is_integer()
    """
    return truncate(number, right_truncate=True)


def left_truncate(number):
    """Truncate an integer from the left and return the smaller integer.

    This is a simple wrapper around truncate. The source is simply:
        return truncate(number, right_truncate=False)

    Args:
        number (int): the number to truncate

    Returns:
        int: the result of truncation, or None if the number is truncated to
            nothing

    Raises:
        ValueError: If number is none integral
        AttributeError: If number doesn't support number.is_integer()
    """
    return truncate(number, right_truncate=False)
