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
# Write a function to find the smallest missing element in a sorted array.
#
# SOLUTION CODE
# ============================================
def smallest_missing(A, left_element, right_element):

    if left_element > right_element:

        return left_element

    mid = left_element + (right_element - left_element) // 2

    if A[mid] == mid:

        return smallest_missing(A, mid + 1, right_element)

    else:

        return smallest_missing(A, left_element, mid - 1)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, left_element, right_element, expected):
    try:
        if validate_solution(smallest_missing(
            a, left_element, right_element),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



