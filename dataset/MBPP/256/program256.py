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
# Write a python function to count the number of prime numbers less than a given non-negative number.
#
# SOLUTION CODE
# ============================================
def count_primes_nums(n):

    ctr = 0

    for num in range(n):

        if num <= 1:

            continue

        for i in range(2,num):

            if (num % i) == 0:

                break

        else:

            ctr += 1

    return ctr

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(count_primes_nums(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



