def is_palindromic(number: int) -> bool:
    """Returns True if the number is palindromic, that is, read the same
    forward as backwards, otherwise returns False.

    Negative numbers are palindromic if their absolute values are palindromic.

    Args:
        number (int): The number to test.

    Returns:
        bool: True if number is palindromic, False otherwise.
    """
    test_number: str = str(abs(number))
    return test_number == test_number[::-1]  # [::-1] reverses a list


def is_binary_palindromic(number: int) -> bool:
    """Returns True if the number is palindromic in binary, that is, read the
    same forward as backwards, otherwise returns False.

    Negative numbers are palindromic if their absolute values are palindromic.

    Args:
        number (int): The number to test.

    Returns:
        bool: True if number's binary representation is palindromic, False
            otherwise.
    """
    binary_string: str = bin(abs(number))[2:]  # We strip the "0b" prefix
    return binary_string == binary_string[::-1]  # [::-1] reverses a list
