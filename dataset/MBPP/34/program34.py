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
# Write a python function to find the missing number in a sorted array.
#
# SOLUTION CODE
# ============================================
def find_missing(ar,N): 

    l = 0

    r = N - 1

    while (l <= r):  

        mid = (l + r) / 2

        mid= int (mid) 

        if (ar[mid] != mid + 1 and ar[mid - 1] == mid): 

            return (mid + 1)  

        elif (ar[mid] != mid + 1): 

            r = mid - 1 

        else: 

            l = mid + 1

    return (-1) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(ar, n, expected):
    try:
        if validate_solution(find_missing(
            ar, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



