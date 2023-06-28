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
# Write a function to check if the given array represents min heap or not.
#
# SOLUTION CODE
# ============================================
def check_min_heap(arr, i):

    if 2 * i + 2 > len(arr):

        return True

    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap(arr, 2 * i + 1)

    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 

                                      and check_min_heap(arr, 2 * i + 2))

    return left_child and right_child

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, i, expected):
    try:
        if validate_solution(check_min_heap(
            arr, i),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



