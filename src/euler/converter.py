from typing import Dict, Iterable, Tuple, Union, List
import euler.countable as countable


def iterable_to_int(input_tuple: Iterable[int]) -> int:
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
    str_tuple: Iterable[str] = (str(i) for i in input_tuple)
    return int(''.join(str_tuple))


def int_to_tuple(number: int) -> Tuple[int, ...]:
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


def sort_digits(number: int) -> int:
    """Sort the digits of an integer and return a new integer.

    This is useful for seeing if two numbers are permutations of each other.

    Args:
        number (int): An integer to sort.

    Returns:
        int: The sorted integer.

    Raises:
        ValueError: If number is < 0.

    """
    sorted_digits: List[int] = sorted(int_to_tuple(number), reverse=True)

    return iterable_to_int(sorted_digits)


def sum_digits(number: int) -> int:
    """Sum the digits of an integer and return a new integer.

    Args:
        number (int): An integer to sum.

    Returns:
        int: The sum of the digits.

    Raises:
        ValueError: If number is < 0.

    """
    return sum(int_to_tuple(number))


def truncate(number: int, right_truncate: bool=False) -> Union[int, None]:
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
    is_negative: bool = number < 0
    number = abs(number)

    # Convert to a string and strip the correct element
    str_number: str = str(number)
    truncated_str: str = ""
    if right_truncate:
        truncated_str = str_number[:-1]
    else:
        truncated_str = str_number[1:]
    # An empty string means we truncated the number away, so return None
    if not truncated_str:
        return None
    # Convert to int, restore the sign if needed, and return
    truncated_number: int = int(truncated_str)
    if is_negative:
        truncated_number *= -1

    return truncated_number


def right_truncate(number: int) -> Union[int, None]:
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


def left_truncate(number: int) -> Union[int, None]:
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


def reverse_int(number: int) -> int:
    """ Given an integer, returns the reverse of the integer.

    For negative numbers, the digits are reversed but the number remains
    negative.

    Args:
        number (int): returns the reverse of this number

    Returns:
        int: the reversed number

    Raises:
        ValueError: If number is none integral
        AttributeError: If number doesn't support number.is_integer()
    """
    # Only integers are supported
    if not countable.is_integer:
        raise ValueError("Input is non-integral")
    # For negative numbers, we remember that they are negative and strip the
    # sign
    is_negative: bool = number < 0
    number = abs(number)

    # Convert to string to reverse
    str_number: str = str(number)
    reversed_number: int = int(str_number[::-1])  # [::-1] reversed a string
    if is_negative:
        reversed_number *= -1

    return reversed_number


NumberWords = Dict[str, Dict[int, str]]

NUMBER_WORDS: NumberWords = {
    "ones": {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        0: '',
    },
    "teens": {
        1: 'eleven',
        2: 'twelve',
        3: 'thirteen',
        4: 'fourteen',
        5: 'fifteen',
        6: 'sixteen',
        7: 'seventeen',
        8: 'eighteen',
        9: 'nineteen',
        0: 'ten',
    },
    "tens": {
        1: 'ten',
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
        0: '',
    },
}


class NumberWriter(object):
    def __init__(self, number: int, number_words: NumberWords=NUMBER_WORDS) -> None:
        """Takes a number and returns the number written out in words.

        Supports numbers up to (1,000,000,000,000,000 - 1)

        For example:

            NumberWriter(342).word -> "three hundred and forty-two"

        Args:
            number (int): The number to convert to written English.
            number_words (object): any object that supports the following access:

                    object["ones"][ 0 through 9]
                    object["teens"][ 0 through 9]
                    object["tens"][ 0 through 9]

                It should return a string indicating the number from
                the digit in that place. For example,
                object["teens"][3] should return "thirteen" for
                English.

        Raises:
            ValueError: If number is < 0.
        """
        self.number_words: NumberWords = number_words
        self.number_tuple: Tuple[int, ...] = int_to_tuple(number)
        self.values: List[str] = ["", "thousand", "million", "billion", "trillion",]
        self.__convert_to_blocks()

        self.__create_string()

    def __create_string(self):
        self.word: str = ""

        # Zero is a special case, because otherwise a 0 in the ones
        # place has no word associated with it.
        if self.blocks == [[0]]:
            self.word = "zero"
            return

        # Otherwise recursively build the solution
        for i, block in enumerate(reversed(self.blocks)):
            current_value: str = self.values[i]
            digit_count: int = len(block)
            current_string: str = ""
            if digit_count == 1:
                current_string = self.__handle_one(block)
            if digit_count == 2:
                current_string = self.__handle_two(block)
            if digit_count == 3:
                current_string = self.__handle_three(block)

            # Some blocks, like 000, should produce no words, so don't
            # add anything.
            if current_string:
                self.word = current_string + " " + current_value + " " + self.word

        self.word = self.word.strip()

    def __convert_to_blocks(self):
        self.blocks = []
        number = list(self.number_tuple[:])

        # The leading digits are not always a group of 3, so get them first
        first_offset: int = len(number) % 3
        block: List[int] = []
        for _ in range(first_offset):
            block.append(number.pop(0))
        if block:
            self.blocks.append(block)

        # Now get all the rest, which are all three digits long
        block: List[int] = []
        for i, digit in enumerate(number):
            # Starting a new block
            if not i % 3:
                if block:
                    self.blocks.append(block)
                block = [digit]
            else:
                block.append(digit)
        # The last set will not trigger the new block check above, so add it
        # now
        if block:
            self.blocks.append(block)

    def __handle_one(self, tup) -> str:
        return self.number_words["ones"][tup[0]]

    def __handle_two(self, tup) -> str:
        # 10 - 19, which are weird
        if tup[0] == 1:
            return self.number_words["teens"][tup[1]]
        else:
            string: str = ""
            string += self.number_words["tens"][tup[0]]
            ones: str = self.__handle_one(tup[1:])
            if ones:
                string += "-" + ones
            return string

    def __handle_three(self, tup) -> str:
        # Length 3
        string: str = ""
        leading_value: str = self.number_words["ones"][tup[0]]
        if leading_value:
            string += leading_value + " hundred"
        tens: str = self.__handle_two(tup[1:])
        if tens:
            string += " and " + tens
        return string
