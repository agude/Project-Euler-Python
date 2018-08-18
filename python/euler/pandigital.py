from typing import Generator, List
import itertools
import euler.converter as converter


def is_pandigital(number: int) -> bool:
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
    str_number: str = str(number)
    test_numbers: List[str] = [str(i) for i in range(1, len(str_number) + 1)]

    # Check that each digit is in our number
    for digit in test_numbers:
        if digit not in str_number:
            return False

    return True


def pandigitals(minimum_digits: int = 1, maximum_digits: int = 9, include_zero: bool = False) -> Generator[int, None, None]:
    """A generator over all pandigital numbers.

    An n-digit pandigital number contains digits 1 through n each exactly once,
    although the order is not important. Sometimes 0 is included as an allowed
    digit, but by default this function does not include it; set
    `include_zero=True` to allow 0.

    If 0 is not included, then the one and two digit pandigital numbers are:

    1
    12
    21

    If it is included, than they are:

    0
    1
    10
    12
    21

    In this latter case, 1 could be viewed as the two digit number "01", 12 and
    21 as the three digit numbers "012" and "021" respectively. However, we
    always strip leading zeros and then consider the length of the resulting
    number when applying the maximum_digits and minimum_digits constraints.
    This is so that setting `include_zero=True` strictly adds numbers the list
    to yield as compared to running it with the value set to False.

    Args:
        minimum_digits (int, default 1): The minimum number of digits to
            consider.
        maximum_digits (int, default 9): The maximum number of digits to
            consider.
        include_zero (bool, default False): Should 0 be included in the digit
            list.

    Yields:
        int: All the pandigital numbers that satisfy the criteria specified.

    Raises:
        ValueError if minimum_digits is less than 1, or maximum_digits is
            greater than 10.
    """
    # Check for non-sense input values and raise and error
    err: str = ""
    if minimum_digits < 1:
        err = "can not generate numbers with fewer than 1 digit"
        raise ValueError(err)
    if maximum_digits > 9 and not include_zero:
        err = "can not generate numbers with more than 9 digits if 0 is not allowed"
        raise ValueError(err)
    if maximum_digits > 10:
        err = "can not generate numbers with more than 10 digits"
        raise ValueError(err)

    # Loop over the allowed number of digits
    for max_number in range(minimum_digits, maximum_digits + 1):
        # We only ever generate digits 1-9, even if max_number is 10
        max_digit_range: int = min(10, max_number + 1)
        digits: List[int] = [i for i in range(1, max_digit_range)]

        # Sometimes we want to include 0
        if include_zero:
            digits = [0] + digits

        # Iterate through all the permutations
        for perm in itertools.permutations(digits, max_number):
            # If we include 0, there are a few cases produced by permutations
            # that are not-pandigital numbers that we need to check for. These
            # only arise if we have more than just one digit in the number.
            if include_zero and len(perm) > 1:
                # A leading 0 would generate a duplicate number, so we ignore
                # these. However, we still want "0".
                if perm[0] == 0:
                    continue
                # Likewise, the number is not pandigital if it includes both 0
                # and the last number in digits, as this means we skipped a
                # number in the middle.
                if len(perm) < 10 and 0 in perm and digits[-1] in perm:
                    continue

            # Convert to a number and return
            yield converter.iterable_to_int(perm)
