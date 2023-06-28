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
# Write a function to find the lateral surface area of a cone.
#
# SOLUTION CODE
# ============================================
import math

def lateralsurface_cone(r,h):

  l = math.sqrt(r * r + h * h)

  LSA = math.pi * r  * l

  return LSA

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(r, h, expected):
    try:
        if validate_solution(lateralsurface_cone(
            r, h),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



