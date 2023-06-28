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
# Write a function to find the diameter of a circle.
#
# SOLUTION CODE
# ============================================
def diameter_circle(r):

  diameter=2*r

  return diameter

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(r, expected):
    try:
        if validate_solution(diameter_circle(
            r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



