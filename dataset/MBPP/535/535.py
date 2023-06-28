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
# Write a function to find the top or bottom surface area of a cylinder.
#
# SOLUTION CODE
# ============================================
def topbottom_surfacearea(r):

  toporbottomarea=3.1415*r*r

  return toporbottomarea

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(r, expected):
    try:
        if validate_solution(topbottom_surfacearea(
            r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



