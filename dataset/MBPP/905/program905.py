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
# Write a python function to find the sum of squares of binomial co-efficients.
#
# SOLUTION CODE
# ============================================
def factorial(start,end): 

    res = 1 

    for i in range(start,end + 1): 

        res *= i      

    return res 

def sum_of_square(n): 

   return int(factorial(n + 1, 2 * n)  /factorial(1, n)) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(factorial(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



