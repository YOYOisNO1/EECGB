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
# Write a python function to find the last digit in factorial of a given number.
#
# SOLUTION CODE
# ============================================
def last_digit_factorial(n): 

    if (n == 0): return 1

    elif (n <= 2): return n  

    elif (n == 3): return 6

    elif (n == 4): return 4 

    else: 

      return 0

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(last_digit_factorial(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



