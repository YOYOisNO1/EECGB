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
# Write a python function to find the minimum sum of absolute differences of two arrays.
#
# SOLUTION CODE
# ============================================
def find_min_sum(a,b,n): 

    a.sort() 

    b.sort() 

    sum = 0  

    for i in range(n): 

        sum = sum + abs(a[i] - b[i]) 

    return sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, n, expected):
    try:
        if validate_solution(find_min_sum(
            a, b, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



