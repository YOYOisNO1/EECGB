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
# Write a python function to check whether the count of inversion of two types are same or not.
#
# SOLUTION CODE
# ============================================
import sys 

def solve(a,n):   

    mx = -sys.maxsize - 1

    for j in range(1,n):  

        if (mx > a[j]):  

            return False  

        mx = max(mx,a[j - 1])    

    return True

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, expected):
    try:
        if validate_solution(solve(
            a, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



