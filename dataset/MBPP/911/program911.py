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
# Write a function to compute maximum product of three numbers of a given array of integers using heap queue algorithm.
#
# SOLUTION CODE
# ============================================
def maximum_product(nums):

    import heapq

    a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)

    return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, expected):
    try:
        if validate_solution(maximum_product(
            nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



