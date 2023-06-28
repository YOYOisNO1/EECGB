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
# Write a function to rearrange positive and negative numbers in a given array using lambda function.
#
# SOLUTION CODE
# ============================================
def rearrange_numbs(array_nums):

  result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)

  return result 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(array_nums, expected):
    try:
        if validate_solution(rearrange_numbs(
            array_nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



