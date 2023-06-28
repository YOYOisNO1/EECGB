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
# Write a function to convert the given tuple to a floating-point number.
#
# SOLUTION CODE
# ============================================
def tuple_to_float(test_tup):

  res = float('.'.join(str(ele) for ele in test_tup))

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(test_tup, expected):
    try:
        if validate_solution(tuple_to_float(
            test_tup),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



