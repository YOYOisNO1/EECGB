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
# Write a python function to find the position of the last removed element from the given array.
#
# SOLUTION CODE
# ============================================
import math as mt 

def get_position(a,n,m): 

    for i in range(n): 

        a[i] = (a[i] // m + (a[i] % m != 0))  

    result,maxx = -1,-1

    for i in range(n - 1,-1,-1): 

        if (maxx < a[i]): 

            maxx = a[i] 

            result = i 

    return result + 1

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, m, expected):
    try:
        if validate_solution(get_position(
            a, n, m),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



