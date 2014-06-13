def iterable_to_int(input_tuple):
    """Returns an integer from an ordered iterable, with the first item in the
    iterable taking the most significant digit's place, and so on.

    For example: (1, 2, 3) -> 123

    Args:
        input_tuple (ordered iterable): An order iterable of the digits of an
            integer in order from most to least significant digit.

    Returns:
        int: The number represented by the tuple.

    Raises:
        TypeError: If input_tuple does not support reversed().
    """
    number = 0
    place = 0
    for digit in reversed(input_tuple):
        number += (10 ** place) * digit
        place += 1

    return number


def int_to_tuple(number):
    pass
