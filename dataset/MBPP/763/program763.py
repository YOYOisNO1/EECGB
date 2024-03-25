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
# Write a python function to find the minimum difference between any two elements in a given array.
#
# SOLUTION CODE
# ============================================
def find_min_diff(arr,n): 

    arr = sorted(arr) 

    diff = 10**20 

    for i in range(n-1): 

        if arr[i+1] - arr[i] < diff: 

            diff = arr[i+1] - arr[i]  

    return diff 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(find_min_diff(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



