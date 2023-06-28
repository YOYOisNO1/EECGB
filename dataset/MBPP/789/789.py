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
# Write a function to calculate the perimeter of a regular polygon.
#
# SOLUTION CODE
# ============================================
from math import tan, pi

def perimeter_polygon(s,l):

  perimeter = s*l

  return perimeter

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, l, expected):
    try:
        if validate_solution(perimeter_polygon(
            s, l),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



