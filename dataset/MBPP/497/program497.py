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
# Write a function to find the surface area of a cone.
#
# SOLUTION CODE
# ============================================
import math

def surfacearea_cone(r,h):

  l = math.sqrt(r * r + h * h)

  SA = math.pi * r * (r + l)

  return SA

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(r, h, expected):
    try:
        if validate_solution(surfacearea_cone(
            r, h),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



