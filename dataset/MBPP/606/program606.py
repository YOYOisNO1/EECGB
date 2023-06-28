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
# Write a function to convert degrees to radians.
#
# SOLUTION CODE
# ============================================
import math

def radian_degree(degree):

 radian = degree*(math.pi/180)

 return radian

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(degree, expected):
    try:
        if validate_solution(radian_degree(
            degree),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



