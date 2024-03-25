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
# Write a function to find the median of three specific numbers.
#
# SOLUTION CODE
# ============================================
def median_numbers(a,b,c):

 if a > b:

    if a < c:

        median = a

    elif b > c:

        median = b

    else:

        median = c

 else:

    if a > c:

        median = a

    elif b < c:

        median = b

    else:

        median = c

 return median

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(a, b, c, expected):
    try:
        if validate_solution(median_numbers(
            a, b, c),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



