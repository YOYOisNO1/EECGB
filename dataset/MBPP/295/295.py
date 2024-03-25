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
# Write a function to return the sum of all divisors of a number.
#
# SOLUTION CODE
# ============================================
def sum_div(number):

    divisors = [1]

    for i in range(2, number):

        if (number % i)==0:

            divisors.append(i)

    return sum(divisors)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(number, expected):
    try:
        if validate_solution(sum_div(
            number),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



