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
