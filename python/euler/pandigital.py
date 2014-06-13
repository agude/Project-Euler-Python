import itertools
try:
    import euler.converter as converter
except ImportError:
    import converter


def is_pandigital(number):
    """Returns True if number is pandigital, False otherwise.

    An n-digit pandigital number contains digits 1 through n each exactly once,
    although the order is not important.

    For example: 123, 4231, 98765412

    Args:
        number (int): The number to test.

    Returns:
        bool: True if number is pandigital, False otherwise.
    """
    # Turn our number into a string and make a list of all digits to check
    test_numbers = []
    str_number = str(number)
    test_numbers = [str(i) for i in range(1, len(str_number) + 1)]

    # Check that each digit is in our number
    for digit in test_numbers:
        if digit not in str_number:
            return False

    return True

def pandigitals(digits):
    """Returns a list of all pandigital numbers length digits or less.

    An n-digit pandigital number contains digits 1 through n each exactly once,
    although the order is not important.

    For example: 123, 4231, 98765412

    Args:
        digits (int): The maximum number of digits to consider.

    Returns:
        list: A list of pandigital numbers.
    """
    numbers = []
    for max_number in range(1, digits + 1):
        digits = [i for i in range(1, max_number + 1)]
        for perm in itertools.permutations(digits):
            numbers.append(converter.iterable_to_int(perm))

    return numbers
