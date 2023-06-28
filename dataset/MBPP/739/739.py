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
# Write a python function to find the index of smallest triangular number with n digits.
#
# SOLUTION CODE
# ============================================
import math 

def find_index(n): 

    x = math.sqrt(2 * math.pow(10,(n - 1))); 

    return round(x); 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(find_index(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



