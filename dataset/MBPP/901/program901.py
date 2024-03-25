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
# Write a function to find the smallest multiple of the first n numbers.
#
# SOLUTION CODE
# ============================================
def smallest_multiple(n):

    if (n<=2):

      return n

    i = n * 2

    factors = [number  for number in range(n, 1, -1) if number * 2 > n]

    while True:

        for a in factors:

            if i % a != 0:

                i += n

                break

            if (a == factors[-1] and i % a == 0):

                return i

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(smallest_multiple(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



