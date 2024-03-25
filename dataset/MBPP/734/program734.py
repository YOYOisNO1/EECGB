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
# Write a python function to find sum of products of all possible subarrays.
#
# SOLUTION CODE
# ============================================
def sum_of_subarray_prod(arr,n):

    ans = 0

    res = 0

    i = n - 1

    while (i >= 0):

        incr = arr[i]*(1 + res)

        ans += incr

        res = incr

        i -= 1

    return (ans)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(sum_of_subarray_prod(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



