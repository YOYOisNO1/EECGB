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
# Write a function to round up a number to specific digits.
#
# SOLUTION CODE
# ============================================
import math

def round_up(a, digits):

    n = 10**-digits

    return round(math.ceil(a / n) * n, digits)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(a, digits, expected):
    try:
        if validate_solution(round_up(
            a, digits),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



