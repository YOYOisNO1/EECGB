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
# Write a function to find minimum of two numbers.
#
# SOLUTION CODE
# ============================================
def min_of_two( x, y ):

    if x < y:

        return x

    return y

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, expected):
    try:
        if validate_solution(min_of_two(
            x, y),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



