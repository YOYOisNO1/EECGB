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
# Write a function to find the surface area of a cuboid.
#
# SOLUTION CODE
# ============================================
def surfacearea_cuboid(l,w,h):

  SA = 2*(l*w + l * h + w * h)

  return SA

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, w, h, expected):
    try:
        if validate_solution(surfacearea_cuboid(
            l, w, h),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



