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
# Write a function to find the sum of geometric progression series.
#
# SOLUTION CODE
# ============================================
import math

def sum_gp(a,n,r):

 total = (a * (1 - math.pow(r, n ))) / (1- r)

 return total

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, r, expected):
    try:
        if validate_solution(sum_gp(
            a, n, r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



