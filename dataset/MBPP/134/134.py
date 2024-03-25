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
# Write a python function to check whether the last element of given array is even or odd after performing an operation p times.
#
# SOLUTION CODE
# ============================================
def check_last (arr,n,p): 

    _sum = 0

    for i in range(n): 

        _sum = _sum + arr[i] 

    if p == 1: 

        if _sum % 2 == 0: 

            return "ODD"

        else: 

            return "EVEN"

    return "EVEN"

      

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, p, expected):
    try:
        if validate_solution((
            arr, n, p),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



