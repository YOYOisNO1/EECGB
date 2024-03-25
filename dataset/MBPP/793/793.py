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
# Write a python function to find the last position of an element in a sorted array.
#
# SOLUTION CODE
# ============================================
def last(arr,x,n):

    low = 0

    high = n - 1

    res = -1  

    while (low <= high):

        mid = (low + high) // 2 

        if arr[mid] > x:

            high = mid - 1

        elif arr[mid] < x:

            low = mid + 1

        else:

            res = mid

            low = mid + 1

    return res

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, x, n, expected):
    try:
        if validate_solution(last(
            arr, x, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



