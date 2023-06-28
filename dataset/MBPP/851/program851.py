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
# Write a python function to find sum of inverse of divisors.
#
# SOLUTION CODE
# ============================================
def sum_of_inverse_divisors(N,Sum): 

    ans = float(Sum)*1.0 /float(N);  

    return round(ans,2); 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(n, sum, expected):
    try:
        if validate_solution(sum_of_inverse_divisors(
            n, sum),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



