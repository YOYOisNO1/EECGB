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
# Write a function to find the index of the last occurrence of a given number in a sorted array.
#
# SOLUTION CODE
# ============================================
def find_last_occurrence(A, x):

    (left, right) = (0, len(A) - 1)

    result = -1

    while left <= right:

        mid = (left + right) // 2

        if x == A[mid]:

            result = mid

            left = mid + 1

        elif x < A[mid]:

            right = mid - 1

        else:

            left = mid + 1

    return result 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, x, expected):
    try:
        if validate_solution(find_last_occurrence(
            a, x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



