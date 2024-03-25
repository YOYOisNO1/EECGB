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
# Write a python function to find the maximum occuring divisor in an interval.
#
# SOLUTION CODE
# ============================================
def find_divisor(x,y):  

    if (x==y): 

        return y 

    return 2

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, expected):
    try:
        if validate_solution(find_divisor(
            x, y),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



