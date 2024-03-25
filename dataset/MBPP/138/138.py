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
# Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
#
# SOLUTION CODE
# ============================================
def is_sum_of_powers_of_two(n): 

    if (n % 2 == 1): 

        return False

    else: 

        return True

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(is_sum_of_powers_of_two(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



