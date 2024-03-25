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
# Write a function to calculate the geometric sum of n-1.
#
# SOLUTION CODE
# ============================================
def geometric_sum(n):

  if n < 0:

    return 0

  else:

    return 1 / (pow(2, n)) + geometric_sum(n - 1)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(n, expected):
    try:
        if validate_solution(geometric_sum(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



