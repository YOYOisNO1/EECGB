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
# Write a function to find the surface area of a cube.
#
# SOLUTION CODE
# ============================================
def surfacearea_cube(l):

  surfacearea= 6*l*l

  return surfacearea

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, expected):
    try:
        if validate_solution(surfacearea_cube(
            l),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



