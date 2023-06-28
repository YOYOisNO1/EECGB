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
# Write a python function to find the maximum difference between any two elements in a given array.
#
# SOLUTION CODE
# ============================================
def max_abs_diff(arr,n): 

    minEle = arr[0] 

    maxEle = arr[0] 

    for i in range(1, n): 

        minEle = min(minEle,arr[i]) 

        maxEle = max(maxEle,arr[i]) 

    return (maxEle - minEle) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(max_abs_diff(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



