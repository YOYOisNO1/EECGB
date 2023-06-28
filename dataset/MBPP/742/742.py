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
# Write a function to caluclate the area of a tetrahedron.
#
# SOLUTION CODE
# ============================================
import math

def area_tetrahedron(side):

  area = math.sqrt(3)*(side*side)

  return area

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(side, expected):
    try:
        if validate_solution(area_tetrahedron(
            side),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



