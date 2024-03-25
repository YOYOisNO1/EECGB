import array
import bisect
import collections
import datetime
import functools
import heapq
import itertools
import math
import queue
import re
import string
import sys
from typing import Any, Dict, List, Optional, Set

# Question Prompt (NOT what is passed to the model)
# Write a function to sum all amicable numbers from 1 to a specified number.
#
# SOLUTION CODE
# ============================================
def amicable_numbers_sum(limit):

    if not isinstance(limit, int):

        return "Input is not an integer!"

    if limit < 1:

        return "Input must be bigger than 0!"

    amicables = set()

    for num in range(2, limit+1):

        if num in amicables:

            continue

        sum_fact = sum([fact for fact in range(1, num) if num % fact == 0])

        sum_fact2 = sum([fact for fact in range(1, sum_fact) if sum_fact % fact == 0])

        if num == sum_fact2 and num != sum_fact:

            amicables.add(num)

            amicables.add(sum_fact2)

    return sum(amicables)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(limit, expected):
    try:
        if validate_solution(amicable_numbers_sum(
            limit),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



