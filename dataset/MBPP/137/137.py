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
# Write a function to find the ration of zeroes in an array of integers.
#
# SOLUTION CODE
# ============================================
from array import array

def zero_count(nums):

    n = len(nums)

    n1 = 0

    for x in nums:

        if x == 0:

            n1 += 1

        else:

          None

    return round(n1/n,2)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(nums, expected):
    try:
        if validate_solution(zero_count(
            nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



