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
# Write a python function to find number of elements with odd factors in a given range.
#
# SOLUTION CODE
# ============================================
def count_odd_squares(n,m): 

    return int(m**0.5) - int((n-1)**0.5) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, m, expected):
    try:
        if validate_solution(count_odd_squares(
            n, m),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



