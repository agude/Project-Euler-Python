#!/usr/bin/env python3

#  Copyright (C) 2014  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#  The most recent version of this program is available at:
#  https://github.com/agude/Project-Euler

"""
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3,
4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5,
6.

Peter and Colin roll their dice and compare totals: the highest total wins. The
result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer
rounded to seven decimal places in the form 0.abcdefg
"""

from euler.dice import roll_under_probability, roll_probability
from time import time


def problem_205():
    start_time = time()

    # Probability of rolling i for 9d4s
    d4_sides = 4
    n_d4 = 9
    top_number = n_d4 * d4_sides
    d4_prob = {i: roll_probability(d4_sides, n_d4, i) for i in range(1, top_number + 1)}

    # Probability of rolling under i for 6d4s
    d6_sides = 6
    n_d6 = 6
    d6_prob = {i: roll_under_probability(d6_sides, n_d6, i) for i in range(1, top_number + 2)}

    # The total probability of the d4s winning is the probability of the d4s
    # rolling a number multiplied by the probability of the d6s rolling under
    # that number, for every number the d4s can roll.
    total_probability = 0
    for i in d4_prob:
        total_probability += d4_prob[i] * d6_prob[i]

    end_time = time() - start_time

    answer = round(total_probability, 7)

    print(answer, 'in', end_time, 'secs')
    return answer


# Only runs if executed directly
if __name__ == '__main__':

    problem_205()
