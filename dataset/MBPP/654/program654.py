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
# Write a function to find the perimeter of a rectangle.
#
# SOLUTION CODE
# ============================================
def rectangle_perimeter(l,b):

  perimeter=2*(l+b)

  return perimeter

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, b, expected):
    try:
        if validate_solution(rectangle_perimeter(
            l, b),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



