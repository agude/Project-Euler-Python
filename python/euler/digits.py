try:
    import euler.converter as converter
except ImportError:
    import converter


def square_and_add(number):
    """Return the sum of the square of a number's digits.

    Args:
        number (int): An integer square the digits of and sum.

    Returns:
        int: The sum of the square of the digits.

    Raises:
        ValueError: If number is < 0.
    """
    result = 0
    for i in converter.int_to_tuple(number):
        result += i**2

    return result
