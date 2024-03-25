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
# Write a function to check for the number of jumps required of given length to reach a point of form (d, 0) from origin in a 2d plane.
#
# SOLUTION CODE
# ============================================
def min_jumps(a, b, d): 

    temp = a 

    a = min(a, b) 

    b = max(temp, b) 

    if (d >= b): 

        return (d + b - 1) / b 

    if (d == 0): 

        return 0

    if (d == a): 

        return 1

    else:

        return 2

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(a, b, d, expected):
    try:
        if validate_solution(min_jumps(
            a, b, d),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



