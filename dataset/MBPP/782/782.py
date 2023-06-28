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
# Write a python function to find the sum of all odd length subarrays.
#
# SOLUTION CODE
# ============================================
def odd_length_sum(arr):

    Sum = 0

    l = len(arr)

    for i in range(l):

        Sum += ((((i + 1) *(l - i) + 1) // 2) * arr[i])

    return Sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, expected):
    try:
        if validate_solution(odd_length_sum(
            arr),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



