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
# Write a python function to find gcd of two positive integers.
#
# SOLUTION CODE
# ============================================
def gcd(x, y):

    gcd = 1

    if x % y == 0:

        return y

    for k in range(int(y / 2), 0, -1):

        if x % k == 0 and y % k == 0:

            gcd = k

            break  

    return gcd

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, expected):
    try:
        if validate_solution(gcd(
            x, y),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



