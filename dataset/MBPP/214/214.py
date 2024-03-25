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
# Write a function to convert radians to degrees.
#
# SOLUTION CODE
# ============================================
import math

def degree_radian(radian):

 degree = radian*(180/math.pi)

 return degree

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(radian, expected):
    try:
        if validate_solution(degree_radian(
            radian),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



