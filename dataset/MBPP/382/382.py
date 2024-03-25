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
# Write a function to find the number of rotations in a circularly sorted array.
#
# SOLUTION CODE
# ============================================
def find_rotation_count(A):

    (left, right) = (0, len(A) - 1)

    while left <= right:

        if A[left] <= A[right]:

            return left

        mid = (left + right) // 2

        next = (mid + 1) % len(A)

        prev = (mid - 1 + len(A)) % len(A)

        if A[mid] <= A[next] and A[mid] <= A[prev]:

            return mid

        elif A[mid] <= A[right]:

            right = mid - 1

        elif A[mid] >= A[left]:

            left = mid + 1

    return -1

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, expected):
    try:
        if validate_solution(find_rotation_count(
            a),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



