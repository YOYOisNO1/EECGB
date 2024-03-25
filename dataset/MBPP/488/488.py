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
# Write a function to find the area of a pentagon.
#
# SOLUTION CODE
# ============================================
import math

def area_pentagon(a):

  area=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(a,2))/4.0

  return area

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(a, expected):
    try:
        if validate_solution(area_pentagon(
            a),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



