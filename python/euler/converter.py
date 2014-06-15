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
