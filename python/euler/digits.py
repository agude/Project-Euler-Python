import euler.countable as countable


def square_and_add(number: int) -> int:
    """Return the sum of the square of a number's digits.

    Args:
        number (int): An integer square the digits of and sum.

    Returns:
        int: The sum of the square of the digits.

    Raises:
        ValueError: If number is < 0 or non-integral.
    """
    # Only non-negative integers are supported
    if not countable.is_nonnegative_integer(number):
        raise ValueError("Input must be integral and non-negative")

    # Use mod 10 and integer division to pull off digits
    result = 0
    while number:
        digit = number % 10
        number //= 10
        result += digit * digit

    return result
