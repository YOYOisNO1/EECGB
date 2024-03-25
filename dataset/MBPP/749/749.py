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
# Write a function to sort a given list of strings of numbers numerically.
#
# SOLUTION CODE
# ============================================
def sort_numeric_strings(nums_str):

    result = [int(x) for x in nums_str]

    result.sort()

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums_str, expected):
    try:
        if validate_solution(sort_numeric_strings(
            nums_str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



