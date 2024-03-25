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
# Write a python function to find the sum of all odd natural numbers within the range l and r.
#
# SOLUTION CODE
# ============================================
def sum_Odd(n): 

    terms = (n + 1)//2

    sum1 = terms * terms 

    return sum1  

def sum_in_range(l,r): 

    return sum_Odd(r) - sum_Odd(l - 1)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, r, expected):
    try:
        if validate_solution(sum_Odd(
            l, r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



