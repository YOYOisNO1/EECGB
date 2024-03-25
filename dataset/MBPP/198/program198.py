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
# Write a function to find the largest triangle that can be inscribed in an ellipse.
#
# SOLUTION CODE
# ============================================
import math

def largest_triangle(a,b): 

    if (a < 0 or b < 0): 

        return -1 

    area = (3 * math.sqrt(3) * pow(a, 2)) / (4 * b);  

    return area 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(a, b, expected):
    try:
        if validate_solution(largest_triangle(
            a, b),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



