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
# Write a python function to find the difference between highest and least frequencies in a given array.
#
# SOLUTION CODE
# ============================================
def find_diff(arr,n): 

    arr.sort()  

    count = 0; max_count = 0; min_count = n 

    for i in range(0,(n-1)): 

        if arr[i] == arr[i + 1]: 

            count += 1

            continue

        else: 

            max_count = max(max_count,count) 

            min_count = min(min_count,count) 

            count = 0

    return max_count - min_count 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(find_diff(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



