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
# Write a python function to find the minimum number of squares whose sum is equal to a given number.
#
# SOLUTION CODE
# ============================================
def get_min_squares(n):

    if n <= 3:

        return n;

    res = n 

    for x in range(1,n + 1):

        temp = x * x;

        if temp > n:

            break

        else:

            res = min(res,1 + get_min_squares(n  - temp)) 

    return res;

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(get_min_squares(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



