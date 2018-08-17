from math import floor
import euler.combinatorics as combinatorics
import euler.countable as countable


def roll_probability(s: int, n: int, k: int) -> float:
    """ Return the probability of rolling a total k using n dice of size s.

    Uses:
        F_{s,n}(x) = \frac{1}{s^n}\sum_{i=0}^{\left \lfloor \frac{k-n}{s}
        \right \rfloor} (-1)^i {n \choose i} {k-si-1 \choose n-1}

    Args:
        s (int): A positive integer indicating the number of sides on the dice.
        n (int): A positive integer indicating the number of dice to consider.
        k (int): A positive integer indicating the target number.

    Returns:
        float: The probability of rolling a total k on n s-sided dice.

    Raises:
        ValueError: if s, n, or k are not non-negative integers.
    """
    # Check that s, n, and k are allowed
    if not countable.is_nonnegative_integer(s):
        raise ValueError("s is a not a non-negative integer")
    if not countable.is_nonnegative_integer(n):
        raise ValueError("n is a not a non-negative integer")
    if not countable.is_nonnegative_integer(k):
        raise ValueError("k is a not a non-negative integer")

    # Coefficient
    coef = 1. / s**n

    # Sum
    sum_terms = 0
    ending_term = int(floor((k - n) / s))
    for i in range(0, ending_term + 1):
        term = 1
        term *= ((-1)**i) * combinatorics.n_choose_k(n, i)
        term *= combinatorics.n_choose_k(k - (s * i) - 1, n - 1)
        sum_terms += term

    # Combine and return
    return coef * sum_terms


def roll_under_probability(s: int, n: int, k: int) -> float:
    """ Return the probability of rolling less than k using n dice of size s.

    Uses:
        F_{s,n}(x) = \frac{1}{s^n}\sum_{i=0}^{\left \lfloor \frac{k-n}{s}
        \right \rfloor} (-1)^i {n \choose i} {k-si-1 \choose n-1}

    Args:
        s (int): A positive integer indicating the number of sides on the dice.
        n (int): A positive integer indicating the number of dice to consider.
        k (int): A positive integer indicating the target number.

    Returns:
        float: The probability of rolling less than k on n s-sided dice.

    Raises:
        ValueError: if s, n, or k are not non-negative integers.
    """
    combined_probability = 0.0
    for i in range(n, min(k, s * n + 1)):
        combined_probability += roll_probability(s, n, i)

    return combined_probability


def roll_over_probability(s: int, n: int, k: int) -> float:
    """ Return the probability of rolling more than k using n dice of size s.

    Uses:
        F_{s,n}(x) = \frac{1}{s^n}\sum_{i=0}^{\left \lfloor \frac{k-n}{s}
        \right \rfloor} (-1)^i {n \choose i} {k-si-1 \choose n-1}

    Args:
        s (int): A positive integer indicating the number of sides on the dice.
        n (int): A positive integer indicating the number of dice to consider.
        k (int): A positive integer indicating the target number.

    Returns:
        float: The probability of rolling more than k on n s-sided dice.

    Raises:
        ValueError: if s, n, or k are not non-negative integers.
    """
    combined_probability = 0.0
    for i in range(max(k + 1, n), s * n + 1):
        combined_probability += roll_probability(s, n, i)

    return combined_probability
