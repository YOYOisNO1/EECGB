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
# Write a python function to find the largest product of the pair of adjacent elements from a given list of integers.
#
# SOLUTION CODE
# ============================================
def adjacent_num_product(list_nums):

    return max(a*b for a, b in zip(list_nums, list_nums[1:]))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list_nums, expected):
    try:
        if validate_solution(adjacent_num_product(
            list_nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



