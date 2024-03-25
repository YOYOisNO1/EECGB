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
# Write a python function to find the first element occurring k times in a given array.
#
# SOLUTION CODE
# ============================================
def first_element(arr,n,k): 

    count_map = {}; 

    for i in range(0, n): 

        if(arr[i] in count_map.keys()): 

            count_map[arr[i]] += 1

        else: 

            count_map[arr[i]] = 1

        i += 1

    for i in range(0, n):  

        if (count_map[arr[i]] == k): 

            return arr[i] 

        i += 1 

    return -1

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, k, expected):
    try:
        if validate_solution(first_element(
            arr, n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



