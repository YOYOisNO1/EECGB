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
# Write a function to find t-nth term of geometric series.
#
# SOLUTION CODE
# ============================================
import math

def tn_gp(a,n,r):

  tn = a * (math.pow(r, n - 1))

  return tn

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, r, expected):
    try:
        if validate_solution(tn_gp(
            a, n, r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



