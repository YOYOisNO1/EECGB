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
# Write a function to divide a number into two parts such that the sum of digits is maximum.
#
# SOLUTION CODE
# ============================================
def sum_digits_single(x) : 

    ans = 0

    while x : 

        ans += x % 10

        x //= 10  

    return ans 

def closest(x) : 

    ans = 0

    while (ans * 10 + 9 <= x) : 

        ans = ans * 10 + 9  

    return ans   

def sum_digits_twoparts(N) : 

    A = closest(N)  

    return sum_digits_single(A) + sum_digits_single(N - A) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(sum_digits_single(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



