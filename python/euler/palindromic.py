def is_palindromic(number):
    """Returns True if the number is palindromic, that is, read the same
    forward as backwards, otherwise returns False.

    Args:
        number (int): The number to test.

    Returns:
        bool: True if number is palindromic, False otherwise.
    """
    test_number = str(number)
    return test_number == test_number[::-1]  # [::-1] reverses a list
