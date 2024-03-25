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
# Write a python function to find the sum of absolute differences in all pairs of the given array.
#
# SOLUTION CODE
# ============================================
def sum_pairs(arr,n): 

    sum = 0

    for i in range(n - 1,-1,-1): 

        sum += i*arr[i] - (n-1-i) * arr[i] 

    return sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(sum_pairs(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



