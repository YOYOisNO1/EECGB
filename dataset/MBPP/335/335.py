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
# Write a function to find the sum of arithmetic progression.
#
# SOLUTION CODE
# ============================================
def ap_sum(a,n,d):

  total = (n * (2 * a + (n - 1) * d)) / 2

  return total

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, d, expected):
    try:
        if validate_solution(ap_sum(
            a, n, d),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



