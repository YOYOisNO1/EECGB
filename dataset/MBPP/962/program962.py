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
# Write a python function to find the sum of all even natural numbers within the range l and r.
#
# SOLUTION CODE
# ============================================
def sum_Natural(n): 

    sum = (n * (n + 1)) 

    return int(sum) 

def sum_even(l,r): 

    return (sum_Natural(int(r / 2)) - sum_Natural(int((l - 1) / 2))) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, r, expected):
    try:
        if validate_solution(sum_Natural(
            l, r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



